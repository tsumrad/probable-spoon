## Security remediation — @vue/cli-plugin-babel (npm) [transitive]

**Severity:** HIGH
**Action required:** Bump `@vue/cli-plugin-babel` to `>= 3.0.3`
**Breaking change:** No
**GHSAs:** GHSA-grv7-fg5c-xmjg

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `braces` |
| Ecosystem | `npm` |
| Vulnerable range | `< 3.0.3` |
| Patched vulnerable package version | `3.0.3` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-plugin-babel` |
| Required source version | `>= 3.0.3` |
| Source candidates from dependency graph | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, sass@1.32.13, ts-loader@6.2.2, chokidar@3.5.2, micromatch@4.0.4, chokidar@2.1.8, micromatch@3.1.10 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `braces` |
| Vulnerable range | `< 3.0.3` |
| Pulled in via | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, sass@1.32.13, ts-loader@6.2.2, chokidar@3.5.2, micromatch@4.0.4, chokidar@2.1.8, micromatch@3.1.10 |
| Fix: upgrade source to | `@vue/cli-plugin-babel >= 3.0.3` |

### Vulnerability summary
- **GHSA-grv7-fg5c-xmjg** (CVSS 7.5) — Uncontrolled resource consumption in braces

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-plugin-babel` to `>= 3.0.3` manually

### Notes
_Add context, blockers, or migration hints here._
