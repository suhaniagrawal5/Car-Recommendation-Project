import streamlit as st
import numpy as np
from car_data import fetch_car_data, fetch_car_makes
from vector_store import build_faiss_index

st.set_page_config(page_title="Car Recommender", layout="centered")
st.title("🚗 Car Recommendation System")
st.write("FAISS Vector Similarity Search using Local Data")

# Load dynamic available makes from local database
available_makes = fetch_car_makes()

# User Inputs
budget = st.slider("Budget (in Lakh ₹)", 5, 80, 20)
fuel = st.selectbox("Fuel Type", ["gas", "diesel", "electricity"])
brand = st.selectbox("Preferred Brand", available_makes)
usage = st.selectbox("Usage", ["City", "Highway", "City + Highway"])

if st.button("Recommend Car"):
    with st.spinner("Analyzing cars..."):
        # Step 1: Fetch filtered cars from local database
        car_data = fetch_car_data(make=brand, fuel_type=fuel)

        if not car_data:
            st.error("No cars found for this brand/fuel combination.")
        else:
            # Step 2: Filter by budget
            filtered_cars = []
            for car in car_data:
                min_p = car.get('min_price')
                max_p = car.get('max_price')
                
                if min_p and max_p:
                    avg_price = (min_p + max_p) / 2 / 100000  # Convert to Lakhs
                    if avg_price <= budget:
                        filtered_cars.append(car)
                else:
                    filtered_cars.append(car)

            if not filtered_cars:
                st.error("No cars found under the given budget limit.")
            else:
                # Step 3: Build FAISS index
                index, vectors = build_faiss_index(filtered_cars)

                # Step 4: User Query Feature Vector
                fuel_score = 1.0 if fuel == "electricity" else 0.5
                transmission_score = 1.0
                drive_score = 1.0
                cylinders_score = 0.5
                
                user_vec = np.array([[1.0, fuel_score, transmission_score, drive_score, cylinders_score]]).astype('float32')

                # Step 5: Perform similarity search
                k_neighbors = min(5, len(filtered_cars))
                D, I = index.search(user_vec, k=k_neighbors)

                recommended_cars = [
                    filtered_cars[i] 
                    for i in I[0] 
                    if 0 <= i < len(filtered_cars)
                ]

                # Step 6: Display results
                if recommended_cars:
                    st.success("✅ Recommended Cars:")
                    for car in recommended_cars:
                        st.write(
                            f"**{car.get('make')} {car.get('model')}** | "
                            f"Fuel: {car.get('fuel_type').title()} | "
                            f"Transmission: {car.get('transmission').title()} | "
                            f"Cylinders: {car.get('cylinders')}"
                        )
                else:
                    st.warning("No vector recommendations match your criteria.")
