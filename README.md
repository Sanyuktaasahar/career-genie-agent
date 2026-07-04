# 🤖 CareerGenie — AI Career Guidance Agent

A simple, explainable AI Agent built with Python and Streamlit.
It takes a user's interests and skills, reasons through them step-by-step
(like a real agent), and gives a personalized career path + roadmap + resume tip.

## Why this counts as an "AI Agent"

Unlike a plain chatbot that just answers one question, this app:
1. Takes a **goal** (find the best career path)
2. Breaks it into **multiple reasoning steps** (analyze interests → analyze skills → cross-check → decide → generate output)
3. Shows its **thinking process** transparently
4. Produces a **complete actionable result** (roadmap + tips), not just one line of text

That step-by-step, goal-driven behavior is exactly what defines an "agent" —
it doesn't have to use a paid AI API to qualify.

## How to run it locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

It will open in your browser at `http://localhost:8501`

## How to deploy it for FREE (so anyone can use it) — Streamlit Community Cloud

1. Create a free GitHub account (if you don't have one): https://github.com
2. Create a new **public** repository, e.g. `career-genie-agent`
3. Upload these 2 files to the repo:
   - `app.py`
   - `requirements.txt`
4. Go to https://share.streamlit.io and sign in with your GitHub account
5. Click **"New app"**
6. Select your repository, branch (`main`), and set the main file as `app.py`
7. Click **Deploy**
8. In 1-2 minutes, you'll get a public link like:
   `https://your-app-name.streamlit.app`
9. Share that link with anyone — it works in any browser, no installation needed!

## Optional Next Steps (to make it even more impressive)

- Add a free Google Gemini API key to make the reasoning step actually
  call a real LLM instead of keyword matching (upgrade path, not required)
- Add more career domains to `DOMAIN_KEYWORDS`
- Add a simple logo/banner using `st.image()`
