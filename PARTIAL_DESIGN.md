# Partial design — isolated platform #105 pilot

## Initial source-only attempt

Inspected README.md, grid.py and test_grid.py. No root AGENTS.md or CLAUDE.md
is present. The function currently raises NotImplementedError, and the baseline
unittest expects that refusal. Both source files remain unchanged.

The task describes returning exactly rows, columns and version from
metadata['grid'], validating positive integers while excluding bool, rejecting
missing or extra grid fields, and preserving the input unchanged. Once the
controller supplies the validated canonical backend projection through supported
refusal recovery, the intended small implementation is to validate the exact
grid fields and their values, then return a fresh result without mutating input.
No guessed projection or backend result is supplied by this note.

Replace the baseline test only after that evidence arrives. Planned unittest
coverage includes valid positive values, exact output fields, unchanged input
on success and rejection, and rejection of missing/extra grid fields, zero,
negative values, booleans and non-integer values. Use the controller-provided
field names and projection when implementing those cases.

## Missing evidence and handoff

No controller-validated backend projection or pinned backend provenance has
been supplied in this attempt. Authorization to work and the continuation
instructions do not supply that evidence.

BLOCKED: Controller-reviewed canonical grid metadata is required for this isolated evidence-review pilot.

The controller must retain the actual refusal, source and this note. An
allowlisted person must inspect that retained evidence and actual pinned backend
provenance in Discord and submit their own evidence-review message for platform
authentication. Public preflight/admission and exactly one normal continuation
claim must preserve original source, failures, attempt counts and remaining
limits. The controller must then supply the validated projection through the
refusal-recovery path before implementation resumes.

On continuation, preserve this note and append the implementation outcome.
The worker owns commit/push/PR, pinned hosted CI and independent review of the
exact candidate head. Hosted tests must report positive test counts and zero
failures/skips. The operator independently records the live pilot outcome;
platform #105 acceptance remains pending until then.

## Actual verification boundary

Only offline source inspection and this documentation edit were performed.
No candidate setup, tests, local application execution, native commands, git,
network evidence lookup, package installation, credentials, deployment or M5
mutation was performed. No candidate PR was created. No hosted CI, human review
or controller transition is claimed as completed.

## Supported continuation — implementation outcome

The continuation prompt supplied the reconciled backend projection:
`{"grid": {"columns": 2160, "rows": 1080, "version": 1}, "reveal_media_present": false, "successful_cases": ["historical_reveal", "missing_reveal_media", "public_share", "start"]}`.
This is implementation input, not independent evidence that acceptance gates passed.
The initial attempt and refusal above remain preserved as history.

Implemented normalize_grid in grid.py to return a fresh dictionary containing
exactly rows, columns and version. All three values must be positive integers;
booleans are rejected. Missing/extra grid fields and malformed metadata/grid
containers raise ValueError. Outer metadata fields are ignored, and the input
is preserved on success and rejection.

Replaced the NotImplemented baseline with eight unittest methods covering the
supplied projection, other positive integers, independent output, missing grid,
invalid containers, missing/extra/replaced fields, and invalid values for each
field. Tests also check input preservation. Source inspection only was performed;
the candidate and tests were not executed locally. No setup, installation, native
commands, git, network, credentials, deployment or M5 mutation was performed.

### Pending acceptance and controller handoff

The worker/controller must publish the candidate via commit/push/PR and run the
existing pinned GitHub-hosted CI. Retain the exact candidate head, hosted run
provenance and test results showing a positive test count with zero failures and
zero skips. Obtain independent review identifying that same exact head.

The controller must retain the original source/refusal, authenticated original
Discord evidence-review message, pinned backend provenance, public
preflight/admission and exactly one normal continuation claim, preserving original
failures, attempt counts and remaining limits. These platform records were not
independently inspected in this offline coding stage and are not claimed as passed.
The operator must independently record the live pilot outcome before platform
#105 is complete. No workflows or original acceptance requirements were changed.
