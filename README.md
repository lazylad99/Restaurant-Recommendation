
# Restaurant Recommendation System 🍴

This project is a **Restaurant Recommendation System** that helps users find restaurants based on their preferences, such as cuisine, price range, and location. It uses a **content-based filtering approach** to recommend restaurants that match the user's criteria.

---

## Features ✨

- **Cuisine Filter**: Recommend restaurants based on the user's preferred cuisines.
- **Price Range Filter**: Filter restaurants within the user's specified price range.
- **Weighted Rating**: Prioritize restaurants with high ratings and a significant number of reviews.
- **Area Prioritization**: Show restaurants in the user's preferred area first. If none are available, recommend restaurants from other areas.
- **User-Friendly Interface**: Built with **Streamlit**, the app provides an intuitive and interactive interface.

---

## How It Works 🛠️

1. **Preprocessing**:
   - The dataset is cleaned by removing unnecessary columns, duplicates, and missing values.
   - Categorical variables (e.g., cuisines) are encoded using `MultiLabelBinarizer`.
   - Numerical features (e.g., price, rating) are normalized using `MinMaxScaler`.

2. **Recommendation Logic**:
   - **Step 1**: Filter restaurants by the user's selected cuisines.
   - **Step 2**: Filter restaurants within the user's specified price range.
   - **Step 3**: Sort restaurants by a **weighted rating** (balancing average rating and number of ratings).
   - **Step 4**: Prioritize restaurants in the user's preferred area. If none are available, recommend restaurants from other areas.

3. **Streamlit UI**:
   - Users can select their preferences (cuisine, price range, area) using interactive widgets.
   - The app displays the top recommendations with key details (name, area, price, rating, cuisines, etc.).

---

## Installation 🚀

### Prerequisites
- Python 3.8 or higher
- Streamlit
- Pandas
- Scikit-learn

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/lazylad99/restaurant-recommendation-system.git
   cd restaurant-recommendation-system
   ```

2. Install the required packages:
   ```bash
   pip install streamlit pandas scikit-learn
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run recommend.py
   ```

4. Open the app in your browser:
   ```
   Local URL: http://localhost:8501
   ```

---

## Dataset 📊

The dataset used in this project contains the following columns:
- `restaurant_name`: Name of the restaurant.
- `rating`: Average rating (out of 5).
- `num_ratings`: Number of ratings.
- `avg_cost`: Average cost for two people.
- `online_order`: Whether online ordering is available (`Yes`/`No`).
- `table_booking`: Whether table booking is available (`Yes`/`No`).
- `cuisines`: List of cuisines served by the restaurant.
- `area`: Area where the restaurant is located.

---

## Usage 🖥️

1. **Select Cuisines**:
   - Choose one or more cuisines from the multi-select dropdown.

2. **Set Price Range**:
   - Use the slider to specify your preferred price range.

3. **Choose Area**:
   - Select a preferred area from the dropdown. Choose `Any` if you have no preference.

4. **Get Recommendations**:
   - Click the **Get Recommendations** button to see the top restaurants matching your preferences.

---

## Example Output 🖼️

### Input:
- Cuisines: `Italian`, `Chinese`
- Price Range: ₹300–₹600
- Area: `Bellandur`

### Output:
```
**Ristorante Italiano**  
📍 Bellandur | 💰 ₹550  
⭐ 4.2 (120 ratings)  
🍴 Italian, Chinese  
🖥️ Online Order: Yes  
🪑 Table Booking: No
```

---

## Customization 🛠️

- **Dataset**: Replace `cleaned_restaurants.csv` with your own dataset. Ensure it has the required columns.
- **Weighted Rating Formula**: Adjust the formula in the `load_data` function to change how ratings are weighted.
- **Filters**: Add more filters (e.g., dietary restrictions, delivery time) by modifying the `get_recommendations` function.

---

## Contributing 🤝

Contributions are welcome! If you'd like to improve this project, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

---

## License 📄

This project is licensed under the MIT License. See the [LICENSE]

---

## Acknowledgments 🙏

- Built with ❤️ using **Streamlit**, **Pandas**, and **Scikit-learn**.
- Inspired by content-based recommendation systems.

---

Enjoy exploring restaurants! 🍽️

---
   git commit -m "Add README file"
   git push origin main
   ```
