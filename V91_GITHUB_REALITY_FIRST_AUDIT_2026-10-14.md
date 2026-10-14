# V91 MAX BEST – GitHub Reality-First Audit Snapshot

**Stand:** 2026-10-14  
**Scope:** targeted review of accessible V91 repositories and high-risk runtime paths. This is not a line-by-line audit of every file in the large Aurelia-Prisma repository.  
**Rule:** `CLAIM != EVIDENCE`. Open PRs are proposals, not merged behavior.

## Results by repository

### 1. v91-core-system

- **Original finding:** the default controller generated random metrics and could invoke host/Docker actions from those values.
- **Merged to main:** PR [#10](https://github.com/guenny9000/v91-core-system/pull/10) keeps the random controller as a manual demo and changes the Compose stack to a real filesystem observer plus shared-queue workers. Merge commit: `267f1f45a48b342f20c75954d5daa406a2bae31b`.
- **Real work:** the worker accepts only `health_snapshot`, `sha256_file`, and `verify_sha256`. Tasks require a purpose and expected effect, reject unsupported fields/actions, enforce workspace boundaries and size limits, and write results plus audit events.
- **Real control:** host-side `runtime_control.py` reads actual Docker Compose state and CPU/memory metrics. It can scale only the worker service from 1 to 3 replicas; scale-up and scale-down have separate explicit authorization settings. It records the decision before acting, verifies the result, measures resource deltas, and attempts rollback after failed verification.
- **Isolation:** Compose uses an internal-only Docker network with no published ports. The controller/worker containers are not given the Docker socket. The Windows host launcher defaults to observation only.
- **Evidence:** GitHub Actions [run](https://github.com/guenny9000/v91-core-system/actions/runs/38585438842) passed Compose validation, unit tests, Python compilation, a container build, a real container task integration test, observer/audit checks, and checksum artifact generation on commit `6c16d753a1644523e6962093c07fcdb4b6218af7`.
- **Current safety follow-up:** PR [#11](https://github.com/guenny9000/v91-core-system/pull/11) adds explicit `UNKNOWN`/`NO_DATA_AVAILABLE` logging for missing live telemetry and regression tests separating missing CPU data from measured `0.0%`. At this snapshot, its CI run is still in progress; do not treat it as merged until the exact head passes and the merge is confirmed.\n- **Limit:** CI exercised containers on GitHub's runner; no action was executed on the user's PC. The JSONL log is not WORM or signed, application-level latency/error telemetry is not connected, and production deployment is unverified.

### 2. v91-audit-ledger

- **Finding:** the repository was empty, so it had no ledger implementation to verify.
- **Change:** initialized the empty repository with an honest README, then opened PR [#1](https://github.com/guenny9000/v91-audit-ledger/pull/1) containing a local Python-standard-library JSONL ledger with canonical hashing, sequential records, chain verification, exclusive locking, and fail-closed handling.
- **Evidence:** GitHub Actions [run](https://github.com/guenny9000/v91-audit-ledger/actions/runs/38581344446) passed on commit `71aba085c3697f935f97115e2403996d0b2249c1`, including a regression test that rejects malformed UTC timestamps even when the hash is recomputed.
- **Limit:** hash-linked JSONL is not WORM, does not establish identity or trusted time, and does not prove that event contents are true. The implementation PR is not merged.

### 3. Aurelia-Prisma

This repository contains hundreds of files. The work below addresses selected high-risk areas; it does not certify all files or all runtime paths.

- **V94 supervisor and V95 recovery:** PR [#234](https://github.com/guenny9000/Aurelia-Prisma/pull/234) removes hard-coded success flags, surfaces audit failure, labels confidence as an uncalibrated heuristic, requires explicit UTC timestamps, limits request/audio size, binds the default host port to loopback, uses non-root Docker images, fixes the missing validator copy in Docker, and makes restart an explicit opt-in without PowerShell policy bypass. GitHub Actions [Reality-First checks](https://github.com/guenny9000/Aurelia-Prisma/actions/runs/38580789605) and [Python Quality checks](https://github.com/guenny9000/Aurelia-Prisma/actions/runs/38580789607) passed on code/test commit `0b65897ca1e709bc7803cf890762d4f4f3989f8d`; the later commit updates audit documentation.
- **Flowise AuditBlock:** PR [#235](https://github.com/guenny9000/Aurelia-Prisma/pull/235) fixes Node crypto hashing, recursively canonicalizes nested payloads, validates the chain before appending, and removes false WORM/automatic-operation claims. GitHub Actions [Node regression tests](https://github.com/guenny9000/Aurelia-Prisma/actions/runs/38578075273) passed on commit `d3c8eb597f4122bc00ac3212e1ba0debd565dd69`.
- **Validator locking and request load:** PR [#237](https://github.com/guenny9000/Aurelia-Prisma/pull/237) replaces a race-prone lock, removes an unsafe fallback, bounds batch size and request timeouts, and adds a request pause. GitHub Actions [focused safety tests](https://github.com/guenny9000/Aurelia-Prisma/actions/runs/38579189619) passed on commit `81e11a11a007a9e492b14d0a0f561971122ae851`.
- **Known CI backlog:** the repository's older whole-repository Pylint workflow still fails on the validator PR branch; the focused tests pass. That broader lint backlog is not marked resolved.
- **Limit:** these are review branches, not merged deployments. Flowise end-to-end calls, scheduler operation, webhook delivery, trusted identity, WORM storage, and real restart execution were not verified.

### 4. V91_Agathon

- **Change:** PR [#1](https://github.com/guenny9000/V91_Agathon/pull/1) makes core helpers executable, adds a synthetic offline demo, hardens hash-chain verification and lock behavior, and explicitly labels Semgrep/multi-node functions as unimplemented.
- **Evidence:** GitHub Actions [package tests](https://github.com/guenny9000/V91_Agathon/actions/runs/38579593171) passed on Python 3.10 and 3.12 at commit `16be1f44d42137254bcc5b376a040fa76461ceec`.
- **Limit:** the PR remains draft and GitHub currently reports it as not mergeable; its branch has diverged from `main` (29 commits ahead, 3 behind at the last comparison). Reconcile that history before merge. Semgrep execution, multi-node transport, persistent key management, trusted identity, and production operation are not implemented.

### 5. guenny9000-uni-lern-bloc

- PR [#2](https://github.com/guenny9000/guenny9000-uni-lern-bloc/pull/2) adds a machine-readable learning contract, validator, regression tests, and GitHub Actions workflow. It is now merged to `main` as `9c1a5cf393ac3eaa0e603acb6db2dc16a8dac23c`; its validation passed on PR head `81157439c3033145fe13b550cfab321f8c49ff78`.
- PR [#3](https://github.com/guenny9000/guenny9000-uni-lern-bloc/pull/3) adds the MAX BEST learning and ecology protocol.
- **Limit:** the learning block is a versioned instruction, not model training and not proof that another model or local system has adopted it.

## Cross-repository state

- Confirmed merges during this work: `v91-core-system` PR #10 and `guenny9000-uni-lern-bloc` PR #2. Other PRs remain proposals unless their merge state is checked separately.
- CI success applies only to the exact commit and checks linked above.
- GitHub access does not establish access to the user's Windows PC, AMD CPU, local models, network isolation, or production environment.
- No local hardware readings, live telemetry, or production status were fabricated.
- Existing ledgers and historical records were not reset or deleted.
- The next safe step is review/merge decisions, then controlled integration tests on the actual runtime. Until then, production status remains **UNBEKANNT**.
