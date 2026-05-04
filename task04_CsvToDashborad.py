import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------- PAGE CONFIG --------
st.set_page_config(page_title="Dynamic CSV Dashboard", layout="wide")

st.title("Universal CSV Dashboard")

# -------- FILE UPLOAD --------
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # -------- PREVIEW --------
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # -------- INFO --------
    st.subheader("Dataset Info")
    st.write(df.dtypes)

    # -------- MISSING VALUES --------
    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    # -------- HANDLE NULLS --------
    df = df.copy()

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

    # Fill numeric → median
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    # Fill categorical → Unknown
    for col in categorical_cols:
        df[col] = df[col].fillna('Unknown')

    # -------- SIDEBAR FILTER --------
    st.sidebar.header("Filters")

    if categorical_cols:
        selected_col = st.sidebar.selectbox("Select Category Column", categorical_cols)
        selected_val = st.sidebar.selectbox(
            "Select Value", df[selected_col].unique()
        )
        df = df[df[selected_col] == selected_val]

    # -------- CATEGORICAL PLOT --------
    st.subheader("Categorical Distribution")

    if categorical_cols:
        col = st.selectbox("Choose categorical column", categorical_cols)
        temp_df = df[df[col] != 'Unknown']

        fig, ax = plt.subplots()
        temp_df[col].value_counts().head(10).plot(kind='bar', ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.warning("No categorical columns found.")

    # -------- NUMERIC HISTOGRAM --------
    st.subheader("Numeric Distribution")

    if numeric_cols:
        col = st.selectbox("Choose numeric column", numeric_cols)
        temp_df = df[[col]].dropna()

        fig, ax = plt.subplots()
        sns.histplot(temp_df[col], bins=30, ax=ax)
        st.pyplot(fig)
    else:
        st.warning("No numeric columns found.")

    # -------- SCATTER PLOT --------
    st.subheader("Scatter Plot")

    if len(numeric_cols) >= 2:
        x_col = st.selectbox("X-axis", numeric_cols, key="x")
        y_col = st.selectbox("Y-axis", numeric_cols, key="y")

        temp_df = df[[x_col, y_col]].dropna()
        
        if temp_df.empty:
            st.warning("No data available after filtering.")

        elif x_col == y_col:
            st.warning("X and Y axis must be different columns.")

        elif temp_df[x_col].nunique() <= 1 or temp_df[y_col].nunique() <= 1:
            st.warning("Not enough variation in selected columns.")

        else:
            fig, ax = plt.subplots()
            sns.scatterplot(data=temp_df, x=x_col, y=y_col, ax=ax)
            st.pyplot(fig)

    else:
        st.warning("Need at least 2 numeric columns.")


    # -------- CORRELATION HEATMAP --------
    st.subheader("Correlation Heatmap")

    if len(numeric_cols) >= 2:
        temp_df = df[numeric_cols].dropna()

        fig, ax = plt.subplots()
        sns.heatmap(temp_df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
    else:
        st.warning("Not enough numeric columns.")

else:
    st.info("Upload a CSV file to start.")