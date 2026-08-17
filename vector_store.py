import faiss
import numpy as np

def build_faiss_index(car_data):
    """Convert car features into numeric vectors and construct a FAISS index."""
    vectors = []
    for car in car_data:
        budget_score = 1.0
        fuel_score = 1.0 if car.get('fuel_type') else 0.0
        transmission_score = 1.0 if car.get('transmission') == 'automatic' else 0.5
        drive_score = 1.0 if car.get('drive') == '4wd' else 0.5
        
        # Safely convert cylinders to handle EV (0) or missing inputs
        raw_cylinders = car.get('cylinders')
        cylinders = int(raw_cylinders) if raw_cylinders is not None else 4
        cylinders_score = cylinders / 8.0
        
        vec = [budget_score, fuel_score, transmission_score, drive_score, cylinders_score]
        vectors.append(vec)

    vectors = np.array(vectors).astype('float32')
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)
    return index, vectors
