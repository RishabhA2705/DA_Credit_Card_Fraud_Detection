---- Credit Card Fraud Detection – Project Report
1. Objective

The aim of this project is to detect fraudulent credit card transactions by combining data analysis (pandas, SQL, Excel) and machine learning.
The project also includes reporting dashboards (Excel, Power BI) for clear business insights.

2. Dataset

Source: Credit Card Transactions Dataset (highly imbalanced).

Features:

Time – transaction time (in seconds)

Amount – transaction amount

Class – target (0 = Legit, 1 = Fraud)

3. Tools & Technologies

Python (pandas, numpy, matplotlib, seaborn, scikit-learn, xgboost, lightgbm)

SQL (MySQL) – for querying transaction patterns

Excel – pivot tables & trend analysis

Power BI – interactive dashboard for visualization

4. Data Analysis using Pandas

Loaded dataset into pandas for exploration.

Checked for missing values (none found).

Performed feature scaling with StandardScaler.

Split dataset into train/test sets (80/20).

----> Key Pandas Findings:

Fraudulent transactions are <1% of the dataset.

Fraud cases usually involve smaller amounts.

Fraud transactions are not evenly distributed across time.

5. SQL Analysis

Queries written in queries.sql and executed with Python (export_to_excel.py).

----> Example Queries:

Total number of transactions

Fraud vs Legit transaction counts

Fraud percentage

Average transaction amount by class

Top 10 largest frauds

Fraud distribution by hour of day

Results exported to Excel workbook (fraud_analysis.xlsx) for easy review.

6. Excel Analysis

Imported SQL query results into Excel.

Created pivot tables to analyze fraud patterns.

Added charts (fraud vs legit, hourly distribution, fraud percentage).

Used Excel as a business-friendly reporting tool.

7. Power BI Dashboard

Built an interactive dashboard with:

Fraud vs Legit bar chart

Fraud percentage KPI card

Top 10 fraud transactions (by amount)

Fraud distribution by time of day

This helped visualize hidden patterns in the data.

8. Machine Learning Models

Several ML algorithms were trained and evaluated:

Logistic Regression – baseline model.

Decision Tree – interpretable, simple model.

Random Forest – improved recall & precision.

KNN – distance-based, but slower on large datasets.

XGBoost – boosting model, strong performance.

LightGBM – very efficient gradient boosting.

9. Model Evaluation

Metrics used:

Accuracy – overall correctness.

Precision – how many predicted frauds were correct.

Recall – how many actual frauds were detected.

F1-score – balance between precision & recall.

----> Results:

Random Forest, XGBoost, and LightGBM performed the best.

Recall was prioritized (better to catch frauds than miss them).

Logistic Regression and KNN had weaker recall.

Model comparison exported to Excel (model_comparison.xlsx).

10. Insights & Conclusion

Fraud detection is a class imbalance problem. Accuracy alone is misleading.

Fraud transactions are rare but show distinct time & amount patterns.

Ensemble models (Random Forest, XGBoost, LightGBM) are most effective.

SQL + Excel + Power BI allowed business-side reporting.

ML pipeline is ready for real-time fraud detection deployment.

11. Deliverables

Python notebooks (EDA + ML)

SQL queries (queries.sql)

Excel dashboards (fraud_analysis.xlsx, model_comparison.xlsx)

Power BI Dashboard (fraud_dashboard.pbix)