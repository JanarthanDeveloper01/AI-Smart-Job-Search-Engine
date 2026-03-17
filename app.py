import streamlit as st
from utils.helper import detect_domain_roles
from resume_parser import extract_text_from_resume
from ai_role_extractor import extract_resume_insights
from job_search import search_jobs
from job_matcher import calculate_match_score


st.set_page_config(page_title="AI Job Search Engine", page_icon="💼")

st.title("💼 AI Smart Job Search Engine")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])


if uploaded_file is not None:

    st.success("Resume Uploaded Successfully!")

    # STEP 1: Extract text
    resume_text = extract_text_from_resume(uploaded_file)

    st.subheader("📄 Extracted Resume Text")
    st.write(resume_text)

    # STEP 2: Analyze button
    if st.button("Analyze Resume"):

        # 🔹 Step 3: AI Role Detection
        roles = extract_resume_insights(resume_text)

        # 🔥 Step 4: Fallback Logic (VERY IMPORTANT)
        if not roles or any(r.lower() in ["data scientist", "data analyst"] for r in roles):
            roles = detect_domain_roles(resume_text)

        # Remove duplicates (clean output)
        roles = list(set(roles))

        st.subheader("🎯 Final Suggested Roles")

        for r in roles:
            st.write("-", r)

        # 🔹 Step 5: Job Recommendation
        st.subheader("🔎 Recommended Jobs")

        for role in roles:

            st.write(f"## Jobs for: {role}")

            jobs = search_jobs(role)

            for job in jobs:

                job_description = job["title"] + " " + job["company"]

                score = calculate_match_score(resume_text, job_description)

                st.write("###", job["title"])
                st.write("🏢 Platform:", job["company"])
                st.write("📍 Location:", job["location"])
                st.write("📊 Match Score:", score, "%")
                st.write("🔗 Apply Here:", job["link"])
                st.write("---")