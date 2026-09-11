# Week 5 Tutorial — Answers
*60 minutes*

## Learning goals
- Analyse stakeholders.
- Distinguish functional and non-functional requirements.
- Recognise ambiguity and unsupported requirements.
- Define scope.
- Develop user stories and acceptance criteria.
- Critique AI-generated requirements.

# Activity 1 - Stakeholder Map

| Stakeholder | Need                                                              | Potential conflict                                                                                                                        |
|----------|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Patients | Book and attend appointments without confusion, double-booking or long waits. | They may want flexible booking or rescheduling which can be conflicting with the pratitioner's fixed schedules.                           |
| Practitioners (GPs) | Clear, up-to-date view of their own schedule and availability.    | They may resist extra data-entry steps (e.g. recording cancellation or rescheduling reasons).                                             |
| Receptionist / Administrative staff | A single reliable and efficient system to replace physical paper records of bookings. | They may want the system to be as simple as possible which can conflict with management's wish for more detailed reporting.               |
| Clinic Management | Ability to see appointment history and basic operational reports. | They may want more advanced features (e.g. analytics, billing) than the "small, maintainable system" which can be out of scope or budget. |

# Activity 2 - Functional or Non-Functional?

Functional — The system shall allow staff to cancel an appointment.

Non-functional — The system should remain responsive for the course-scale dataset.

Functional — The system shall retain cancelled appointments.

Non-functional — Core business logic should be independently testable.

Functional — The system shall search for a patient by ID.

# Activity 3 - Repair Ambiguous Requirements

**The system should be easy to use.**
- Problem: "Easy to use" is subjective and not measurable - there is no way to test whether it has been achieved.
- Clarification question: What specific task and completion time or error rate defines "easy" (e.g. can a new receptionist book an appointment in under 2 minutes with no training)?

**Patient search should be fast.**
- Problem: "Fast" has no defined threshold, so two people could disagree on whether the requirement is met.
- Clarification question: What is the maximum acceptable response time for a patient search (e.g. under 2 seconds) and under what data load?

**The system should securely manage data.**
- Problem: "Securely" doesn't specify which security mechanism, threat or standard applies.
- Clarification question: What specific protections are required (e.g. login/authentication) and are there compliance standards (e.g. health data privacy rules) that must be met?

**Appointments should normally be easy to cancel.**
- Problem: "Normally" and "easy" are both vague - it's unclear what the exception cases are or what "easy" means.
- Clarification question: What are the exact steps required to cancel an appointment and are there specific cases (e.g. same-day cancellation, already-completed appointment) that should be handled differently?

# Activity 4 - AI Requirements Audit

| AI suggestion | Classification | Evidence / reason                                                                                                                                   |
|---|---|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Patients receive SMS reminders. | Assumption requiring validation | Plausible and common in booking systems but not mentioned anywhere in the client's requirements. This needs client confirmation before being added. |
| Facial recognition login. | Unsupported / Out of scope | No stated evidence, the client explicitly wants a small, maintainable system and biometric login adds complexity.                                   |
| Receptionists create appointments. | Confirmed | Matches the requirements, staff currently manage bookings manually and need this to continue in the new system.                                     |
| Online payment. | Out of scope | Not mentioned, billing or payment is not one of the stated operational problems.                                                                    |
| Practitioners view schedules. | Confirmed | Directly addresses the client's stated problem of "limited visibility of practitioner availability".                                                |
| AI recommends treatments. | Unsupported / Out of scope | Beyond the project scope, this clinical feature was not included in the origninal requirements.                                                     |
| Cancelled appointments remain in history. | Confirmed | Matches the problem of "limited appointment history" and need for reliable records.                                                                 |

# Exit question

**Why is 'AI suggested it' not sufficient evidence for a requirement?**

An AI can only give suggestions based on patterns it has seen before, it doesn't know the clients real needs, limitations or priorities.
It might propose something like facial recognition or AI treatment suggestions which sounds reasonable but were never requested and may not fit the client's actual problem, budget or risk tolerance.
If we accept any suggestions just because AI recommended it, we risk adding thing that the client never wanted and might not even be useful to them.
Real evidence has to come from the client's requirements or stakeholders input or something they have confirmed.
AI suggestions should be treated as ideas for double-checking with the clients and not as proof on their own.