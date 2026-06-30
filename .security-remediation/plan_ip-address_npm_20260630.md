## Security remediation — node-sass (npm) [transitive]

**Severity:** MEDIUM
**Action required:** Bump `node-sass` to `>= 10.1.1`
**Breaking change:** No
**GHSAs:** GHSA-v2v4-37r5-5v8g

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `ip-address` |
| Ecosystem | `npm` |
| Vulnerable range | `<= 10.1.0` |
| Patched vulnerable package version | `10.1.1` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `node-sass` |
| Required source version | `>= 10.1.1` |
| Source candidates from dependency graph | node-sass@7.0.3, socks@2.8.3 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `ip-address` |
| Vulnerable range | `<= 10.1.0` |
| Pulled in via | node-sass@7.0.3, socks@2.8.3 |
| Fix: upgrade source to | `node-sass >= 10.1.1` |

### Vulnerability summary
- **GHSA-v2v4-37r5-5v8g** (CVSS 0.0) — ip-address has XSS in Address6 HTML-emitting methods

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `node-sass` to `>= 10.1.1` manually

### Notes
_Add context, blockers, or migration hints here._
