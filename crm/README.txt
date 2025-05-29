# 🏠 Real Estate CRM

A clean and modern Real Estate CRM (Customer Relationship Management) system to help agents manage clients, properties, and leads. Built using Flask (Python) and a fully responsive HTML dashboard.

---

## 🚀 Features

- 📊 **Dashboard:** Overview of total clients, properties, active leads, and monthly sales
- 👥 **Clients Management:** Add, edit, delete, and filter clients by status and type
- 🏘️ **Properties Management:** Manage property listings with filters for type, status, and price range
- 📞 **Leads Management:** Track prospective clients with status, interest, and budget
- 📈 **Reports:** Monthly performance and property type distribution charts
- 🧠 **Activity Feed:** Recent updates on clients, properties, and leads
- 🔍 **Search Functionality:** Easily find clients or leads using search bars
- 🎨 **Responsive UI:** Works beautifully on desktop and mobile

---

## 🛠️ Tech Stack

| Layer        | Technology     |
|--------------|----------------|
| Frontend     | HTML, CSS, JavaScript, Font Awesome |
| Backend      | Python (Flask) |
| Database     | SQLite (`real_estate_crm.db`) |

---

## 📁 Project Structure

```
real-estate-crm/
├── app.py                 # Flask backend server
├── real_estate_crm.db     # SQLite database file
└── index.html             # Frontend UI (dashboard, forms, etc.)
```

---

## ▶️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/real-estate-crm.git
cd real-estate-crm
```

### 2. Set Up the Environment

Make sure Python 3 is installed. Then install Flask:

```bash
pip install flask
```

### 3. Run the Flask Server

```bash
python app.py
```

This will start the app on:

```
http://127.0.0.1:5000
```

### 4. Open the CRM Dashboard

In your browser, open the `index.html` file or point to the Flask route (if integrated).

---

## 📷 Screenshots

> Add real screenshots in your GitHub repo and link them here:

- **Dashboard Overview**

  ![Dashboard](screenshots/dashboard.png)

- **Client Management**

  ![Clients](screenshots/clients.png)

- **Property Listings**

  ![Properties](screenshots/properties.png)

- **Lead Management**

  ![Leads](screenshots/leads.png)

---

## 🔒 Limitations

- No user authentication (anyone can access data)
- In-memory sample data used in HTML — not persistent unless integrated with Flask
- For production use, integrate `index.html` as Flask templates or serve via a web server

---

## 🧩 To Do

- [ ] Add authentication (login/logout)
- [ ] Migrate sample data to use SQLite fully
- [ ] RESTful API endpoints for client/property/lead management
- [ ] Deploy on Render/Heroku

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss your ideas.

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
