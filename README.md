Data Storytelling & Hypothesis Testing Project
Project Overview

This project demonstrates how data analysis and statistical testing can support business decision-making. The analysis evaluates whether a new website layout improves the conversion rate compared to the old layout.

The project applies A/B testing and hypothesis testing to validate insights and presents results through a data storytelling approach suitable for business stakeholders.

Objective

The main objectives of this project are:

Perform data analysis on A/B testing data.
Conduct hypothesis testing to evaluate business assumptions.
Interpret p-value and statistical significance.
Build a business narrative using data storytelling.
Present insights using a professional presentation deck.
Business Problem

A company redesigned its website and wants to determine whether the new layout improves user conversion rate.

Key Question

Does the new website layout lead to a statistically significant increase in conversions?

Hypothesis Testing
Null Hypothesis (H₀)

The new website layout does not change the conversion rate.

Alternative Hypothesis (H₁)

The new website layout increases the conversion rate.

Dataset Description

The dataset contains A/B testing information comparing the old website (Group A) and the new website (Group B).

Column	Description
group	Website version (A = Old, B = New)
visitors	Number of users visiting the website
conversions	Number of users who completed a purchase

Example dataset:

group	visitors	conversions
A	1000	120
B	1000	150
Tools and Technologies
Python
Pandas
SciPy
Matplotlib
Jupyter Notebook

These tools are used for data processing, statistical testing, and visualization.

Project Structure
data_story_hypothesis_project/

│
├── data.csv
│   
│
├── data_analysis.py
├── hypothesis_test.py
└── visualization.py│
├── final_presentation.pptx
│
├── hypothesis_summary.md
├── requirements.txt
└── README.md
Methodology
Data Collection
A/B testing dataset containing visitor and conversion data.
Data Analysis
Calculate conversion rates for each group.
Hypothesis Testing
Apply a statistical test to determine significance.
Visualization
Compare conversion rates using charts.
Data Storytelling
Translate insights into a clear business narrative.
Results
Metric	Value
Conversion Rate (Old Layout)	12%
Conversion Rate (New Layout)	15%
Statistical Test	Two-sample T-Test
Significance Level	0.05
Interpretation

The new website layout shows a higher conversion rate compared to the old layout.

Based on the statistical test results, the improvement is considered statistically significant.

Business Recommendation

Based on the analysis:

Deploy the new website layout to all users.
Continue performing A/B testing for further optimization.
Monitor conversion metrics regularly.
How to Run the Project
Install dependencies
pip install -r requirements.txt
Run data analysis
python src/data_analysis.py
Run hypothesis testing
python src/hypothesis_test.py
Generate visualization
python src/visualization.py
Output

The project generates:

Conversion rate comparison
Hypothesis testing results
Visualization charts
Final presentation slides
Presentation

The project includes a stakeholder presentation deck summarizing:

Business problem
Data insights
Statistical validation
Business recommendations
Author

Jagruthi
Specialization Student – AI & Data Analytics
GitHub: https://github.com/jagruthi083
