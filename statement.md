# PROJECT STATEMENT

# LIBRARY MANAGEMENT SYSTEM

## 1. Introduction

The Library Management System is a Python-based console application developed to simplify basic library operations. Libraries contain different types of books, and managing their details and student borrowing records manually can sometimes become difficult.

This project provides a simple platform where students can explore books from different categories, select their preferred books, and submit their personal details for borrowing records.

The system also includes an admin login facility that allows authorized users to access the borrowing records using a password.

The project is developed using basic Python programming concepts and focuses on creating a simple, understandable, and user-friendly application.

## 2. Problem Statement

In a traditional library system, managing books and maintaining student borrowing records manually can consume time and may lead to errors. Students may also face difficulties in finding books from different categories.

There is a need for a simple computerized system that can organize book information, provide easy access to available book categories, and maintain basic borrowing records.

The main problem addressed by this project is the lack of a simple and organized method for handling basic library activities through a computerized application.

To solve this problem, the proposed Library Management System uses Python programming to provide book selection facilities, student information collection, and password-protected admin access.

## 3. Aim of the Project

The main aim of this project is to design and develop a simple Library Management System using Python that helps students explore different categories of books and allows the administrator to check borrowing records.

## 4. Objectives of the Project

The major objectives of this project are:

1. To develop a basic library management application using Python.
2. To provide separate access options for Admin and Students.
3. To implement a password-based authentication system for administrators.
4. To display books under different categories.
5. To organize books into Literature, Physics, and CSE categories.
6. To allow students to select books using serial numbers.
7. To collect student names and registration numbers.
8. To maintain basic borrowing records.
9. To provide an easy-to-understand console interface.
10. To apply Python programming concepts in a real-world application.
11. To reduce the complexity of maintaining manual borrowing records.
12. To improve the understanding of conditional statements, loops, lists, and strings.

## 5. Proposed System

The proposed system is a console-based application developed using Python. It provides two types of users: Admin and Student.

The administrator must enter a password to access the borrowing records. After successful authentication, the admin can choose whether to view the available records.

Students can directly access the book selection section. The system displays three categories of books: Literature, Physics, and Computer Science and Engineering.

After selecting a category, students can view the available books and choose a particular book using its serial number. The system then asks whether they want to borrow the selected book.

If the student agrees, the application collects their name, registration number, and book name. These details are added to the borrowing record list.

The application also displays a borrowing period of 14 days to inform students about the allowed borrowing duration.

## 6. Functional Requirements

The system provides the following functional requirements:

### 6.1 User Role Selection

The application allows users to select either Admin or Student when starting the program.

### 6.2 Admin Authentication

The system asks the administrator to enter a password before accessing borrowing records.

### 6.3 Limited Login Attempts

The administrator gets a maximum of three password attempts.

### 6.4 Borrowing Record Access

After successful login, the administrator can choose whether to view the existing borrowing records.

### 6.5 Book Categories

The system provides three different book categories:

* Literature
* Physics
* Computer Science and Engineering

### 6.6 Book Display

The application displays the books available in the selected category.

### 6.7 Book Selection

Students can select books by entering their corresponding serial numbers.

### 6.8 Student Information

The system collects the following details:

* Student Name
* Registration Number
* Selected Book Name

### 6.9 Borrowing Record Creation

The system stores the entered student details and selected book information in a Python list.

### 6.10 User Feedback

The application displays appropriate messages for valid and invalid inputs.

## 7. Non-Functional Requirements

The non-functional requirements describe the quality and usability of the application.

### 7.1 Simplicity

The system is designed with simple Python code so that beginners can easily understand its working.

### 7.2 User-Friendly Interface

The application uses clear instructions and menu-based input to help users navigate through the system.

### 7.3 Basic Security

The admin section is protected using a password-based login mechanism.

### 7.4 Reliability

The system uses conditional statements to handle different user choices and provide suitable responses.

### 7.5 Maintainability

The code is organized into understandable sections, making it easier to modify or improve in the future.

### 7.6 Portability

Since Python is a cross-platform programming language, the application can run on different operating systems with Python installed.

## 8. Technology Used

**Programming Language:** Python 3

**Development Environment:** Python IDLE / VS Code / PyCharm

**Application Type:** Console-Based Application

**Python Concepts Used:**

* Variables
* Strings
* Lists
* Conditional Statements
* While Loops
* If-Else Statements
* User Input and Output
* String Methods
* Password Validation

## 9. System Workflow

The application follows the workflow given below:

1. The program starts.
2. The user selects Admin or Student.
3. If Admin is selected, the system requests a password.
4. The password is checked for a maximum of three attempts.
5. After successful authentication, the admin can view borrowing records.
6. If Student is selected, the system displays the available book categories.
7. The student selects a category.
8. The system displays the books under that category.
9. The student enters the serial number of the preferred book.
10. The system displays the selected book information.
11. The student is asked whether they want to borrow the book.
12. If the student agrees, their details are collected.
13. The details are added to the borrowing record list.
14. The program completes the selected operation.

## 10. Expected Results

The expected result of this project is a working Python application that performs basic library management activities.

The system should successfully allow administrators to access borrowing records after password verification.

Students should be able to explore different categories of books, select books using serial numbers, and enter their personal information for borrowing records.

The project demonstrates how Python can be used to develop a simple application for solving basic management problems.

## 11. Limitations of the Project

Although the system provides basic library management facilities, it has certain limitations:

1. The application works only through a console interface.
2. The records are stored temporarily in a Python list.
3. The records are not permanently saved after the program terminates.
4. The system does not automatically check book availability.
5. There is no separate book return facility.
6. Multiple users cannot access the system simultaneously.
7. The admin password is directly written in the source code.
8. The system does not automatically calculate overdue days or fines.

## 12. Future Enhancements

The project can be improved in the future by introducing additional features.

1. Permanent storage of records using files or databases.
2. A graphical user interface for better interaction.
3. Automatic book availability checking.
4. Book return and renewal facilities.
5. Student login authentication.
6. Automatic calculation of late return fines.
7. Search books by title or author.
8. Admin facilities to add and remove books.
9. Better record management using dictionaries and databases.
10. Generation of borrowing reports.

## 13. Conclusion

The Library Management System is a beginner-friendly Python project that demonstrates the practical application of fundamental programming concepts.

It provides a simple method for displaying books, selecting books, collecting student information, and maintaining basic borrowing records.

Through this project, we gain practical knowledge of conditional statements, loops, lists, strings, and user input in Python.

The project also helps us understand how programming can be used to solve real-world management problems.

Although the current version focuses on basic functionalities, it provides a foundation for developing a more advanced library management application in the future.

## 14. Project Information

**Project Title:** Library Management System

**Project Developer:** Siddesh S P

**Registration Number:** 26BCE10178

**Course:** B.Tech CSE Core

**Institution:** VIT Bhopal University

**Programming Language:** Python

**Project Category:** Build Your Own Project

**Application Type:** Console-Based Application
