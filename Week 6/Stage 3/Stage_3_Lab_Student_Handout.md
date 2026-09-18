# SmartCare Domain Model Lab 
*AI OFF -> AI ON -> COMPARE -> VERIFY | 1 hour*

# A - Requirements Review: AI OFF

| Requirement | Concept | State/behaviour | Decision                                                                                   |
|-------------|---|---|--------------------------------------------------------------------------------------------|
| FR-01       | Patient | State: name, DOB, contact, address | Included as patient class                                                                  |
| FR-02       | Patient | Behaviour: searchable by name/ID | Included but as a search action done by the system, not something patient does itself      |
| FR-03       | Patient | Behaviour: update contact details | Included                                                                                   |
| FR-04       | Practitioner | State: name, specialty, working hours | Included as Practitioner class                                                             |
| FR-05       | Practitioner | Behaviour: report availability (derived, not stored) | Included as availability is calculated from practitioner plus appointment and not stored separately |
| FR-06       | Appointment | State: date/time, links to Patient and Practitioner | Included as Appointment class                                                              |
| FR-07       | Appointment | Behaviour: check for conflict (including partial overlaps) | Included as this is the main rule for appointment                                          |
| FR-08       | Appointment | State/behaviour: cancel + record reason | Included                                                                                   |
| FR-09       | Appointment | State: status (fixed set of values) | Included as an attribute of Appointment, not a separate class                              |
| FR-10       | Appointment | Behaviour: retain history, no deletion | Included                                                                                   |
| FR-11       | (Report) | Behaviour: summarise appointment counts | Not modelled as a domain class — treated as a generated report/service operation           |
| FR-12       | Practitioner / Appointment | Behaviour: view own daily appointments | Included — a query on Appointment filtered by Practitioner                                 |

# B - Candidate Classes: AI OFF

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

# C - CRC Cards: AI OFF

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

# D - UML Model: AI OFF
Attached as drawio file

# E - AI Design Review: AI ON

| AI suggestion | Evidence                                | Decision | Reason                                                                                         | Model change                                     |
|---|-----------------------------------------|---|------------------------------------------------------------------------------------------------|--------------------------------------------------|
| Add Patient, Practitioner, and Appointment as the main classes | FR-01–FR-12 broadly support these three | Accepted | These three cover everything the requirements ask for                                          | None, since it confirms the existing model       |
| Make Appointment check for overlapping times, not just exact matches | FR-07                                   | Accepted | The requirements say double-booking isn't allowed and that includes times that partly overlap  | Added a checkConflict() behaviour to Appointment |
| Keep status and cancellation reason as simple data inside Appointment | FR-08, FR-09                            | Accepted | They're just information about an appointment, not separate things with their own identity     | No new classes added, just kept as attributes    |
| Add extra classes like PatientManager, AppointmentManager | Not mentioned in the requirements       | Modified | Not needed right now, noted as something to maybe add later if the system grows                | None to the model for now                        |
| Add ClinicController, NotificationManager, or ScheduleEngine |  Not mentioned in the requirements                    | Rejected | None of these are mentioned anywhere in the requirements, so they don't belong in this version | None                                             |

# F - Compare and Decide: AI ON / VERIFY

Critique of AI-proposed classes: PatientManager, PractitionerManager, AppointmentManager, ClinicController, NotificationManager, ScheduleEngine.

- **PatientManager** — Rejected. This feels more like a coding-layer idea than something from the case study itself. Things like search, create and update can just live on Patient, no separate class needed.
- **PractitionerManager** — Rejected, same reason as PatientManager. It just repeats what Practitioner already does.
- **AppointmentManager** — Not added as a real class right now, but kept as a note in case booking or conflict logic (FR-07) gets more complex later. For now, this stays with Appointment.
- **ClinicController** — Rejected. Sounds more like a setup idea than anything the requirements actually ask for. Nothing supports it.
- **NotificationManager** — Rejected. Nothing in the brief talks about reminders or notifications at all, feels like the AI just made this one up.
- **ScheduleEngine** — Rejected for now. Availability can already be worked out using Practitioner and Appointment together (FR-05), so a separate scheduling class isn't needed.

# G - Python Skeletons: AI OFF

```python
class Patient:
    """A patient at the clinic. Patients do not book appointments themselves -
    a receptionist creates and manages bookings on their behalf."""

    def __init__(self, patient_id: int, name: str, dob: str, contact: str, address: str):
        self.patient_id = patient_id
        self.name = name
        self.dob = dob
        self.contact = contact
        self.address = address

    def update_contact_details(self, contact: str = None, address: str = None) -> None:
        """Update the patient's contact details."""
        pass


class Practitioner:
    """A practitioner (GP) at the clinic."""

    def __init__(self, practitioner_id: int, name: str, specialty: str, working_hours: str):
        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty
        self.working_hours = working_hours

    def get_availability(self) -> str:
        """Return this practitioner's available time slots."""
        pass

    def get_daily_appointments(self) -> str:
        """Return this practitioner's appointments for today."""
        pass


class Appointment:
    """An appointment booked by a receptionist, linking a Patient and a Practitioner."""

    def __init__(self, appointment_id: int, patient: Patient, practitioner: Practitioner,
                 date_time: str, status: str = "Scheduled"):
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date_time = date_time
        self.status = status
        self.cancellation_reason = None

    def check_conflict(self, other_appointment: "Appointment") -> bool:
        """Check if this appointment overlaps with another one for the same practitioner."""
        pass

    def cancel(self, reason: str) -> None:
        """Cancel this appointment and record the reason."""
        pass

    def update_status(self, new_status: str) -> None:
        """Update the appointment's status."""
        pass


def main() -> None:
    pass


if __name__ == '__main__':
    main()
```

# H - Consistency Check: VERIFY

- Class names match between the UML model and the code. Patient, Practitioner, and Appointment are the same in both places.
- Attribute names match too, just changed to fit Python style. For example dateTime becomes date_time and cancellationReason becomes cancellation_reason.
- All the operations named in the UML model, checkConflict, cancel, and updateStatus, show up as method stubs in the Appointment class.
- None of the rejected classes like PatientManager, ClinicController, NotificationManager, or ScheduleEngine appear anywhere in the code.
- The Patient class docstring confirms that patients don't book their own appointments. This matches the assumption that a receptionist handles the bookings instead.

# Reflection

**What modelling decision was hardest?**

The hardest part was figuring out whether "Status" and "Cancellation" should be their own classes. At first they felt important enough to be separate things but when I looked closer, they're really just changes to an Appointment like setting status to "Cancelled" and adding a reason. They don't have their own identity or do anything on their own, so I kept them as attributes inside Appointment. That was the trickiest call to make.

**Where did AI over-design?**

The AI went a bit overboard in a few places. It suggested things like ClinicController and NotificationManager, but nothing in the requirements actually asks for those — it just made them up because they sound like good architecture. It also wanted Manager classes for every entity (PatientManager, PractitionerManager, AppointmentManager), which is a common pattern but not needed for a small v1 system like this. I only kept AppointmentManager as a note in case booking logic gets more complex later.

**What evidence supported your final choices?**

I kept Patient, Practitioner and Appointment because they line up directly with FR-01 to FR-12, every requirement points to one of them. Anything that didn't have a requirement ID behind it (like ClinicController, NotificationManager, ScheduleEngine) got rejected or put on hold. This follows the rule from the AI review: no class without a cited requirement. I also checked that the UML model and the Python skeletons matched, class names, attributes and methods all line up and none of the rejected classes show up in the code.

