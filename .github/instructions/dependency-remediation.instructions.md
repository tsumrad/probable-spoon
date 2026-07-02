---
description: Security dependency remediation workflow
applyTo: "**/package.json,**/package-lock.json,**/yarn.lock,**/pnpm-lock.yaml,**/pyproject.toml,**/poetry.lock,**/requirements*.txt,**/pom.xml,**/build.gradle,**/build.gradle.kts,**/gradle.properties"
---

# Dependency Security Remediation

Read `plan.md` before making any changes.

Treat `plan.md` as the source of truth for:
- Vulnerable packages
- Affected package version ranges
- Fixed package versions
- Advisory identifiers (GHSA/CVE)
- Dependency paths
- Severity

For each vulnerability:

1. Determine the dependency manager and ecosystem for the affected project.
2. Use the dependency path and direct dependency information in plan.md as authoritative.
3. Update the minimum compatible direct dependency that resolves the vulnerability.
4. Avoid unnecessary major version upgrades unless required.
5. Do not manually pin or add transitive dependencies unless there is no supported remediation path.

Before making any changes:

1. Fetch the latest changes from `origin/main`.
2. If the fetch fails, stop and report the error. Do not make any repository changes.
3. Do not modify any files until the fetch completes successfully.
4. Perform all remediation work on the current branch. Do not switch branches, create a new branch, or commit changes unless explicitly instructed.

After updating dependencies:

- Regenerate the appropriate lock file using the project's package manager.
- Never manually edit generated lock files.
- Run dependency installation.
- Run the project's dependency/security validation.
- Run the project's tests if applicable.

Provide a summary including:
- Files changed
- Direct dependency changes (old → new)
- Transitive dependency versions fixed
