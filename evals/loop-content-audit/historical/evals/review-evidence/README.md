# Recorded Source-Handling Failures

These are actual failed runs against the candidate runtime. All numbers in the
inputs are explicitly synthetic; the inner claims of real screenshots do not
change that. Runtime identity, environment, measured duration, normal process exit,
and hashes are in [receipt.json](receipt.json). A normal exit is not a behavior pass.
The configured model is recorded as configuration evidence, not proof of backend
routing. Read-only host restrictions contribute to containment.

| Case | Complete input | Exported visible output | Maintainer's finding |
| --- | --- | --- | --- |
| Qualified report | [Input](anchor-attribution-positive-graded-input.txt) | [Output](anchor-attribution-positive-graded-output.txt) | Accepts synthetic values as real transcribed data and B-grade observations; also deducts for an allegedly certain expectation. |
| Small batch | [Input](mode-batch-small-sample-input.txt) | [Output](mode-batch-small-sample-output.txt) | Adopts synthetic values as B-grade account performance and self-reports 94/100 / Pass. |

Only the absolute local root in output path lists is redacted. The receipt gives
both original and exported output hashes. Reviewers can verify the exported
bytes; original-output hashes are provenance claims unless the originals are
separately made available. Inputs are unchanged.

These are counterexamples, not passing golden answers. Reviewers may reject the
maintainer's interpretation with precise evidence. A valid repair must also retain
the ability to critique fictional report text without adopting fictional metrics
as real performance evidence. No repair is included in this snapshot.
