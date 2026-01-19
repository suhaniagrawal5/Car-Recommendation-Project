import streamlit as st
from vector_store import build_faiss_index
import numpy as np

st.set_page_config(page_title="Car Recommender (API Only)", layout="centered")
st.title("🚗 Car Recommendation System (API Only)")
st.write("Pure API-based recommendation using FAISS and numeric features")

# User Input
budget = st.slider("Budget (in Lakh ₹)", 5, 30, 12)
fuel = st.selectbox("Fuel Type", ["petrol", "diesel", "electric"])
brand = st.text_input("Preferred Brand", "Toyota")
usage = st.selectbox("Usage", ["City", "Highway", "City + Highway"])

if st.button("Recommend Car"):
    with st.spinner("Fetching & analyzing cars..."):
        # Step 1: Fetch car data from API
        car_data =make=brand,
        car_data1=fuel_type=fuel
        if len(car_data) == 0:
            st.error("No cars found for this brand/fuel combination.")
        else:
            # Step 2: Filter cars by budget
            filtered_cars = []
            for car in car_data:
                if car.get('min_price') and car.get('max_price'):
                    avg_price = (car['min_price'] + car['max_price']) / 2 / 100000  # convert to Lakh
                    if avg_price <= budget:
                        filtered_cars.append(car)
                else:
                    filtered_cars.append(car)  # include if no price info

            if len(filtered_cars) == 0:
                st.error("No cars found under the given budget.")
            else:
                # Step 3: Build FAISS index for similarity
                index, vectors = build_faiss_index(filtered_cars)

                # Step 4: Create user query vector
                fuel_score = 1
                transmission_score = 1
                drive_score = 1
                cylinders_score = 0.5  # default
                user_vec = np.array([[1, fuel_score, transmission_score, drive_score, cylinders_score]]).astype('float32')

                # Step 5: Search top 5 similar cars
                D, I = index.search(user_vec, k=min(5, len(filtered_cars)))
                recommended_cars = [filtered_cars[i] for i in I[0]]

                # Step 6: Display results
                st.success("✅ Recommended Cars:")
                for car in recommended_cars:
                    st.write(f"**{car['make']} {car['model']}** | Fuel: {car['fuel_type']} | Transmission: {car.get('transmission','NA')} | Cylinders: {car.get('cylinders','NA')}")