
# part 2 

# data_cleaning_script.py:

import pandas as pd
import numpy as np

# Load raw CSV
df = pd.read_csv("/content/sample_customer_reviews_raw - sample_customer_reviews_raw.csv.csv")

# --- Step 1: Standardize Timestamps ---
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')

# --- Step 2: Fix inconsistent category/product names ---
df['Product Name'] = df['Product Name'].str.title().str.strip()
df['Product Category'] = df['Product Category'].str.lower().str.strip()

# --- Step 3: Filter out blank/invalid reviews ---
df['Review Content'] = df['Review Content'].astype(str).str.strip()
df = df[df['Review Content'].str.split().str.len() >= 3]  # keep reviews with at least 3 words

# --- Step 4: Handle missing Ratings ---
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
avg_rating = df['Rating'].mean()
df['Rating'] = df['Rating'].fillna(round(avg_rating, 1))

# --- Step 5: Normalize missing Order Values ---
df['Order Value'] = pd.to_numeric(df['Order Value'], errors='coerce')
mean_order_value = df['Order Value'].mean()
df['Order Value'] = df['Order Value'].fillna(mean_order_value)

# --- Step 6: Drop rows with critical missing data ---
df = df.dropna(subset=['Product Name', 'Customer Email', 'Shipping Country'])

# Save the cleaned dataset
df.to_csv("shopify_reviews_cleaned.csv", index=False)
print("✅ Cleaned data saved as 'shopify_reviews_cleaned.csv'")

# Answer Stakeholder Questions

# Q1. "Which product categories have the most 1-star reviews in Canada?"

canada_1_star = df[(df['Shipping Country'].str.lower() == 'canada') & (df['Rating'] == 1)]
top_1_star_categories = canada_1_star['Product Category'].value_counts().head(5)
print(top_1_star_categories)

#Q2. "Do higher order values correlate with lower ratings?

correlation = df[['Order Value', 'Rating']].corr()
print("Correlation between Order Value and Rating:")
print(correlation)


# Q3. "Top 5 complaints and compliments"

from sklearn.feature_extraction.text import CountVectorizer

# Complaints (1-star & 2-star reviews)
complaints = df[df['Rating'] <= 2]['Review Content']
vectorizer = CountVectorizer(stop_words='english', max_features=50)
X = vectorizer.fit_transform(complaints)
complaint_words = vectorizer.get_feature_names_out()

# Compliments (4-star & 5-star reviews)
compliments = df[df['Rating'] >= 4]['Review Content']
vectorizer2 = CountVectorizer(stop_words='english', max_features=50)
Y = vectorizer2.fit_transform(compliments)
compliment_words = vectorizer2.get_feature_names_out()

print("Top 5 complaint keywords:", complaint_words[:5])
print("Top 5 compliment keywords:", compliment_words[:5])


# Q4. "Which fulfillment statuses are associated with negative feedback?"

neg_reviews = df[df['Rating'] <= 2]
status_counts = neg_reviews['Fulfillment Status'].value_counts()
print(status_counts)


