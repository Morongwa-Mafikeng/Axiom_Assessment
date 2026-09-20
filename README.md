# Axiom_Assessment
Purpose
This fictional assessment is designed to show how you organise data, write Python and SQL, use Git, test your work and explain your decisions. It is not production work and contains no confidential AxioGlobe information. You are not expected to build an API or use C++.
Files Provided
AxioGlobe_Fictional_Product_Data.csv containing fictional construction products and deliberate data quality problems.
This candidate assessment brief.
Your Task
Create a new GitHub repository for the assessment.
Load the supplied CSV using Python. You may use the standard csv module or pandas.
Identify and report missing product IDs, missing product names, duplicate IDs, likely duplicate products, inconsistent category or material naming, invalid dimensions, invalid prices, invalid lead times and inconsistent currencies.
Clean and standardise the records using documented rules. Do not silently delete questionable records; record what you changed, rejected or flagged.
Load the cleaned valid records into SQLite or another SQL database you can run locally.
Write SQL queries that answer the required questions below.
Create a short data quality report and README.
Commit your work progressively and submit the GitHub repository link before the deadline.
Required SQL Questions
How many valid cleaned products remain?
How many products appear in each standardised category?
Which five manufacturers have the most valid products?
Which products have the highest unit price in GBP after excluding invalid or incompatible currency values?
Which products have a lead time above 25 days?
How many records were rejected or flagged for manual review, grouped by reason?
