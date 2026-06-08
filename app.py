import streamlit as st

st.set_page_config(page_title="Mini AI English Tutor", page_icon="📘")

# ---------------- SESSION STATE ----------------
if "level" not in st.session_state:
    st.session_state.level = 1
if "step" not in st.session_state:
    st.session_state.step = "diagnose"
if "score" not in st.session_state:
    st.session_state.score = 0

# ---------------- TITLE ----------------
st.title("📘 Mini AI English & Vocabulary Tutor")
st.write("Improve your English step-by-step with AI guidance.")

# ---------------- DIAGNOSIS ----------------
def diagnose():
    st.subheader("Step 1: Quick Diagnosis")
    q = st.text_input("Write a sentence in English:")

    if st.button("Submit Diagnosis"):
        if len(q.split()) < 5:
            st.warning("Your sentence is very short. Let’s build more detail.")
        else:
            st.success("Good start! We will improve your grammar and vocabulary.")
        st.session_state.step = "lesson"

# ---------------- LESSON ----------------
def lesson():
    st.subheader("Step 2: Simple Explanation")

    st.info("""
    📌 Today’s Topic: Vocabulary Expansion
    
    Instead of saying:
    ❌ “I am happy”
    
    You can say:
    ✅ “I am delighted / joyful / thrilled”
    """)

    if st.button("Next → Question"):
        st.session_state.step = "question"

# ---------------- QUESTION ----------------
def question():
    st.subheader("Step 3: Try This Question")

    st.write("Rewrite this sentence using a better vocabulary:")
    st.code("I am very happy today")

    ans = st.text_input("Your answer:")

    if st.button("Check Answer"):
        if any(word in ans.lower() for word in ["delighted", "thrilled", "joyful"]):
            st.success("Excellent! You used advanced vocabulary 👏")
            st.session_state.score += 1
        else:
            st.warning("Good try 👍 Try using words like: delighted, thrilled, joyful")

        st.session_state.step = "feedback"

# ---------------- FEEDBACK ----------------
def feedback():
    st.subheader("Step 4: Feedback")

    st.write(f"Your Score: {st.session_state.score}")

    if st.session_state.score >= 1:
        st.success("You are improving! Next level unlocked 🚀")
        st.session_state.level += 1
    else:
        st.info("Let’s repeat with easier examples.")

    if st.button("Continue Learning"):
        st.session_state.step = "lesson"

# ---------------- ROUTER ----------------
if st.session_state.step == "diagnose":
    diagnose()
elif st.session_state.step == "lesson":
    lesson()
elif st.session_state.step == "question":
    question()
elif st.session_state.step == "feedback":
    feedback()

# ---------------- SIDEBAR ----------------
st.sidebar.title("🎯 Controls")
st.sidebar.write("Level:", st.session_state.level)

if st.sidebar.button("Reset App"):
    st.session_state.clear()
