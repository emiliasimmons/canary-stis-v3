# Experiments

Experiment tracks for canary-stis, one folder per track under `experiments/<track>/`.

## Tracks

Tracks are lines of experiments working toward one question or goal, each in
`experiments/<track>/`:

- `README.md` is the standing summary for the researcher and colleagues: purpose,
  framing, the anchor. It changes slowly. Experiment results and parameter names live in
  the experiments' SUMMARYs.
- `STATUS.md` orients the next session: where the track stands, the last result linked to
  its SUMMARY, the plan, and what to settle next. It is rewritten with each SUMMARY, under
  the same approval, and skips what the README already says.
- The tracking issue, labeled `track`, links both files and holds the track's experiment
  issues as sub-issues.

## Experiment issues

Experiment issues state one clear question or goal and are labeled `experiment`. They are
sub-issues of their tracking issue, written before any work on their question starts, by
the user or by the agent with the user's confirmation. Issue numbers are experiment
numbers.

## Experiment lifecycle

Calib's `project-workflow` and `experiment-close` skills govern experiments, with three
changes: the question comes from an experiment issue, the issue number is the experiment
number, and each experiment lives on its own branch. Where those skills say "the most
recent experiment", read each unmerged experiment branch on the track. Where they say to
commit, use the commits below.

Experiments address one experiment issue each. Each runs on its own branch,
`exp/<number>-<slug>`, cut from the default branch, and merges back into it locally.
Several approaches to one experiment issue can run at the same time, each with its own
slug, branch and folder at `experiments/<track>/<number>_<slug>/`.
A change made in response to a result is a new question and gets a new experiment issue.
A different way of answering the same question is another approach on the same issue.

1. **Open.** Create the branch and the folder with empty `outputs/` and `figures/`. Draft
   the README from the issue: the question (linking the issue and the SUMMARY that
   motivated it), the plan, and the success criteria. Show it and wait for approval.
   Commit it as `open-exp-<number>: <question>` and push to `origin`.
2. **Build.** Write `config.yaml` and `run.py`. Code a second experiment would need goes
   into `src/`, through `tdd` then `code-review`. Commit as
   `exp-<number>: <scientific change>` and push before running, so every result traces to
   a commit. `scripts/mirror` refuses to launch from a dirty tree.
3. **Run.** Run locally with `uv run python experiments/<track>/<number>_<slug>/run.py`,
   or remotely per Remote runs below. `run.py` appends results to `outputs/` as each
   simulation finishes and saves every figure as `figures/figN_<name>.png`, numbered in
   the order the SUMMARY embeds them. Each figure's title starts with `Fig N: `, so
   a figure seen outside the SUMMARY still says which one it is.
4. **Close.** When a run finishes, offer to close before diagnosing or fixing anything.
   Write the SUMMARY per `experiment-close`, run its validator, and rewrite STATUS.md.
   Show both and wait for approval. Commit them with the figures the SUMMARY embeds as
   `close-exp-<number>: <result>` and push. When the result answers a well-defined
   question, propose a canon finding in `docs/findings/` to commit on the same branch.
5. **Merge.** Once the user approves, merge the branch into the default branch with a
   merge commit and switch the checkout to it. Close the experiment issue unless the
   SUMMARY leaves it open for another approach. If the SUMMARY's Next section names
   a clear next experiment, draft its issue and open it once the user confirms.

`outputs/` is git-ignored: it regenerates from the committed `run.py`, and remote outputs
come back with `scripts/mirror-pull`. `figures/` is committed so SUMMARYs render them.
pngs will have to be force-staged.

At session start on a track, run `project-workflow`'s two checks on each unmerged
experiment branch: a README before any code, and a SUMMARY wherever outputs or figures exist.

Experiment branches share the main checkout by default, so open experiments take turns
there. When the user asks to run one in true parallel, give it its own worktree and run
`uv sync` in it. When two approaches are open at once, the second to merge rewrites
STATUS.md to cover both SUMMARYs.

## Remote runs

Run a committed experiment on a remote VM with `scripts/mirror <ssh-target>
<track>/<number>_<slug> [run.py args]`. It pushes the current branch to the git remote
named after the target and launches `run.py` in a detached tmux session there. Pull
results back with `scripts/mirror-pull <ssh-target> <track>/<number>_<slug>`. Report the
launch and the `ssh <target> tail -f` command it prints, then stop: the user checks on
the run.

Each target needs a one-time setup: the repo cloned at `~/Projects/<repo>` on the VM,
`git config receive.denyCurrentBranch updateInstead` in that clone, and a local git
remote of the target's name (`git remote add <target> <target>:Projects/<repo>`).

### Zebra

160 logical cores (80 physical). Check load before submitting. Default to 80 workers, one
per physical core. Each STIsim simulation runs twice as fast with 80 workers as with 160,
and the other half of the logical cores stays open for other users. When other users have
jobs running, size the run to leave at least 5 to 10 cores idle. The local machine is fine
for setup and small runs.

## Intake

The current work is a scenario analysis: hypothetical settings spanning high and medium
HIV prevalence crossed with a mature or expanding epidemic, each run under the SOC and POC
arms, with the pathway decomposition (direct treatment, prevention targeting, network
identification) reported per setting to show how the split shifts across epidemics.
Each setting is an ensemble of simulations selected from a parameter exploration by its
2026 HIV prevalence, so no likelihood or posterior is needed. The model is the Starsim/STIsim simulation in `src/sim.py`
(10,000 agents, 1985 to 2040, monthly step); run time per simulation is not yet measured.
Compute is the laptop for setup and small runs and zebra for sweeps. The environment is
managed with `uv`.
