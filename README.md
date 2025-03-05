# YouTube Video Summarizer API

This API, built with FastAPI, extracts and summarizes key points from YouTube videos using AI. If you don't have time to watch a full video or podcast, simply provide the link, and the API will generate a concise summary.

## Features
- Extracts transcripts from YouTube videos
- Cleans and processes transcript text
- Uses AI to summarize key insights
- Retrieves video details (title, description, duration)

## Tech Stack
- **FastAPI** - Web framework for building APIs
- **YouTube API** - To fetch video data
- **Google Gemini AI** - For AI-powered summarization
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server for running the API

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/youtube-summarizer-api.git
   cd youtube-summarizer-api
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up your YouTube API key in the script:
   ```python
   youtube_api_key = "YOUR_KEY"
   ```

## Usage

### Start the API
Run the server with Uvicorn:
```sh
uvicorn youtube_summarizer:app --host 127.0.0.1 --port 8000 --reload
```

### Endpoints

#### Summarize a YouTube Video
```http
POST /youtube/summarize/
```
**Request Body:**
```json
{
  "youtube_url": "https://www.youtube.com/watch?v=VIDEO_ID"
}
```
**Response:**
```json
{
  "message": "URL received - processing video. Please wait.",
  "Transcript": "Summarized key points from the video."
}
```

#### Get YouTube Video Details
```http
GET /youtube/details/{video_id}
```
**Response:**
```json
{
  "title": "Video Title",
  "description": "Video Description",
  "duration": "PT15M10S"
}
```

## Future Improvements
- Add support for multiple languages
- Deploy the API for public use
- Improve transcript processing for better AI summaries

## Contributing
Feel free to open issues or submit pull requests to improve this project!

## License
This project is open-source and available under the [MIT License](LICENSE).
