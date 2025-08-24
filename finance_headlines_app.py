
import streamlit as st
import pandas as pd
import os

DATA_FILE = "group_responses.csv"

if not os.path.exists(DATA_FILE):
    df_init = pd.DataFrame(columns=["Group Name", "Headline", "Group Response", "Values Reflection"])
    df_init.to_csv(DATA_FILE, index=False)

df = pd.read_csv(DATA_FILE)

page = st.sidebar.radio("Navigate", ["Submit Response", "View Responses", "Reset App"])

if page == "Submit Response":
    st.title("Finance in the Headlines - Icebreaker Activity")
    st.write("Welcome to the FIN 325 introductory activity. Select a headline below to explore and discuss.")

    headlines = {
        "Startup Valuations Blast Beyond Historic IPO Market Caps": "Tech startups like OpenAI and SpaceX are reaching valuations over $100 billion, surpassing traditional IPO benchmarks.",
        "Fidelity: RIA Mergers and Acquisitions on Pace for Record 2025": "Registered investment advisory firms are merging at record rates despite macroeconomic uncertainty.",
        "Chevron Acquires Hess Corp in $53 Billion Deal": "Chevron’s acquisition of Hess marks one of the largest energy sector deals of the year.",
        "Record $166 Billion in Stock Buybacks Announced in July": "U.S. companies are repurchasing shares at historic levels, signaling confidence in their valuations.",
        "IPO Market Surges: 204 Public Offerings in 2025, Up 80%": "The IPO market is booming, with high-quality offerings and strong investor demand."
    }

    group_name = st.text_input("Enter your group name:")
    selected_headline = st.selectbox("Choose a headline to analyze:", list(headlines.keys()))
    st.subheader("Headline Summary")
    st.write(headlines[selected_headline])

    st.subheader("Discussion Prompts")
    st.write("""
    - What financial decision is being made?
    - Who are the stakeholders involved?
    - What risks or ethical issues might be present?
    - Which course concepts might help us analyze this situation?
    """)

    group_response = st.text_area("Enter your group's insights and analysis here:")
    reflection = st.text_area("How do integrity and responsible stewardship apply to the financial decision in this headline?")

    if st.button("Submit Responses"):
        new_entry = pd.DataFrame([[group_name, selected_headline, group_response, reflection]],
                                 columns=df.columns)
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_csv(DATA_FILE, index=False)
        st.success("Thank you! Your responses have been saved.")

elif page == "View Responses":
    st.title("Submitted Group Responses")
    if df.empty:
        st.info("No responses submitted yet.")
    else:
        for group in df["Group Name"].unique():
            st.subheader(f"Group: {group}")
            group_data = df[df["Group Name"] == group]
            for _, row in group_data.iterrows():
                st.markdown(f"**Headline:** {row['Headline']}")
                st.markdown(f"**Response:** {row['Group Response']}")
                st.markdown(f"**Reflection:** {row['Values Reflection']}")
                st.markdown("---")

elif page == "Reset App":
    st.title("Reset App")
    if st.button("Delete All Responses"):
        df_empty = pd.DataFrame(columns=df.columns)
        df_empty.to_csv(DATA_FILE, index=False)
        st.success("All responses have been deleted.")
