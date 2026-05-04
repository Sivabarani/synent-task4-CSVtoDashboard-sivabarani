# synent-task4-CSVtoDashboard-sivabarani

# Universal CSV Dashboard

An interactive data visualization dashboard built using Streamlit.  
This application allows users to upload any CSV file and perform quick exploratory data analysis (EDA) with dynamic visualizations.

---

## Features

- Upload any CSV file
- View dataset preview (first 5 rows)
- Display column data types
- Show missing values summary
- Automatic missing value handling:
  - Numeric columns filled with median
  - Categorical columns filled with "Unknown"
- Sidebar filtering based on categorical columns
- Data visualizations:
  - Categorical distribution (bar chart)
  - Numeric distribution (histogram)
  - Scatter plot for numeric relationships
  - Correlation heatmap

---

## Tech Stack

- Python
- Streamlit
- Pandas
- Seaborn
- Matplotlib

---

## Installation

Clone the repository:

git clone https://github.com/your-username/universal-csv-dashboard.git
cd universal-csv-dashboard

### Install dependencies:

pip install -r requirements.txt

Or install manually:

pip install streamlit pandas seaborn matplotlib

### Usage

#### Run the application:

streamlit run app.py

### Steps to use:

Upload a CSV file
View dataset information
Apply filters from the sidebar
Explore visualizations

### Project Structure
universal-csv-dashboard/
│
├── app.py
├── README.md
└── requirements.txt

### Data Handling
Numeric columns: Missing values are filled with median
Categorical columns: Missing values are filled with "Unknown"
### Limitations
Supports only CSV files
Performance may degrade with very large datasets
No advanced preprocessing (encoding, scaling, etc.)
Future Improvements
Download filtered dataset
Advanced filtering (range sliders)
Time-series analysis
Machine learning integration
Automated EDA reports

### Use Cases
Quick exploratory data analysis (EDA)
Data science learning projects
Business data exploration
Portfolio or demo projects

---
