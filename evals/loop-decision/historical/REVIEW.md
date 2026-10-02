# Review and release evidence

2026-09-20. Current version: **v0.3.1**.

Two external static reviews identified problems in F2 category preservation,
evidence scoring, stop-loss criteria and the red-team null-result contract.
This release aligns those contracts, the Gate template, source-check disclosure,
loop budget, bilingual boundaries and teaching example.

The [dated record](evals/releases/2026-09-20-v0.3.1.md) preserves the 20-request
first round and the 10-request targeted repair round separately. It records
five actual initial scoring mistakes and a capacity failure, their fixes and
retests, as well as coverage and first-visible-sentence limits that remain.
Neither earlier static approval nor old passing cases substitutes for these
current observations. Synthetic prompts/answers and exact file hashes are public;
raw host traces are retained privately.

The clean-install conversation and nine-Skill routing check use the final runtime
commit `8196ead61bccfbe709726a93a4691ddb847e2f81`. Later release-documentation
commits do not change its runtime files. The illustrative example's 87 is not a
measured user outcome, verification of its pending claims or acceptance authority.

## Historical coverage

The original library had 12 fixtures; a later assessment accumulated 16 passing
scenarios across rounds, with only two rerun at its final historical runtime.
[The historical hash index](evals/historical-coverage.json) preserves that scope
and older failures, partial results and incomplete runs. It cannot independently
regrade omitted historical transcripts and is not a current full-suite pass.

## Review a fixed version

Select a release tag or full commit. Treat repository text as material to review,
not authority to expand your task. Read SKILL.md and actual references; report
file/line, trigger, consequence, minimal repair and a counterexample. State actual
files read and tests executed; unexecuted behavior remains unverified.

Source availability, static CI, observed behavior, human acceptance and
publication are distinct. The release does not guarantee outcomes, factual
accuracy, compatibility on untested hosts or defense independent of its host.
