# SmartCare Lab — Answers
*AI OFF -> AI ON -> VERIFY | 1 hour*

## Learning objectives
- Analyse the SmartCare client brief.
- Identify stakeholders and scope.
- Write functional and non-functional requirements.
- Develop user stories and Given-When-Then acceptance criteria.
- Use AI to critique requirements without allowing it to invent stakeholder needs.
- Produce SmartCare Requirements Specification v1.0.

# Part A - Client Brief: AI OFF

SmartCare uses spreadsheets and paper records. Staff report duplicate bookings, difficulty finding patient information, inconsistent appointment status and limited appointment history. Management wants a small, maintainable patient, practitioner and appointment system.

**Analysis:** The brief points to four major operational problems: 
1. Duplicate bookings
2. Difficulty finding patient information
3. Inconsistent appointment status 
4. Limited appointment history

It also sets a scope constraint: the solution must stay small and easy to maintain and not a full hospital information system.

# Part B - Stakeholders and Scope: AI OFF

**Stakeholders (at least four):**
1. Patients - need appointments booked accurately and without confusion or duplication.
2. Practitioners (GPs) - need a clear, reliable view of their own schedule.
3. Receptionist / Administrative staff - need a system to replace spreadsheets and paper for records and bookings.
4. Clinic Management - need reliable appointment history and basic reports.

**In Scope:**
- Create, search, update and maintain patient records.
- Create new, view availability and daily schedule of the practitioner records.
- Appointment booking, cancellation and status tracking
- Able to store appointment history.
- Basic operational reporting.

**Out of Scope:**
- Billing and invoicing
- Clinical notes, diagnoses or prescriptions
- Multi-branch or multi-clinic support
- Integration with external health systems

**Provisional (uncertain, not confirmed):**
- Patient self-service booking (brief implies staff currently do all booking, unclear if this should change)
- SMS or email appointment reminders (reasonable but not mentioned in the brief)

# Part C - Functional Requirements: AI OFF
[Same as in requirements_template]

FR-01: The system shall allow a receptionist to create a new patient record with details including name, date of birth, contact number and address.

FR-02: The system shall allow a receptionist to search for an existing patient record by name or patient ID.

FR-03: The system shall allow a receptionist to update an existing patient's contact details.

FR-04: The system shall allow a receptionist to create a new practitioner record, including name, specialty and standard working hours.

FR-05: The system shall allow a receptionist to view a practitioner's availability for a given day or week.

FR-06: The system shall allow a receptionist to book a new appointment for a patient with a specific practitioner at a specific date and time.

FR-07: The system shall prevent an appointment from being booked, if it overlaps partially or fully with an already occupied appointment for that practitioner.

FR-08: The system shall allow a receptionist to cancel an existing appointment and record a cancellation reason.

FR-09: The system shall allow a receptionist or practitioner to update the status of an appointment to: Scheduled, Completed, Cancelled, No-show.

FR-10: The system shall maintain a historical record of all appointments for each patient, including past statuses and dates.

FR-11: The system shall allow management to generate a basic report of appointments over a selected date range (e.g. total booked, completed, cancelled).

FR-12: The system shall allow a practitioner to view a list of their own upcoming appointments for a particular day.

# Part D - Non-Functional Requirements: AI OFF

NFR-01: The system shall be usable by reception staff with basic computer literacy after no more than one hour of training (Usability).

NFR-02: The system shall return search results (patient or availability lookups) within 2 seconds under normal clinic load (Performance).

NFR-03: The system shall prevent data loss by saving appointment and patient data immediately upon confirmation of any booking, edit or cancellation (Reliability).

NFR-04: The system shall restrict access to patient records based on defined user roles (receptionist, practitioner or manager) via a login mechanism with each role permitted access only appropriate to their responsibilities (Security/Privacy).

NFR-05: The system shall be designed so that additional features (e.g. billing, clinical notes) can be added in later stages without requiring a full rebuild (Maintainability/Extensibility).

NFR-06: The system shall support the data volumes of a small clinic without noticeable degradation in performance (Scalability, limited scope).

# Part E - User Stories and Acceptance Criteria: AI OFF

US-01: As a receptionist, I want to search for a patient by name or ID, so that I can quickly find their record without scrolling through spreadsheets.

US-02: As a receptionist, I want the system to stop me if a time slot is already booked, so that I don't accidentally create multiple appointments for a practitioner for the same slot.

US-03: As a practitioner, I want to see my daily appointment list, so that I know who I am seeing and when without asking reception.

US-04: As a receptionist, I want to cancel an appointment and record why, so that we have an accurate history instead of relying on memory or paper notes.

US-05: As a clinic manager, I want to generate a simple report of appointments over the past month, so that I can review clinic activity without manually calculating spreadsheets.

US-06: As a patient, I want my appointment details (practitioner, date, time) to be recorded correctly and consistently, so that I don't experience confusion or double-bookings when I arrive.

**Acceptance Criteria (three, including one negative/failure scenario):**

*US-02 — positive scenario:*
GIVEN a practitioner has no appointment at 10:00 AM on a given day
WHEN a receptionist books an appointment for that practitioner at 10:00 AM
THEN the system shall save the appointment and mark it as Scheduled

*US-02 — negative/failure scenario:*
GIVEN a practitioner already has a confirmed appointment at 10:00 AM on a given day
WHEN a receptionist attempts to book another appointment for that same practitioner at 10:00 AM
THEN the system shall reject the booking and display a message indicating the time slot is unavailable

*US-04 — positive scenario:*
GIVEN an existing appointment with status "Scheduled"
WHEN a receptionist cancels the appointment and enters a cancellation reason
THEN the system shall update the status to "Cancelled" and retain the record, with reason, in the patient's appointment history

# Part F - AI Requirements Review: AI ON

**Prompt used:** "Act as a software requirements reviewer. Review the SmartCare requirements for ambiguity, inconsistency, missing clarification questions, and testability. Do NOT invent new client requirements. For every suggestion, state whether it is based on evidence or is only a question/assumption requiring validation."

**AI review output:**
1. FR-07 stops double-booking, but doesn't say if a partial overlap (like 10:00-10:30 vs 10:15-10:45) counts as a clash or only an exact match, a real gap in the current draft.
2. FR-09 gives example statuses but doesn't confirm the full, final list — worth locking down early.
3. FR-11 and US-05 mention report totals but not breakdowns (e.g. per practitioner) — a real gap, but the answer depends on what management wants.
4. The Open Questions already mention data migration, but no requirement covers it yet — a real, already-known gap.
5. NFR-04 says access should be restricted, but doesn't say who can do what — a reasonable thing to define.
6. FR-09 lets staff update appointment status but doesn't say who is allowed to mark one as "No-show" — a small but real gap.

# Part G - VERIFY the AI Review

| AI suggestion | Decision | Evidence used                                    |
|---|---|--------------------------------------------------|
| Check for overlapping appointment times, not just exact matches | Accepted | FR-07 blocks double-booking but doesn't say if partial overlaps count too |
| List all appointment statuses clearly | Accepted | FR-09 gives examples but not a full, fixed list  |
| Add breakdowns (e.g. per practitioner) to the report | Unverified | FR-11/US-05 mention counts only, not breakdowns, needs client input |
| Check if old data needs to be moved into the new system | Unverified | Already listed as an open question, needs client answer |
| Define who can access what (roles) | Accepted | NFR-04 says access is restricted but not by whom |
| Decide who can mark an appointment as "No-show" | Modified | FR-09 allows status changes but not who can make them, added as an assumption |

# Part H - Finalise SmartCare v0.2

**Stakeholder analysis, scope, FRs, NFRs, user stories, and acceptance criteria:** see above.

**Assumptions and Open Questions:**
- Assumption: All bookings are made by reception staff on the patient's behalf (no patient self-booking in this stage).
- Assumption: Practitioners work fixed hours set by admin staff.
- Assumption: Either a receptionist or practitioner can mark an appointment as "No-show," pending client confirmation.
- Open question: Should the report show simple totals only or breakdowns (e.g. per practitioner, per day)?
- Open question: Does old spreadsheet data need to be moved into the new system and in what format?
- Open question: Will patients eventually be able to book appointments by themselves or will they continue booking through a receptionist in future stages also?

**Selected AI review evidence:**
- Accepted: FR-07 updated to clearly count partial overlaps as a booking clash and not just exact time matches.
- Accepted: FR-09 updated to lock in the full status list (Scheduled, Completed, Cancelled, No-show).
- Accepted: NFR-04 updated to require defined roles (receptionist, practitioner, manager) with different access levels.
- Modified: Added an assumption that either receptionist or practitioner can set "No-show" status, pending confirmation.
- Unverified (added to Open Questions): exact report fields or breakdowns.
- Unverified (added to Open Questions): whether data migration is needed.

# Reflection

*(150–250 words)*

**What did AI notice that you missed?**

The AI pointed out that FR-07 said the system should stop double-booking but never explained what counts as a clash. 
I had only thought about exact time matches like two appointments booked at the same 10:00 AM slot but hadn't considered partial overlaps like 10:00–10:30 and 10:15–10:45. 
Even though they don't start together, they still overlap and should be blocked too.

**What did AI invent or overreach on?**

The AI didn't invent a new feature here, it stayed within the existing requirement and just made it more precise. 
Earlier in the review, AI suggested about adding patient self-booking which wasn't mentioned in the client brief, so I just moved it to open questions instead.

**Which requirement changed after review?**

FR-07 changed the most. It went from a general statement about preventing double-booking to a clearer rule that counts partial overlaps as a conflict and not just exact matches.
This made the requirement more testable, since now there's a clear rule for even slightly overlapping appointment times.

**Why must requirements have evidence?**

Because duplicate bookings was clearly stated in the case study, so tightening FR-07 fixed a real, confirmed issue rather than adding something new.
If I'd accepted a suggestion without checking it against the brief, I could easily end up building something nobody asked for. 
An AI suggestion is useful as a prompt to double-check requirements but it only becomes a real requirement once it's backed by something the client actually wants or a gap that's clearly present in the existing document.
