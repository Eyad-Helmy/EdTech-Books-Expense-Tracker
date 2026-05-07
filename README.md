# EdTech-Books-Expense-Tracker
Manages and tracks expenses for a company that distributes educational tech books.

## Setup

1. Create and activate a Python virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
2. Install project dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Copy the environment template and update the database values:
   ```powershell
   copy .env.example .env
   ```
4. Update `.env` with your MySQL credentials.
5. Apply migrations:
   ```powershell
   python manage.py migrate
   ```
6. Run the development server:
   ```powershell
   python manage.py runserver
   ```

## Environment variables

Use `.env` to configure:
- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DJANGO_ALLOWED_HOSTS`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`
