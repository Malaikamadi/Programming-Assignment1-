# Programming-Assignment1-
#  Limkokwing Library API Simulation

##  Project Overview

This project is a simple Python-based simulation of a library API system designed for Limkokwing University. It demonstrates how a digital system can manage core library operations such as searching for books, borrowing, returning, and tracking overdue items with fines.

The system is built with simplicity, efficiency, and usability in mind, ensuring it can be easily understood and used by staff with limited technical knowledge.



##  Objectives

* Simulate core API endpoints for a library system
* Demonstrate asynchronous programming to handle multiple users
* Implement borrowing and returning logic with error handling
* Track overdue books and calculate fines
* Use clean and structured JSON-like responses



##  Features

*  Search books by title, author, or category (conceptual API)
*  Borrow books (with availability check)
*  Return books (with fine calculation)
*  Overdue tracking system
*  Asynchronous handling of multiple users
*  Structured responses similar to real APIs



## API Endpoints (Simulated)

### 1. GET /books

Search for books using filters such as title, author, or category.

### 2. POST /borrow

Allows a user to borrow a book if it is available.

### 3. POST /return

Allows a user to return a borrowed book and calculates fines if overdue.

### 4. GET /overdue

Displays overdue books and associated fines.


##  System Architecture

```
Client (User Interface)
        ↓
      API Layer
        ↓
   Server Logic
        ↓
     Database
```

* Client sends requests (search, borrow, return)
* API processes and validates requests
* Server handles business logic
* Database stores books and transactions



##  Technologies Used

* Python 3
* asyncio (for asynchronous programming)
* datetime (for due dates and fines)
* typing (for type annotations)



##  How to Run the Project

### Step 1: Navigate to the project folder

```bash
cd your-folder-name
```

### Step 2: Run the script

```bash
python3 library.py
```



##  Sample Output

```
User 101 borrowed 'Python Basics' (Due: 2026-05-06)
User 102: Book not available
User 101 returned 'Python Basics' | Fine: 0 Le
User 102 borrowed 'Python Basics' (Due: 2026-05-06)
```



##  Challenges Faced

* Managing multiple users accessing the system simultaneously
* Preventing duplicate borrowing of the same book
* Structuring responses to remain simple and readable
* Implementing asynchronous logic correctly



##  Security Considerations

* Input validation to prevent invalid requests
* Controlled access to book records
* Prevention of unauthorized returns



##  Future Improvements

* Add user authentication (login system)
* Connect to a real database (e.g., PostgreSQL)
* Build a frontend interface for staff
* Convert simulation into a real API using frameworks like FastAPI



##  SDG Alignment

This project supports SDG 4: Quality Education by improving access to educational resources through digital transformation of library services.



##  Author

Alimatu Maliaka Jalloh
BSc Software Engineering & Multimedia
Limkokwing University



##  Conclusion

This project demonstrates how a simple API-driven system can significantly improve efficiency in library management. By leveraging asynchronous programming and structured design, the system ensures scalability, usability, and reliability for real-world applications.
