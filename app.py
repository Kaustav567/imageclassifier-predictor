from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io
import uvicorn

app = FastAPI()

# Allow CORS (Cross-Origin Resource Sharing) to enable communication between frontend and backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (you can specify your frontend domain)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the static directory to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Route to serve the index.html file
@app.get("/")
async def root():
    return FileResponse("static/index.html")

# Load the model
model = load_model('imgclassifier.keras')

class PredictionResponse(BaseModel):
    predictions: list

@app.post("/predict", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):
    # Read image file
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data))
    
    # Preprocess image
    image = image.resize((32, 32))
    image = np.array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    
    # Make prediction
    predictions = model.predict(image)
    predictions = predictions.tolist()
    
    return {"predictions": predictions}

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

