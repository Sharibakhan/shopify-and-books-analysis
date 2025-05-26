# shopify-and-books-analysis
A web scraping project to clone the "Books to Scrape" website using Python and BeautifulSoup.  A data cleaning and analysis project on a messy Shopify customer reviews dataset, including insights extraction using AI tools like ChatGPT.
# Shopify Customer Reviews Data Cleaning and Analysis

## Project Overview

This project involves cleaning and analyzing a raw customer reviews dataset from a Shopify store. The dataset contains thousands of reviews with inconsistent formatting, missing fields, and unstructured content.

## Dataset Details

The raw dataset includes the following columns:

- Review ID  
- Product Name  
- Rating (1–5)  
- Review Content  
- Timestamp  
- Customer Email  
- Product Category  
- Order Value  
- Fulfillment Status  
- Shipping Country  

## Objectives

- Clean the dataset by:  
  - Standardizing timestamps  
  - Fixing inconsistent category and product names  
  - Filtering out blank or invalid reviews  
  - Normalizing missing fields (imputing or flagging)  

- Use AI (ChatGPT or similar) to answer key stakeholder questions:  
  - Which product categories have the most 1-star reviews in Canada?  
  - Do higher order values correlate with lower ratings?  
  - Summarize the top 5 complaints and compliments across all reviews.  
  - Identify fulfillment statuses most associated with negative feedback.

- Build a simple interface/script for non-technical users to input questions and receive AI-powered answers, with optional filters like country, rating range, and product.

## Deliverables

- Cleaned CSV file (before and after cleaning)  
- Prompt templates or code used to extract insights with AI  
- Summary report answering stakeholder questions  
- Interface or script for querying the cleaned data using AI  

## Usage

1. Run the data cleaning script (`shopify_cleaning.py`) to process the raw dataset.  
2. Use the prompt templates to query the cleaned data via AI tools.  
3. Use the interface script (if included) to get answers interactively.  

## Notes

- This project leverages AI tools for natural language understanding and data summarization.  
- The cleaned data and insights help stakeholders make informed decisions on product quality and customer satisfaction.



Feel free to contact me for any questions or feedback.

