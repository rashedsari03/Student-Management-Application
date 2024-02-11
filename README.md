
# Student Management Application

This project is a Student Management Application developed using Python's Tkinter library for the graphical user interface (GUI) and MySQL database for data storage. The application allows users to perform various operations related to student management, such as adding new students, deleting existing students, updating student data, searching for students, and viewing all students' information.

## Key Features

- **User Interface:** The application provides a user-friendly interface with labeled entry fields, buttons, and dropdown menus for ease of interaction.
  
- **Data Validation:** It includes validation checks, such as validating email addresses using regular expressions, and ensuring data integrity.
  
- **Database Integration:** The application connects to a MySQL database to store and retrieve student information, utilizing CRUD (Create, Read, Update, Delete) operations.
  
- **Functionality:** Users can add, delete, update, and search for students within the application. The interface dynamically updates to reflect changes made to the database.
  
- **About Us:** The application includes an "About Us" feature, displaying information about the developer and the version of the application.

## Deployment

To deploy this application, users would need to have Python and MySQL installed on their systems. They would also need to create a MySQL database named "students" with a table named "stu" containing columns for student ID, name, email, phone, gender, and address. Once the database is set up, users can run the provided Python script to launch the application.
------------------------------------------------------------------------------------------------------------------------------------------------

To set up the Student Management Application to work on any device, including connecting it to a MySQL database via XAMPP, follow these steps:

### Prerequisites:
1. **Python**: Ensure Python is installed on your device. You can download and install Python from the official [Python website](https://www.python.org/).
2. **XAMPP**: Download and install XAMPP, which provides an Apache server, MySQL database, and PHP interpreter. You can download XAMPP from the [official website](https://www.apachefriends.org/index.html).

### Steps to Set Up the Application:

#### 1. Clone the Repository:
   - Clone the repository containing the Student Management Application from GitHub to your local machine.

#### 2. Install Required Libraries:
   - Ensure you have the required Python libraries installed. You can install them using pip:
     ```
     pip install pymysql
     ```

#### 3. Set Up XAMPP:
   - Install and launch XAMPP on your device.
   - Start the Apache and MySQL modules from the XAMPP control panel.

#### 4. Set Up MySQL Database:
   - Open your web browser and navigate to `http://localhost/phpmyadmin`.
   - Create a new database named `students`.
   - Inside the `students` database, create a table named `stu` with the following columns:
     - `id` (INT, Primary Key, Auto Increment)
     - `name` (VARCHAR)
     - `email` (VARCHAR)
     - `phone` (VARCHAR)
     - `gender` (VARCHAR)
     - `address` (VARCHAR)

#### 5. Update Database Connection Settings:
   - Open the Python script (`student_management.py`) in a text editor.
   - Locate the database connection settings:
     ```python
     connection = pymysql.Connect(
         host="localhost", user="root", password="", database="students"
     )
     ```
   - Modify the `host`, `user`, `password`, and `database` parameters as per your XAMPP MySQL configuration. Typically, the default settings are:
     - `host`: "localhost"
     - `user`: "root"
     - `password`: "" (empty string by default)
     - `database`: "students"

#### 6. Run the Application:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the Python script.
   - Run the script using the following command:
     ```
     python student_management.py
     ```

### Usage:
- Once the application is launched, you can use it to perform various student management operations, including adding, deleting, updating, and searching for students.
- The application's GUI will provide a user-friendly interface for interacting with the database.

By following these steps, you can set up and run the Student Management Application on any device, connecting it to a MySQL database via XAMPP for data storage and retrieval.
