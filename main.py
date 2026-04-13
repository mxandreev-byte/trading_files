from fastapi import FastAPI, Request
import httpx

app = FastAPI()

TELEGRAM_TOKEN = "8689371831:AAEzBzxkCMnSr3uSAul88RLdquooWvocsrA"
CHAT_ID = "181550422"

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    message = data.get("message", "BUY сигнал!")
    
    async with httpx.AsyncClient() as client:
        await client.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            json={"chat_id": CHAT_ID, "text": f"📈 {message}"}
        )
    return {"status": "ok"}

@app.get("/")
async def root():
    return {"status": "running"}
