## Security remediation — node-sass (npm) [transitive]

**Severity:** HIGH
**Action required:** Bump `node-sass` to `>= 4.1.1`
**Breaking change:** No
**GHSAs:** GHSA-rc47-6667-2j5j

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `http-cache-semantics` |
| Ecosystem | `npm` |
| Vulnerable range | `< 4.1.1` |
| Patched vulnerable package version | `4.1.1` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `node-sass` |
| Required source version | `>= 4.1.1` |
| Source candidates from dependency graph | node-sass@7.0.3, vue-resource@1.5.3, cacheable-request@7.0.2, make-fetch-happen@9.1.0 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `http-cache-semantics` |
| Vulnerable range | `< 4.1.1` |
| Pulled in via | node-sass@7.0.3, vue-resource@1.5.3, cacheable-request@7.0.2, make-fetch-happen@9.1.0 |
| Fix: upgrade source to | `node-sass >= 4.1.1` |

### Vulnerability summary
- **GHSA-rc47-6667-2j5j** (CVSS 7.5) — http-cache-semantics vulnerable to Regular Expression Denial of Service

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `node-sass` to `>= 4.1.1` manually

### Notes
_Add context, blockers, or migration hints here._
