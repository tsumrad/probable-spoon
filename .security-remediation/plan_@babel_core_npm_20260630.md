## Security remediation — @vue/cli-plugin-babel (npm) [transitive]

**Severity:** LOW
**Action required:** Bump `@vue/cli-plugin-babel` to `>= 7.29.6`
**Breaking change:** No
**GHSAs:** GHSA-4x5r-pxfx-6jf8

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `@babel/core` |
| Ecosystem | `npm` |
| Vulnerable range | `<= 7.29.0` |
| Patched vulnerable package version | `7.29.6` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-plugin-babel` |
| Required source version | `>= 7.29.6` |
| Source candidates from dependency graph | @vue/cli-plugin-babel@4.5.19, jest@30.3.0, @jest/transform@30.3.0, @vue/babel-preset-app@4.5.19, istanbul-lib-instrument@6.0.3, jest-config@30.3.0, jest-snapshot@30.3.0 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `@babel/core` |
| Vulnerable range | `<= 7.29.0` |
| Pulled in via | @vue/cli-plugin-babel@4.5.19, jest@30.3.0, @jest/transform@30.3.0, @vue/babel-preset-app@4.5.19, istanbul-lib-instrument@6.0.3, jest-config@30.3.0, jest-snapshot@30.3.0 |
| Fix: upgrade source to | `@vue/cli-plugin-babel >= 7.29.6` |

### Vulnerability summary
- **GHSA-4x5r-pxfx-6jf8** (CVSS 3.2) — @babel/core: Arbitrary File Read via sourceMappingURL Comment

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-plugin-babel` to `>= 7.29.6` manually

### Notes
_Add context, blockers, or migration hints here._
