## Security remediation — @vue/cli-plugin-babel (npm) [transitive]

**Severity:** HIGH
**Action required:** Bump `@vue/cli-plugin-babel` to `>= 2.14.1`
**Breaking change:** No
**GHSAs:** GHSA-v6wh-96g9-6wx3, GHSA-c27g-q93r-2cwf

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `launch-editor` |
| Ecosystem | `npm` |
| Vulnerable range | `<= 2.14.0` |
| Patched vulnerable package version | `2.14.1` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-plugin-babel` |
| Required source version | `>= 2.14.1` |
| Source candidates from dependency graph | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-router@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, @vue/cli-shared-utils@4.5.19, launch-editor-middleware@2.8.0 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `launch-editor` |
| Vulnerable range | `<= 2.14.0` |
| Pulled in via | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-router@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, @vue/cli-shared-utils@4.5.19, launch-editor-middleware@2.8.0 |
| Fix: upgrade source to | `@vue/cli-plugin-babel >= 2.14.1` |

### Vulnerability summary
- **GHSA-v6wh-96g9-6wx3** (CVSS 0.0) — launch-editor: NTLMv2 hash disclosure via UNC path handling on Windows
- **GHSA-c27g-q93r-2cwf** (CVSS 0.0) — launch-editor vulnerable to command injection via the crafted request on Windows

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-plugin-babel` to `>= 2.14.1` manually

### Notes
_Add context, blockers, or migration hints here._
