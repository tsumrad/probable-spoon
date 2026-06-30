## Security remediation — @vue/cli-plugin-babel (npm) [transitive]

**Severity:** MEDIUM
**Action required:** Bump `@vue/cli-plugin-babel` to `>= 11.1.1`
**Breaking change:** No
**GHSAs:** GHSA-w5hq-g745-h8pq

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `uuid` |
| Ecosystem | `npm` |
| Vulnerable range | `< 11.1.1` |
| Patched vulnerable package version | `11.1.1` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-plugin-babel` |
| Required source version | `>= 11.1.1` |
| Source candidates from dependency graph | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-router@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, node-sass@7.0.3, sockjs@0.3.24, request@2.88.2, webpack-log@2.0.0 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `uuid` |
| Vulnerable range | `< 11.1.1` |
| Pulled in via | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-router@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, node-sass@7.0.3, sockjs@0.3.24, request@2.88.2, webpack-log@2.0.0 |
| Fix: upgrade source to | `@vue/cli-plugin-babel >= 11.1.1` |

### Vulnerability summary
- **GHSA-w5hq-g745-h8pq** (CVSS 7.5) — uuid: Missing buffer bounds check in v3/v5/v6 when buf is provided

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-plugin-babel` to `>= 11.1.1` manually

### Notes
_Add context, blockers, or migration hints here._
