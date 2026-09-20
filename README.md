# Axiom_Assessment
Purpose
This fictional assessment is designed to show how you organise data, write Python and SQL, use Git, test your work and explain your decisions. It is not production work and contains no confidential AxioGlobe information. You are not expected to build an API or use C++.
Files Provided
AxioGlobe_Fictional_Product_Data.csv containing fictional construction products and deliberate data quality problems.
This candidate assessment brief.
Your Task
1. Create a new GitHub repository for the assessment.
2. Load the supplied CSV using Python. You may use the standard csv module or pandas.
3. Identify and report missing product IDs, missing product names, duplicate IDs, likely duplicate products, inconsistent category or material naming, invalid dimensions, invalid prices, invalid lead times and inconsistent currencies.
4. Clean and standardise the records using documented rules. Do not silently delete questionable records; record what you changed, rejected or flagged.
Load the cleaned valid records into SQLite or another SQL database you can run locally.
5. Write SQL queries that answer the required questions below.
6. Create a short data quality report and README.
7. Commit your work progressively and submit the GitHub repository link before the deadline.
Required SQL Questions
1. How many valid cleaned products remain?
2. How many products appear in each standardised category?
3. Which five manufacturers have the most valid products?
4. Which products have the highest unit price in GBP after excluding invalid or incompatible currency values?
5. Which products have a lead time above 25 days?
6. How many records were rejected or flagged for manual review, grouped by reason?
