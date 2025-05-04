import streamlit as st
import ollama
import json
import re
import requests

# Function to generate the study plan
def generate_study_plan(user, subjects, hours_per_day, deadlines, weeks):
   prompt = f"""
Generate a personalized {weeks}-week study plan for {user} based on the given subjects, available study hours, and deadlines. 
Ensure that each week has unique topics, covering the full {weeks} weeks.

Subjects: {', '.join(subjects)}
Study Hours per Day: {hours_per_day}
Deadlines: {', '.join(deadlines)}

**Important: The output must strictly contain {weeks} weeks, labeled as 'Week 1', 'Week 2', ..., 'Week {weeks}' in JSON format.** 
Example:
{{
    "Week 1": {{"{subjects[0]}": ["Topic1", "Topic2"], "{subjects[1] if len(subjects) > 1 else subjects[0]}": ["Topic3"]}},
    "Week 2": {{"{subjects[0]}": ["Topic4", "Topic5"], "{subjects[1] if len(subjects) > 1 else subjects[0]}": ["Topic6"]}},
    ...
    "Week {weeks}": {{"{subjects[-1]}": ["Final Review"]}}
}}
"""
   try:
        response = ollama.chat(model='deepseek-r1:1.5b', messages=[{"role": "user", "content": prompt}])

        json_match = re.search(r"\{.*\}", response["message"]["content"], re.DOTALL)
        if json_match:
            study_plan = json.loads(json_match.group(0))
        else:
            study_plan = {"error": "Failed to parse AI response. Ensure valid JSON format."}
        
        return study_plan
   except Exception as e:
        return {"error": f"API request failed: {str(e)}"}

# Function to fetch YouTube video suggestions

def fetch_youtube_videos(query):
    API_KEY = "AIzaSyD-XpxtHYbXABlJyTJEMHlpDz8MtJGzapc"  # Replace with your valid API key
    search_query = f"{query}"

    search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={search_query}&type=video&key={API_KEY}&maxResults=3"

    try:
        response = requests.get(search_url).json()

        if "error" in response:
            return f"❌ YouTube API Error: {response['error']['message']}"

        videos = [
            {"title": item["snippet"]["title"], "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}"}
            for item in response.get("items", []) if "videoId" in item["id"]
        ]

        return videos if videos else ["⚠️ No relevant YouTube videos found."]
    
    except Exception as e:
        return [f"⚠️ Failed to fetch YouTube videos: {str(e)}"]
    
    
# Streamlit UI
st.set_page_config(page_title="AI Study Planner", layout="wide")

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "home"
if "study_plan" not in st.session_state:
    st.session_state.study_plan = {}

# Home Page (Study Plan Generation)
if st.session_state.page == "home":
    st.title("📚 AI-Powered Study Planner")
    
    user_name = st.text_input("Enter Your Name")
    subjects_input = st.text_area("Enter Subjects (comma-separated)")
    subjects = [s.strip() for s in subjects_input.split(',') if s.strip()]
    hours_per_day = st.slider("Study Hours Per Day", 1, 10, 3)
    weeks = st.slider("Study Duration (Weeks)", 1, 12, 4)
    deadlines_input = st.text_area("Enter Deadlines (comma-separated YYYY-MM-DD)")
    deadlines = [d.strip() for d in deadlines_input.split(',') if d.strip()]
    
    if st.button("Generate Study Plan"):
        if user_name and subjects and hours_per_day and deadlines:
            study_plan = generate_study_plan(user_name, subjects, hours_per_day, deadlines, weeks)
            st.session_state.study_plan = study_plan
            st.session_state.page = "learning"
            st.rerun()
        else:
            st.warning("⚠️ Please enter all required details!")

# Learning Page (Tracking Progress)
elif st.session_state.page == "learning":
    st.title("📖 Start Learning")

    study_plan = st.session_state.study_plan
    progress = {}

    for week, details in study_plan.items():
        st.subheader(f"📅 {week}")
        for subject, topics in details.items():
            st.markdown(f"**{subject}**")
            for topic in topics:
                is_completed = st.checkbox(f"{topic} ✅", key=f"{week}_{subject}_{topic}")
                progress[f"{week}_{subject}_{topic}"] = is_completed

            # Fetch YouTube Videos
            # Fetch YouTube Videos
                youtube_videos = fetch_youtube_videos(f"{subject}{topic}")
                if isinstance(youtube_videos, list):  # Ensure it's a list
                    for video in youtube_videos:
                        if isinstance(video, dict):  # Ensure it's a dictionary before accessing keys
                            st.markdown(f"📺 [{video['title']}]({video['url']})")
                        else:
                            st.warning(video)  # Show the error message instead of crashing
                else:
                    st.warning(f"⚠️ No YouTube videos found for {subject}.")

            

    # Show progress
    completed = sum(1 for x in progress.values() if x)
    total = len(progress)
    st.progress(completed / total if total > 0 else 0)
    st.write(f"📊 Progress: {completed}/{total} topics completed!")

    # Navigation back to home
    if st.button("🔙 Back to Study Plan"):
        st.session_state.page = "home"
        st.rerun()





