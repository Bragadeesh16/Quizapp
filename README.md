
# Project Name: Quiz App

## 1. How to Run the Project

### Prerequisites
Ensure the following are installed on your system:

- Python 3.10+
- Django
- SQLAlchemy (or any other database of your choice)
- SQLite (or another database, if preferred)

### Installation Steps
1. **Clone the repository**:

    ```bash
    git clone https://github.com/Bragadeesh16/Quizapp.git
    cd Quizapp
    ```

2. **Set up a virtual environment**:

    ```bash
    python3 -m venv env
    source env/bin/activate  # For Linux/MacOS
    env\Scripts\activate     # For Windows
    ```

3. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run database migrations** (if you're using Django's default database setup with SQLite or any other database):

    ```bash
    python manage.py makemigrations
    ```

    ```bash
    python manage.py migrate
    ```

5. **Run the Django development server**:

    ```bash
    python manage.py runserver
    ```

   The application will be accessible at [http://127.0.0.1:8000](http://127.0.0.1:8000).
