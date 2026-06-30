## Security remediation — eslint (npm) [transitive]

**Severity:** HIGH
**Action required:** Bump `eslint` to `>= 6.0.6`
**Breaking change:** No
**GHSAs:** GHSA-3xgq-45jj-v275

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `cross-spawn` |
| Ecosystem | `npm` |
| Vulnerable range | `< 6.0.6` |
| Patched vulnerable package version | `6.0.6` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `eslint` |
| Required source version | `>= 6.0.6` |
| Source candidates from dependency graph | eslint@6.8.0, @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-router@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, jest@30.3.0, yorkie@2.0.0, execa@1.0.0, execa@0.8.0 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `cross-spawn` |
| Vulnerable range | `< 6.0.6` |
| Pulled in via | eslint@6.8.0, @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-router@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, jest@30.3.0, yorkie@2.0.0, execa@1.0.0, execa@0.8.0 |
| Fix: upgrade source to | `eslint >= 6.0.6` |

### Vulnerability summary
- **GHSA-3xgq-45jj-v275** (CVSS 7.5) — Regular Expression Denial of Service (ReDoS) in cross-spawn

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `eslint` to `>= 6.0.6` manually

### Notes
_Add context, blockers, or migration hints here._
