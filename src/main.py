from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import joblib
from pathlib import Path

app = FastAPI()

# Load the pre-trained model
model_path = Path(__file__).parent / 'iris_model.joblib'
model = joblib.load(model_path)

class IrisModelInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict/")
def predict(input: IrisModelInput):
    try:
        input_data = np.array(
            [[input.sepal_length, input.sepal_width, input.petal_length, input.petal_width]]
        )
        prediction = model.predict(input_data)
        return {"prediction": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
