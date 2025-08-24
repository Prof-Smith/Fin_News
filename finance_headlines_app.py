
import streamlit as st

# Define headlines and excerpts
headlines = {
    "Startup Valuations Blast Beyond Historic IPO Market Caps": "Tech startups like OpenAI and SpaceX are reaching valuations over $100 billion, surpassing traditional IPO benchmarks.",
    "Fidelity: RIA Mergers and Acquisitions on Pace for Record 2025": "Registered investment advisory firms are merging at record rates despite macroeconomic uncertainty.",
    "Chevron Acquires Hess Corp in $53 Billion Deal": "Chevron’s acquisition of Hess marks one of the largest energy sector deals of the year.",
    "Record $166 Billion in Stock Buybacks Announced in July": "U.S. companies are repurchasing shares at historic levels, signaling confidence in their valuations.",
    "IPO Market Surges: 204 Public Offerings in 2025, Up 80%": "The IPO market is booming, with high-quality offerings and strong investor demand."
}

# Streamlit app layout
st.title("Finance in the Headlines - Icebreaker Activity")
st.write("Welcome to the FIN 325 introductory activity. Select a headline below to explore and discuss.")

# Headline selection
selected_headline = st.selectbox("Choose a headline to analyze:", list(headlines.keys()))
st.subheader("Headline Summary")
st.write(headlines[selected_headline])

# Discussion prompts
st.subheader("Discussion Prompts")
st.write("""
- What financial decision is being made?
- Who are the stakeholders involved?
- What risks or ethical issues might be present?
- Which course concepts might help us analyze this situation?
""")

# Group response form
st.subheader("Group Response")
group_response = st.text_area("Enter your group's insights and analysis here:")

# Values reflection
st.subheader("Values Reflection")
reflection = st.text_area("How do integrity and responsible stewardship apply to the financial decision in this headline?")

# Submit button
if st.button("Submit Responses"):
    st.success("Thank you! Your responses have been submitted.")
