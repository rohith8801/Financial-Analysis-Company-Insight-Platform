# How to Run the Project

Follow the steps below to run the complete application.

---

# Step 1 — Clone Repository

```bash
git clone <repository-url>
```

---

# Step 2 — Setup MySQL Database

Start the MySQL server.

Create a database named:

```
bluestocks
```

Import the SQL file:

```
database/database.sql
```

---

# Step 3 — Run Backend

Open Terminal.

Navigate to backend folder.

```bash
cd backend
```

Install required packages.

```bash
pip install -r requirements.txt
```

Run the Flask server.

```bash
python app.py
```

Backend runs on:

```
http://127.0.0.1:5000
```

---

# Step 4 — Test Backend API

Open your browser.

Example:

```
http://127.0.0.1:5000/company/TCS
```

If JSON is displayed, the backend is running correctly.

---

# Step 5 — Run Frontend

Open another terminal.

Navigate to frontend folder.

```bash
cd frontend
```

Install dependencies.

```bash
npm install
```

Start React.

```bash
npm start
```

Frontend runs on:

```
http://localhost:3000
```

---

# Step 6 — Using the Application

1. Open the React application.
2. Enter a valid Company ID.
3. Click **Analyze**.
4. The application fetches financial data.
5. The backend processes the data.
6. Results are stored in MySQL.
7. The frontend displays:
   - Company details
   - Financial metrics
   - Pros & Cons
   - Charts
   - Company comparison

---

# Project Workflow

```
User
 │
 ▼
React Frontend
 │
 ▼
Flask REST API
 │
 ▼
Financial Data Processing
 │
 ▼
MySQL Database
 │
 ▼
JSON Response
 │
 ▼
Interactive Dashboard
```

---

# Notes

- MySQL server must be running before starting the backend.
- Backend must be running before starting the frontend.
- `node_modules` is intentionally excluded from the repository.
- Install frontend dependencies using `npm install`.
