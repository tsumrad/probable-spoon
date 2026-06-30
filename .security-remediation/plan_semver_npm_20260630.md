## Security remediation — @vue/cli-plugin-typescript (npm) [transitive]

**Severity:** HIGH
**Action required:** Bump `@vue/cli-plugin-typescript` to `>= 6.3.1`
**Breaking change:** No
**GHSAs:** GHSA-c2qf-rxjj-qqgw

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `semver` |
| Ecosystem | `npm` |
| Vulnerable range | `>= 6.0.0, < 6.3.1` |
| Patched vulnerable package version | `6.3.1` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-plugin-typescript` |
| Required source version | `>= 6.3.1` |
| Source candidates from dependency graph | @vue/cli-plugin-typescript@4.5.19, @vue/eslint-config-typescript@5.1.0, eslint-plugin-vue@6.2.2, ts-loader@6.2.2, vue-eslint-parser@7.11.0 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `semver` |
| Vulnerable range | `>= 6.0.0, < 6.3.1` |
| Pulled in via | @vue/cli-plugin-typescript@4.5.19, @vue/eslint-config-typescript@5.1.0, eslint-plugin-vue@6.2.2, ts-loader@6.2.2, vue-eslint-parser@7.11.0 |
| Fix: upgrade source to | `@vue/cli-plugin-typescript >= 6.3.1` |

### Vulnerability summary
- **GHSA-c2qf-rxjj-qqgw** (CVSS 7.5) — semver vulnerable to Regular Expression Denial of Service

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-plugin-typescript` to `>= 6.3.1` manually

### Notes
_Add context, blockers, or migration hints here._
