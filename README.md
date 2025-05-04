# LearnSync: AI-Powered Study Planner 📚🧠

LearnSync is a web application built with Streamlit that leverages the power of local Large Language Models (LLMs) via Ollama to generate personalized study plans. It helps users organize their learning by providing weekly topic breakdowns based on subjects, available time, and deadlines, and enhances the learning experience by suggesting relevant YouTube videos for each topic.

## ✨ Features

*   **Personalized Plan Generation:** Creates custom multi-week study schedules based on user input (name, subjects, hours/day, deadlines, duration).
*   **AI-Driven Topics:** Utilizes a local Ollama model (e.g., `deepseek-r1:1.5b`) to suggest relevant topics for each subject within the plan.
*   **Structured Output:** Presents the study plan in a clear, week-by-week format.
*   **Progress Tracking:** Allows users to check off completed topics.
*   **Visual Progress Bar:** Shows the overall completion percentage.
*   **Integrated Learning Resources:** Automatically fetches and suggests relevant YouTube videos for each study topic using the YouTube Data API.
*   **Interactive Web UI:** Built with Streamlit for an easy-to-use interface.

## 🛠️ Technologies Used

*   **Language:** Python 3
*   **Web Framework:** Streamlit
*   **AI/LLM Interaction:** Ollama Python Client (`ollama`)
*   **Local LLM Provider:** Ollama (running locally)
*   **LLM Model:** `deepseek-r1:1.5b` (or other compatible Ollama model)
*   **Web Requests:** `requests` (for YouTube API)
*   **Data Handling:** `json`, `re` (Regular Expressions for parsing AI output)

## ⚙️ Prerequisites

Before running LearnSync, ensure you have the following installed and configured:

1.  **Python:** Version 3.9 or higher recommended.
2.  **Pip:** Python package installer.
3.  **Ollama:** Installed and running locally on your machine. You can download it from [ollama.com](https://ollama.com/).
4.  **Ollama Model:** Download the model specified in the script (or update the script to use a model you have). Run `ollama pull deepseek-r1:1.5b` (or your chosen model) in your terminal. *Note: Smaller models might require less powerful hardware but may yield less detailed plans.*
5.  **YouTube Data API v3 Key:** You need a valid API key from the Google Cloud Console.
    *   Go to [https://console.cloud.google.com/](https://console.cloud.google.com/)
    *   Create a new project (or select an existing one).
    *   Navigate to "APIs & Services" > "Credentials".
    *   Click "Create Credentials" > "API key".
    *   Enable the "YouTube Data API v3" for your project under "APIs & Services" > "Library".
    *   **Important:** Keep your API key secure and consider setting restrictions (e.g., IP address restrictions) in the Google Cloud Console.

## 🚀 Setup & Installation

1.  **Clone the Repository:**
    ```bash
    git clone <your-repository-url> # Or download the script directly
    cd <your-project-directory>
    ```
2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Install Dependencies:** Create a `requirements.txt` file with the following content:
    ```txt
    streamlit
    ollama
    requests
    ```
    Then install them:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure API Key:**
    *   Open the Python script.
    *   Find the line `API_KEY = ""` within the `fetch_youtube_videos` function.
    *   Replace the empty string `""` with your actual YouTube Data API v3 Key.
    *   **(Security Suggestion):** For better security, consider using environment variables or a separate configuration file (`.env`) to store your API key instead of hardcoding it directly in the script. Libraries like `python-dotenv` can help with this.
5.  **Ensure Ollama is Running:** Start the Ollama application or service on your machine. Make sure the model specified in the script (`deepseek-r1:1.5b` or your choice) is available (`ollama list`).

## ▶️ Usage

1.  **Run the Streamlit App:** Open your terminal, navigate to the project directory, and run:
    ```bash
    streamlit run your_script_name.py # Replace with the actual name of your python file
    ```
2.  **Input Details:** The application will open in your web browser. Enter your name, subjects (separated by commas), desired study hours per day, study duration in weeks, and any relevant deadlines (comma-separated).
3.  **Generate Plan:** Click the "Generate Study Plan" button. The app will interact with your local Ollama instance to create the schedule.
4.  **Learn & Track:** Navigate through the weekly plan on the "Start Learning" page.
    *   Check off topics as you complete them using the checkboxes ✅.
    *   Click the YouTube links 📺 provided below each topic for relevant video resources.
    *   Monitor your overall progress with the progress bar at the bottom.
5.  **Return:** Use the "Back to Study Plan" button if you need to regenerate or view the input page again.

## 🌱 Future Enhancements

*   Implement more robust error handling for AI responses and JSON parsing.
*   Use environment variables or a config file for the YouTube API key.
*   Add persistence to save and load study plans and progress (e.g., using local files, databases, or browser storage).
*   Allow users to select different Ollama models.
*   Integrate more diverse learning resources (articles, documentation links).
*   Add features for editing/customizing the generated plan.
*   Implement calendar integration (e.g., export to Google Calendar/ICS).
*   Refine the UI/UX for better navigation and presentation.


