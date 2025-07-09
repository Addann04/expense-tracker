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
    expense-tracker/
    ├── src/
    │   ├── app.py
    │   ├── db.py
    │   └── ...
    ├── requirements.txt
    └── README.md
    ```

# UML Diagrams
### Class Diagram
```mermaid
classDiagram
    class Expense {
        +int id
        +str item_name
        +str item_type
        +int quantity
        +float price
        +date date_of_purchase
    }

    class db {
        +add_expense(item_name, item_type, quantity, price, date_of_purchase)
        +get_expenses()
        +clear_expenses()
    }

    class utils {
        +validate_file_type(file)
        +log_message(message)
        +format_expense_data(expense_data)
    }

    class app {
        +main()
    }

    Expense <.. db : uses
    db <.. app : uses
    utils <.. app : uses
```
### Object Diagram
```mermaid
erDiagram
    EXPENSE {
        int id
        string item_name
        string item_type
        int quantity
        float price
        date date_of_purchase
    }

    APP {
        string app_name
    }

    DB {
        string db_type
    }

    UTILS {
        string utility_name
    }

    APP ||--o| EXPENSE : manages
    APP ||--o| DB : uses
    APP ||--o| UTILS : uses

```
### Sequence Diagram
```mermaid
sequenceDiagram
    participant User
    participant App
    participant DB
    User->>App: Fill purchase details & click "Add Purchases"
    App->>DB: add_expense(item_name, category, quantity, price, date)
    DB-->>App: (commit to DB)
    App-->>User: Show success message, update tables
```
### Use Case Diagram
```mermaid
usecase
    actor User
    User --> (Add Purchase)
    User --> (Edit Expense)
    User --> (View Expenses)
    User --> (Analyze Spending)
```
### Collaborative Diagram
```mermaid
graph TD
    User-->|inputs purchase|App
    App-->|calls add_expense|DB
    DB-->|stores data|Expense
    App-->|shows update|User
```
### Activity Diagram
```mermaid
flowchart TD
    Start([Start])
    Enter[Enter Purchase Details]
    Validate[Validate Input]
    Add[Add Purchases Button Clicked?]
    Save[Save to Database]
    Update[Update Entry Table]
    Show[Show Expenses Table]
    Edit[Edit Expenses?]
    SaveEdit[Save Changes]
    UpdateDB[Update Database]
    Analyze[Show Analysis Graphs]
    End([End])

    Start --> Enter --> Validate
    Validate --> Add
    Add -- Yes --> Save --> Update --> Show
    Add -- No --> Enter
    Show --> Edit
    Edit -- Yes --> SaveEdit --> UpdateDB --> Analyze
    Edit -- No --> Analyze
    Analyze --> End
```

## Customization

- **Categories:**  
  You can edit the lists for item names and types in `app.py` to match your needs.

- **Database:**  
  Uses SQLite by default. You can change the database URL in `db.py` for other SQL databases.
