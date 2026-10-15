# V91 AGATHON — MAX BEST / Reality-First Status
**Stand:** 2026-10-15 (GitHub-verified state; not a local-PC health claim)

## Status model
`UNBEKANNT → DOKUMENTIERT → IMPLEMENTIERT → VERIFIZIERT → PRODUKTIV`
A passing CI run verifies only the exact tested commit and checks executed. `CLAIM ≠ EVIDENCE`. Missing evidence stays `UNKNOWN`. GitHub storage does not train or synchronize models automatically.

## Confirmed changes in this session

### Core repository: `guenny9000/v91-core-system`
- **PR #16 Guarded Tool Runner merged.** Merge commit: `3d449e58a98d175e60eb883b29928cb8021000dc`. Exact-head CI run #167 passed: [run 38639183827](https://github.com/guenny9000/v91-core-system/actions/runs/38639183827). The runner executes only host-registered callables; `read_only` is a declaration, not an OS sandbox.
- **PR #14 trusted peer-key registry merged.** Merge commit: `8f8e042f065501efe41aa74e21ec325c877be08f`. Post-merge CI passed: [run 38672929444](https://github.com/guenny9000/v91-core-system/actions/runs/38672929444). It is a lookup helper, not key distribution or proof of authenticated production peers.
- **PR #17 Global Guard merged.** Merge commit: `0a0d8b581d57ab7907b9b15e3bc5c2ab64554f26`. Exact-head CI run #170 passed, including unit tests, compilation, Compose worker/observer integration, hash verification and artifact upload: [run 38673094808](https://github.com/guenny9000/v91-core-system/actions/runs/38673094808). Post-merge CI passed: [run 38673171945](https://github.com/guenny9000/v91-core-system/actions/runs/38673171945).
- The Global Guard now includes a deterministic **30-case regression matrix** plus fail-closed handling for malformed requests, invalid policy configuration, non-boolean approval flags, malformed scenario records, and malformed feedback records. The passing CI is evidence for those repository tests, not proof of universal security.
- **PR #15 closed as superseded by #17.** The earlier CI pass applies only to its old head.
- PR #10, #11, #12 and #13 are merged. PR #9 is closed without merge.
- Core PR #1, #3 and #5 remain open and currently non-mergeable. Do not force-merge:
  - #1 changes the SafeSignal envelope/signature protocol; coordinate producer migration and key management first.
  - #3 overlaps with already-merged controller/runtime changes; reconcile diffs before any rebase or merge.
  - #5 changes peer-handshake/signature logic. The trusted key registry is now merged, but the handshake still needs safe integration, migration/compatibility tests, key lifecycle design, and new CI on the current head.
- Separate Agathon PR #1 was not changed. Keep it isolated as requested.

### Audit ledger: `guenny9000/v91-audit-ledger`
- **PR #2 merged** as `fb6de901dd916b90a1c28e7bbb1af979d1e5cd3b`; post-merge CI passed: [run 38673202680](https://github.com/guenny9000/v91-audit-ledger/actions/runs/38673202680).
- Found and fixed a verification gap: a record's timestamp was not checked by the current verifier. **PR #3 added strict UTC ISO timestamp validation**, including cases where a malformed timestamp's record hash is recomputed. PR #3 merged as `c9c410aa67b0804e044d7877d1f5abb9153be336`; exact-head CI run #9 passed: [run 38673238745](https://github.com/guenny9000/v91-audit-ledger/actions/runs/38673238745). Post-merge CI passed: [run 38673272988](https://github.com/guenny9000/v91-audit-ledger/actions/runs/38673272988).
- Older ledger PR #1 closed as superseded after porting its useful timestamp-validation behavior. No real ledger data was read, changed, reset, or repaired.
- Ledger remains a local hash-linked JSONL file. **Not WORM, not signed evidence, not trusted time, not proof of event truth, and not production deployment.**

### Learning repository: `guenny9000/guenny9000-uni-lern-bloc`
- Previous learning handoff PR #8 is merged.
- This report is a status addendum, not evidence that another model consumed or learned from it. Local models must fetch/read the repository and report their own verifiable result if cross-model adoption is to be claimed.

## Claims from the pasted third-model report — evidence split
- **Global Guard policy tests and 30-case matrix:** implemented in core repository; exact-head and post-merge CI passed.
- **Logging E “operational / attack detection active”: UNKNOWN here.** No independently retrievable source/run/artifact was available in the inspected repositories.
- **Standalone Policy Engine 5/5:** UNKNOWN as a separate deliverable. Do not equate it with the Global Guard without a path and exact commit.
- **Standalone Learning Core “convergent and stable”: UNKNOWN.** No numerical output, exact source commit, test command, and reproducible artifact were available for this claim.
- Files allegedly under `/mnt/user-data/outputs/` were not available through the inspected GitHub repositories in this session. Their existence and execution results are therefore not verified.
- No local Windows/NVIDIA runtime, actual attack injection, production tool adapter, external WORM anchor, model training, or cross-model synchronization was executed or verified here.

## Remaining work, in safe order
1. Obtain or commit the actual Logging E and standalone Policy/Learning Core files; run them in an isolated test job and save the exact command, commit SHA, output, and artifact hash.
2. Reconcile core PR #3 against merged PR #10 before deciding whether any unique changes remain.
3. Rebase/rework core PR #5 only after inspecting its current diff against the merged key registry; add compatibility and key-lifecycle tests; rerun CI on the new exact head.
4. Keep core PR #1 and the separate Agathon PR #1 isolated until protocol migration and independent review are ready.
5. Test the ledger on synthetic temporary files only. If WORM or trusted time is needed, implement and independently verify a real external anchor; a hash chain is not WORM.

## Operating rule
Do only additive, reversible changes supported by evidence. No force-push, broad merge batch, destructive cleanup, network/production action, privilege escalation, or model-rule change without explicit authorization and a tested rollback. A successful CI run is not a production PASS.


## Additional work completed later on 2026-10-15 — safe Windows verification
- **Core PR #18 merged** as `af403ce3347f7bb2479de1e2f455449653d42fea`.
- Added `scripts/V91-Local-Verify.ps1`, German instructions at `docs/V91_WINDOWS_LOCAL_VERIFICATION.md`, and a Windows-hosted CI workflow that executes the script and uploads a bounded evidence artifact.
- Exact PR-head Windows verification passed: https://github.com/guenny9000/v91-core-system/actions/runs/38674370983
- Exact PR-head core audit pipeline passed: https://github.com/guenny9000/v91-core-system/actions/runs/38674370919
- The script was run on a GitHub-hosted Windows runner, **not on the user's own PC**. It does not fetch/pull code, install packages, start containers, deploy, or repair data.
- Handoff and safe operating instructions: https://github.com/guenny9000/guenny9000-uni-lern-bloc/blob/main/reports/V91_WINDOWS_VERIFY_HANDOFF_2026-10-15.md
- Post-merge CI is being checked separately. The local Windows runtime, actual user PC, production tool adapters, WORM storage, and model training remain UNKNOWN.
