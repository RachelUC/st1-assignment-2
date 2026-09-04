# <u>*PART B*</u> 
## 5 Limitations:
1. Only works for a fixed number of appointments - 
The basic version uses separate variables for each appointment, like patient1_name and patient2_name. 
If we want to add a third appointment, we would have to write a whole new set of variables and another print line by hand. 
The enhanced version keeps all appointments in one list, so we can just call book_appointment() again to add more, with no extra typing needed.
2. Doesn't check the input properly - 
In the basic version we can type in anything, even a blank patient name. The other version checks if the patient name is empty and stops the booking with an error message if it is, so bad data doesn't get saved.
3. Can't remove or change an appointment - 
Once we add an appointment, there's no way to cancel it or fix a mistake in either version. For example, if Bob Johnson cancels his visit, his appointment still stays in the list in both versions, since there's no way to delete it.
4. Doesn't stop double-booking - 
Neither version checks if a doctor is already busy at that time. For example, we could book Ali Khan with Dr. John Doe at the same time Alice Smith already has, and the program just adds it anyway, so Dr. John Doe ends up with two patients booked for the same time slot.
5. No format checking on appointment time - 
The time is stored as plain text, so anything can be typed in, even something that isn't a real time. 
For example, calling book_appointment('Alice Smith', 'Dr. John Doe', 'sometime tomorrow') would be accepted just as easily as a properly formatted time like '2024-07-20 10:00 AM'. 
The program has no way to tell the difference between a real time and just text.