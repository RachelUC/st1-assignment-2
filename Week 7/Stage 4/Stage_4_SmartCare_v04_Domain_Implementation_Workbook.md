# SmartCare v0.4 Domain Implementation Workbook
*Week 7 student resource*

# 1. UML-to-Code Trace

| UML element | Python element | Implemented? | Notes |
|---|---|---|---|
| Patient class | class Patient | Yes | Matches the stage 3 UML attributes and operations |
| Patient.updateContactDetails() | update_contact_details() | Yes | Updates contact and address directly |
| (not shown in stage 3 UML) | get_name() and set_name() | Yes | Added during implementation to protect the rule that a name cannot be empty. This is an implementation detail the UML did not need to show |
| Practitioner class | class Practitioner | Yes | Matches the stage 3 UML |
| (not shown in stage 3 UML) | appointments list and add_appointment() | Yes | Added during implementation so a Practitioner can hold its own list of appointments. A new Appointment adds itself to this list when it is created |
| Practitioner.getAvailability() | get_availability() | Yes | Returns the list of times already booked, built from the practitioner's own appointments list |
| Practitioner.getDailyAppointments() | get_daily_appointments() | Yes | It takes a date and filters the practitioner's own appointments to match |
| Appointment class | class Appointment | Yes | Matches the stage 3 UML |
| Appointment.status | private status attribute with get_status() | Yes | Made private and only readable through get_status(). Can only change through update_status() |
| (not shown in stage 3 UML) | AppointmentStatus enum | Yes | Added during implementation to give status a fixed and checkable set of values instead of a plain string |
| (not shown in stage 3 UML) | InvalidStatusTransitionError | Yes | Added to make sure illegal status changes are rejected instead of silently allowed, raised inside update_status() |
| Appointment.checkConflict() | check_conflict() | Partial | Implemented as a simplified exact time match check. Full partial overlap logic is not implemented yet |
| Appointment.cancel(reason) | cancel(reason) | Yes | Implemented. Calls update_status() internally |
| Appointment.updateStatus(newStatus) | update_status(new_status) | Yes | Implemented with checking for legal transitions |


# 2. Domain Invariants

| Class | Invariant or rule | How protected                                                                                     |
|---|---|---------------------------------------------------------------------------------------------------|
| Patient | Name cannot be empty | set_name() checks this when the object is created and raises a ValueError if incorrect            |
| Appointment | Status can only move from Scheduled to Completed, Cancelled or No show and never any other direction | update_status() checks the allowed transitions and raises a InvalidStatusTransitionError on an illegal move                   |
| Appointment | A cancelled appointment stays in the system and is never deleted | cancel() only changes the status and cancellation reason fields. The object itself is never removed |
| Appointment | Two appointments for the same practitioner should not share the same time slot | check_conflict() compares practitioner and date and time.|


# 3. Composition / Inheritance Decisions

| Relationship | Decision | Rationale                                                                                                                                                                                                                       |
|---|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Patient and Appointment | Association | Appointment references a Patient, but a Patient can exist independently, and appointment history must persist even if Patient details change later                                                                              |
| Practitioner and Appointment | Association | A Practitioner is not owned or changed by an appointment, they are just linked                                                                                                                                                  |
| Doctor and Practitioner (hypothetical) | Inheritance | A Doctor would technically be a type of practitioner. This is the one case here where inheritance would make sense                                                                                                              |
| Clinic and Appointment | Not modelled | Clinic is not part of the v1 domain model, since the scope is a single clinic. If added later, it would likely be a loose association rather than composition, since appointments should not disappear if clinic details change |

# 4. AI Pair-Programming Record

**Prompt used:** "Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML."

| AI contribution | Conforms? | Decision | Reason | Verification |
|---|---|---|---|---|
| Implemented Appointment with an AppointmentStatus enum and a private status attribute | Yes | Accepted | Matches the approved UML and adds the encapsulation the UML implied | Manually created an Appointment and confirmed its starting status is Scheduled |
| Raised a InvalidStatusTransitionError inside update_status() when an illegal transition was attempted | Yes | Accepted | Directly protects the domain rule that appointments cannot move backward or illegally between statuses | Manually called update_status() with an illegal transition and confirmed the error was raised |
| Suggested adding a NotificationManager when cancelling an appointment | No | Rejected | No requirement mentions notifications anywhere in the brief | Not applicable. Left out of the implementation entirely |
| Suggested writing SQL directly inside cancel() to persist the change | No | Rejected | Mixes database and persistence concerns into a domain class, breaking separation of concerns | Not applicable. cancel() only updates fields in memory |
| Suggested making status a public attribute for simplicity | No | Modified | Public mutation would let any code skip the transition rules. Status was kept private, with update_status() as the only way to change it | Manually confirmed that setting status directly is not possible, and that update_status() correctly enforces the rule |


# 5. Updated UML

Some updates were needed to the UML. The Stage 3 UML already had Patient, Practitioner and Appointment connected correctly, with checkConflict() and updateStatus() as Appointment operations, so the main classes and relationships stayed the same. However, a few changes from the implementation were important enough to add to the UML.

The AppointmentStatus enum was added as a separate element and connected to Appointment because status now uses a fixed set of named values. Appointment’s status was also made private, and get_status() was added so the status can be read without being changed directly. Practitioner was also updated with an appointments attribute and an add_appointment() operation because it now keeps its own list of appointments. This was needed for get_availability() and get_daily_appointments() to work properly.
