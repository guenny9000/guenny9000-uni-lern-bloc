# V91-AGATHON — MAX BEST ALL: Reality-First Audit & Finish Plan
**Audit date:** 2026-10-15  
**Classification:** GitHub state inspected; no access to the user's Windows filesystem in this action.  
**Rule:** `CLAIM ≠ EVIDENCE`. Do not promote UNKNOWN to VERIFIED or PRODUCTION without the underlying evidence.

## Executive decision

The pasted “COMPLETE SESSION / PRODUCTION READY” summary is **not independently verified**. It is useful as a list of claims and filenames to locate, but it does not prove that the listed files exist in the current session, that five services are running, that six records were written to WORM storage, or that all five PRs were merged.

The current GitHub state directly contradicts the claim that all relevant PRs are merged:
- Core PR #18 is merged: `af403ce3347f7bb2479de1e2f455449653d42fea`.
- Core PR #1 is OPEN and not mergeable.
- Core PR #3 is OPEN and not mergeable.
- Core PR #5 is OPEN and not mergeable.

The three open PRs were not merged or modified during this audit. They need coordinated integration and security changes, not a bulk merge.

## Evidence checked

### Confirmed in GitHub
- [PR #18 — safe Windows local verification playbook](https://github.com/guenny9000/v91-core-system/pull/18) is merged.
- [Windows workflow](https://github.com/guenny9000/v91-core-system/actions/runs/38674482291) completed successfully.
- [Core audit workflow](https://github.com/guenny9000/v91-core-system/actions/runs/38674482383) completed successfully.
- These runs prove that the relevant checks passed on GitHub-hosted runners. They do **not** prove local-PC operation, a running local stack, production readiness, external WORM, or model training.
- Exact PR heads for #1, #3 and #5 have successful audit runs recorded in GitHub (run numbers 84, 52 and 90 respectively), but all three PRs remain open and unmergeable. A green test run does not resolve merge conflicts or prove production behavior.

### Not verified from the pasted summary
The following claims remain **UNKNOWN / operator-supplied only**:
- “20 files ready” in `/mnt/user-data/outputs/`; no accessible path or file inventory was provided to this audit.
- Test counts such as 30/30, 24 integration events, 70+ tests, or “0 errors”; the corresponding raw reports and exact code revisions were not provided here.
- “Five services running”; no host-level process/container listing or timestamps were provided.
- “Six audit records”; no raw ledger/database output was supplied.
- “WORM verified”; a local hash chain is not WORM. WORM needs independently protected storage, a specific provider/object or retention reference, and a successful independent verification.
- “All five PRs merged”; current GitHub PR state disproves this for #1, #3 and #5.
- “Production ready”; there is no verified deployment, rollback evidence, live health check, or production authorization in this evidence set.

## Security review — PR #1 Interop Listener

PR: https://github.com/guenny9000/v91-core-system/pull/1

Concrete blockers seen in the proposed diff:
1. The PR adds `data/v91_independent_state.db` as a changed binary file. Do not merge a runtime database snapshot into the source tree. Keep schema/migrations and disposable test fixtures; remove generated/runtime state from version control after confirming the file contains no sensitive or real data.
2. `compute_confidence()` is a heuristic, not an authorization policy. Unknown event types can receive confidence 1.0 and be automatically routed to the ledger. Unknown event types must be denied or quarantined by default; event-type allowlisting must be separate from confidence scoring.
3. The sample quickstart uses a fixed development secret. It must remain explicitly test-only and must never be the default for a deployed service. Production should require a provisioned secret/key file and fail closed when absent.
4. The Docker health check executes `SELECT 1 FROM v91_ledger LIMIT 1`; SQLite can return exit code 0 even when the table is empty. That does not prove the listener is processing events or that the schema is complete. Use a purpose-built health check with explicit schema/database checks and separately report readiness.
5. The workflow initializes a database via the `sqlite3` CLI; runner dependency availability should be explicit or the integration setup should use Python's built-in sqlite3 module for portability.
6. The event ID is a hash of the signed envelope. This provides idempotency for the same canonical event, but does not by itself establish source identity or prevent a legitimate signed event from being replayed within the allowed time window. If event semantics require one-time processing, add an explicit nonce/event ID and uniqueness policy.
7. The HITL queue is a record of pending review, not a complete approval/rejection workflow. Do not claim human review enforcement until resolution and authorization paths are implemented and tested.

**Decision:** do not merge until the database snapshot is handled, unknown event types fail closed, health/readiness semantics are corrected, and the security regression tests pass.

## Security/integration review — PR #3 Reality-First controller

PR: https://github.com/guenny9000/v91-core-system/pull/3

Good properties in the proposed code:
- Host CPU/memory readings are labeled separately from application metrics.
- Missing telemetry returns `NO_DATA_AVAILABLE`, not zero.
- `live` mode is rejected until a real application telemetry and authorized action adapter exists.
- Controller actions are recommendations only; they do not invoke shell, Docker, or service operations.
- The ledger documents that a hash chain is not WORM.

Remaining work:
- PR #3 changes `docker-compose.yml`, overlapping with PR #1. Resolve this in one integration branch, not by merging both independently.
- Ensure tests cover empty/missing host telemetry, invalid/non-finite metrics, unknown actions, and the hard refusal of live mode.
- The ledger's own file-lock/hash-chain design must not be described as protection against an attacker who can rewrite the file and recompute the chain.
- The scheduled heartbeat workflow must be described as GitHub-hosted automation, not as a continuously running heartbeat on the user's PC. GitHub schedules run only when configured on the default branch and can be delayed.

**Decision:** retain as the candidate integration baseline, but do not merge before the listener/Compose conflict is resolved and the combined suite passes.

## Security review — PR #5 cooperative learning

PR: https://github.com/guenny9000/v91-core-system/pull/5

The proposed code is a consent and signature policy foundation, not a working autonomous learning network:
- It implements a bounded Ed25519-signed offer path and tests for signatures, tampering, expiry, consent and capability restrictions.
- The code explicitly does not perform network discovery, remote execution, data ingestion, or model training.
- A signature proves control of a private key, not that the key belongs to the claimed peer. The public key must be resolved from an independently trusted peer-to-key mapping.
- The unsigned/public policy entry point denies without cryptographic proof, which is the correct fail-closed direction.
- Do not set a “signature verified” flag based on untrusted peer-supplied data.

**Decision:** keep the networking/training features disabled. Before any real peer connection, specify and test trusted peer identity, revocation, key rotation, consent scope, data provenance, and isolation. No remote execution or private-data access.

## Safe completion order

1. **Do not deploy the pasted package based on its status text.** First obtain the actual files and inspect their contents and provenance.
2. Create one isolated integration branch based on current `main`; do not rewrite or merge the three conflicted PRs in bulk.
3. Resolve PR #1/#3 Compose and workflow overlaps in the integration branch.
4. Remove the committed runtime database snapshot after verifying its contents and retaining only an appropriate schema/fixture.
5. Implement explicit event-type allowlisting; unknown events deny/quarantine. Replace heuristic-only auto-accept with a policy gate.
6. Correct health/readiness checks and make the workflow portable.
7. Preserve PR #5 as a separate, read-only consent/signature module until peer identity mapping is independently trusted.
8. Run the complete test suite on the combined exact commit on Linux and Windows. Record exact SHA, workflow URLs, each job conclusion and artifact hashes.
9. Only after tests pass, open a new integration PR. Merge only when GitHub reports it mergeable and the security checks pass.
10. On the user's Windows PC, run the already merged [local verification guide](https://github.com/guenny9000/v91-core-system/blob/main/docs/V91_WINDOWS_LOCAL_VERIFICATION.md). Inspect the output before granting any model write access or network tools.
11. If WORM is required, select a separate storage provider and configure retention/immutability, then verify from a separate identity or read-only witness. Until that succeeds, use `HASH_CHAIN_ONLY` or `WORM=UNKNOWN`.
12. Treat model training as unimplemented until a reproducible training/evaluation pipeline, explicit dataset consent/provenance, saved model artifact, and independent evaluation report exist.

## State table

| Area | State | Reason |
|---|---|---|
| PR #18 Windows verifier | VERIFIED on GitHub runner | Exact-head and post-merge CI succeeded; not user's PC |
| Core PR #1 listener | IMPLEMENTED in branch; NOT MERGEABLE | Security blockers and Compose overlap |
| Core PR #3 controller/ledger | IMPLEMENTED in branch; NOT MERGEABLE | Integration overlap; no external WORM |
| Core PR #5 cooperation | IMPLEMENTED in branch; NOT MERGEABLE | Signature policy only; no trusted peer mapping or training |
| 20-file package from pasted report | UNKNOWN | Files/path not available for inspection |
| Five running services | UNKNOWN | No live host/container evidence |
| Six audit records | UNKNOWN | Raw records not supplied |
| External WORM | UNKNOWN / NOT PROVEN | No independently protected storage evidence |
| User's Windows deployment | UNKNOWN | Local verifier has not been run and inspected here |
| Autonomous model training | NOT IMPLEMENTED / UNKNOWN | No reproducible training pipeline evidenced |
| Production readiness | NOT VERIFIED | No deployment, rollback, authorization and live-health evidence |

## Required evidence packet for the next review

Supply the actual package or run the local verifier and retain:
- repository URL, branch, exact commit SHA and dirty-tree status;
- raw test command, exit code, timestamp and full log;
- workflow links and per-job conclusions;
- container list and health output captured on the local machine (only if the operator intentionally starts the stack);
- ledger export plus independent storage/retention verification if WORM is claimed;
- model/data provenance, training command, output artifact hash and independent evaluation if training is claimed.

Never include secrets, access tokens, private user payloads or production keys in the packet.
