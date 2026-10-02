# Loop Skills · Draft. Review. Improve

[中文](README.md) · [Installation](docs/installation.md) · [Compatibility and evidence](docs/compatibility.md)

A family of Agent Skills for content, career preparation, and decisions, using explicit criteria, bounded revision, and traceable evidence.

This branch is a consolidation candidate. Nine independently versioned, self-contained products live under `skills/`. Their original fixed releases remain available in the legacy repositories. Candidate installation, native execution and semantic review are separate gates; the default entry and legacy repositories have not been switched or archived.

## Choose one product

| Product | Use it for |
| --- | --- |
| [Topic Picker](skills/loop-topic-picker) | Select topics and produce a brief; no article drafting |
| [Article Writer](skills/loop-article-writer) | Chinese opinion articles and QA |
| [Script Writer](skills/loop-script-writer) | Spoken-video scripts and QA |
| [Content Audit](skills/loop-content-audit) | Evidence-graded content postmortems |
| [Report Writer](skills/loop-report-writer) | Workplace reports from real achievements |
| [Resume Writer](skills/loop-resume-writer) | Chinese resumes and career-facts ledgers |
| [Interview Writer](skills/loop-interview-writer) | Spoken interview answers and preparation |
| [Negotiation](skills/loop-negotiation) | Salary and critical workplace conversations |
| [Decision](skills/loop-decision) | Reversibility, evidence and decision memos |

Install only the product you need. Each runtime bundle closes over its own resources. Shared root documentation explains the family; it is not a runtime dependency. See [installation](docs/installation.md), [migration and rollback](docs/migration.md), and the exact [compatibility scope](docs/compatibility.md).

## Evidence and limits

Original inputs, outputs and environment limitations remain in `evals/<product>/historical/`. [Original release and review records](REVIEW-CANDIDATES.md) are preserved. New execution does not regrade old HOLD, PARTIAL or NOT_RUN results. Provenance maps every imported file to its fixed source. Scores do not verify facts or authorize publication.

## Contribute and license

[Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [MIT](LICENSE). Each product retains its original copyright and third-party notices. See [provenance](docs/provenance.md).
