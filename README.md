# Flask Authentication + Menu Workshop

## Goal

Build a simple admin authentication flow and menu management system using the Flask concepts from Session 1.

## Already provided

- Flask application
- SQLite database
- `users` table
- `menu` table
- Default admin user: `admin` / `1234`
- Login HTML page
- Menu HTML page
- Menu display using `SELECT`
- `/login`, `/menu`, and `/add-item` routes
- Codespaces configuration

## Participant Tasks

### 1. Login

Complete `/login`:

- Get username and password using `request.form`
- Check the `users` table
- If the credentials are correct, store the login in the session
- Send the admin to `/menu`

### 2. Add Menu Item

Complete `/add-item`:

- Get name and price using `request.form`
- Insert the item into SQLite
- Commit the change
- Show the updated menu

### 3. Access Control

The `/menu` route should only be accessible after admin login.

## Run

```bash
python app.py
```

The application uses port **5001**.

## Submission

Work on your own branch and create a Pull Request to `main`.

The instructor reviews the Pull Request and approves or requests changes before merging.

## Note

This is a beginner workshop exercise. The authentication implementation is intentionally simple and is not intended for production use.
