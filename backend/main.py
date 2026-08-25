import serial
import random
import asyncio
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from collections import deque, Counter

app = FastAPI(title="Oscila API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SERIAL_PORT = "COM3"
BAUD_RATE = 115200
VOTING_WINDOW_SIZE = 5

current_mode = "Menginisialisasi..."
latest_prediction = "Menunggu Data"
latest_confidence = 0.0
history = deque(maxlen=VOTING_WINDOW_SIZE)

LABELS = ["Normal", "Baut_Kendor", "Unbalance", "Kritis"]

def get_majority_vote(new_label: str) -> str:
    history.append(new_label)
    vote_counts = Counter(history)
    return vote_counts.most_common(1)[0][0]

async def background_data_acquisition():
    global current_mode, latest_prediction, latest_confidence
    ser = None
    while True:
        try:
            if ser is None or not ser.is_open:
                try:
                    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
                except serial.SerialException:
                    ser = None

            if ser and ser.is_open:
                line = ser.readline().decode('utf-8').strip()
                if line:
                    parts = line.split(',')
                    if len(parts) >= 2:
                        raw_label = parts[0]
                        latest_confidence = float(parts[1])
                        latest_prediction = get_majority_vote(raw_label)
                        current_mode = "Hardware Integrated (Live Data)"
            else:
                raw_label = random.choice(LABELS)
                latest_confidence = round(random.uniform(85.5, 99.9), 2)
                latest_prediction = get_majority_vote(raw_label)
                current_mode = "Mock Data Mode (Hardware Offline)"
            
            await asyncio.sleep(1)
        except Exception:
            ser = None
            current_mode = "Mock Data Mode (Hardware Offline)"
            await asyncio.sleep(1)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(background_data_acquisition())

@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/api/predict")
async def get_prediction():
    return {
        "status": "success",
        "data": {
            "mode": current_mode,
            "prediction": latest_prediction,
            "confidence_score": latest_confidence
        }
    }