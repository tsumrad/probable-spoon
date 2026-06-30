## Security remediation — @vue/cli-plugin-eslint (npm) [transitive]

**Severity:** HIGH
**Action required:** Bump `@vue/cli-plugin-eslint` to `>= 0.2.6`
**Breaking change:** No
**GHSAs:** GHSA-ph9p-34f9-6g65, GHSA-52f5-9888-hmc6

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `tmp` |
| Ecosystem | `npm` |
| Vulnerable range | `< 0.2.6` |
| Patched vulnerable package version | `0.2.6` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-plugin-eslint` |
| Required source version | `>= 0.2.6` |
| Source candidates from dependency graph | @vue/cli-plugin-eslint@4.5.19, eslint@6.8.0, external-editor@3.1.0 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `tmp` |
| Vulnerable range | `< 0.2.6` |
| Pulled in via | @vue/cli-plugin-eslint@4.5.19, eslint@6.8.0, external-editor@3.1.0 |
| Fix: upgrade source to | `@vue/cli-plugin-eslint >= 0.2.6` |

### Vulnerability summary
- **GHSA-ph9p-34f9-6g65** (CVSS 0.0) — tmp has Path Traversal via unsanitized prefix/postfix that enables directory escape
- **GHSA-52f5-9888-hmc6** (CVSS 2.5) — tmp allows arbitrary temporary file / directory write via symbolic link `dir` parameter

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-plugin-eslint` to `>= 0.2.6` manually

### Notes
_Add context, blockers, or migration hints here._
