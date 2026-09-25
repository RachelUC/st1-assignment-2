# Week 7 Tutorial
*60 minutes*

# Activity 1 - Encapsulation Review

| Class | Protected state / invariant                                                                                                                | Public operations                                                         |
|---|--------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Patient | name cannot be empty this is checked in set_name() and called from the constructor                                                         | set_name(), update_contact_details(), get_name()                          |
| Practitioner | No extra validation yet in this version                                                                                                    | get_availability(), get_daily_appointments()                              |
| Appointment | status can only move along allowed transitions (Scheduled → Completed/Cancelled/No-show); stored as private status, never changed directly | 	cancel(reason), update_status(new_status), get_status(), check_conflict() |

# Activity 2 - Composition or Inheritance?

**Appointment and Patient** → Composition/association

Reason: Appointment is connected to a patient but doesn't own it. A patient can exist even without any appointments and appointments need to stay in the system as history even if the patient's details change later. It's just a link, not a type of relationship.

**Appointment and Practitioner** → Composition/association

Reason: Same idea. Appointment just refers to a practitioner, it doesn't control their lifecycle. A practitioner isn't affected or deleted when an appointment gets cancelled, they're just connected.

**Doctor and Practitioner (hypothetical)** → Inheritance

Reason: A doctor would be a type of practitioner. In this case, inheritance makes sense, since a doctor would have all the same data and behaviour as a practitioner and more.

**Clinic and Appointment** → Composition/association

Reason: Even if a clinic gets added later, it shouldn't fully own appointments to the point where they disappear if the clinic changes. It would just be a loose connection, not ownership or a type relationship.

# Activity 3 - Responsibility Allocation

**Who decides whether SCHEDULED can become CANCELLED?**
Appointment itself, through update_status() which checks the if the change is allowed before actually changing it. It's not something the UI or a separate manager class should be deciding.

**Who validates a patient name?**
Patients does this themselves using set_name(), which runs when a new patient is created.

**Should Appointment execute SQL? Why?**
No. Saving data to a database is a different role from what an appointment is meant to do. If SQL was mixed with appointment, it would be harder to test and would break the line between the actual logic and how the data gets stored.

**Should the UI decide whether a status transition is legal?**
No. This should be inside appointment, not the UI. If the UI decided this instead, the rule could get missed, duplicated or applied inconsistently everywhere depending on where it is checked, like in tests or in future stages.

# Activity 4 - AI Code Critique

AI generates an Appointment class with public status mutation, SQL inside cancel(), a NotificationManager dependency and inheritance from PatientRecord.

**Design problems and corrections:**

1. **Public status mutation** (appointment.status should get cancelled directly) — Problem: this skips the rules completely, allowing invalid changes such as moving from Cancelled back to Scheduled.
Correction: keep status private and only allow it to change through update_status(), since this method is responsible for checking whether the change is actually permitted.


2. **SQL inside cancel()** — Problem: this combines database logic with the class's own data and rules, which makes it hard to test or reuse. 
Correction: keep appointment focused only on its own responsibilities, persisting data is a separate concern and does not belong in this class.


3. **NotificationManager dependency** — Problem: no requirement mentions notifications anywhere in the brief, so this dependency is unsupported and effectively invented.
Correction: remove the dependency entirely since there's no requirement backing it.


4. **Inheritance from PatientRecord** — Problem: Appointment isn't a type of PatientRecord, there's no is-a relationship, so this misuses inheritance and creates unnecessary, confusing coupling. 
Correction: use a normal association instead where Appointment just holds a reference to a Patient object.


5. **No protection around cancellation** — Problem: if status can be modified freely then nothing prevents an appointment from being cancelled without a reason or being changed later. 
Correction: route all state changes through cancel() and update_status() which records a reason and blocks invalid transitions.


6. **No input validation in the constructor** — Problem: nothing prevents empty or invalid data from being stored when a Patient or Appointment is created. 
Correction: validate key fields during creation, the same way patient's name is checked in this implementation.

# Exit question

**Why can code be object-oriented syntactically but still have poor object-oriented design?**

Using the class keyword does not automatically mean the design is good. Code can still be written using classes and objects while making mistakes such as exposing internal data publicly, mixing unrelated tasks into one class (for example, handling database work or sending notifications inside a domain class), using inheritance when there is no real is-a relationship or adding dependencies that were never required.
These mistakes go against the core ideas of object-oriented design, keeping data private, giving each class one clear responsibility and only creating relationships that are supported by evidence, even though the code is technically written using classes.