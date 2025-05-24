import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("result.csv", index_col=0)

result = load_data()

st.title("Student Result Analysis Dashboard")

# Sidebar menu
menu = st.sidebar.selectbox("Choose a Section", [
    "View Data", "Statistics", "Display Records", "Modify Records", "Modify Columns", "Search Data", "Visualizations", "Analytics"
])

if menu == "View Data":
    st.subheader("All Records")
    st.dataframe(result)

elif menu == "Statistics":
    st.subheader("DataFrame Statistics")
    st.write("Transpose:", result.T)
    st.write("Column Names:", result.columns.tolist())
    st.write("Indexes:", result.index.tolist())
    st.write("Shape:", result.shape)
    st.write("Dimension:", result.ndim)
    st.write("Data Types:", result.dtypes)
    st.write("Size:", result.size)

elif menu == "Display Records":
    st.subheader("Display Specific Records")
    if st.button("Top 5 Records"):
        st.dataframe(result.head())
    if st.button("Bottom 5 Records"):
        st.dataframe(result.tail())
    n = st.number_input("Number of records from top", min_value=1, step=1)
    if n:
        st.dataframe(result.head(int(n)))
    m = st.number_input("Number of records from bottom", min_value=1, step=1)
    if m:
        st.dataframe(result.tail(int(m)))
    subject = st.text_input("Enter subject name for details")
    if subject:
        st.write(result.loc[subject])

elif menu == "Modify Records":
    st.subheader("Modify Subject Records")
    action = st.radio("Choose action", ["Insert", "Update", "Delete"])
    subject = st.text_input("Subject name")
    if subject:
        if action in ["Insert", "Update"]:
            b = st.number_input("Students appeared", step=1)
            c = st.number_input("Highest marks", step=1)
            d = st.number_input("Average marks", step=1)
            e = st.number_input("Number of A1's", step=1)
            f = st.number_input("Number of A2's", step=1)
            g = st.number_input("% of A1 + A2", step=1)
            h = st.number_input("Number of B1's", step=1)
            i = st.number_input("Number of B2's", step=1)
            j = st.number_input("Number of C1's", step=1)
            k = st.number_input("Number of C2's", step=1)
            l = st.number_input("Number of D's", step=1)
            m = st.number_input("Number of E's", step=1)
            data = [b, c, d, e, f, g, h, i, j, k, l, m, 0]
            if st.button("Save Record"):
                result.loc[subject] = data
                st.success(f"Data {'inserted' if action == 'Insert' else 'updated'} for {subject}")
        elif action == "Delete" and st.button("Delete Record"):
            result.drop(subject, inplace=True)
            st.success(f"Data deleted for {subject}")

elif menu == "Modify Columns":
    st.subheader("Modify Columns")
    col_action = st.radio("Action", ["Insert New Column", "Delete Column"])
    if col_action == "Insert New Column":
        new_col = st.text_input("New column name")
        details = st.text_area("Enter values (comma-separated)")
        if st.button("Add Column"):
            try:
                values = list(map(int, details.split(',')))
                result[new_col] = pd.Series(data=values, index=result.index)
                st.success("Column added successfully")
            except:
                st.error("Error processing values")
    elif col_action == "Delete Column":
        col_name = st.selectbox("Select column to delete", result.columns)
        if st.button("Delete Column"):
            result.drop(columns=[col_name], inplace=True)
            st.success(f"Column {col_name} deleted")

elif menu == "Search Data":
    st.subheader("Search")
    option = st.radio("Search by", ["Subject", "Column"])
    if option == "Subject":
        sub = st.text_input("Enter subject")
        if sub:
            st.write(result.loc[sub])
    else:
        col = st.selectbox("Select column", result.columns)
        st.write(result[col])

elif menu == "Visualizations":
    st.subheader("Data Visualizations")
    chart_type = st.selectbox("Select chart type", ["Line", "Bar", "Horizontal Bar", "Histogram"])
    metric = st.selectbox("Select metric", ["highest", "appeared", "average", "per"])
    if chart_type == "Line":
        plt.plot(result.index, result[metric])
    elif chart_type == "Bar":
        plt.bar(result.index, result[metric])
    elif chart_type == "Horizontal Bar":
        plt.barh(result.index, result[metric])
    elif chart_type == "Histogram":
        plt.hist(result[metric], bins=5)
    st.pyplot(plt)

elif menu == "Analytics":
    st.subheader("Analytics")
    st.write("Max Average Marks:", result['average'].max())
    st.write("Min Average Marks:", result['average'].min())
    st.write("Max Highest Marks:", result['highest'].max())
    st.write("Min Highest Marks:", result['highest'].min())
    st.write("Max % of A1 + A2:", result['per'].max())
    st.write("Min % of A1 + A2:", result['per'].min())
