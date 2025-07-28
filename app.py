import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.set_page_config(page_title="ThreatGuard", layout="centered" , page_icon="🛡️")
st.title("🛡️ ThreatGuard")

st.header("📄 Malicious File Detection")
uploaded_file = st.file_uploader("Upload a file (PDF/TXT only):", type=["pdf", "txt"])
if uploaded_file is not None:
    with st.spinner("Analyzing file..."):
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        response = requests.post(f"{API_URL}/scam/", files=files)
        if response.ok:
            st.success(response.json().get("message"))
        else:
            st.error("Error analyzing file.")

st.header("🔗 URL Threat Detection")
url = st.text_input("Enter URL (include http:// or https://):")
if st.button("Classify URL"):
    if url:
        with st.spinner("Classifying URL..."):
            response = requests.post(f"{API_URL}/predict", json={"url": url})
            if response.ok:
                data = response.json()
                if "predicted_class" in data:
                    st.markdown(f"**URL:** {data['input_url']}")
                    st.markdown(f"**Predicted Class:** :blue[{data['predicted_class']}]")
                else:
                    st.warning(data.get("message", "Unknown error."))
            else:
                st.error("Error classifying URL.")
    else:
        st.warning("Please enter a URL.")