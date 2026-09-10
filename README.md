# OpenToolpath — public discussion portal

Public entry point for an early-stage toolpath exchange initiative:
https://opentoolpath.github.io/

The site invites producer/consumer use cases and feedback on a proposed collaborative
development process. There is no jointly adopted specification edition or ratified
governance announced here. Earlier independent implementations are private pre-alpha
experiments, not official SDKs or partner-approved requirements.

## Take part

- [Share an exchange problem](https://github.com/opentoolpath/opentoolpath.github.io/issues/new?template=use-case.yml).
- [Review a proposal or ask a question](https://github.com/opentoolpath/opentoolpath.github.io/issues/new?template=review.yml).
- Read the [proposed process](development/PROCESS.md), [roadmap](development/ROADMAP.md),
  [decision matrix](development/DECISIONS.md) and [draft changelog](development/CHANGELOG.md).

No SDK adoption, partner commitment or endorsement is required to contribute. Issue
submission requires a GitHub account; the documents and discussions are publicly readable.
Share only non-confidential examples you have permission to publish.

## Maintain the site

The portal is plain HTML/CSS, with no application dependencies or external font requests.
Preview with `python3 -m http.server 8080`. Run `python3 tools/check_site.py` before review.
PRs validate the site; main publishes only the explicitly staged public assets to Pages.
Experimental sample archives and the private viewer are not part of the published site.

The process documents are discussion drafts. Edits must not imply votes, roles, releases
or endorsements that have not actually occurred. Changes to this portal do not enact the
proposed governance.

Licensed under the [Apache License 2.0](LICENSE).
