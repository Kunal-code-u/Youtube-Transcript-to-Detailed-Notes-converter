# YouTube Transcript to Detailed Notes Converter

## 📑 Project Overview

This project builds a YouTube video transcriber and summarizer using **Google Gemini Pro**. The application takes a YouTube video link as input, automatically extracts the transcript, and generates a concise summary.

## ✨ Features

- Extracts transcripts from YouTube videos.
- Summarizes the extracted transcript using **Google Gemini Pro**.
- Simple and interactive **Streamlit** web app for easy usage.
- Displays the video thumbnail and the generated summary.
- Robust error handling for invalid or unavailable transcripts.

## 💻 Technologies Used

- **Python 3.10**: Programming language.
- **Streamlit**: For building the web application.
- **youtube_transcript_api**: To fetch transcripts from YouTube videos.
- **google-generativeai**: To generate summaries using Google Gemini Pro.
- **python-dotenv**: To manage API keys securely.

## ⚙️ Setup and Installation

Follow these steps to set up the project in your local environment:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/youtube-transcript-summarizer.git
   cd youtube-transcript-summarizer
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv env
   source env/bin/activate   # On Windows: .\env\Scripts\activate
   ```

3. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the API key:

   - Obtain an API key for **Google Gemini Pro**.
   - Create a `.env` file in the project root:
     ```bash
     touch .env
     ```
   - Add your API key to the `.env` file:
     ```bash
     GEMINI_API_KEY=your_api_key_here
     ```

## 🚀 Running the Application

To start the Streamlit app, run the following command:

```bash
streamlit run app.py
```

Access the app in your browser at **[http://localhost:8501](http://localhost:8501)**.

## 📝 Usage

1. Enter the YouTube video link in the input box.
2. Click the **"Get Detailed Notes"** button.
3. The app will display the video thumbnail and the summarized notes.

## 🗃️ Code Structure

- **app.py**: Main Streamlit application.
- **transcript_extraction.py**: Extracts and formats video transcripts.
- **summarizer.py**: Summarizes transcripts using Gemini Pro.
- **.env**: Stores the API key securely.


## 📝 License

This project is licensed under the MIT License.


