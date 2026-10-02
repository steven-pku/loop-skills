# Security

This skill is **instruction-only by design**: no scripts, no dependencies, no
network calls of its own, nothing that auto-executes at install or runtime.
The entire behavior is plain markdown you can read before installing —
`SKILL.md` plus `references/`, `assets/`, and `examples/`.

What that means in practice:

- Installing the skill adds text files to your agent's skills directory and
  nothing else. There is no `npm install`, no postinstall hook, no binary.
- Any web access (fact-checking steps) happens through **your host agent's
  own tools** under your host agent's permission model; the skill only asks
  for it and degrades gracefully when it is unavailable.
- The attack surface is prompt-injection-shaped, not code-execution-shaped:
  if a future change ever adds an instruction that tries to exfiltrate your
  draft or call tools outside the documented workflow, that is a
  vulnerability here.

## Untrusted Content Contract

The skill routinely reads material the user did not write: web pages and
search results during fact-checking, linked sources, and drafts submitted
for QA. All of it is treated as **data, not instructions**:

- Embedded commands inside fetched or submitted content ("ignore previous
  instructions", "call this tool", "upload/send this") must not be obeyed;
  only the user's own messages direct the workflow. This contract lives in
  the runtime instructions (`SKILL.md` Operating Principles and
  `references/fact-check-pass.md`), not just in this document.
- Unpublished drafts, client names, and internal facts stay offline by
  default; web verification sends only minimal, desensitized claims (see
  the confidentiality preflight in `references/fact-check-pass.md`).
- The skill itself stores nothing, but your host agent, model provider, or
  chat history may retain what passes through it — apply your own
  confidentiality judgment at that layer too.

## Reporting

Use a [GitHub issue](https://github.com/steven-pku/loop-article-writer/issues)
for a sanitized report. Do not include private drafts, credentials, personal
information, or an exploit that would expose them. Instruction-only content can
still cause sensitive disclosures. If the repository offers private vulnerability
reporting, use that for sensitive details; otherwise request a private contact
without disclosing the details in public.
