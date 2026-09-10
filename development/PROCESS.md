# Specification Development Process

Document: OTP-PROCESS · revision: 0.1-draft · prepared: 2026-09-10
Status: proposal for discussion; no participant has adopted this process by being named here.
Working language: English; translated comments are welcome. This document governs how
agreement would be reached, not the contents of the toolpath format.

## 1. Purpose and authority

Build a durable, jointly governed specification around demonstrated exchange needs.
Partners should be able to join, influence decisions, implement independently and plan
against stable editions. The project should remain small enough to maintain.

This process becomes effective only through the explicit bootstrap and ratification
steps in section 3. Until then, MUST and MUST NOT below describe proposed future rules.
Neither this draft, repository permissions nor an existing implementation confers authority.

Three boundaries apply:

- The specification defines exchanged data and observable behavior, not an SDK architecture.
- Experimental work contributes evidence and alternatives; it creates no presumption of adoption.
- Publication, partnership, approval and implementation are different claims and need separate records.

Asle and Dmytro are proposed equal conveners of the initial discussion, subject to their
agreement. Neither has a permanent veto, casting vote or unilateral normative authority
under the proposed steady-state process. Funding, commit count and agent throughput do
not buy additional votes.

## 2. Principles

1. Participation is open; decision rights and affiliations are visible.
2. Affected producers and consumers both participate in adoption decisions.
3. Technical objections receive a reasoned response, even when their proponents are a minority.
4. The least complex option that meets the agreed use cases is preferred. “Do nothing yet”
   is a valid option, not a failed deliverable.
5. Every adopted requirement is traceable to a need, a decision and a published edition.
6. Stable editions change deliberately; working drafts may change frequently.
7. Decisions are asynchronous and documented. Meeting attendance is not a voting prerequisite.
8. One human is accountable for every contribution, including agent-assisted contributions.

The balance and openness principles draw on [RFC 6852](https://www.rfc-editor.org/rfc/rfc6852.html).
The proposal-first, objection-aware approach draws on
[RFC 7282](https://www.rfc-editor.org/rfc/rfc7282.html), which describes IETF rough consensus
rather than majority voting. Our formal ballots below are a separate, proposed local
mechanism; they are not presented as the IETF process.

## 3. Bootstrap without manufacturing consent

### B0 — agree to convene

Asle and Dmytro explicitly agree an interim scope, public/sandbox separation and invitation
text. Record both responses. Silence is not agreement. They can prepare discussion drafts
and invite participants, but cannot claim partner endorsement or publish an adopted edition.
If they disagree, keep the proposal in the sandbox and record the unresolved choice.

The interim arrangement expires after 90 calendar days unless both renew it publicly.
It is not a perpetual two-person governing body. No organization is assigned a seat,
role, logo placement or endorsement without its own consent.

### B1 — constitute the group

Invite producers, consumers and independent research/end-user participants. Hold at least
30 calendar days of open charter/process review after invitations are published. Record
who was approached, responses and representation gaps, without publishing private contacts.

For first ratification, seek at least four independent voting parties, including at least
two primarily producer and two primarily consumer parties. This is a proposed minimum
for legitimacy, not a claim that such a group already exists. If the minimum is not met,
continue discussion and experiments; do not label a two-party result an adopted standard.

Before the ratification ballot, every proposed voting party explicitly accepts the roster,
affiliation grouping and ballot mechanics for this one bootstrap vote. A roster dispute
must be resolved first. The group then ratifies its charter and this process using rule G
in section 5. Alternatives to this draft must receive the same review opportunity.

### B2 — authorize the first season

Ratify the first season's scope, roles and decision packages. Previously published
experimental “v1.0” material is not grandfathered into the new baseline. It is identified
by its repository and commit, with an explicit notice that it predates joint adoption.

## 4. Participation, parity and roles

Anyone may submit use cases, alternatives, review comments and reproducible evidence.
Voting parties are organizations under independent control, or unaffiliated individuals.
An organization and its controlled affiliates share one vote and nominate a representative
and alternate. Employment, funding relevant to the work and representation are disclosed.
An employee cannot gain a second vote by registering as an independent individual.

Each party selects one primary constituency for a season: producer (P), consumer (C) or
other (O: research, end users or independent expertise). A company doing both may describe
both interests but occupies only one voting seat and one primary constituency. Classification
and common-control questions are reviewed publicly; disputes use the appeal mechanism.

After bootstrap, voting eligibility requires acceptance of the charter and contribution
terms, affiliation disclosure and one substantive use-case, review or evidence contribution.
These are objective criteria, not a discretionary invitation by the founders. The secretary
posts an application for 14 days; absent a documented eligibility dispute it takes effect
for ballots opened after that period. Disputed eligibility is independently reviewed before
activation. Existing members do not vote on whether they like the applicant's position.

The roster is published and frozen seven days before each ballot. New members may comment
immediately but do not change an open ballot's denominator. Resignations/affiliation changes
during a ballot trigger a roster review and restart if eligibility changes. There is no
retroactive removal of a non-voter to make a ballot pass. Membership is reconfirmed each
season; inactivity is not an excuse for excluding an inconvenient view.

Start with one working group and three functions, not a hierarchy of committees:

| Function | Responsibility | Limit |
|---|---|---|
| Two co-chairs from different parties | Facilitate scope, consensus and review; ideally represent P and C | No casting vote; a chair's preferred option has no special status |
| Editor(s) | Translate agreed decisions into precise text; maintain traceability | Cannot turn an editorial merge into a normative decision |
| Secretary/release steward | Maintain roster, minutes, ballots and publication records | Cannot certify their own release without a second-party check |

People may combine functions to reduce overhead, but an author cannot be their own sole
reviewer. Roles are elected for one season under rule O, renewable, with rotation encouraged.
Commercial interest alone does not prohibit a technical vote; it must be disclosed. A party
in a procedural dispute cannot adjudicate its own appeal. GitHub administrators act as
custodians of recorded decisions, not as an additional legislative body.

## 5. Decision classes and ballot arithmetic

Always seek agreement first: publish alternatives, solicit affected views, answer comments
and record remaining objections. A preference poll helps discussion but cannot adopt text.
Normative ballots open only after the evidence and objection gates in sections 6–8 pass.

For a frozen eligible roster, let N be all eligible parties, Y yes, V no, A abstain and
U no response. N = Y + V + A + U. Participation is Y + V + A; quorum is ceil(2N/3).
Abstention counts for quorum but not support. Silence counts for neither. An alternate
replaces their party's ballot; they do not add a vote. A tie or missed threshold fails.

“Cross-constituency support” means strictly more than half of all eligible P parties vote
yes AND strictly more than half of all eligible C parties vote yes. A stable adoption
requires at least two eligible parties in each constituency. O votes count fully in N.

| Rule | Decisions | Notice / ballot minimum | Approval |
|---|---|---|---|
| E — editorial | Spelling, links and layout; no change in meaning, obligations or accepted data | Public PR available 3 days | Editor plus reviewer from another party; no ballot |
| O — operational | Meeting arrangements, role elections, workload/order within agreed scope | 7 days notice / 7 days ballot | Quorum and Y > V; at least one P and one C participate |
| N — normative | Scope packages, data semantics, profiles, accepted-value changes, deprecation and amendments | 14 days notice / 14 days ballot | Quorum, Y >= ceil(2N/3), cross-constituency support |
| R — release | Adoption of an immutable complete edition or maintenance amendment | 14 days notice / 14 days ballot after review closes | Rule N plus all release gates |
| G — governance | Charter/process, voting rights, licensing policy, ownership/hosting transfers | 30 days review/notice / 14 days ballot | Quorum, Y >= ceil(3N/4), cross-constituency support |

All periods are calendar days with explicit UTC start/end times. Ballots follow their notice
periods; a public review may also satisfy notice, but a final release ballot opens only after
comment disposition. Holiday/travel extensions are announced before closing and apply to all.
The exact thresholds, windows and constituency model are proposals for B1 ratification,
not rules borrowed wholesale from any standards body.

Example: N=6, with two P, two C and two O parties. Quorum=4; N/R require four yes votes,
including both P and both C votes. Four yes votes from P and O with no C support fail.
Five responses containing three yes and two abstentions meet quorum but fail adoption.
G requires five yes votes plus P/C support. With N=4 and two P/two C, cross-support requires
all four yes votes; this deliberate bootstrap constraint should be reviewed after two seasons.

Any participant may challenge an E classification. If the change could alter interpretation,
accepted data or required behavior, reclassify it as N. A bug fix is not automatically editorial.
Governance changes never alter the rules for a ballot already opened. A party may update
its response before closure; retain the history and count only its latest authenticated
response for each DP. Self-recusal is recorded as abstention, not removal from N.

## 6. Decision packages and transparent checkpoints

Use stable IDs: UC-### (need), DP-### (decision), OB-### (objection), B-### (ballot),
EXP-### (experiment) and REL-### (release). An ID is never reused. The
[decision register](DECISIONS.md) records status, exact text revision, dependencies,
positions, evidence and outcomes. “Proposed”, “reviewed”, “adopted” and “released” differ.

Each season selects at most three technical decision packages; bootstrap governance is
a separate, visible packet. A package groups related decisions
around one exchange need, not one implementation's module structure. Every decision has:

- a producer/consumer use case and a named human editor;
- explicit alternatives, including deferral and a smaller option;
- intended normative text, examples and acceptance criteria;
- cost, complexity, compatibility and rights/dependency considerations;
- dependency edges and proposed core/optional/out-of-scope placement;
- evidence and unresolved objections, including evidence against the preferred option.

Use the [templates](TEMPLATES.md). Compare options with justified findings, not a weighted
score that hides policy choices. Hard requirements agreed at scope review cannot be traded
away by a high aggregate score.

| Gate | Question | Required record | Failure outcome |
|---|---|---|---|
| G0 — mandate | Is this problem in charter and season scope? | UC, affected parties, N scope decision | Backlog or charter review |
| G1 — alternatives | Is there a smaller option and an honest comparison? | DP text, options, dependencies, evidence plan | Return to drafting |
| G2 — review | Have affected parties and external reviewers had time to respond? | Frozen draft, comment log, dispositions | Revise and review again |
| G3 — decision | Are objections addressed and the ballot valid? | Frozen roster, text hash, positions, ballot arithmetic | Defer, split or reject |
| G4 — publication | Does the release match adopted decisions and evidence? | Release manifest, compatibility notes, approvals | Candidate remains unreleased |
| G5 — maintenance | Is this edition still useful and supported? | Adoption/issues review and recorded disposition | Confirm, amend, revise or withdraw |

Batch review is encouraged; bundled coercion is not. A ballot names every DP and records
Yes/No/Abstain for each. An uncontested block may use one response only if it enumerates its
DP IDs and every voter can split any item before voting. A failed DP does not pass because
its neighbors passed. Dependent DPs remain conditional until dependencies pass; a changed
premise requires affected text to return to review. The release ballot checks the resulting
coherent set and cannot quietly add a rejected item.

## 7. Review, objections and appeals

The initial public review of a normative package lasts at least 30 days. Post the exact
review artifact and announce it through the agreed public channel and relevant partner
contacts. Meetings generate proposals and minutes, never decisions binding absent parties.
Publish minutes within seven days and allow seven days for corrections.

Every comment receives an ID, owner and disposition: accepted with change; addressed by
explanation; deferred with the affected feature; or rejected with reasons. Acknowledgment
is not resolution. “Addressed” does not mean the author must agree, but their disagreement
and the response remain visible. Missing a response blocks that item's ballot.

An unresolved, evidenced ambiguity that prevents independent interpretation, a known
interoperability failure, an unaddressed essential-use-case failure or an unresolved
rights blocker prevents advancement of the affected feature. A majority cannot waive
these gates by calling the objection a preference. Co-chairs propose the disposition;
participants may challenge it. An objection alone is not an unlimited veto: the question
and evidence must be evaluated and the outcome recorded.

After material changes, publish a diff and run at least 15 days of renewed review. Reopen
all affected decisions. Editorial corrections are separately logged. This use of public
review and comment disposition is informed by the
[OASIS public-review process](https://docs.oasis-open.org/TChandbook/Reference/PublicReviews.html).

Any participant, including a non-voter, may file a procedural appeal within 14 days of the
recorded decision. The affected adoption/publication pauses. Two independent parties not
involved in the dispute review the notice, evidence, conflicts and arithmetic, and publish
a recommendation within 21 days. The parties to the dispute can each exclude one proposed
reviewer for a documented conflict; if an independent pair cannot be formed, seek mutually
acceptable external reviewers or defer. Do not have a founder decide their own appeal.
The panel may uphold or require a corrected review/reballot, but cannot substitute new
technical text. If the panel disagrees, the affected decision returns to review. Late new
technical evidence enters maintenance, not a retroactive change to the ballot tally.

The formal objection and recorded-response idea is informed by the
[W3C Process](https://www.w3.org/policies/process/). Our small-group appeal arrangement is
proposed locally; there is no claim that OpenToolpath has W3C's institutional review bodies.

## 8. Evidence without implementation capture

Specification work publishes requirements, examples and expected outcomes. Implementers
choose languages, libraries, data structures, codecs and test infrastructure independently.
No “official SDK” is required to implement or interpret an adopted clause.

Experiments may run at any time in a clearly separate namespace. Record authorship,
funding, human ownership, agent assistance where material, source revision, reproducibility,
limitations and alternatives tested. Multiple languages or multiple agents controlled by
one author do not count as independent stakeholder validation.

For a stable core edition, demonstrate at least one exchange between a producer and consumer
maintained by two independent parties. For each normative feature, show concrete coverage
and review by an affected party independent of the original proposal authors. A claimed
robotics or AM use case requires corresponding evidence; absent evidence, narrow the claim
or defer the feature. A majority cannot relabel internal tests as external adoption.

Tests establish observable behavior, not blanket certification or machine safety. Expected
outcomes trace to clauses and adopted DPs; an SDK's current behavior is not its own oracle.
Publish failures and non-covered requirements as well as passing results. Implementation
experience as a maturity criterion is informed by the
[W3C implementation-experience guidance](https://www.w3.org/policies/process/#implementation-experience).

The existing Dmytro-led implementation family is EXP-001, one historical exploration.
It may supply measurements, failure cases and option sketches. Its schema, binary layouts,
registries, profiles and earlier decision IDs do not become the new group's decisions.
Retain attribution and history; do not erase it or present it as joint ratification.

## 9. Seasons, revisions and roadmap

Use two planning seasons per year, each with a nominal 16-week decision cycle and buffer
for review, implementation and partner availability. Season labels are YYYY-A and YYYY-B;
exact dates are approved at kickoff. Seasons are work windows, not mandatory releases.
A missed gate rolls work forward; it does not lower the gate.

A typical season: weeks 1–2 needs/scope; 3–6 alternatives; 7–11 public review; 12–14
comment disposition and decisions; 15–16 integration/retrospective. Notice periods and
14-day ballots still apply. Extensions, appeals or material changes can push the result
beyond week 16. A release has its own review/ballot schedule and cannot be forced into
this outline. The first roadmap uses relative S0–S4 labels until partners agree dates.

Target no more than one ordinary stable core edition per year initially. Issue drafts
and experiment reports as useful between editions. Add optional modules only for a
supported need with ownership and maintenance capacity. Review the roadmap every season
and the process after the first two seasons, then annually.

A stable edition receives an annual maintenance assessment. At least every three years,
explicitly confirm, revise, supersede or withdraw it, even if no change is proposed.
The staged-development/systematic-review concept comes from
[ISO's development stages](https://www.iso.org/stages-and-resources-for-standards-development.html)
and [systematic-review guidance](https://www.iso.org/files/live/sites/isoorg/files/store/en/PUB100413.pdf).
The proposed 16-week and annual/three-year cadences are ours, not ISO requirements.

## 10. Versions, changelog and releases

Version the development process separately from the data specification. This proposal is
process 0.1-draft; it is not data format v0.1 or a release. Reserve the first jointly
adopted specification edition identifier at S0 after inventorying earlier experimental
names. Do not recycle “v1.0” in a way that makes old experimental files look conformant.
The edition-to-wire-version mapping is itself a DP.

Use draft IDs such as WD-S1-01 and review candidates RC-S1-01 until that naming decision.
Stable editions are immutable; tags/artifacts must not be silently replaced. “Latest”
may link to an edition but is not an artifact identifier. Date, status, superseded-by
links and exact source commit are visible on every publication.

| Change | Treatment |
|---|---|
| Typo/layout with no changed meaning | E decision; immutable corrigendum and changelog entry |
| A correction changing accepted data or required behavior | N review plus R maintenance amendment; never a silent patch |
| Optional addition | Compatibility analysis and N/R gates; “optional” alone does not make it compatible |
| Breaking change/removal | New edition, migration guidance and explicit coexistence/deprecation plan |
| Urgent defect | Publish an advisory promptly; corrected normative text still follows N/R gates |

Assess compatibility in both directions: old producer/new consumer and new producer/old
consumer. Cover unknown fields, missing fields, changed defaults, units, refusal behavior
and capability discovery where relevant. Declare unsupported combinations explicitly.
Deprecation normally spans at least one stable edition and 12 months; an accelerated
withdrawal needs an explained N/R decision and an immediate advisory, not rewritten history.

The changelog separates added, clarified, changed, deprecated, removed and corrected items,
with DP IDs, affected clauses, compatibility impact and release status. “Unreleased” is not
“approved”. Old entries remain; corrections append an explanation.

An R ballot is on one immutable release package containing the specification, agreed schema
if any, examples, clause/evidence map, all included DPs, comment/objection dispositions,
compatibility/migration notes, known limits, license notices and a manifest of artifact hashes.
All material integration changes go back to review. One steward assembles the package;
a person from another party verifies it matches approvals. Publication occurs after the
ballot and its 14-day appeal window close, with no pending appeal. Record the final URL,
source commit, hashes, ballot and publication date. Corrections never overwrite artifacts.

## 11. Rights, communications and stewardship

Before accepting normative contributions under the adopted process, agree document/code
licenses, contribution authority and an intellectual-property policy with the participants.
A goal is implementation without discriminatory or royalty barriers; this draft grants no
patent rights and claims no royalty-free status. Existing repository licensing is evidence
to review, not automatic consent to new agreements. Record any exclusions or unresolved
rights and keep affected features from stable adoption until resolved.

Document rights and implementation patent commitments are distinct concerns, as illustrated
by the [W3C Community Group policy summary](https://www.w3.org/community/about/process/summary/).
Choose an appropriate host/policy with informed review instead of copying an organization's
legal agreement or inventing one in a technical PR.

Publish open minutes, decisions and review records in a portable repository. Private partner
calls can discover needs but do not adopt clauses. Publish a non-confidential rationale and
obtain permission before naming a partner, displaying a logo or asserting support. A review
contribution or test result is not commercial endorsement. Do not require disclosure of
private CAD/process data; accept shareable reduced examples with clear limitations.

Maintain at least two agreed repository custodians from independent parties, exportable
records and backups. Transfers of domains, repositories or names require G approval plus
consent/authorization of their current owners. Votes cannot transfer someone else's property.
Sponsorship, hosting costs and affiliations are disclosed; they confer no normative priority.

## 12. Awareness, learning and participant development

The process has two linked outputs: better decisions and a broader, better-informed
community capable of making the next decisions. Each season must allocate capacity to
explanation, outreach and onboarding as well as text editing. Outreach is not a campaign
to obtain endorsements for a design already chosen.

Maintain a public entry page explaining the exchange problem, current maturity, who may
benefit, open questions, next review window and a small first contribution. Before adoption,
say “standardization initiative” or “discussion draft”, not “established standard”. Use
short producer/consumer stories and an annotated example before advanced format details.
Maintain a glossary; do not require familiarity with the internal experiment history.

A newcomer should be able to follow this path without a private introduction:

| Step | Public invitation | Small action | Human response |
|---|---|---|---|
| Discover | Problem brief, partner/community presentation | Read a worked exchange example | Named contact and next open session |
| Understand | Open introduction/demo and recording or written recap | Ask what the format would need for their use case | Answer publicly within seven days where practical |
| Contribute | “First contribution” list and simple template | Supply a sanitized path, UC or review comment | Acknowledge and assign an owner within seven days |
| Collaborate | Review clinic and feedback log | Compare options or reproduce an exchange | Link their input to a DP and record its disposition |
| Participate in decisions | Published charter, eligibility and upcoming ballot | Apply for a seat or review without voting | Apply the same objective rules to new and existing parties |
| Sustain | Next-season invitation and visible contribution history | Co-edit, mentor or host an independent demo | Shared responsibility, attribution and succession |

Comments, use cases and learning sessions remain open to non-voters. Do not make membership,
sponsorship, buying software or implementing an SDK a prerequisite for contributing. Offer
asynchronous participation, rotate meeting times and provide a written recap; a recording
requires consent. A newcomer is not expected to catch up on hundreds of historical issues.

At kickoff publish a plain-language season brief and invitations to affected sectors,
especially missing producer/consumer groups. During alternatives review run an open learning
session showing two options and their trade-offs. Before a public ballot/review deadline
hold an office hour for first-time reviewers. At close publish what changed because of
feedback, what was deferred, remaining gaps and how to join the next season. Provide a
written route for every meeting-based interaction.

Each season has a consenting outreach/onboarding owner, rotating like other roles; this
function can be combined with secretary. Keep a lightweight stakeholder coverage map
(producers, CAM/slicers, robotic integrators, simulation including AM thermal, end users,
research), with gaps and next invitations. The map is not a predetermined voting taxonomy
or a list of endorsers. Obtain authorization before sending messages on another person's
behalf and consent before publishing contact details, names or logos.

Measure contribution and learning, not only audience size. Report aggregate new inquiries,
first-time contributors, acknowledged/resolved feedback, independent represented parties,
returning contributors next season, and decisions improved by new input. Where counts permit, also show inquiry-to-first-contribution
and first-contribution-to-next-season-return rates with their denominators; never infer
individual tracking or publish misleading percentages from an unidentified audience. Ask newcomers
whether the introductory example and next action were understandable. Page views and event
attendance are secondary signals and never substitutes for adoption evidence. Track no
individual without a disclosed purpose; private outreach contacts are not a public register.

Invite people into decisions before locking scope. If outreach reveals an unrepresented
essential use case, revise or defer the relevant package through the existing gates.
An event, trade show or sponsor deadline must not shorten review or inflate release claims.

## 13. Minimum operating footprint and adoption

Keep the core format short. Keep this process separate from normative format clauses.
Start with Markdown records and an issue tracker; no voting service, registry generator,
certification platform or permanent subcommittee is required. One decision record may
contain its review, ballot and evidence links; do not duplicate the same information
across tools. Automate only repetitive administration after the group sees a need.

At a season retrospective, inspect unresolved objections, decision lead time, independent
producer/consumer participation, features without external evidence and maintenance burden.
Do not measure progress by PR count, lines of specification or number of SDKs.

To adopt this proposal: resolve the G-class choices in [DECISIONS.md](DECISIONS.md), complete
B0/B1, record explicit ratification, assign consenting role holders and publish the dated
process revision with its ballot. Until that happens, [ROADMAP.md](ROADMAP.md) is an invitation
to plan, not a delivery commitment; [CHANGELOG.md](CHANGELOG.md) records drafting only.

## 14. Source basis and deliberate adaptations

Sources consulted 2026-09-10 are linked at the relevant clauses. They support the design
principles, not an assertion of institutional compliance. This proposal combines IETF
objection-focused discussion, W3C maturity/evidence review, OASIS documented public-review
practice and ISO staged revision/maintenance. It does not recreate their membership,
legal structures, accreditation, formal status names or national voting arrangements.

Our proposed organization-level seats, P/C support rule, membership windows, numeric voting
thresholds, small appeal panel, seasonal cadence and historical-experiment reset all require
local agreement. If partners prefer another standards-development host, map decisions and
records to its process through an explicit G decision rather than maintaining two conflicting
sources of authority.
