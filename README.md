# synent-task4-CSVtoDashboard-sivabarani
Universal CSV Dashboard (Streamlit)

A dynamic and interactive CSV data visualization dashboard built using Streamlit, Pandas, Seaborn, and Matplotlib.

This app allows users to upload any CSV file and instantly explore, analyze, and visualize the dataset without writing code.

Features
File Upload
Upload any CSV file dynamically
Supports real-time data loading
Data Overview
Dataset preview (first 5 rows)
Column data types
Missing values summary
Data Cleaning (Automatic)
Numeric columns → Missing values filled with median
Categorical columns → Missing values filled with "Unknown"
Interactive Filtering
Sidebar filters based on categorical columns
Select specific category values to filter dataset
Visualizations
1. Categorical Distribution
Bar chart of top categories
Automatically removes "Unknown" values
2. Numeric Distribution
Histogram using Seaborn
Adjustable bins (default: 30)
3. Scatter Plot
Compare two numeric features
Handles:
Same column selection
No variation data
Empty filtered data
4. Correlation Heatmap
Displays correlation between numeric features
Annotated heatmap for better insights
Tech Stack
Python
Streamlit
Pandas
Seaborn
Matplotlib
Installation
1. Clone the Repository
git clone https://github.com/your-username/csv-dashboard.git
cd csv-dashboard
2. Install Dependencies
pip install -r requirements.txt

Or install manually:

pip install streamlit pandas seaborn matplotlib
Run the App
streamlit run app.py
Project Structure
csv-dashboard/
│
├── app.py              # Main Streamlit application
├── README.md           # Project documentation
└── requirements.txt    # Dependencies
How It Works
Upload a CSV file
View dataset summary
Apply filters from sidebar
Explore visualizations
Limitations
Only supports CSV files
Large datasets may slow down rendering
No advanced preprocessing (encoding, scaling, etc.)
Future Improvements
Add:
Download filtered dataset
Advanced filtering (range sliders)
Time series analysis
ML model integration
Auto insights (EDA summary)
Use Cases
Quick Exploratory Data Analysis (EDA)
Data Science beginners
Business analytics dashboards
Interview/demo projects
License

This project is open-source and free to use.
