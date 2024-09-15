import requests
import time

API_KEY = "tLOuKoQzI6JYTR27Y7XEq9yNy8WuKOPO"
BASE_URL = "https://studio-api.suno.ai/api/external"

def generate_song_for_mood(mood):
    url = f"{BASE_URL}/generate/"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "gpt_description_prompt": f"A {mood} song about Uncle Iroh", 
        "tags": mood,  
        "mv": "chirp-v3-5",
        "topic": f"A {mood} song about Uncle Iroh" 
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        response_data = response.json()
        song_id = response_data["id"]
        print(f"Song generation started with ID: {song_id}")
        return song_id
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def fetch_song_url(song_id):
    url = f"{BASE_URL}/clips/?ids={song_id}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    while True:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            clips = response.json()
            clip_data = clips[0]
            if clip_data["status"] == "complete":
                return clip_data["audio_url"]
            else:
                print("Song still generating, checking again...")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
        
        time.sleep(5)

if __name__ == "__main__":
    mood = input("Enter a mood: ").lower()

    print(f"Generating song for mood: {mood}")
    song_id = generate_song_for_mood(mood)
    
    if song_id:
        print(f"Waiting for song generation...")
        song_url = fetch_song_url(song_id)
        
        if song_url:
            print(f"Song generated successfully! Audio URL: {song_url}")
        else:
            print("Failed to fetch the generated song.")
    else:
        print("Failed to generate song.")
