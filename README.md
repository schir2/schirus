#schir.us _website_

## Setup

1. activate virtual environment
2. run `pip install -r requirements.txt`
3. create `/schirus/.env'` and add `SECRET_KEY=your_key` variable to the file.

## Migrations
Run the following manage shell commands in order 
- `python manage.py shell` (To activate shell)
- `makemigrations`
- `sqlmigrate users 0001`
- `migrate`
- `makemigrations blog`
- `sqlmigrate blog 0001`
- `migrate`