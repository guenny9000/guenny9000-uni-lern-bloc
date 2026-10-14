# V91 MAX BEST – GitHub Reality-First Audit Snapshot

**Stand:** 2026-10-14  
**Scope:** targeted review of accessible V91 repositories and high-risk runtime paths. This is not a line-by-line audit of every file in the large Aurelia-Prisma repository.  
**Rule:** `CLAIM != EVIDENCE`. Open PRs are proposals, not merged behavior.

## Results by repository

### 1. v91-core-system

- **Finding:** the default-branch controller generated random synthetic metrics and used `os.system` to change Docker worker counts or restart workers based on those values. That could turn simulation into real host action.
- **Change proposed:** PR [#10](https://github.com/guenny9000/v91-core-system/pull/10) labels the source as simulation, turns actions into proposals only, rejects invalid metrics, and scores anomalies against the prior observation window.
- **Evidence:** GitHub Actions [run #89](https://github.com/guenny9000/v91-core-system/actions/runs/38578372467) succeeded on commit `9c9e469484f2d37f50389cd72145301a8920709f`.
- **Documentation:** PR [#9](https://github.com/guenny9000/v91-core-system/pull/9) corrects unsupported production-readiness claims.
- **Limit:** neither PR is merged; no production deployment or live telemetry was verified.

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

- PR [#2](https://github.com/guenny9000/guenny9000-uni-lern-bloc/pull/2) adds a machine-readable learning contract and tests. Its GitHub Actions validation passed on commit `81157439c3033145fe13b550cfab321f8c49ff78`.
- PR [#3](https://github.com/guenny9000/guenny9000-uni-lern-bloc/pull/3) adds the MAX BEST learning and ecology protocol.
- **Limit:** the learning block is a versioned instruction, not model training and not proof that another model or local system has adopted it.

## Cross-repository state

- No implementation PR listed above has been merged by this work.
- CI success applies only to the exact commit and checks linked above.
- GitHub access does not establish access to the user's Windows PC, AMD CPU, local models, network isolation, or production environment.
- No local hardware readings, live telemetry, or production status were fabricated.
- Existing ledgers and historical records were not reset or deleted.
- The next safe step is review/merge decisions, then controlled integration tests on the actual runtime. Until then, production status remains **UNBEKANNT**.
