from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from bson import ObjectId
import os
import gridfs
from dotenv import load_dotenv

load_dotenv()

MONGO_STR=os.getenv("MONGO_STR")

app = FastAPI()

# MongoDB कनेक्शन
MONGO_URL = "mongodb+srv://dashu:Dashrath%4014@jaipur.fy4hf.mongodb.net/?retryWrites=true&w=majority&appName=jaipur&authSource=admin"
client = MongoClient(MONGO_STR)
db = client["telegram_db"]
collection = db["ImageWithCaption"]
fs = gridfs.GridFS(db)

# HTML टेम्प्लेट्स लोड करना
templates = Jinja2Templates(directory="templates")

# 📂 इमेज स्टोरेज फोल्डर
IMAGE_FOLDER = "images"
os.makedirs(IMAGE_FOLDER, exist_ok=True)


# 🔹 MongoDB से डेटा और इमेज URL लाना
@app.get("/fetch-data/")
def fetch_data():
    data = list(collection.find({}, {"_id": 0}))

    for item in data:
        if "image_id" in item:
            item["image_url"] = f"http://127.0.0.1:8000/get-image/{item['image_id']}"
    
    return data


# 🔹 MongoDB से इमेज फेच करके सर्व करना
@app.get("/get-image/{image_id}")
def get_image(image_id: str):
    image_path = os.path.join(IMAGE_FOLDER, f"{image_id}.jpg")

    # अगर इमेज पहले से सेव नहीं है, तो MongoDB से डाउनलोड करो
    if not os.path.exists(image_path):
        try:
            image_data = fs.get(ObjectId(image_id))
            with open(image_path, "wb") as f:
                f.write(image_data.read())
        except:
            raise HTTPException(status_code=404, detail="Image not found in database")

    return FileResponse(image_path, media_type="image/jpeg")


# 🔹 Web Browser में इमेज और डेटा दिखाने के लिए HTML टेम्प्लेट
@app.get("/")
def show_images(request: Request):
    data = list(collection.find({}, {"_id": 0}))

    for item in data:
        if "image_id" in item:
            item["image_url"] = f"http://127.0.0.1:8000/get-image/{item['image_id']}"

    return templates.TemplateResponse("index.html", {"request": request, "data": data})
