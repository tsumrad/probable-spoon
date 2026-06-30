## Security remediation — @vue/cli-plugin-typescript (npm) [transitive]

**Severity:** HIGH
**Action required:** Bump `@vue/cli-plugin-typescript` to `>= 2.3.2`
**Breaking change:** No
**GHSAs:** GHSA-3v7f-55p6-f55p, GHSA-c2c7-rcm5-vvqj

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `picomatch` |
| Ecosystem | `npm` |
| Vulnerable range | `< 2.3.2` |
| Patched vulnerable package version | `2.3.2` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-plugin-typescript` |
| Required source version | `>= 2.3.2` |
| Source candidates from dependency graph | @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, jest@30.3.0, sass@1.32.13, ts-loader@6.2.2, anymatch@3.1.3, micromatch@4.0.4, readdirp@3.6.0 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `picomatch` |
| Vulnerable range | `< 2.3.2` |
| Pulled in via | @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, jest@30.3.0, sass@1.32.13, ts-loader@6.2.2, anymatch@3.1.3, micromatch@4.0.4, readdirp@3.6.0 |
| Fix: upgrade source to | `@vue/cli-plugin-typescript >= 2.3.2` |

### Vulnerability summary
- **GHSA-3v7f-55p6-f55p** (CVSS 5.3) — Picomatch: Method Injection in POSIX Character Classes causes incorrect Glob Matching
- **GHSA-c2c7-rcm5-vvqj** (CVSS 7.5) — Picomatch has a ReDoS vulnerability via extglob quantifiers

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-plugin-typescript` to `>= 2.3.2` manually

### Notes
_Add context, blockers, or migration hints here._
