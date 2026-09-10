# Decision and voting register — proposed starting backlog

Status: **no ballots opened; no votes cast; no decisions adopted**. This is a proposed
agenda, not a reconstructed record of consensus. Historical D09–D15 and experimental PR
merges are evidence references only and do not populate the adopted column.

## Ratification matrix

| ID | Decision to agree | Proposed starting option | Real alternative | Rule | Sequence / dependency | Status |
|---|---|---|---|---|---|---|
| DP-001 | Initial convening and public scope | Asle and Dmytro act as equal interim conveners, with explicit consent | Another convening arrangement or existing standards host | B0, both explicit responses | First | Proposed |
| DP-002 | Voting unit and representation | One independent party/one vote; P/C/other primary constituency | Individual voting with anti-dominance rules; host body's existing rules | G bootstrap | DP-001; accept bootstrap roster/mechanics first | Proposed |
| DP-003 | Consensus, thresholds, objections and appeals | PROCESS sections 5–7, including cross-constituency support | Consensus-only with external mediation; different balanced thresholds | G bootstrap | DP-002; jointly ratify with DP-004/005 | Proposed |
| DP-004 | Participation, rights and stewardship | Open contributions; agreed rights policy; independent custodians | Join a suitable standards-development host and adopt its framework | G bootstrap | Actual rights/owner consent required | Proposed |
| DP-005 | Seasonal work and stable-edition cadence | Two planning seasons; nominal 16-week cycles; at most one ordinary stable edition/year | One annual cycle; demand-driven revisions | G bootstrap | DP-003 | Proposed |
| DP-006 | Historical experiment separation and edition naming | Preserve EXP-001 separately; explicit new adoption baseline | Retain selected historical material after full review with distinct status | G for namespace/ownership; N for technical version mapping | DP-004; no automatic repo moves | Proposed |
| DP-007 | Outreach and first participant journey | Public problem brief, open examples, review clinics, response owners | Existing partner forums as entry points with public recap | O after charter; G if obligations change | DP-001–005; obtain communication permissions | Proposed |
| DP-101 | Coordinates and units | Small explicit shared convention from producer/consumer examples | Other coherent convention justified by exchanges | N | Ratified process and S1 scope | Backlog |
| DP-102 | Geometry and ordering | Smallest unambiguous initial primitive set | Larger primitive set; sampled trajectory model | N | UC evidence; DP-101 | Backlog |
| DP-103 | Orientation and process information | Explicit needs for robotics and AM; no guessed defaults | Process-specific modules vs shared fields | N | UC evidence; do not preselect Euler or power semantics | Backlog |
| DP-201 | First wire contract and version identity | Human-readable JSON candidate | Alternative justified by actual exchange requirements | N | DP-101–103 | Backlog |
| DP-202 | Missing, unknown and unsupported data | Explicit compatibility and refusal rules | Alternative preservation/capability mechanisms | N | DP-201 | Backlog |
| DP-203 | Tool/context references and packaging | Minimum referential context required by use cases | Standalone documents; container only as optional module | N | DP-201/202 | Backlog |

A G bootstrap packet may be discussed together, but each numbered choice remains visible
and splittable. Any conflict between alternatives must be settled before the bootstrap
ratification ballot; this document cannot establish its own legitimacy by arithmetic alone.

## Option comparison matrix — for each DP

Use a qualitative finding plus evidence link; do not manufacture numerical certainty.

| Criterion | Option A | Option B | Defer / smaller option | Agreed hard requirement? |
|---|---|---|---|---|
| Producer need met | Pending | Pending | Pending | Pending |
| Consumer need met | Pending | Pending | Pending | Pending |
| Semantic clarity / interoperability | Pending | Pending | Pending | Pending |
| Implementation and maintenance burden | Pending | Pending | Pending | Pending |
| Compatibility and migration cost | Pending | Pending | Pending | Pending |
| Independence from one vendor/SDK | Pending | Pending | Pending | Pending |
| Rights/dependencies and accessibility | Pending | Pending | Pending | Pending |
| Evidence against this option / remaining uncertainty | Pending | Pending | Pending | — |

## Ballot matrix — instantiate only for a ready decision

| Party ID | Primary constituency | Representative / alternate | DP and exact text hash | Yes / No / Abstain | Rationale / OB references | UTC timestamp |
|---|---|---|---|---|---|---|
| Not yet constituted | — | — | — | No ballot | — | — |

Each DP has a separate tally: N, Y, V, A, U, quorum, numeric threshold, P support, C support,
evidence gates, appeals and result. “No response” is a distinct register entry, never Yes.
Include roster freeze/start/end times and the rule/process revision used. Do not replace
named positions with a green checkmark on a GitHub PR.

## Worked arithmetic — hypothetical, not participant votes

Six parties: two P, two C, two O. N/R threshold=4 Yes; quorum=4 participants; cross-support
requires both P and both C. Four Yes from the two P and two C pass if other gates pass.
Four Yes from two P and two O fail cross-support. Three Yes plus two Abstain fail the
support threshold despite quorum. For G, five Yes and cross-support are required.
