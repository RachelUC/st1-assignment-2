# SmartCare Implementation Lab 
*DESIGN FIRST -> AI PAIR PROGRAMMING -> REVIEW -> VERIFY | 1 hour*

# A - Revisit Approved UML

Before coding, the stage 3 UML was confirmed. There are three classes: Patient, Practitioner and Appointment, with one Patient linked to many Appointments, and one Practitioner linked to many Appointments. Appointment's operations, checkConflict(), cancel(reason) and updateStatus(newStatus), were already agreed.

The three classes and their links stayed the same going into implementation. A few small additions were made during coding to support them properly, such as the AppointmentStatus enum for a fixed set of status values, and giving Practitioner its own list of appointments so it can look up its own bookings.


# B - Implement Patient: AI OFF

```python
class Patient:

    def __init__(self, patient_id: int, name: str, dob: str, contact: str, address: str):
        self.patient_id = patient_id
        self.set_name(name)
        self.dob = dob
        self.contact = contact
        self.address = address

    def get_name(self) -> str:
        """Return the patient's name."""
        return self.__name

    def set_name(self, name: str) -> None:
        """Set the patient's name after checking it is not empty."""
        if name.strip() == "":
            raise ValueError("Patient name cannot be empty")
        self.__name = name

    def update_contact_details(self, contact: str = None, address: str = None) -> None:
        """Update the patient's contact details."""
        if contact is not None:
            self.contact = contact
        if address is not None:
            self.address = address
```


# C - Implement Practitioner: AI OFF

```python
class Practitioner:
    """A practitioner (GP) at the clinic."""

    def __init__(self, practitioner_id: int, name: str, specialty: str, working_hours: str):
        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty
        self.working_hours = working_hours
        self.appointments = []

    def add_appointment(self, appointment) -> None:
        """Add an appointment to this practitioner's own list of appointments."""
        self.appointments.append(appointment)

    def get_availability(self) -> list:
        """Return the list of times this practitioner already has an appointment booked."""
        booked_times = []
        for appointment in self.appointments:
            booked_times.append(appointment.date_time)
        return booked_times

    def get_daily_appointments(self, date: str) -> list:
        """Return this practitioner's appointments that fall on the given date."""
        daily_appointments = []
        for appointment in self.appointments:
            if appointment.date_time.startswith(date):
                daily_appointments.append(appointment)
        return daily_appointments
```


# D - Implement Appointment: AI ON

**Prompt used:** "Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML."

```python
from enum import Enum


class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
    NO_SHOW = "No-show"


class InvalidStatusTransitionError(Exception):
    """Raised when an appointment tries to move to a status it is not allowed to."""
    pass


class Appointment:
    """An appointment booked by a receptionist. It links a Patient and a Practitioner."""

    allowed_transitions = {
        AppointmentStatus.SCHEDULED: [AppointmentStatus.COMPLETED, AppointmentStatus.CANCELLED, AppointmentStatus.NO_SHOW],
        AppointmentStatus.COMPLETED: [],
        AppointmentStatus.CANCELLED: [],
        AppointmentStatus.NO_SHOW: [],
    }

    def __init__(self, appointment_id: int, patient: Patient, practitioner: Practitioner, date_time: str):
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.practitioner.add_appointment(self)
        self.date_time = date_time
        self.__status = AppointmentStatus.SCHEDULED
        self.cancellation_reason = None

    def get_status(self) -> AppointmentStatus:
        """Return the appointment's current status."""
        return self.__status

    def update_status(self, new_status: AppointmentStatus) -> None:
        """Move the appointment to a new status only if that move is allowed."""
        allowed_next_statuses = self.allowed_transitions[self.__status]

        if new_status in allowed_next_statuses:
            self.__status = new_status
        else:
            raise InvalidStatusTransitionError(
                f"Cannot change status from {self.__status.value} to {new_status.value}"
            )

    def cancel(self, reason: str) -> None:
        """Cancel this appointment and records the reason. The appointment stays in the system."""
        self.update_status(AppointmentStatus.CANCELLED)
        self.cancellation_reason = reason

    def check_conflict(self, other_appointment: "Appointment") -> bool:
        """Check if this appointment clashes with another one for the same practitioner."""
        same_practitioner = self.practitioner is other_appointment.practitioner
        same_time = self.date_time == other_appointment.date_time
        return same_practitioner and same_time
```

# E - Review Generated Code

- **Model consistency:** Appointment's attributes and methods still match the stage 3 UML (appointmentId, dateTime, status, cancellationReason, checkConflict(), cancel(), updateStatus()). The enum and exception are implementation details, not new UML elements.
- **Unsupported features:** None added, no database, UI, or notification code appeared in the generated class.
- **Public state mutation:** Avoided. Status is private (`__status`) and only readable through `get_status()`, so the only way to change it is `update_status()`.
- **Unnecessary inheritance:** None, Appointment does not inherit from anything.
- **Invented dependencies:** None, Appointment only depends on the AppointmentStatus enum and its own exception class, both of which exist to support requirements already in the model.
- **Error handling:** `update_status()` raises `InvalidStatusTransitionError` with a clear message instead of silently allowing or ignoring an illegal change.


# F - Manual Behaviour Checks

```python
patient = Patient(1, "Jane Doe", "1990-01-01", "0400 000 000", "123 Main St")
practitioner = Practitioner(1, "Dr. Smith", "General Practice", "9am-5pm")

# Create a valid object
appointment = Appointment(1, patient, practitioner, "2026-09-20 10:00")
print(appointment.get_status())  # AppointmentStatus.SCHEDULED

# Test invalid input
try:
    bad_patient = Patient(2, "", "1990-01-01", "0400 000 000", "123 Main St")
except ValueError as e:
    print("Caught expected error:", e)

# Cancel a scheduled appointment
appointment.cancel("Patient requested reschedule")
print(appointment.get_status())         # AppointmentStatus.CANCELLED
print(appointment.cancellation_reason)  # Patient requested reschedule

# Attempt an illegal repeated transition
try:
    appointment.update_status(AppointmentStatus.SCHEDULED)
except InvalidStatusTransitionError as e:
    print("Caught expected error:", e)

# Check get_availability() and get_daily_appointments() now that Practitioner tracks its own appointments
print(practitioner.get_availability())
print(practitioner.get_daily_appointments("2026-09-20"))
```


# G - Refactor

The AI-generated Appointment code did not have any extra classes, unused imports, or unnecessary complexity, so nothing needed to be removed. The main improvement was connecting Practitioner and Appointment properly. When a new Appointment is created, it now adds itself to its Practitioner's list of appointments using add_appointment(). This way, Practitioner can actually look up its own appointments to answer get_availability() and get_daily_appointments(), instead of only Appointment knowing about the Practitioner. The UML diagram was also updated afterwards to show this link, along with the AppointmentStatus enum, since both were important enough to add to the diagram rather than leave as details only visible in the code.

# H - AI Engineering Log

| AI generated contribution | Decision | Verification evidence |
|---|---|---|
| Implemented Appointment with an AppointmentStatus enum and a private status attribute | Accepted | Manually created an Appointment and confirmed its starting status is Scheduled |
| Raised InvalidStatusTransitionError inside update_status() when an illegal transition was attempted | Accepted | Manually called update_status() with an illegal transition and confirmed the error was raised |
| Suggested adding a NotificationManager when cancelling an appointment | Rejected | Not applicable, left out of the implementation entirely |
| Suggested writing SQL directly inside cancel() to persist the change | Rejected | Not applicable, cancel() only updates fields in memory |
| Suggested making status a public attribute for simplicity | Modified | Manually confirmed that setting status directly is not possible, and that update_status() correctly enforces the rule |

# Reflection

One thing I changed was the AI’s suggestion to make status a public attribute “for simplicity.” I decided to keep it private and only allow it to be changed through update_status(). This is because if status was public, any part of the code could change it directly without following the rules.

I also rejected two other suggestions from the AI: putting SQL inside cancel() and adding a NotificationManager. These were not part of the SmartCare requirements, so I did not include them. Adding these features would make the system more complicated and add functionality that was not needed.

Having the approved design made it easier to check the AI’s suggestions. The UML and requirements already showed what the class should do and what should not be included, such as database, UI, and notification code. This gave me something clear to compare the AI’s work with, so I could easily notice and fix suggestions that were outside the requirements.
