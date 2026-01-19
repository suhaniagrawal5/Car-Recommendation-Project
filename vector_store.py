import faiss
import numpy as np

def build_faiss_index(car_data):
    # Convert car features into numeric vectors for similarity
    vectors = []
    for car in car_data:
        budget_score = 1  # placeholder, we filter by budget separately
        fuel_score = 1 if car['fuel_type'] else 0
        transmission_score = 1 if car.get('transmission') else 0
        drive_score = 1 if car.get('drive') else 0
        cylinders_score = int(car.get('cylinders', 4))/8  # normalize
        vec = [budget_score, fuel_score, transmission_score, drive_score, cylinders_score]
        vectors.append(vec)

    vectors = np.array(vectors).astype('float32')
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)
    return index, vectors