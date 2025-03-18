import streamlit as st
import base64
from io import BytesIO
from PIL import Image
import pandas as pd
from utils.openai_helper import analyze_plant_disease
from utils.data_helper import (
    get_irrigation_recommendation,
    get_mock_experts,
    SOIL_TYPES,
    CLIMATE_TYPES
)

st.set_page_config(
    page_title="Agro Assis",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 Agro Assis")

# Main navigation
tab1, tab2, tab3 = st.tabs(["Irrigation Advisor", "Disease Detection", "Expert Connect"])

with tab1:
    st.header("Irrigation Recommendation System")

    col1, col2 = st.columns(2)

    with col1:
        soil_type = st.selectbox("Soil Type", SOIL_TYPES)
        temperature = st.slider("Average Temperature (°C)", 0, 50, 25)
        humidity = st.slider("Humidity (%)", 0, 100, 50)
        rainfall = st.number_input("Recent Rainfall (mm)", 0.0, 500.0, 0.0)
        climate_type = st.selectbox("Climate Type", CLIMATE_TYPES)

    if st.button("Get Recommendations"):
        recommendation = get_irrigation_recommendation(
            soil_type, temperature, humidity, rainfall, climate_type
        )

        with col2:
            st.info("Irrigation Recommendations")
            st.write(recommendation["schedule"])
            st.metric("Water requirement (Liters/m²)", recommendation["water_amount"])
            st.write("**Additional Notes:**")
            st.write(recommendation["notes"])

with tab2:
    st.header("Plant Disease Detection")

    uploaded_file = st.file_uploader("Upload a photo of your plant", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Analyze Disease"):
            with st.spinner("Analyzing image..."):
                # Convert image to base64
                buffered = BytesIO()
                image.save(buffered, format="JPEG")
                img_str = base64.b64encode(buffered.getvalue()).decode()

                try:
                    analysis = analyze_plant_disease(img_str)

                    st.subheader("Analysis Results")
                    st.json(analysis)

                    if analysis.get("disease_detected"):
                        st.error(f"Disease Detected: {analysis['disease_name']}")
                        st.write("**Treatment Recommendations:**")
                        for treatment in analysis["treatments"]:
                            st.write(f"- {treatment}")
                    else:
                        st.success("No disease detected! Plant appears healthy.")

                except Exception as e:
                    st.error(f"Error analyzing image: {str(e)}")

with tab3:
    st.header("Connect with Agricultural Experts")

    experts = get_mock_experts()

    # Expert Directory
    st.subheader("Expert Directory")
    for expert in experts:
        with st.expander(f"{expert['name']} - {expert['specialization']}"):
            st.write(f"**Experience:** {expert['experience']} years")
            st.write(f"**Location:** {expert['location']}")
            st.write(f"**Expertise Areas:** {', '.join(expert['expertise'])}")

    # Contact Form
    st.subheader("Contact Form")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        expert_select = st.selectbox(
            "Select Expert",
            [f"{expert['name']} - {expert['specialization']}" for expert in experts]
        )
        message = st.text_area("Your Message")

        if st.form_submit_button("Send Message"):
            st.success("Message sent! The expert will contact you soon.")