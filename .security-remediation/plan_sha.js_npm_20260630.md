## Security remediation — @vue/cli-plugin-babel (npm) [transitive]

**Severity:** CRITICAL
**Action required:** Bump `@vue/cli-plugin-babel` to `>= 2.4.12`
**Breaking change:** No
**GHSAs:** GHSA-95m3-7q98-8xr5

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `sha.js` |
| Ecosystem | `npm` |
| Vulnerable range | `<= 2.4.11` |
| Patched vulnerable package version | `2.4.12` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-plugin-babel` |
| Required source version | `>= 2.4.12` |
| Source candidates from dependency graph | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, create-hash@1.2.0, create-hmac@1.1.7, pbkdf2@3.1.2 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `sha.js` |
| Vulnerable range | `<= 2.4.11` |
| Pulled in via | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, create-hash@1.2.0, create-hmac@1.1.7, pbkdf2@3.1.2 |
| Fix: upgrade source to | `@vue/cli-plugin-babel >= 2.4.12` |

### Vulnerability summary
- **GHSA-95m3-7q98-8xr5** (CVSS 9.1) — sha.js is missing type checks leading to hash rewind and passing on crafted data

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-plugin-babel` to `>= 2.4.12` manually

### Notes
_Add context, blockers, or migration hints here._
