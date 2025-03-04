from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from googleapiclient.discovery import build
from backend.helpers import check_youtube_video_exists, clean_transcript, extract_video_id, youtube_transcript_video
from backend.ai_transcript import sumarry_key_points_ai

app = FastAPI()

youtube_api_key = "YOUR_KEY"
youtube = build("youtube", "v3", developerKey=youtube_api_key)


class UserYoutubeUrl(BaseModel):
    youtube_url: str


@app.post("/youtube/summarize/")
async def summarize_youtube_video(youtube_url: UserYoutubeUrl):
    url = youtube_url.youtube_url

    # Extract the video ID
    video_id = extract_video_id(url)
    if not video_id:
        raise HTTPException(
            status_code=400, detail="Incorrect YouTube URL. Please check."
        )

    # Check if the video exists on YouTube
    if not check_youtube_video_exists(video_id):
        raise HTTPException(
            status_code=404, detail="YouTube video not found or unavailable."
        )

    # Get the transcription and clean the text - removing unnecessary characters 
    transcription = youtube_transcript_video(url)
    cleaned_text = clean_transcript(transcription)
    text_summarized_ai = sumarry_key_points_ai(cleaned_text)
    print(text_summarized_ai)

    if not cleaned_text:
        raise HTTPException(
            status_code=404, detail="YouTube video not found or unavailable."
        )
    else:
        return {
            "message": "URL received - processing video. Please wait.",
            "Transcript": text_summarized_ai,
        }


# - GET youtube video details by ID
@app.get("/youtube/details/{video_id}")
async def youtube_video_details_by_id(video_id: str):
    request = youtube.videos().list(part="snippet,ContentDetails", id=video_id)
    response = request.execute()

    print(f"Fetching youtube video details: ", {video_id})

    if response["items"]:
        video_data = response["items"][0]
        title = video_data["snippet"]["title"]
        description = video_data["snippet"]["description"]
        duration = video_data["contentDetails"]["duration"]

        return {"title": title, "description": description, "duration": duration}
    else:
        return None


 

# Start server
if __name__ == "__main__":
    import uvicorn 
    uvicorn.run("youtube-summarizer:app", host="127.0.0.1", port=8000, reload=True)
