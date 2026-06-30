## Security remediation — node-sass (npm) [transitive]

**Severity:** HIGH
**Action required:** Bump `node-sass` to `>= 7.5.16`
**Breaking change:** No
**GHSAs:** GHSA-vmf3-w455-68vh, GHSA-9ppj-qmqm-q256, GHSA-qffp-2rhf-9h96, GHSA-83g3-92jg-28cx, GHSA-34x7-hfp2-rc4v, GHSA-r6q2-hw4h-h46w, GHSA-8qq5-rm4j-mr97

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `tar` |
| Ecosystem | `npm` |
| Vulnerable range | `<= 7.5.15` |
| Patched vulnerable package version | `7.5.16` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `node-sass` |
| Required source version | `>= 7.5.16` |
| Source candidates from dependency graph | node-sass@7.0.3, cacache@15.3.0, node-gyp@8.4.1 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `tar` |
| Vulnerable range | `<= 7.5.15` |
| Pulled in via | node-sass@7.0.3, cacache@15.3.0, node-gyp@8.4.1 |
| Fix: upgrade source to | `node-sass >= 7.5.16` |

### Vulnerability summary
- **GHSA-vmf3-w455-68vh** (CVSS 0.0) — node-tar applies PAX size override to intermediary GNU long-name/long-link headers, causing tar parser interpretation differential (file smuggling)
- **GHSA-9ppj-qmqm-q256** (CVSS 0.0) — node-tar Symlink Path Traversal via Drive-Relative Linkpath
- **GHSA-qffp-2rhf-9h96** (CVSS 0.0) — tar has Hardlink Path Traversal via Drive-Relative Linkpath
- **GHSA-83g3-92jg-28cx** (CVSS 7.1) — Arbitrary File Read/Write via Hardlink Target Escape Through Symlink Chain in node-tar Extraction
- **GHSA-34x7-hfp2-rc4v** (CVSS 8.2) — node-tar Vulnerable to Arbitrary File Creation/Overwrite via Hardlink Path Traversal
- **GHSA-r6q2-hw4h-h46w** (CVSS 8.8) — Race Condition in node-tar Path Reservations via Unicode Ligature Collisions on macOS APFS
- **GHSA-8qq5-rm4j-mr97** (CVSS 0.0) — node-tar is Vulnerable to Arbitrary File Overwrite and Symlink Poisoning via Insufficient Path Sanitization

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `node-sass` to `>= 7.5.16` manually

### Notes
_Add context, blockers, or migration hints here._
