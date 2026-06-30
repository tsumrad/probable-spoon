## Security remediation — @vue/cli-plugin-babel (npm) [transitive]

**Severity:** CRITICAL
**Action required:** Bump `@vue/cli-plugin-babel` to `>= 1.8.4`
**Breaking change:** No
**GHSAs:** GHSA-w7jw-789q-3m8p

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `shell-quote` |
| Ecosystem | `npm` |
| Vulnerable range | `>= 1.1.0, <= 1.8.3` |
| Patched vulnerable package version | `1.8.4` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-plugin-babel` |
| Required source version | `>= 1.8.4` |
| Source candidates from dependency graph | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-router@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, launch-editor@2.8.0 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `shell-quote` |
| Vulnerable range | `>= 1.1.0, <= 1.8.3` |
| Pulled in via | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-router@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, launch-editor@2.8.0 |
| Fix: upgrade source to | `@vue/cli-plugin-babel >= 1.8.4` |

### Vulnerability summary
- **GHSA-w7jw-789q-3m8p** (CVSS 8.1) — shell-quote quote() does not escape newlines in object .op values

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-plugin-babel` to `>= 1.8.4` manually

### Notes
_Add context, blockers, or migration hints here._
