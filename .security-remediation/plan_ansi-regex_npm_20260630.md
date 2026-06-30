## Security remediation — strip-ansi (npm) [transitive]

**Severity:** HIGH
**Action required:** Bump `strip-ansi` to `>= 4.1.1`
**Breaking change:** No
**GHSAs:** GHSA-93q8-gq69-wqmw

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `ansi-regex` |
| Ecosystem | `npm` |
| Vulnerable range | `>= 4.0.0, < 4.1.1` |
| Patched vulnerable package version | `4.1.1` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `strip-ansi` |
| Required source version | `>= 4.1.1` |
| Source candidates from dependency graph | strip-ansi@5.2.0 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `ansi-regex` |
| Vulnerable range | `>= 4.0.0, < 4.1.1` |
| Pulled in via | strip-ansi@5.2.0 |
| Fix: upgrade source to | `strip-ansi >= 4.1.1` |

### Vulnerability summary
- **GHSA-93q8-gq69-wqmw** (CVSS 7.5) — Inefficient Regular Expression Complexity in chalk/ansi-regex

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `strip-ansi` to `>= 4.1.1` manually

### Notes
_Add context, blockers, or migration hints here._
