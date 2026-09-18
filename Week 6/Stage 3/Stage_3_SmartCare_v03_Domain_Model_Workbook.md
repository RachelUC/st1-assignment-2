# SmartCare v0.3 Domain Model Workbook 
*Week 6 student resource*

# Requirement-to-Concept Trace

| Requirement | Concept | State/behaviour | Decision                                                                                   |
|---|---|---|--------------------------------------------------------------------------------------------|
| FR-01 | Patient | State: name, DOB, contact, address | Included as patient class                                                                  |
| FR-02 | Patient | Behaviour: searchable by name/ID | Included but as a search action done by the system, not something patient does itself      |
| FR-03 | Patient | Behaviour: update contact details | Included                                                                                   |
| FR-04 | Practitioner | State: name, specialty, working hours | Included as Practitioner class                                                             |
| FR-05 | Practitioner | Behaviour: report availability (derived, not stored) | Included as availability is calculated from practitioner plus appointment and not stored separately |
| FR-06 | Appointment | State: date/time, links to Patient and Practitioner | Included as Appointment class                                                              |
| FR-07 | Appointment | Behaviour: check for conflict (including partial overlaps) | Included as this is the main rule for appointment                                          |
| FR-08 | Appointment | State/behaviour: cancel + record reason | Included                                                                                   |
| FR-09 | Appointment | State: status (fixed set of values) | Included as an attribute of Appointment, not a separate class                              |
| FR-10 | Appointment | Behaviour: retain history, no deletion | Included                                                                                   |
| FR-11 | (Report) | Behaviour: summarise appointment counts | Not modelled as a domain class — treated as a generated report/service operation           |
| FR-12 | Practitioner / Appointment | Behaviour: view own daily appointments | Included — a query on Appointment filtered by Practitioner                                 |

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

## Optional class

| Responsibilities                                                                                                                                                                                                                                 | Collaborators |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| No additional class was added. Clinic and Report were both considered and rejected: Clinic because only one clinic instance exists in scope and for Report because it's a generated output rather than a persistent object with its own identity | — |

# UML Class Diagram

Classes, attributes, and operations:

- **Patient**: patientId, name, dob, contact, address — `updateContactDetails()`
- **Practitioner**: practitionerId, name, specialty, workingHours — `getAvailability()`, `getDailyAppointments()`
- **Appointment**: appointmentId, dateTime, status, cancellationReason — `checkConflict()`, `cancel(reason)`, `updateStatus(newStatus)`

Associations: Patient 1:MANY Appointment; Practitioner 1:MANY appointment.
Attached as drawio file 

# Design Rationale

I choose Patient, Practitioner and Appointment as my three main classes because every requirement (FR-01 - FR-12) fits under one of them. None of the requirements needed a class outside these three. I kept status and cancellation reason as simple attributes inside appointment instead of making them separate classes, since they're just data describing what state an appointment is in, not things with their own identity or actions.

I split up responsibilities based on what the requirements actually asked for. Patient and Practitioner mostly just hold data, with a few small actions like updating contact details or showing availability. I gave appointment the harder job of checking for time conflicts, including partial overlaps, since that depends on comparing two appointment times.

For the links between Patient–Appointment and Practitioner–Appointment, I used simple one-to-many relationships instead of composition or inheritance. I avoided composition because appointments need to stay in the history even if a patient's record changes later. I avoided inheritance too, since a Patient isn't a type of Appointment, they're just connected, not related by type. I also left out a Clinic class, since this version only supports one clinic.

I stuck to just three classes, each with its own clear job, so no single class ends up trying to do everything (handling patient data, appointment logic and reports all at once). Because it would get complicated, so I kept each class focused and only connected to the classes it actually needed.

# AI Design Review Record

**Prompt used:** "Use only the confirmed SmartCare requirements and business rules. Suggest candidate classes, responsibilities, collaborators and relationships. For every proposed element, cite the supporting requirement. Do not invent features, database concerns or UI details. Identify uncertain proposals separately for human review."

Each AI suggestion below was checked against four questions before a decision was made: Does it represent the confirmed domain? Does each class have a clear responsibility? Is the relationship backed by evidence? Is any added complexity justified?

| AI suggestion | Evidence                                | Decision | Reason                                                                                         | Model change                                     |
|---|-----------------------------------------|---|------------------------------------------------------------------------------------------------|--------------------------------------------------|
| Add Patient, Practitioner, and Appointment as the main classes | FR-01–FR-12 broadly support these three | Accepted | These three cover everything the requirements ask for                                          | None, since it confirms the existing model       |
| Make Appointment check for overlapping times, not just exact matches | FR-07                                   | Accepted | The requirements say double-booking isn't allowed and that includes times that partly overlap  | Added a checkConflict() behaviour to Appointment |
| Keep status and cancellation reason as simple data inside Appointment | FR-08, FR-09                            | Accepted | They're just information about an appointment, not separate things with their own identity     | No new classes added, just kept as attributes    |
| Add extra classes like PatientManager, AppointmentManager | Not mentioned in the requirements       | Modified | Not needed right now, noted as something to maybe add later if the system grows                | None to the model for now                        |
| Add ClinicController, NotificationManager, or ScheduleEngine |  Not mentioned in the requirements                    | Rejected | None of these are mentioned anywhere in the requirements, so they don't belong in this version | None                                             |