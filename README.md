# AndikaKode – Learn Python the Fun Way!

AndikaKode is an interactive learning platform that introduces beginners to Python programming through a clean, simple, and visually engaging dashboard. Users can track their progress, watch video lessons, and mark chapters as complete.

---

## Live Demo

🔗 [View the live site](https://andikakode.onrender.com)

---

## 📂 Project Structure
AndikaKode/
├── AndikaKode/        # Django project root
├── app/               # Core Django app
├── media/             # Uploaded media files
├── static/            # Static assets (CSS, images)
├── db.sqlite3         # SQLite database
├── manage.py
|-- requirement.txt
README.md

---

## ⚙️ Tech Stack

- **Backend**: Django 5.2.4
- **Frontend**: HTML5, CSS3, JS
- **Database**: SQLite3
- **Hosting**: Render

---

## 🧪 Features

- User registration and login
- Course dashboard with chapter tracking
- Video embedding per chapter
- Progress tracking and completion stars
- Fully responsive UI

---

## 🛠️ Getting Started Locally

Follow these steps to run the project on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/aimable0/AndikaKode.git
cd AndikaKode

2. Create and Activate a Virtual Environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

3. Install the Dependencies
pip install -r requirements.txt

4. Apply Migrations
python manage.py migrate

5. Run the Development Server
python manage.py runserver


LICENSE:
This project is open for educational review and contributions. No license applied.


THANK YOU!