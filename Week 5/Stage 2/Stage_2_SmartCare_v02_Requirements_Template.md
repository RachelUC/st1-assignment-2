# 1. Problem and Scope

**Problem:** SmartCare Clinic is a small community clinic that currently manages patient records and appointments through a mix of spreadsheets, paper records and manual processes. 
This has led to several recurring operational problems: duplicate appointment bookings, difficulty locating patient records, inconsistent appointment status information, limited visibility of practitioner availability, manual and error-prone cancellation handling, unreliable appointment history and difficulty producing basic operational reports for management.

**Scope:** The first version of the system will support three core areas:
patient management, practitioner management and appointment management. 
It is intentionally a simple, lightweight application, not a full hospital information system which is suitable for a single small clinic with a limited number of practitioners and administrative staff. 
The system will be built iteratively over multiple stages with increasing functionality at each stage. 
Out of scope for this version are the billing/invoicing, clinical records (diagnoses, prescriptions), multi-clinic/branch support and integration with external health systems.

# 2. Stakeholders

| Stakeholder | Need  | Evidence  |
|---|-------|-----------|
| Patients | Book, view and cancel appointments without confusion or double-booking. | Case study notes "duplicate appointment bookings" as a recurring problem. |
| Practitioners (GPs) | Clear, up-to-date view of their own schedule and availability. | Case study notes "limited visibility of practitioner availability". |
| Receptionist / Clinic Administrator | A single, reliable place to manage patient records, bookings and cancellations instead of spreadsheets or paper. | Case study notes reliance on "spreadsheets, paper records and manual processes". |
| Clinic Management | Ability to see appointment history and produce basic operational reports | Case study notes "difficulty producing basic operational reports". |

# 3. Functional Requirements

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

# 4. Non-Functional Requirements

NFR-01: The system shall be usable by reception staff with basic computer literacy after no more than one hour of training (Usability).

NFR-02: The system shall return search results (patient or availability lookups) within 2 seconds under normal clinic load (Performance).

NFR-03: The system shall prevent data loss by saving appointment and patient data immediately upon confirmation of any booking, edit or cancellation (Reliability).

NFR-04: The system shall restrict access to patient records based on defined user roles (receptionist, practitioner or manager) via a login mechanism with each role permitted access only appropriate to their responsibilities (Security/Privacy).

NFR-05: The system shall be designed so that additional features (e.g. billing, clinical notes) can be added in later stages without requiring a full rebuild (Maintainability/Extensibility).

NFR-06: The system shall support the data volumes of a small clinic without noticeable degradation in performance (Scalability, limited scope).

# 5. User Stories

US-01: As a receptionist, I want to search for a patient by name or ID, so that I can quickly find their record without scrolling through spreadsheets.

US-02: As a receptionist, I want the system to stop me if a time slot is already booked, so that I don't accidentally create multiple appointments for a practitioner for the same slot.

US-03: As a practitioner, I want to see my daily appointment list, so that I know who I am seeing and when without asking reception.

US-04: As a receptionist, I want to cancel an appointment and record why, so that we have an accurate history instead of relying on memory or paper notes.

US-05: As a clinic manager, I want to generate a simple report of appointments over the past month, so that I can review clinic activity without manually calculating spreadsheets.

US-06: As a patient, I want my appointment details (practitioner, date, time) to be recorded correctly and consistently, so that I don't experience confusion or double-bookings when I arrive.

# 6. Acceptance Criteria

GIVEN a practitioner already has a confirmed appointment at 10:00 AM on a given day
WHEN a receptionist attempts to book another appointment for that same practitioner at 10:00 AM 
THEN the system shall reject the booking and display a message indicating the time slot is unavailable.

GIVEN an existing appointment with status "Scheduled"
WHEN a receptionist cancels the appointment and enters a cancellation reason
THEN the system shall update the appointment status to "Cancelled" and save the record with the reason in the patient's appointment history.

GIVEN a clinic manager selects a date range and requests an appointment report
WHEN the system generates the report
THEN it shall display the total number of appointments booked, completed and cancelled within that date range.

# 7. Assumptions and Open Questions

**Assumptions:**
- The clinic operates from a single physical location, multi-branch is not needed at this stage.
- Practitioners work fixed, regular hours that can be maintained by administrative staff rather than changing daily.
- Patients do not book appointments directly through the system, all bookings are made by reception staff on their behalf.
- The system will be used by a small number of staff, so multi-user complexities is not a primary concern.

**Open Questions:**
- Will patients eventually be able to booking appointments by themselves or will they continue booking through a receptionist in future stages also?
- Do any patients need weekly or regular appointments or is every appointment booked individually?
- For the basic operational report, what level of detail is required, is a simple count sufficient or do they want breakdowns by each practitioner?
- Is there old data that needs to be transferred into the new system and in what format?

# 8. AI Requirements Review Record

| AI suggestion | Evidence? | Decision | Reason | Verification |
|---|---|---|---|---|
| Check for overlapping appointment times, not just exact matches | Yes | Accepted | FR-07 blocks double-booking but doesn't define partial overlaps | Test with overlapping times (e.g. 10:00–10:30 vs 10:15–10:45) |
| List all appointment statuses clearly | Yes | Accepted | FR-09 gives examples, not a full list | Ask staff which statuses they actually use |
| Add breakdowns (e.g. per practitioner) to the report | Yes | Unverified | FR-11/US-05 mention counts only | Ask management if they want breakdowns |
| Check if old data needs to be moved into the new system | Yes | Unverified | Already an open question in the brief | Ask what old data exists and its format |
| Define who can access what (roles) | Yes | Accepted | NFR-04 says access is restricted but not by whom | Confirm roles with management |
| Decide who can mark an appointment as "No-show" | Partial | Modified | FR-09 allows status changes but not by whom | Confirm with staff who should do this |