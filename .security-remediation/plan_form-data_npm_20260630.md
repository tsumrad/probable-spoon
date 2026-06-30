## Security remediation — axios (npm) [transitive]

**Severity:** CRITICAL
**Action required:** Bump `axios` to `>= 4.0.6`
**Breaking change:** No
**GHSAs:** GHSA-hmw2-7cc7-3qxx, GHSA-fjxv-7rqg-78g4

> ⚠️ **Existing PR #1 is insufficient** — it bumps `axios` to `1.18.1`, which does not reach the required `4.0.6`. [View PR](https://github.com/tsumrad/probable-spoon/pull/1)

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `form-data` |
| Ecosystem | `npm` |
| Vulnerable range | `>= 4.0.0, < 4.0.6` |
| Patched vulnerable package version | `4.0.6` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `axios` |
| Required source version | `>= 4.0.6` |
| Source candidates from dependency graph | axios@0.28.1 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `form-data` |
| Vulnerable range | `>= 4.0.0, < 4.0.6` |
| Pulled in via | axios@0.28.1 |
| Fix: upgrade source to | `axios >= 4.0.6` |

### Vulnerability summary
- **GHSA-hmw2-7cc7-3qxx** (CVSS 7.5) — form-data: CRLF injection in form-data via unescaped multipart field names and filenames
- **GHSA-fjxv-7rqg-78g4** (CVSS 0.0) — form-data uses unsafe random function in form-data for choosing boundary

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `axios` to `>= 4.0.6` manually

### Notes
_Add context, blockers, or migration hints here._
