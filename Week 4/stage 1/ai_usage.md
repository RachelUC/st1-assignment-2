#  <u>*PART C*</u> 

## What the Code Does

In short: it records appointments in a list and prints them out.

Here's the flow:

- The global list appointments stores every booking.
- book_appointment() creates a dictionary with a patient, practitioner, and time.
  - It checks that the patient name isn't empty.
  - It appends the appointment to the global list.
- display_appointments() prints all stored appointments, or a message if none exist.
- At the bottom, two appointments are booked and then displayed.

So the program acts as a tiny in-memory scheduling system.

## Three Limitations

- **No time conflict detection** — The system doesn't check whether two appointments overlap.
- **No persistence** — All data disappears when the program ends because it only lives in RAM.
- **Weak validation** — Only the patient name is validated; practitioner and time could be empty or malformed.

## Improvements (Without Rewriting the Whole App)

- **Add stronger validation** — Ensure practitioner and time are not empty and follow a valid format.
- **Check for conflicts** — Before adding an appointment, scan the list for overlapping times.
- **Add persistence** — Save appointments to a JSON file so they survive program restarts.

These keep your structure intact while making the system more realistic.

## Two Questions to Test Your Understanding

1. Why might storing appointments in a global list cause problems in a larger application?
- Because it's shared by everything, any part of the code can change it, which makes bugs easy and testing hard. 
It also doesn't scale well (searching gets slow) and isn't safe if multiple bookings happen at once.

2. What advantage does using a dictionary for each appointment give you compared to using a tuple?
- A dictionary lets us access values by name instead of position which makes the code easier to read and safer to change. 
For example, with a tuple like ("John", "Dr. Smith", "10am"), we will get the time by using appointment[2], we just have to remember what each position means.
- With a dictionary like {"patient": "John", "practitioner": "Dr. Smith", "time": "10am"}, we will have to write appointment ["time"] instead which is much clearer.
Dictionaries also make it easier to add new fields later (like a "status") without breaking existing code, since tuples rely on strict position and order.