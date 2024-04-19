from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import joblib
import pandas as pd
from pydantic import BaseModel

# Initialize the FastAPI app
app = FastAPI()

# Mount the static folder to serve HTML files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load the trained models
rf_regressor = joblib.load('random_forest_regressor.pkl')
svr_regressor = joblib.load('support_vector_regressor.pkl')

# Define the input data model
class InputData(BaseModel):
    Weather_Temperature: float
    Weather_Humidity: float
    Weather_Precipitation: float
    Weather_Wind_Speed: float
    Weather_Solar_Radiation: float
    Building_Size: int
    Building_Age: int
    Occupancy_Count: int
    Equipment_Usage_HVAC: int
    Equipment_Usage_Lighting: int
    Equipment_Usage_Machinery: int
    Electricity_Price: float
    Gas_Price: float

# Define the prediction endpoint
@app.post("/predict/")
async def predict_energy_consumption(input_data: InputData):
    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data.dict()])
    
    # Make predictions using the Random Forest Regressor
    rf_prediction = rf_regressor.predict(input_df)
    
    # Make predictions using the Support Vector Regressor
    svr_prediction = svr_regressor.predict(input_df)
    
    # Format the predictions
    predictions = {
        "Random_Forest_Prediction": rf_prediction[0],
        "Support_Vector_Prediction": svr_prediction[0]
    }
    
    return predictions

# Serve the HTML file
@app.get("/", response_class=HTMLResponse)
async def serve_html():
    with open("static/upload.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

# Run the FastAPI server with Unicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

