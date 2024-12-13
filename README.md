
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
    pip install -r pip-requirements.txt
    ```

4. **Run database migrations** (if you're using Django's default database setup with SQLite or any other database):

    ```bash
    python manage.py makemigrations
    ```

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:

    Run the following command to create a superuser account:

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to set a email, username, and password.

6. **Run the Django development server**:

    ```bash
    python manage.py runserver
    ```


   The application will be accessible at [http://127.0.0.1:8000](http://127.0.0.1:8000).


## 2. How to Add Questions in the Admin Panel

1. **Login to the Django Admin Panel**:
   - Visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) in your browser.
   - Login using the superuser credentials you created earlier.

2. **Add a Question Bank**:
   - After logging in, you will be directed to the admin dashboard.
   - In the admin panel, look for the "Question Bank" section.
   - Click on the "Question Bank" model to view existing question banks (if any) or to create a new one.
   - Click on the "Add Question Bank" button to create a new question bank, and fill in the necessary fields.

3. **Add Questions to the Question Bank**:
   - Once the question bank is created, go to the "Questions" section.
   - Click on the "Add Question" button to add a new question.
   - For each question, fill in the fields such as:
     - The text of the question.
     - The four possible options (A, B, C, D).
     - The correct answer.
     - The question should belong to the question bank you created earlier (select it from the dropdown list).

4. **Save and Repeat**:
   - After adding the question, click "Save."
   - You can repeat the process to add more questions to your question bank.
"""