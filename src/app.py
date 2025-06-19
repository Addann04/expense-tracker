import streamlit as st
from db import add_expense, get_expenses, clear_expenses
import pandas as pd
from datetime import date
import altair as alt

def main():
    st.title("Expense Tracker")
    st.header("Enter Purchase Details")

    if "purchase_df" not in st.session_state:
        columns = ["Item Name", "Category", "Quantity", "Price", "Date of Purchase"]
        default_row = {
            "Item Name": "",
            "Category": "Grocery",
            "Quantity": 1,
            "Price": 0.0,
            "Date of Purchase": date.today()
        }
        st.session_state.purchase_df = pd.DataFrame([default_row])

    item_names = ["Milk", "Bread", "Eggs", "Rice", "Chicken", "Soap", "Shampoo", "Other"]
    categories = ["Grocery", "Clothing", "Personal Care", "Household", "Electronics", "Other"]
    quantities = list(range(1, 21))
    prices = [round(x * 0.5, 2) for x in range(1, 101)] 

    purchase_df = st.data_editor(
        st.session_state.purchase_df,
        column_config={
            "Item Name": st.column_config.TextColumn(),
            "Category": st.column_config.SelectboxColumn(options=categories),
            "Quantity": st.column_config.NumberColumn(min_value=1, step=1),
            "Price": st.column_config.NumberColumn(min_value=0.0, step=0.5, format="%.2f"),
            "Date of Purchase": st.column_config.DateColumn()
        },
        num_rows="dynamic",
        use_container_width=True,
        key="purchase_editor"
    )

    if st.button("Add Purchases"):
        rows_to_add = []
        for idx, row in purchase_df.iterrows():
            if (
                row["Item Name"] and row["Category"]
                and row["Quantity"] > 0 and row["Price"] > 0
                and pd.notnull(row["Date of Purchase"])
            ):
                add_expense(
                    row["Item Name"],
                    row["Category"],
                    int(row["Quantity"]),
                    float(row["Price"]),
                    row["Date of Purchase"]
                )
                rows_to_add.append(idx)
        st.session_state.purchase_df = purchase_df.drop(rows_to_add).reset_index(drop=True)
        st.success("Purchases added successfully!")

    st.header("Expenses")
    expenses = get_expenses()
    df = pd.DataFrame()  
    if expenses:
        df = pd.DataFrame([{
            "Item Name": e.item_name,
            "Category": e.item_type,  
            "Quantity": e.quantity,
            "Price": e.price,
            "Date of Purchase": e.date_of_purchase
        } for e in expenses])

        df["Price"] = df["Price"].apply(lambda x: f"₹{x:,.2f}")

        edited_df = st.data_editor(
            df,
            column_config={
                "Item Name": st.column_config.TextColumn(),
                "Category": st.column_config.SelectboxColumn(options=categories),
                "Quantity": st.column_config.NumberColumn(min_value=1, step=1),
                "Price": st.column_config.TextColumn(),
                "Date of Purchase": st.column_config.DateColumn()
            },
            num_rows="dynamic",
            use_container_width=True,
            key="expenses_editor"
        )

        if st.button("Save Changes"):
            clear_expenses()  
            for _, row in edited_df.iterrows():
                price_val = float(str(row["Price"]).replace("₹", "").replace(",", ""))
                if (
                    row["Item Name"] and row["Category"]
                    and row["Quantity"] > 0 and price_val > 0
                    and pd.notnull(row["Date of Purchase"])
                ):
                    add_expense(
                        row["Item Name"],
                        row["Category"],
                        int(row["Quantity"]),
                        price_val,
                        row["Date of Purchase"]
                    )
            st.success("Changes saved to the database!")
            df = edited_df.copy()
    else:
        st.write("No expenses found.")

    st.header("Purchase Analysis")
    if not df.empty:
        df_graph = df.copy()
        df_graph["Price"] = df_graph["Price"].apply(lambda x: float(str(x).replace("₹", "").replace(",", "")))
        df_graph["Date of Purchase"] = pd.to_datetime(df_graph["Date of Purchase"])

        st.subheader("Price by Category for Each Date")
        for single_date in sorted(df_graph["Date of Purchase"].dt.date.unique()):
            st.markdown(f"**Date: {single_date}**")
            date_df = df_graph[df_graph["Date of Purchase"].dt.date == single_date]
            chart = alt.Chart(date_df).mark_bar().encode(
                x=alt.X('Category', sort='-y'),
                y=alt.Y('Price', axis=alt.Axis(title='Price (₹)')),
                color='Category'
            ).properties(width=600)
            st.altair_chart(chart, use_container_width=True)

        st.subheader("Total Price per Day (This Month)")
        df_month = df_graph[df_graph["Date of Purchase"].dt.month == date.today().month]
        daily_sum = df_month.groupby(df_month["Date of Purchase"].dt.date)["Price"].sum().reset_index()
        daily_sum.columns = ["Date", "Total Price"]
        chart_all = alt.Chart(daily_sum).mark_bar().encode(
            x=alt.X('Date:T', title="Date"),
            y=alt.Y('Total Price:Q', title="Total Price (₹)"),
            color=alt.value("#5276A7")
        ).properties(width=600)
        st.altair_chart(chart_all, use_container_width=True)
    else:
        st.info("Add some expenses to see the analysis.")

if __name__ == "__main__":
    main()