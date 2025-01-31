import pandas as pd
import streamlit as st
from sklearn.preprocessing import MultiLabelBinarizer, MinMaxScaler

# Load and preprocess data
def load_data():
    df = pd.read_csv("cleaned_restaurants.csv")
    
    # Ensure 'cuisines' is a list of cuisines
    df['cuisines'] = df['cuisines'].apply(lambda x: x.strip("[]").replace("'", "").split(', '))
    
    # Encode cuisines using MultiLabelBinarizer
    mlb = MultiLabelBinarizer()
    cuisine_encoded = pd.DataFrame(mlb.fit_transform(df['cuisines']), 
                                 columns=mlb.classes_, 
                                 index=df.index)
    
    # Normalize numerical features
    scaler = MinMaxScaler()
    df['cost_norm'] = scaler.fit_transform(df[['avg_cost']])
    
    # Calculate weighted rating
    C = df['num_ratings'].mean()  # Average number of ratings
    m = df['num_ratings'].quantile(0.5)  # Minimum number of ratings required
    global_avg_rating = df['rating'].mean()
    df['weighted_rating'] = (df['rating'] * df['num_ratings'] + C * global_avg_rating) / (df['num_ratings'] + C)
    
    # Combine all features
    features = pd.concat([
        cuisine_encoded,
        df[['cost_norm', 'weighted_rating', 'online_order', 'table_booking']]
    ], axis=1)
    
    return df, features, mlb, scaler

# Recommendation function
def get_recommendations(df, selected_cuisines, cost_range, selected_area, top_n=5):
    # Step 1: Filter by cuisine
    if selected_cuisines:
        df = df[df['cuisines'].apply(lambda x: any(cuisine in x for cuisine in selected_cuisines))]
    
    # Step 2: Filter by price range
    df = df[(df['avg_cost'] >= cost_range[0]) & (df['avg_cost'] <= cost_range[1])]
    
    # Step 3: Sort by weighted rating
    df = df.sort_values('weighted_rating', ascending=False)
    
    # Step 4: Prioritize by area
    if selected_area != 'Any':
        area_matches = df[df['area'] == selected_area]
        other_areas = df[df['area'] != selected_area]
        df = pd.concat([area_matches, other_areas])
    
    # Return top N recommendations
    return df.head(top_n)

# Streamlit UI
def main():
    st.title("🍴 Restaurant Recommendation System")
    
    # Load data
    df, features, mlb, scaler = load_data()
    
    # Create filters in sidebar
    st.sidebar.header("Filter Preferences")
    
    # Cuisine multi-select
    all_cuisines = sorted(set([cuisine for sublist in df['cuisines'] for cuisine in sublist]))
    selected_cuisines = st.sidebar.multiselect("Preferred Cuisines", all_cuisines)
    
    # Price range slider
    min_cost = df['avg_cost'].min()
    max_cost = df['avg_cost'].max()
    cost_range = st.sidebar.slider("Average Cost for Two (₹)", 
                                 min_cost, max_cost, 
                                 (min_cost, max_cost))
    
    # Area selector
    areas = sorted(df['area'].unique())
    selected_area = st.sidebar.selectbox("Preferred Area", ['Any'] + areas)
    
    # Get recommendations
    if st.sidebar.button("Get Recommendations"):
        recommendations = get_recommendations(df, selected_cuisines, cost_range, selected_area)
        
        st.subheader("Top Recommendations")
        for idx, row in recommendations.iterrows():
            st.markdown(f"""
            **{row['restaurant_name']}**  
            📍 {row['area']} | 💰 {row['avg_cost']}  
            ⭐ {row['rating']} ({row['num_ratings']} ratings)  
            🍴 {', '.join(row['cuisines'])}  
            🖥️ Online Order: {'Yes' if row['online_order'] else 'No'}  
            🪑 Table Booking: {'Yes' if row['table_booking'] else 'No'}
            """)
            st.markdown("---")

if __name__ == "__main__":
    main()