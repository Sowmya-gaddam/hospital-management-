import streamlit as st


# ---------------- AI SYMPTOM CHECKER ----------------
def symptom_checker_page():

    st.title("🤖 AI Symptom Checker")

    st.write(
        "Enter symptoms separated by commas."
    )

    symptoms = st.text_area(
        "Enter Symptoms Here"
    )

    if st.button("Analyze Symptoms"):

        symptoms = symptoms.lower()

        # -------- RULE-BASED AI --------
        if "fever" in symptoms and "cough" in symptoms:

            disease = "Possible Viral Infection"
            department = "General Medicine"
            severity = "Medium"

        elif "chest pain" in symptoms:

            disease = "Possible Heart Problem"
            department = "Cardiology"
            severity = "High"

        elif "headache" in symptoms:

            disease = "Migraine or Stress"
            department = "Neurology"
            severity = "Low"

        elif "stomach pain" in symptoms:

            disease = "Gastric Issue"
            department = "Gastroenterology"
            severity = "Medium"

        else:

            disease = "Consult Doctor"
            department = "General Medicine"
            severity = "Unknown"

        st.success("Analysis Completed")

        st.subheader("🩺 Prediction Result")

        st.write(f"Possible Condition: {disease}")

        st.write(f"Recommended Department: {department}")

        st.write(f"Severity Level: {severity}")