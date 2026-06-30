## Security remediation — @vue/cli-plugin-babel (npm) [transitive]

**Severity:** CRITICAL
**Action required:** Bump `@vue/cli-plugin-babel` to `>= 3.1.3`
**Breaking change:** No
**GHSAs:** GHSA-v62p-rq8g-8h59, GHSA-h7cp-r72f-jxh6

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `pbkdf2` |
| Ecosystem | `npm` |
| Vulnerable range | `>= 1.0.0, <= 3.1.2` |
| Patched vulnerable package version | `3.1.3` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-plugin-babel` |
| Required source version | `>= 3.1.3` |
| Source candidates from dependency graph | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, crypto-browserify@3.12.0, parse-asn1@5.1.7 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `pbkdf2` |
| Vulnerable range | `>= 1.0.0, <= 3.1.2` |
| Pulled in via | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, crypto-browserify@3.12.0, parse-asn1@5.1.7 |
| Fix: upgrade source to | `@vue/cli-plugin-babel >= 3.1.3` |

### Vulnerability summary
- **GHSA-v62p-rq8g-8h59** (CVSS 0.0) — pbkdf2 silently disregards Uint8Array input, returning static keys
- **GHSA-h7cp-r72f-jxh6** (CVSS 0.0) — pbkdf2 returns predictable uninitialized/zero-filled memory for non-normalized or unimplemented algos

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-plugin-babel` to `>= 3.1.3` manually

### Notes
_Add context, blockers, or migration hints here._
