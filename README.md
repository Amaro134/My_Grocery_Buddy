# My Grocery Buddy

A full-stack web application for managing personal grocery lists with user authentication and category-based organization.

## Project Overview

My Grocery Buddy is a Django-based shopping list application that allows users to:
- Register and log in securely
- Create and manage personal grocery lists
- Organize items by categories (Produce, Dairy, Meat, Bakery, Pantry, Frozen, Beverages, Snacks, Other)
- Mark items as completed/active
- Filter items by status (All, Active, Completed)
- View statistics (Total, Remaining, Completed items)
- Perform bulk operations (Clear Completed, Clear All)

## Tech Stack

- **Backend**: Django 5.2.7
- **Database**: SQLite3
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5.3.2
- **Authentication**: Django's built-in authentication system with password hashing

## Features

### User Authentication
- User registration with username, email, and password
- Email and username uniqueness validation
- Password confirmation
- Secure password hashing (Django's PBKDF2)
- Session-based authentication
- Protected routes (login required for grocery list access)

### Grocery List Management
- Add items with name, quantity, and category
- Edit items (name, quantity, category)
- Delete items with confirmation
- Mark items as completed/active with visual feedback
- Items grouped by category with item counts
- Filter by status: All Items, Active, Completed
- Statistics dashboard showing total, remaining, and completed items
- Bulk actions: Clear Completed, Clear All

### Security Features
- Password hashing (never stored in plain text)
- CSRF protection
- Input validation on both frontend and backend
- User data isolation (users can only access their own items)
- Protected routes with `@login_required` decorator
- Environment variables for sensitive data

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd alindaproject
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Set up environment variables**
   ```bash
   cd alinda
   cp .env.example .env
   # Edit .env and set your SECRET_KEY
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000/`
   - Register a new account or log in

## Project Structure

```
alindaproject/
├── alinda/
│   ├── alinda/          # Project settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   ├── lucky/           # Main application
│   │   ├── models.py    # Task model
│   │   ├── views.py     # View functions
│   │   ├── forms.py     # Form definitions
│   │   ├── urls.py      # URL routing
│   │   ├── templates/   # HTML templates
│   │   │   ├── login.html
│   │   │   ├── signup.html
│   │   │   └── list.html
│   │   └── migrations/  # Database migrations
│   ├── db.sqlite3       # SQLite database
│   └── manage.py
├── venv/                # Virtual environment
└── README.md
```

## Usage

### Registration
1. Navigate to the signup page
2. Enter username (min 3 characters)
3. Enter email address
4. Enter password and confirm password
5. Click "Sign Up"

### Login
1. Enter your username
2. Enter your password
3. Click "Login"

### Managing Grocery List
1. **Add Item**: Enter item name, quantity, and select category, then click "Add Item"
2. **Mark Complete**: Click the checkbox next to an item to mark it as completed
3. **Edit Item**: Click "Edit" button, modify the item details, and save
4. **Delete Item**: Click "Delete" button and confirm
5. **Filter Items**: Use the filter tabs (All Items, Active, Completed)
6. **Bulk Actions**: Use "Clear Completed" or "Clear All" buttons

## Security Notes

- Passwords are hashed using Django's PBKDF2 algorithm
- Never commit `.env` file to version control
- CSRF protection is enabled for all forms
- All grocery list operations require authentication
- Users can only access and modify their own items

## Testing Checklist

- [x] User registration with valid details
- [x] Cannot register with existing username/email
- [x] User login with correct credentials
- [x] Cannot login with wrong password
- [x] Cannot access grocery page without login
- [x] Can add items when logged in
- [x] Can see only own items
- [x] Can edit own items
- [x] Can delete own items
- [x] Can mark items complete/incomplete
- [x] Filters work correctly
- [x] Statistics update properly
- [x] Passwords are hashed in database
- [x] Cannot modify other users' items

## Development Notes

- The application uses Django's built-in User model
- Task model includes category choices and status tracking
- All views are protected with `@login_required` decorator
- Forms include both client-side and server-side validation
- Bootstrap 5 is used for responsive UI design

## License

This project is created for educational purposes.

## Authors

[Your Name/Team Name]

## Acknowledgments

- Django Documentation
- Bootstrap Documentation

