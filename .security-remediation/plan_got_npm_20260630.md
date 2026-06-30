## Security remediation — vue-resource (npm) [transitive]

**Severity:** MEDIUM
**Action required:** Bump `vue-resource` to `>= 11.8.5`
**Breaking change:** No
**GHSAs:** GHSA-pfrx-2q88-qq97

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `got` |
| Ecosystem | `npm` |
| Vulnerable range | `< 11.8.5` |
| Patched vulnerable package version | `11.8.5` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `vue-resource` |
| Required source version | `>= 11.8.5` |
| Source candidates from dependency graph | vue-resource@1.5.3 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `got` |
| Vulnerable range | `< 11.8.5` |
| Pulled in via | vue-resource@1.5.3 |
| Fix: upgrade source to | `vue-resource >= 11.8.5` |

### Vulnerability summary
- **GHSA-pfrx-2q88-qq97** (CVSS 5.3) — Got allows a redirect to a UNIX socket

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `vue-resource` to `>= 11.8.5` manually

### Notes
_Add context, blockers, or migration hints here._
