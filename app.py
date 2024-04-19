# from fastapi import FastAPI, UploadFile, File
# from fastapi.responses import JSONResponse
# from fastapi.responses import HTMLResponse
# from fastai.learner import load_learner
# from PIL import Image
# import torch
# import io
# from torchvision import transforms
# from fastapi.staticfiles import StaticFiles  # Import StaticFiles
# import pathlib
# import uvicorn
# # from fastapi.middleware.cors import CORSMiddleware
# import requests
# app = FastAPI()
# import numpy as np
# import base64
# import joblib

# # Define path to the directory containing static files
# static_dir = "static"

# # Mount the static directory
# app.mount("/static", StaticFiles(directory=static_dir), name="static")

# temp = pathlib.PosixPath
# pathlib.PosixPath = pathlib.WindowsPath

# # Load the model
# model_path = "C:/Users/sharm/OneDrive/Desktop/SustainMe_AI/model/mymodel.pth"
# new_model = torch.load(model_path, map_location=torch.device('cpu'))


# # Define class labels
# class_labels = {0: "metal", 1: "organic", 2: "plastic", 3: "paper", 4:"general"}

# def preprocess_image(image_bytes):
#     image = Image.open(io.BytesIO(image_bytes))
#     preprocess = transforms.Compose([
#         transforms.Resize((224, 224)),
#         transforms.ToTensor(),
#         transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
#     ])
#     input_tensor = preprocess(image)
#     input_batch = input_tensor.unsqueeze(0)  # Add a batch dimension
#     return input_batch

# # def preprocess_image(image_bytes):
# #     image = Image.open(io.BytesIO(image_bytes))
# #     preprocess = transforms.Compose([
# #         transforms.Resize((224, 224)),
# #         transforms.ToTensor(),
# #     ])
# #     input_tensor = preprocess(image)
# #     input_batch = input_tensor.unsqueeze(0)  # Add a batch dimension
# #     return input_batch

# @app.post("/predict/")
# async def predict(file: UploadFile = File(...)):
#     image_bytes = await file.read()
#     input_batch = preprocess_image(image_bytes)

#     # Perform model inference
#     with torch.no_grad():
#         output = new_model.forward(input_batch)

#     # Get the predicted class label
#     _, predicted_class = torch.max(output, 1)
#     predicted_label = class_labels[predicted_class.item()]

#     print("Predicted Label:", predicted_label)
    
#     if predicted_label == 'plastic':
#         return JSONResponse(content={"message": "Plastic"}, status_code=200)
#     elif predicted_label == 'metal':
#         return JSONResponse(content={"message": "Metal"}, status_code=200)
#     elif predicted_label == 'paper':
#         return JSONResponse(content={"message": "Paper"}, status_code=200)
#     elif predicted_label == 'organic':
#         return JSONResponse(content={"message": "Organic"}, status_code=200)
#     elif predicted_label == 'general':
#         return JSONResponse(content={"message": "General"}, status_code=200)
#     else:
#         return JSONResponse(content={"message": "Safe"}, status_code=200)

# # Serve the HTML form
# @app.get("/")
# async def get_upload_form():
#     with open(f"{static_dir}/upload_trash.html", "r") as file:
#         html_content = file.read()
#     return HTMLResponse(content=html_content, status_code=200)


# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=8888)
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse, HTMLResponse
from PIL import Image
import torch
import io
from torchvision import transforms
from fastapi.staticfiles import StaticFiles
import pathlib
import uvicorn

app = FastAPI()

# Define path to the directory containing static files
static_dir = "static"

# Mount the static directory
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Correct path handling for Windows
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# Load the model
model_path = "C:/Users/sharm/OneDrive/Desktop/SustainMe_AI/model/mymodel.pth"
new_model = torch.load(model_path, map_location=torch.device('cpu'))

# Define class labels
class_labels = {0:'general', 1:'metal', 2:'organic', 3:'paper', 4:'plastic'}

def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    input_tensor = preprocess(image)
    input_batch = input_tensor.unsqueeze(0)  # Add a batch dimension
    return input_batch

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    input_batch = preprocess_image(image_bytes)

    # Perform model inference
    with torch.no_grad():
        output = new_model.forward(input_batch)

    # Get the predicted class label
    _, predicted_class = torch.max(output, 1)
    predicted_label = class_labels[predicted_class.item()]

    print("Predicted Label:", predicted_label)
    
    if predicted_label == 'plastic':
        return JSONResponse(content={"message": "Plastic is recyclable please recycle it"}, status_code=200)
    elif predicted_label == 'metal':
        return JSONResponse(content={"message": "Metal is recyclable please recycle it"}, status_code=200)
    elif predicted_label == 'paper':
        return JSONResponse(content={"message": "Paper is recyclable please recycle it"}, status_code=200)
    elif predicted_label == 'organic':
        return JSONResponse(content={"message": "Organic waste is bio-degradable, please use it as a manure"}, status_code=200)
    elif predicted_label == 'general':
        return JSONResponse(content={"message": "General"}, status_code=200)
    else:
        return JSONResponse(content={"message": "Safe"}, status_code=200)

# Serve the HTML form
@app.get("/")
async def get_upload_form():
    with open(f"{static_dir}/upload_trash.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8888)
