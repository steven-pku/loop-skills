# Evaluation Material

This repair candidate contains the [v0.3.1 assertions](releases/current-v0.3.1.md),
the [frozen v0.3.0 assertions](releases/2026-09-20.md),
and [two recorded failed runs](review-evidence/README.md). It does not include the
complete historical case library or all private run receipts. Examples elsewhere
in this repository are teaching material, not evidence that behavior passed.

The v0.3.0 assertions and failure-evidence directory describe the archived
snapshot and remain byte-for-byte unchanged, including its then-current status.
For this repair, use the v0.3.1 contract: the old blanket ban on a synthetic
report's Pass scorecard is superseded by an explicit scored-object distinction.
Fresh behavior validation is pending; static changes are not passing evidence.

For the current HOLD status and the difference between report-text evaluation and
real performance attribution, read [REVIEW.md](../REVIEW.md).

An independent reviewer can reproduce the supplied inputs in a fresh isolated
project with this exact runtime. Preserve the outer synthetic declaration when
testing source handling. Do not adopt the recorded outputs as expected answers.
Compare observable behavior, source status, and gate integrity; exact wording or
model self-scores are not the acceptance criterion.

## v0.3.1 executed checks

See the [dated acceptance record](releases/2026-09-20-v0.3.1.md) for the new runtime, 18 cases and actual three-turn continuation. Archived v0.3.0 results remain unchanged.
