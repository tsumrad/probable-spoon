## Security remediation — eslint (npm) [transitive]

**Severity:** HIGH
**Action required:** Bump `eslint` to `>= 3.4.2`
**Breaking change:** No
**GHSAs:** GHSA-rf6f-7fwh-wjgh

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `flatted` |
| Ecosystem | `npm` |
| Vulnerable range | `<= 3.4.1` |
| Patched vulnerable package version | `3.4.2` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `eslint` |
| Required source version | `>= 3.4.2` |
| Source candidates from dependency graph | eslint@6.8.0, flat-cache@2.0.1 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `flatted` |
| Vulnerable range | `<= 3.4.1` |
| Pulled in via | eslint@6.8.0, flat-cache@2.0.1 |
| Fix: upgrade source to | `eslint >= 3.4.2` |

### Vulnerability summary
- **GHSA-rf6f-7fwh-wjgh** (CVSS 0.0) — Prototype Pollution via parse() in NodeJS flatted

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `eslint` to `>= 3.4.2` manually

### Notes
_Add context, blockers, or migration hints here._
