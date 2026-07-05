---
description: Security dependency remediation workflow
applyTo: "**/package.json,**/package-lock.json,**/yarn.lock,**/pnpm-lock.yaml,**/pyproject.toml,**/poetry.lock,**/requirements*.txt,**/pom.xml,**/build.gradle,**/build.gradle.kts,**/gradle.properties"
---

# Dependency Security Remediation

Locate the remediation plan file(s) in this repository before making any
changes. The filename follows the pattern `plan*.md` (e.g.
`remediation-plan/plan-high-non-breaking.md`) — the exact suffix is
dynamic and encodes severity and/or impact; only the `plan` prefix is
guaranteed. Do not assume a literal filename of `plan.md`.

If more than one `plan*.md` file exists on this branch, read and apply
**all** of them — do not process only the first match.

Treat the contents of every matched plan file as the source of truth for:

* Vulnerable packages
* Affected package version ranges
* Fixed package versions
* Advisory identifiers (GHSA/CVE)
* Severity

Use the project manifest and lockfile as the source of truth for:

* Whether a package is direct or transitive
* Actual dependency paths
* Current installed versions
* The nearest declared parent dependency for transitive vulnerabilities

## Before Making Changes

1. Fetch the latest changes from `origin/main`.
2. If the fetch fails, stop immediately and report the error.
3. Do not modify any files until the fetch completes successfully.
4. Perform all remediation work on the current branch.
5. Do not switch branches, create a new branch, or commit changes unless explicitly instructed.

## Non-Breaking Remediation Strategy

For each vulnerability:

1. Determine the dependency manager and ecosystem.
2. Verify whether the vulnerable package is a direct dependency using the project manifest.
3. If the package is direct:

   * Update it to the lowest compatible fixed version.
4. If the package is transitive:

   * Do **not** add it as a new direct dependency.
   * Use the dependency graph to identify the nearest declared parent dependency.
   * Update that declared parent dependency to the lowest compatible version that resolves the vulnerability.
5. Use `overrides`, `resolutions`, or similar mechanisms only as a documented fallback when no supported non-breaking parent dependency upgrade exists.
6. Avoid unnecessary major version upgrades.

### Transitive Fixes and Overrides — Range Classification

When step 5 above applies (no supported parent upgrade exists) and an
override/resolution is used, classify it before applying:

* **Within range** — the forced version falls within the range the
  current direct parent's manifest already declares for that transitive
  package (compare against the parent version actually resolved in the
  current lockfile, not just the parent's latest release). This is a
  same-major, in-range override. Treat it as non-breaking and continue
  under this section's rules.
* **Outside range / cross-major** — the forced version falls outside what
  the resolved parent declares (e.g. parent declares `^4.1.0` but the
  required fix version is `5.2.5`). This is a forced override the parent
  was never built or tested against. Do not treat this as a routine
  non-breaking override — classify and handle it under the **Breaking
  Dependency Upgrade Policy** below instead, even though no direct
  dependency version number changed.

"No newer parent release exists" (including an unmaintained or
already-latest parent) is not by itself a reason to escalate to manual
review — proceed with the override fallback and classify it per the two
cases above.

## Lockfile

After applying all planned **non-breaking** dependency updates (including
in-range overrides per the classification above):

* Regenerate the appropriate lockfile once using the project's package manager.
* Never manually edit generated lockfiles.
* Run dependency installation only if required to regenerate or verify the lockfile.
* Do not run build, tests, or lint locally for non-breaking changes unless
  explicitly requested. Pull request CI is the source of truth for
  validation of non-breaking remediations.

This local-validation exemption does **not** apply to breaking upgrades or
cross-major overrides — see the Breaking Dependency Upgrade Policy below,
which requires local build and test validation as part of its revert/keep
decision gate. Local validation is required there because the decision to
keep or revert the change must be made immediately, before a PR/CI cycle
would return a result.

## Breaking Dependency Upgrade Policy

For any remediation classified as a **breaking upgrade** (including direct
major upgrades, forced transitive major upgrades, framework/runtime
upgrades, or cross-major `overrides`/`resolutions` per the classification
above), follow these rules.

### Classification

1. Classify the remediation as **breaking** according to the existing fix-class rules.

### Coordinated Upgrade Requirement

2. Only attempt the upgrade if a complete coordinated upgrade set can be identified.

A coordinated upgrade set consists of every dependency that must be
upgraded together because of shared framework, runtime, platform, or API
compatibility — not merely because they appear in the dependency graph.

Do **not** upgrade a breaking dependency in isolation if it is known or
expected to be incompatible with other currently pinned packages.

### Validation

If a coordinated upgrade (or cross-major override) is attempted:

* Apply all required dependency updates together.
* Regenerate the appropriate lockfile.
* Never manually edit generated lockfiles.
* Perform a full dependency installation.
* Run the project build.
* Run the full test suite.

These steps are run **locally, immediately**, regardless of the
non-breaking Lockfile section's CI-only guidance above — the revert/keep
decision below depends on the result being known now, not after a
separate CI cycle.

### Failure Handling

If dependency installation, build, or tests fail:

* Revert **all** changes from the breaking upgrade attempt.
* Do **not** leave the repository in a partially migrated state.
* Classify the remediation as **Manual Review Required**.
* Record the reason in the remediation summary.

### Successful Validation

If installation, build, and tests all succeed:

* Keep the coordinated upgrade.
* Mark the remediation as **Manual Review Required**.
* Never automatically merge or approve a breaking dependency upgrade, even if all automated validation succeeds.

Include the following note in the remediation summary:

> Build and tests passed, but this is a breaking framework upgrade. Automated validation cannot guarantee compatibility or detect all functional, behavioral, runtime, or visual regressions. Manual verification is recommended before merge.

### Unsupported Breaking Upgrades

If a complete coordinated upgrade set cannot be confidently determined — for example, because the migration requires:

* application source code changes,
* framework migration,
* replacement of removed packages,
* bootstrap or runtime initialization changes,
* build tooling or configuration changes,
* API migration,
* or other non-dependency modifications,

then:

* Do **not** attempt the upgrade.
* Do **not** perform a partial upgrade.
* Classify the remediation as **Manual Review Required**.
* Describe the required coordinated dependency and application changes in the remediation summary.

## Remediation Summary

Provide a summary including:

* Files changed.
* Direct dependency updates (`old → new`).
* Parent dependency updates performed to remediate transitive vulnerabilities.
* Transitive vulnerabilities resolved.
* `overrides`/`resolutions` used, whether each was within-range or
  cross-major, and the rationale for each.
* Breaking upgrades attempted and their outcome.
* Vulnerabilities that could not be remediated automatically and the reason.
* Manual review items and recommended follow-up actions.
