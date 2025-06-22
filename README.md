# Expense Tracker

A simple, interactive expense tracker web app built with **Streamlit** and **SQLAlchemy**.  
You can add, edit, and analyze your purchases with an Excel-like interface and visual graphs.

---

## Features

- **Add Purchases:**  
  Enter item name, type, quantity, price (₹), and date of purchase in a dynamic table.

- **Editable Expenses Table:**  
  View and edit all your expenses directly in the web app. Save changes to the database.

- **Purchase Analysis:**  
  Visualize your spending with:
  - Bar charts for each date (item type vs. price)
  - A summary chart for all days in the current month

- **Rupee Symbol Support:**  
  All prices are displayed with the ₹ symbol.

---

## Setup Instructions

1. **Clone the repository:**
    ```
    git clone <your-repo-url>
    ```

2. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

3. **Run the app:**
    ```
    streamlit run src/app.py
    ```

## Project Flow Chart

```mermaid
flowchart TD
    A([Start Web App])
    B([Enter Purchase Details<br/>(Editable Table)])
    C([Add Purchases Button])
    D([Save Purchases to DB<br/>and Remove from Entry])
    E([Show Expenses Table<br/>(Editable, Save Changes)])
    F([Save Changes Button])
    G([Update Expenses in DB])
    H([Purchase Analysis<br/>(Graphs & Charts)])
    I([End])

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> I
```
expense-tracker/
├── src/
│   ├── app.py
│   ├── db.py
│   └── ...
├── requirements.txt
└── README.md
```

---

## Customization

- **Categories:**  
  You can edit the lists for item names and types in `app.py` to match your needs.

- **Database:**  
  Uses SQLite by default. You can change the database URL in `db.py` for other SQL databases.
