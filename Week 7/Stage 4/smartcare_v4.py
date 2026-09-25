from enum import Enum


class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
    NO_SHOW = "No-show"


class InvalidStatusTransitionError(Exception):
    """Raised when an appointment tries to move to a status it is not allowed to."""
    pass


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




# TESTS

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





def main() -> None:
    pass


if __name__ == '__main__':
    main()