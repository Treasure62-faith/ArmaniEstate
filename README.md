# 🏠 ArmaniEstate API

A fully-featured Real Estate backend built with **Django REST Framework**. Supports agent and renter/buyer roles, property listings, media uploads, inquiries, JWT authentication, and is Stripe-ready for payment integration (coming soon).

---

## 🔥 Features

- 🔐 **JWT Authentication**
- 👤 **Agent & Renter/Buyer Roles**
- 🏡 **Agents** can Create, View, Update & Delete Listings
- 🔎 **Renters/Buyers** can Browse & Search Listings
- 💬 **Inquiries System** for Messaging Agents
- 🖼️ **Profile Management** with Image Upload
- 🌍 **Role Selection during Registration**
- 🧠 Modular Django Apps:
  - `user` – registration, login, profile, etc.
  - `listings` – property management
  - `api` – central project settings
  - (Stripe `checkout` integration coming soon)

---

## 🧰 Tech Stack

| Component    | Technology                   |
|--------------|-------------------------------|
| Backend      | Django + Django REST Framework |
| Auth         | JWT (Simple JWT)              |
| Media Upload | Local `media/` storage         |
| Payments     | Stripe API *(coming soon)*    |
| Database     | PostgreSQL                    |
| API Docs     | Swagger (drf-yasg planned)    |

---

## 🧪 Sample Endpoints

| Feature              | Endpoint                                | Method |
|----------------------|-----------------------------------------|--------|
| Register             | `/api/user/register/`                   | POST   |
| Login / Token        | `/api/token/`                            | POST   |
| All Listings         | `/api/listings/`                         | GET    |
| Single Listing       | `/api/listings/<id>/`                   | GET    |
| Create Listing       | `/api/listings/create/`                 | POST   |
| Make Inquiry         | `/api/listings/inquire/`                | POST   |
| User Dashboard       | `/api/user/dashboard/`                  | GET    |

---

## 🧰 Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/Treasure62-faith/ArmaniEstate.git
cd ArmaniEstate

# 2. Create & activate virtual environment
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file and add secrets
# (example below)

# 5. Run migrations
python manage.py migrate

# 6. Run the server
python manage.py runserver

📧 Email: treasurefaithdev@gmail.com
🔗 GitHub: Treasure62-faith
🔗 https://www.linkedin.com/in/olafare-josh-a7a165347/
