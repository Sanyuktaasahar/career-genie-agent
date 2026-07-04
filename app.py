import streamlit as st
import time

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="CareerGenie AI Agent",
    page_icon="🤖",
    layout="centered",
)

# ---------------------------------------------------------
# KNOWLEDGE BASE (this is the "brain" of the agent)
# ---------------------------------------------------------
DOMAIN_KEYWORDS = {
    "Web Development": ["website", "web", "frontend", "backend", "design", "html", "css", "app"],
    "Data Science & Analytics": ["data", "numbers", "statistics", "excel", "analysis", "maths", "math"],
    "Artificial Intelligence / ML": ["ai", "machine learning", "ml", "robot", "automation", "chatbot", "intelligence"],
    "Cybersecurity": ["security", "hacking", "hack", "protect", "cyber", "network safety"],
    "Software Testing / QA": ["testing", "quality", "bug", "debug", "check"],
    "Mobile App Development": ["mobile", "android", "ios", "app development", "flutter"],
}

DOMAIN_ROADMAP = {
    "Web Development": [
        "Master HTML, CSS, and JavaScript fundamentals",
        "Learn a frontend framework (React or Vue)",
        "Learn backend basics with Python (Flask/Django) or Node.js",
        "Understand databases (MySQL/MongoDB)",
        "Build 2–3 real projects and deploy them online",
        "Learn Git & GitHub for version control",
    ],
    "Data Science & Analytics": [
        "Strengthen Python basics (Pandas, NumPy)",
        "Learn statistics and data visualization (Matplotlib/Power BI)",
        "Learn SQL for querying databases",
        "Get comfortable with Excel for quick analysis",
        "Learn basic Machine Learning concepts (Scikit-learn)",
        "Build a portfolio with 2 data projects on real datasets",
    ],
    "Artificial Intelligence / ML": [
        "Build strong Python fundamentals",
        "Learn Machine Learning basics (Scikit-learn)",
        "Understand Neural Networks conceptually",
        "Explore Generative AI tools & prompt engineering",
        "Try building a simple AI agent or chatbot",
        "Stay updated with AI trends (LLMs, Agents, RAG)",
    ],
    "Cybersecurity": [
        "Learn networking basics (TCP/IP, DNS)",
        "Understand common vulnerabilities (OWASP Top 10)",
        "Learn Linux command line",
        "Try beginner platforms like TryHackMe",
        "Learn about firewalls & basic ethical hacking concepts",
        "Get familiar with security tools (Wireshark, Nmap)",
    ],
    "Software Testing / QA": [
        "Learn Software Testing Life Cycle (STLC)",
        "Understand manual testing techniques",
        "Learn to write test cases",
        "Explore automation testing basics (Selenium)",
        "Learn basic SQL for backend testing",
        "Practice with sample projects/bug tracking tools",
    ],
    "Mobile App Development": [
        "Learn programming basics (Java/Kotlin or Dart)",
        "Explore Flutter or React Native for cross-platform apps",
        "Understand mobile UI/UX principles",
        "Learn to connect apps with backend APIs",
        "Build and publish a small app",
        "Learn app deployment basics (Play Store process)",
    ],
}

RESUME_TIPS = {
    "Web Development": "Highlight your projects with live links, mention frameworks used, and show any UI/UX sense.",
    "Data Science & Analytics": "Showcase data projects with visuals/charts, mention tools like Excel, SQL, Python clearly.",
    "Artificial Intelligence / ML": "Mention AI tools you've used, any small AI/agent projects, and your interest in emerging tech.",
    "Cybersecurity": "List any practice platforms used (TryHackMe, etc.) and basic networking/security concepts known.",
    "Software Testing / QA": "Emphasize attention to detail, test case writing ability, and any tool exposure like Selenium.",
    "Mobile App Development": "Show any app you've built, even a small one, with screenshots or a demo link if possible.",
}

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.title("🤖 CareerGenie — AI Career Guidance Agent")
st.caption("An autonomous agent that thinks step-by-step to guide your career path.")
st.divider()

# ---------------------------------------------------------
# SESSION STATE INIT
# ---------------------------------------------------------
if "agent_ran" not in st.session_state:
    st.session_state.agent_ran = False

# ---------------------------------------------------------
# USER INPUT FORM
# ---------------------------------------------------------
with st.form("user_input_form"):
    st.subheader("Tell the agent about yourself")
    name = st.text_input("Your Name", placeholder="e.g. Sanyukta")
    interests = st.text_area(
        "What are your interests / things you enjoy?",
        placeholder="e.g. I like solving problems, working with numbers, exploring new AI tools",
    )
    skills = st.text_area(
        "Any current skills you have? (even basic)",
        placeholder="e.g. Basic Python, HTML, MS Excel",
    )
    submitted = st.form_submit_button("🚀 Run AI Agent")

# ---------------------------------------------------------
# AGENT LOGIC (multi-step reasoning — this is what makes it an "agent")
# ---------------------------------------------------------
def score_domains(text):
    text = text.lower()
    scores = {domain: 0 for domain in DOMAIN_KEYWORDS}
    for domain, keywords in DOMAIN_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                scores[domain] += 1
    return scores

if submitted:
    if not name or not interests:
        st.warning("Please fill at least your name and interests so the agent has something to work with.")
    else:
        st.session_state.agent_ran = True
        combined_text = interests + " " + skills

        # ---- STEP-BY-STEP AGENT REASONING DISPLAY ----
        st.divider()
        st.subheader("🧠 Agent's Thinking Process")

        step_box = st.empty()
        progress = st.progress(0)

        step_box.info("Step 1: Reading and understanding your interests...")
        time.sleep(1)
        progress.progress(20)

        step_box.info("Step 2: Analyzing keywords and mapping to career domains...")
        interest_scores = score_domains(interests)
        time.sleep(1)
        progress.progress(45)

        step_box.info("Step 3: Cross-checking with your current skills...")
        skill_scores = score_domains(skills)
        time.sleep(1)
        progress.progress(65)

        # Combine scores from interests (weighted higher) and skills
        final_scores = {
            domain: interest_scores[domain] * 2 + skill_scores[domain]
            for domain in DOMAIN_KEYWORDS
        }

        step_box.info("Step 4: Ranking best-fit career domains based on combined analysis...")
        time.sleep(1)
        progress.progress(85)

        best_domain = max(final_scores, key=final_scores.get)
        if final_scores[best_domain] == 0:
            best_domain = "Artificial Intelligence / ML"  # sensible trending default

        step_box.info("Step 5: Generating personalized roadmap and resume tips...")
        time.sleep(1)
        progress.progress(100)
        step_box.success("✅ Agent has completed its analysis!")

        # ---- FINAL OUTPUT ----
        st.divider()
        st.subheader(f"👋 Hey {name}, here's what the agent recommends:")

        st.markdown(f"### 🎯 Best-Fit Career Path: **{best_domain}**")

        with st.expander("📍 Why this path? (Agent's reasoning)", expanded=True):
            st.write(
                f"Based on the words and context in your interests and skills, "
                f"the agent found the strongest alignment with **{best_domain}**. "
                f"This decision was made by matching your input against known domain patterns "
                f"and weighing your stated interests more heavily than existing skills, "
                f"since interest often predicts long-term motivation."
            )

        st.markdown("### 🗺️ Personalized Roadmap")
        for i, step in enumerate(DOMAIN_ROADMAP[best_domain], start=1):
            st.checkbox(f"{i}. {step}", key=f"step_{i}")

        st.markdown("### 📄 Resume Tip for this Path")
        st.info(RESUME_TIPS[best_domain])

        st.divider()
        st.caption("Built as a demonstration of a simple, explainable AI Agent — no black-box magic, just transparent step-by-step reasoning.")

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.divider()
st.caption("CareerGenie AI Agent • Built with Python & Streamlit")
