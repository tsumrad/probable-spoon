## Security remediation — moment-timezone (npm) [transitive]

**Severity:** HIGH
**Action required:** Bump `moment-timezone` to `>= 2.29.4`
**Breaking change:** No
**GHSAs:** GHSA-wc69-rhjr-hc9g, GHSA-8hfj-j24r-96c4

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `moment` |
| Ecosystem | `npm` |
| Vulnerable range | `>= 2.18.0, < 2.29.4` |
| Patched vulnerable package version | `2.29.4` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `moment-timezone` |
| Required source version | `>= 2.29.4` |
| Source candidates from dependency graph | moment-timezone@0.5.34 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `moment` |
| Vulnerable range | `>= 2.18.0, < 2.29.4` |
| Pulled in via | moment-timezone@0.5.34 |
| Fix: upgrade source to | `moment-timezone >= 2.29.4` |

### Vulnerability summary
- **GHSA-wc69-rhjr-hc9g** (CVSS 7.5) — Moment.js vulnerable to Inefficient Regular Expression Complexity
- **GHSA-8hfj-j24r-96c4** (CVSS 7.5) — Path Traversal: 'dir/../../filename' in moment.locale

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `moment-timezone` to `>= 2.29.4` manually

### Notes
_Add context, blockers, or migration hints here._
