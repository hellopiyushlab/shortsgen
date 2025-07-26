import requests
import os
from dotenv import load_dotenv

load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

url = "https://api.elevenlabs.io/v1/voices"
headers = {
    "Accept": "application/json",
    "xi-api-key": ELEVENLABS_API_KEY,
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
data = response.json()

for voice in data['voices']:
    print(f"{voice['name']}; {voice['voice_id']}")