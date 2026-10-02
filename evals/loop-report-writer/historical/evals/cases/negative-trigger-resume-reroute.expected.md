# Expected: Negative Trigger — 简历误路由

This is a resume request, not a workplace report.

- Skill should recognize it is out of scope (求职材料, not 在职汇报) and route to loop-resume-writer per its description exclusion clause.
- It should not run the report loop on a resume.
- Acceptable: a one-line note that the ledger/量化 discipline is shared spirit, but the actual work belongs to loop-resume-writer.
- Pass condition: correct routing to loop-resume-writer, no report-loop misfire.
- Fail condition: skill silently treats the resume as a report and QAs it on the report rubric.
