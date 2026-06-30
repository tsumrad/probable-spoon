## Security remediation — bootstrap-vue (npm) [transitive]

**Severity:** HIGH
**Action required:** Bump `bootstrap-vue` to `>= 2.6.7`
**Breaking change:** No
**GHSAs:** GHSA-r683-j2x4-v87g

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `node-fetch` |
| Ecosystem | `npm` |
| Vulnerable range | `< 2.6.7` |
| Patched vulnerable package version | `2.6.7` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `bootstrap-vue` |
| Required source version | `>= 2.6.7` |
| Source candidates from dependency graph | bootstrap-vue@2.21.2, @nuxt/opencollective@0.3.2 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `node-fetch` |
| Vulnerable range | `< 2.6.7` |
| Pulled in via | bootstrap-vue@2.21.2, @nuxt/opencollective@0.3.2 |
| Fix: upgrade source to | `bootstrap-vue >= 2.6.7` |

### Vulnerability summary
- **GHSA-r683-j2x4-v87g** (CVSS 8.8) — node-fetch forwards secure headers to untrusted sites

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `bootstrap-vue` to `>= 2.6.7` manually

### Notes
_Add context, blockers, or migration hints here._
