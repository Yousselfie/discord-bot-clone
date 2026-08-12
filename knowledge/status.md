---
title: Ummah LLC — Project Status
doc_id: status
last_updated: 2026-06-10
---

# Ummah LLC — Project Status

Top-level status of the software side of Ummah LLC, for the team to query.

## What Ummah LLC is building

1. **Ummah Connect** — a consumer-facing Muslim community discovery app. It helps
   people find local Muslim communities, RSVP to in-person gatherings (iftars,
   study circles, hikes, halal meetups), and connect with people through real-life
   events rather than an algorithmic feed. Core values: privacy-first (DMs off by
   default, no public feed, no ads, no algorithm pressure) and oriented toward
   in-person connection.

2. **Company / brand website** — **ummahllc.com**.
   - **ULAC (Ummah LLC Admin Console)** — internal back-office web app. Manages
     Ummah Connect data (communities, events), company finances (expenses,
     subscriptions), analytics, and audit tracking. Access restricted to the
     co-owners.

## Ownership / team

- Youssef
- Mohammed
- Ty'zel
- Issa

## Status at a glance (as of 6/10/2026)

### ULAC (Ummah LLC Admin Console) — Phases 1–7 complete

- **Phase 1:** Sign-in and enforced MFA
- **Phase 2:** Audit log foundation
- **Phase 3:** Expenses page with full CRUD
- **Phase 4:** Subscriptions tab + CRUD, and expenses dashboard widgets wired to
  real expenses
- **Phase 5:** Ummah Connect communities page + CRUD
- **Phase 6:** Ummah Connect events page + CRUD
- **Phase 7:** Analytics page + dashboard widgets wired to real analytics

**Currently working on — Phase 8:** the Team & Access tab — viewing admins'
session and MFA statuses, plus super-admin functionality for managing other
admins (2FA reset, suspension, force logoff).

### Ummah Connect — near completion

- **Last big feature: paid events via Stripe.** Coding is done; now configuring
  Stripe itself.
- **Planned next:** dynamic event creation based on tags selected at creation time
  (selecting a tag surfaces different event-creation options and pages). This is
  planned for once the payment feature is finalized.
- **Shareables:** a new shareable was created for sharing events to others. The
  sharing feature is **not yet wired up correctly** for deep linking and proper
  shareable unfurling/display of the custom shareable.

### Publishing

- **Goal:** app published on both Google Play and the Apple App Store by
  **6/20/2026**.
- Many organizations we've networked with and pitched to have been told to expect
  "a couple weeks" before we reach out with news that the app is available.
