import pandas as pd

# Load the dataset
df = pd.read_csv("restaurants.csv")

# Step 1: Delete unnecessary columns
# Keep only relevant columns for the recommendation system
columns_to_keep = [
    'restaurant name', 'rate (out of 5)', 'num of ratings', 
    'avg cost (two people)', 'online_order', 'table booking', 
    'cuisines type', 'area'
]
df = df[columns_to_keep]

# Step 2: Remove duplicates
df = df.drop_duplicates()

# Step 3: Remove rows with NaN values
df = df.dropna()

# Step 4: Change column names for consistency
df.columns = [
    'restaurant_name', 'rating', 'num_ratings', 
    'avg_cost', 'online_order', 'table_booking', 
    'cuisines', 'area'
]

# Step 5: Data transformations
# Convert 'online_order' and 'table_booking' to binary (1 for Yes, 0 for No)
df['online_order'] = df['online_order'].map({'Yes': 1, 'No': 0})
df['table_booking'] = df['table_booking'].map({'Yes': 1, 'No': 0})

# Step 6: Data cleaning
# Ensure 'cuisines' is a list of cuisines (split by comma)
df['cuisines'] = df['cuisines'].str.split(', ')

# Save the cleaned dataset to a new CSV file
df.to_csv("cleaned_restaurants.csv", index=False)

print("Dataset cleaned and saved as 'cleaned_restaurants.csv'.")