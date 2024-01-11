import streamlit as st
import requests
from io import BytesIO

# Define the FastAPI server URL
FASTAPI_SERVER_URL = "https://sheltered-fjord-66150-411d9b03951b.herokuapp.com"

st.title('Bill Summary Interface')

# Set a default value for the bill link
default_bill_link = "https://www.flsenate.gov/Session/Bill/2023/23/ByCategory/?Tab=BillText"

# Get user input for the bill link with a default value
bill_link = st.text_input('Enter the bill link from FLSenate.gov:', value=default_bill_link)

# Language selection
language = st.radio("Select Language", ("English", "Spanish"))

if st.button('Generate Summary'):
    if bill_link:
        # Determine the endpoint based on the selected language
        if language == "English":
            endpoint = "/generate-bill-summary/"
        elif language == "Spanish":
            endpoint = "/generate-bill-summary-spanish/"

        # Send a POST request to the FastAPI server
        response = requests.post(f"{FASTAPI_SERVER_URL}{endpoint}", json={"url": bill_link})
        if response.status_code == 200:
            st.success('Bill summary generated successfully!')
            pdf_file = BytesIO(response.content)
            st.download_button(label="Download PDF", data=pdf_file, file_name=f"bill_summary_{language.lower()}.pdf", mime="application/pdf")
        else:
            st.error(f'Failed to generate summary: {response.text}')
    else:
        st.error('Please enter a valid bill link.')

# 