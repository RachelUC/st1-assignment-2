# <u>*PART A*</u> 
### What data should be stored? 
For each appointment, 3 data needs to be stored:

- Patient name
- Practitioner name
- Appointment Time

Together these form one "Appointment record"

### What functions might be useful?

- book_appointment - add a new appointment to storage
- display_appointments - show all booked appointments
- cancel_appointment - remove an appointment
- find_appointment - search by patient name or time

### What could go wrong?

- Empty or missing field inputs (e.g., no patient name entered)
- Double-booking (e.g., Two patients get booked with the same practitioner at the same time)
- Appointment time in the wrong format (e.g., "10am" vs "10:00 AM")
- Same patient accidentally booked twice
- All data is lost when the program closes (nothing is saved to a file)

### What requirements are unclear?

- What format should the appointment time be in? (date + time? just time? 12-hour or 24-hour clock?)
- Can one practitioner have multiple patients at the same time or must each slot be exclusive?
- Should the system stop double-bookings or just record whatever is entered?
- Does data need to be saved permanently (to a file or database) or is it fine if it's lost when the program ends?
- Should there be a way to edit or cancel an existing appointment or only add new ones?


# <u>*PART H*</u>

Before the AI, I had only built the basic input/output version of the SmartCare booking system — a few variables for patient name, practitioner name, and appointment time, printed directly using print statements. 
It worked, but only for a fixed number of appointments and it had no way to check for bad input.

AI mainly helped me understand two things: 
why validation matters and how functions and dictionaries work together to organize data. 
Seeing my own code compared side by side with the AI version made it clear why checking every field (not just patient name) prevents bad data from being stored and 
why grouping related data into a dictionary inside a function is more flexible than repeating separate variables for each appointment.

I don't think the AI made any major false assumptions in this case, since the task itself was fairly well-defined and the code stayed close to the structure I already had.
I mostly trusted the AI's output, though I did test it by running both versions with the same inputs to compare results directly.

To verify the AI output, I ran both my version and the AI version through the same four test cases (normal appointment, blank patient name, double-booking, and None values) and 
compared the printed results line by line rather than just assuming the AI was correct.

The engineering work that remained for me was deciding which single improvement was worth making, understanding why the fix mattered and actually testing it to confirm the bug was resolved.

