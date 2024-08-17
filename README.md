# python_tkinter_form

This code implements a simple GUI form using Python's Tkinter library, which is integrated with an Oracle database using the cx_Oracle module. The form collects basic user information, such as first name, last name, gender, and email. It also includes features for validating user input, particularly email addresses, and ensures that required fields are filled out before allowing data submission.

## Features:
1) Input Validation: The form ensures that all required fields are filled, and the email format is validated using regular expressions.
2) Database Integration: Upon submission, the data is securely inserted into the form_details table in an Oracle database.
3) User Experience: Buttons for clearing and submitting data are included, with the submit button only enabled when all fields are valid.

The form ensures data integrity by preventing submission of incomplete or invalid information.
Error handling is incorporated in the database submission process to catch and print any database-related errors.
An owner's name label at the bottom gives credit to the form creator.
This code provides a solid foundation for creating a user-friendly data entry form connected to an Oracle database, demonstrating how to combine Python's GUI capabilities with database management.

## Image:
![image](https://github.com/user-attachments/assets/6dac44ac-b72c-4b43-b4ba-eecc5acc0ced)

