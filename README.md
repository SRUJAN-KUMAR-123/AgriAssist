# AgriAssist – Empowering Agriculture with Technology

AgriAssist is a web-based platform designed to support farmers by providing a digital marketplace for buying and selling agricultural products, accessing the latest news, discussing in forums, and getting assistance through an intelligent chatbot. It bridges the gap between farmers and modern technologies to enhance productivity and profitability in agriculture.

---

## Features

- 🛒 **Product Marketplace:** List and browse fresh produce, crops, vegetables, and fruits.
- 🗣️ **Community Forum:** A dedicated space where farmers can ask questions, share solutions, and interact with each other.
- 📢 **Agri-News Feed:** Stay updated with the latest agricultural trends and policies.
- 💬 **Farming Chatbot:** Integrated chatbot using Voc.ai to resolve farmers' queries.

---

## 🛠️ Tech Stack
_____________________________________________________
| Layer       | Technology Used                     |
|-------------|-------------------------------------|
| Frontend    | HTML, CSS, JavaScript               |
| Styling     | Tailwind CSS                        |
| Backend     | Django (Python Framework)           |
| Database    | PostgreSQL                          |
| Chatbot     | Voc.ai Chatbot Integration          |
_____________________________________________________

---

## 📷 Screenshots

### 🏠 Homepage
![Screenshot 2024-12-01 193224](https://github.com/user-attachments/assets/23b75e54-53b3-483c-8aeb-049658e62ba6)

### 🤖 ChatBot
---![Screenshot 2024-12-02 080802](https://github.com/user-attachments/assets/cca791a8-c98b-4b9a-9c93-dad275789c0c)

### 🛒 Product Page
![Screenshot 2024-12-01 194632](https://github.com/user-attachments/assets/e2ccfd61-308a-4c52-99bc-9e31bc3f7af8)

### ➕ Add Product
![Screenshot 2024-12-01 194746](https://github.com/user-attachments/assets/72c02c24-b7fb-438b-b2b9-b3f52016585e)

### 💬 Community Forum
![Screenshot 2024-11-29 203211](https://github.com/user-attachments/assets/3257e27f-b1e5-4cd5-9bcc-0ad23c4ad010)

## 📁 Project Structure

<code> AgriAssist/
├── agriassist/ # Django project settings
├── forum/ # Community forum discussions and threads
├── login/ # User Registrations Management
├── mediaroot/ # Chatbot interaction and integration
├── shop/ # Product listing and management
├── templates/ # HTML templates
└── manage.py # Django management script</code>

### Requirements
- python 3.11
- postgres server


### Steps to deployment
1. Create a virtual environment in AgriAssist directory\
   `python3 -m venv venv`
2. Install required dependencies (make sure venv is activated)\
   `pip install -r requirements.txt`
3. Install PostGres Server\
   [Link to Installer](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
4. Migrate Django models\
   `python manage.py migrate`
5. Run Django server\
   `python manage.py runserver`
- Create django super user to access/modify models data\
  `python manage.py createsuperuser`
6. Acess Application : Open your browser and go to http://127.0.0.1:8000


## ❌ No payment or transaction modules


## 🤝 Contributions
### We welcome contributions! Here's how you can help:

- Fork the repository

- Create your branch (git checkout -b feature-name)

- Commit your changes (git commit -m 'Add feature')

- Push to the branch (git push origin feature-name)

- Create a pull request


## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).


## 📬 Contact
### Developer: Srujan Kumar Cheekati
- Location: Ongole, Andhra Pradesh, India
- 📧 Email: srujanch75@gmail.com
- 🌐 LinkedIn: https://www.linkedin.com/in/srujan-kumar-cheekati-101828281/

