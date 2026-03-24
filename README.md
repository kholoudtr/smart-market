# 🛒 Smart Market - Django E-commerce Platform 🚀

**Smart Market** is a fully functional, database-driven e-commerce application built with **Django**. It manages a grocery-style marketplace where users can browse products by category, manage a shopping cart, and handle their accounts securely.

## 🌟 Real Features Implemented
* **User Lifecycle Management:** Complete authentication system including Sign-up, Login, and a robust **Password Reset** workflow (via `accounts` app).
* **Dynamic Product Catalog:** Products are organized by categories with support for high-quality image uploads and inventory display.
* **Shopping Cart System:** A dedicated interface (`cart.html`) to manage selected items before final checkout.
* **Template Inheritance:** Optimized frontend using a `base.html` layout to ensure UI consistency across all pages.
* **Admin Control:** Leveraging Django's admin to manage orders, products, and customer data efficiently.

## 🛠️ Technical Implementation
* **Backend:** Python 3.12 / Django.
* **Database:** SQLite (Relational schema with Migrations).
* **Frontend:** Django Templates Engine with custom logic for product filtering.
* **Media Handling:** Configured to manage dynamic product imagery stored in `/media/`.

## 📂 Project Structure
* `accounts/`: Handles user profiles, password security, and authentication views.
* `market/`: Core business logic for products, categories, and shopping interactions.
* `templates/`: Centralized UI components for a seamless user experience.

---

## 🚀 How to Run the Project

### 1. Clone & Setup
```bash
git clone [https://github.com/kholoudtr/smart-market.git](https://github.com/kholoudtr/smart-market.git)
cd smart-market
2. Environment (Recommended)
Bash
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
3. Install & Migrate
Bash
pip install django  # and any other requirements
python manage.py migrate
4. Launch
Bash
python manage.py runserver
Access the market at http://127.0.0.1:8000/