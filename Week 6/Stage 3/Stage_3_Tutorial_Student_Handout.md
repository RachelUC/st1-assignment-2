# Week 6 Tutorial
*60 minutes*

# Candidate Concepts

| Candidate | Class? | Reason                                                                                                                  |
|---|---|-------------------------------------------------------------------------------------------------------------------------|
| Patient | Yes | Has its own identity and data (name, DOB, contact, address)                                                             |
| Practitioner | Yes | Has its own identity and data (name, specialty, hours)                                                                  |
| Appointment | Yes | Has its own state (date, time, status) and connects a Patient to a Practitioner.                                        |
| Name | No | Just a piece of data (attribute) that belongs to Patient or Practitioner, not a thing on its own                        |
| Clinic | No | Scope is a single clinic location only (see Assumptions), no need to model it as an object when there's only one, non-varying instance |
| Database | No | This is a technical or storage detail, not from the real-world problem the system is about                              |
| Cancellation | No | It's an state change on an Appointment (status = Cancelled, plus a reason), not a separate object with its own identity |
| Status | No | It's an attribute of Appointment (one of a fixed set of values), not a class of its own                                 |

# CRC Cards

## Patient

| Responsibilities | Collaborators |
|---|---|
| Hold identifying and contact details (name, DOB, contact, address) | Appointment |
| Perform basic validation on its own data | — |
| Be searchable by name or ID | — |

## Practitioner

| Responsibilities                                        | Collaborators |
|---------------------------------------------------------|---|
| Hold identifying details and working hours              | Appointment |
| Report their own availability and upcoming appointments | Appointment |

## Appointment

| Responsibilities                                                                      | Collaborators |
|---------------------------------------------------------------------------------------|---|
| Hold date, time, status, cancellation detail and link one patient to one practitioner | Patient, Practitioner |
| Check for a time conflict before confirming bookings (includes partial overlaps)      | Practitioner |
| Record a cancellation reason and keep history instead of being deleted                | — |

# Relationship Reasoning

**Patient to Appointment: which relationship and why?**

One-to-many (one patient can have many appointments over time). There is no ownership. If a patient's appointment gets deleted or their record changes, the appointment should still stay in the system as part of the history, it doesn't disappear even when somthing happens to the paitent. So the two are linked, but Appointment doesn't depend on patient to exist.

**Practitioner to Appointment: what multiplicity?**

One-to-many (from Practitioner to Appointment),a practitioner can have many appointments, but each appointment is linked to exactly one Practitioner at a time.

**Should Appointment inherit from Patient?**

No. Inheritance is for when one thing is just a type of another like a GP being a type of practitioner but an appointment isn't a type of patient, it's more like a connector between a patient and a practitioner at a certain time. So it makes more sense to just link them together (an association) instead of making appointment inherit from patient.

**Does Clinic need to own every object?**

No. Since the brief only mentions a single clinic location, adding a Clinic class that "owns" patient, practitioner and appointment would add complexity without solving a real problem in the brief. Direct associations between patient, practitioner and appointment are enough for now. Clinic could be introduced later if multi-branch support is ever needed.

# AI Model Critique

Critique of AI-proposed classes: PatientManager, PractitionerManager, AppointmentManager, ClinicController, NotificationManager, ScheduleEngine.

- **PatientManager** — Rejected. This feels more like a coding-layer idea than something from the case study itself. Things like search, create and update can just live on Patient, no separate class needed.
- **PractitionerManager** — Rejected, same reason as PatientManager. It just repeats what Practitioner already does.
- **AppointmentManager** — Not added as a real class right now, but kept as a note in case booking or conflict logic (FR-07) gets more complex later. For now, this stays with Appointment.
- **ClinicController** — Rejected. Sounds more like a setup idea than anything the requirements actually ask for. Nothing supports it.
- **NotificationManager** — Rejected. Nothing in the brief talks about reminders or notifications at all, feels like the AI just made this one up.
- **ScheduleEngine** — Rejected for now. Availability can already be worked out using Practitioner and Appointment together (FR-05), so a separate scheduling class isn't needed.