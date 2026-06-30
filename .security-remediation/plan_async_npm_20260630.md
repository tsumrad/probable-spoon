## Security remediation — save (npm) [transitive]

**Severity:** HIGH
**Action required:** Bump `save` to `>= 2.6.4`
**Breaking change:** No
**GHSAs:** GHSA-fwr7-v2mv-hh25

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `async` |
| Ecosystem | `npm` |
| Vulnerable range | `>= 2.0.0, < 2.6.4` |
| Patched vulnerable package version | `2.6.4` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `save` |
| Required source version | `>= 2.6.4` |
| Source candidates from dependency graph | save@2.4.0 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `async` |
| Vulnerable range | `>= 2.0.0, < 2.6.4` |
| Pulled in via | save@2.4.0 |
| Fix: upgrade source to | `save >= 2.6.4` |

### Vulnerability summary
- **GHSA-fwr7-v2mv-hh25** (CVSS 7.8) — Prototype Pollution in async

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `save` to `>= 2.6.4` manually

### Notes
_Add context, blockers, or migration hints here._
