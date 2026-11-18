Load /canonize:canon immediately.

# canary-stis

Pathway analysis and calibration harness for the population-level HIV-prevention impact of
point-of-care STI diagnostics. A Starsim/STIsim agent-based model of co-circulating HIV and
four curable STIs. See `README.md` for setup, running, and project structure.

## Agent skills

**Issue tracker**: GitHub Issues on emiliasimmons/canary-stis-v3 via `gh`, see `docs/agents/issue-tracker.md`.
**Triage labels**: the five defaults (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`), see `docs/agents/triage-labels.md`.
**Domain docs**: single-context, the canon only (no ADRs, no root `GLOSSARY.md`), see `docs/agents/domain.md`.

## Discipline

When modeling or when the user asks about the project, **immediately** orient with
/canonize:canon. Read canon pages eagerly whenever scientific context would help.

When the user starts or continues work on a track ("continue settings", "let's do the
next settings experiment"), **immediately**:

1. Load /canonize:canon and orient.
2. Load /calib:project-workflow.
3. Read `experiments/<track>/README.md` and `STATUS.md`, then the track's tracking issue
   and its open experiment issues.

Model and harness changes go through `tdd`, then `code-review`.

## Session state

Two places carry state between sessions:

- GitHub issues, per `docs/agents/issue-tracker.md`, hold tracks, experiment questions,
  and every other open thread, canonize's Catalog, Queries, and Curate threads included.
  Link issues that wait on others with GitHub's native blocking relationship.
- `experiments/<track>/STATUS.md` holds what the track's next experiment needs.

Files in the repository link only to other files in the repository, never to GitHub
issues.

`docs/ledger.md` stays unused. Where a canonize skill would write to the ledger, write to
an issue instead.

## Layout

- `docs`: the evidence, managed by canonize.
- `experiments`: calibration and analysis experiments, managed by calib.
  `experiments/CLAUDE.md` holds calib's intake and the experiment workflow.
- `src`: the simulation library: sim builder, interventions, diagnostics, HIV-STI
  coinfection connectors, and analyzers.
- `scripts`: `mirror` and `mirror-pull` for running experiments on remote VMs.
