## Security remediation — @vue/cli-plugin-babel (npm) [transitive]

**Severity:** CRITICAL
**Action required:** Bump `@vue/cli-plugin-babel` to `>= 1.0.5`
**Breaking change:** No
**GHSAs:** GHSA-cpq7-6gpm-g9rc

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `cipher-base` |
| Ecosystem | `npm` |
| Vulnerable range | `<= 1.0.4` |
| Patched vulnerable package version | `1.0.5` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-plugin-babel` |
| Required source version | `>= 1.0.5` |
| Source candidates from dependency graph | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, browserify-aes@1.2.0, browserify-des@1.0.2, create-hash@1.2.0, create-hmac@1.1.7 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `cipher-base` |
| Vulnerable range | `<= 1.0.4` |
| Pulled in via | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, browserify-aes@1.2.0, browserify-des@1.0.2, create-hash@1.2.0, create-hmac@1.1.7 |
| Fix: upgrade source to | `@vue/cli-plugin-babel >= 1.0.5` |

### Vulnerability summary
- **GHSA-cpq7-6gpm-g9rc** (CVSS 9.1) — cipher-base is missing type checks, leading to hash rewind and passing on crafted data

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-plugin-babel` to `>= 1.0.5` manually

### Notes
_Add context, blockers, or migration hints here._
