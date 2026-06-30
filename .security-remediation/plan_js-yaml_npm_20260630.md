## Security remediation — @vue/cli-plugin-typescript (npm) [transitive]

**Severity:** MEDIUM
**Action required:** Bump `@vue/cli-plugin-typescript` to `>= 3.15.0`
**Breaking change:** No
**GHSAs:** GHSA-h67p-54hq-rp68, GHSA-mh29-5h37-fv8m

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `js-yaml` |
| Ecosystem | `npm` |
| Vulnerable range | `< 3.15.0` |
| Patched vulnerable package version | `3.15.0` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-plugin-typescript` |
| Required source version | `>= 3.15.0` |
| Source candidates from dependency graph | @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, eslint@6.8.0, jest@30.3.0, @istanbuljs/load-nyc-config@1.1.0, cosmiconfig@5.2.1, svgo@1.3.2, tslint@5.20.1 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `js-yaml` |
| Vulnerable range | `< 3.15.0` |
| Pulled in via | @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, eslint@6.8.0, jest@30.3.0, @istanbuljs/load-nyc-config@1.1.0, cosmiconfig@5.2.1, svgo@1.3.2, tslint@5.20.1 |
| Fix: upgrade source to | `@vue/cli-plugin-typescript >= 3.15.0` |

### Vulnerability summary
- **GHSA-h67p-54hq-rp68** (CVSS 5.3) — JS-YAML: Quadratic-complexity DoS in merge key handling via repeated aliases
- **GHSA-mh29-5h37-fv8m** (CVSS 5.3) — js-yaml has prototype pollution in merge (<<)

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-plugin-typescript` to `>= 3.15.0` manually

### Notes
_Add context, blockers, or migration hints here._
