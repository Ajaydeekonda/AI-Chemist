# AI Chemist App

This Streamlit app uses Google Gemini AI to identify pharmaceutical tablets from uploaded images and provides detailed information on their uses, functionalities, and key characteristics. Users can upload an image of tablets and receive AI-powered insights.

## Features

- Upload images of pharmaceutical tablets.
- Analyze and identify tablets using Google Gemini API.
- Get detailed information on the purpose, uses, and distinguishing features of the tablets.
- Simple and interactive user interface built with Streamlit.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or above
- [Google Gemini API Key](https://developers.generativeai.com/) (You'll need to sign up and get the API key)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/ai-chemist-app.git
   cd ai-chemist-app
   ```
2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate    # For MacOS/Linux
    .\venv\Scripts\activate     # For Windows
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt

    ```

4.  **Set up your environment variables:**
    
    Create a .env file in the root directory and add your Google Gemini API key:

    ```bash
    GOOGLE_API_KEY=your-google-api-key-here
    ```

## Usage

1. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

2. Upload an image of pharmaceutical tablets and provide an input prompt for AI analysis. The app will display the identified tablets along with detailed information.

## Deployment

1. Push the code to a GitHub repository.

2. Create a new Web Service in Render, connecting it to your GitHub repo.

3. Set the environment variable `GOOGLE_API_KEY` in the Render dashboard.

4. Configure the start command as:
   ```bash
   streamlit run app.py
