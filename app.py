import streamlit as st
import webbrowser
import requests
from io import BytesIO
from PIL import Image

# Define the FastAPI server URL
FASTAPI_SERVER_URL = "http://54.242.92.10:8080/generate-bill-summary/"

# Display banner image
banner = Image.open('banner.jpeg')
# bill_list = Image.open('Website.jpg')
st.image(banner, use_column_width=True)

# App title and description
st.title('Bill Summary Interface')
st.write("""
    This application allows you to enter the URL of a bill from the Florida Senate website (FLSenate.gov). 
    Choose the language in which you'd like to generate a summary for the bill, and it will output a downloadable PDF. 

    Visit this link to look through the bills, and you can select which bill you would like a summary generated for, then copy and paste that URL to the application. 

""")

# st.image(bill_list, use_column_width=True)

#if st.button('FLSenate.Gov Bill List'):
#    webbrowser.open_new_tab("https://www.flsenate.gov/Session/Bills/2023")

# Create a button-like structure with a clickable hyperlink
st.markdown('[FLSenate.Gov Bill List](https://www.flsenate.gov/Session/Bills/2023)')


# Set a default value for the bill link
default_bill_link = "https://www.flsenate.gov/Session/Bill/2023/23/ByCategory/?Tab=BillText"

# Add a horizontal line
# st.markdown("<hr>", unsafe_allow_html=True)

# Get user input for the bill link with a default value
bill_link = st.text_input('Enter the bill link from FLSenate.gov:', value=default_bill_link)

# User inputs
language = st.selectbox("Select Language", options=["en", "es"])

# Button to generate summary
if st.button('Generate Summary'):
    if bill_link:
        payload = {
            "url": bill_link,
            "lan": language
        }
        headers = {'Content-Type': 'application/json'}
        
        # Send the request to the FastAPI server
        response = requests.post(FASTAPI_SERVER_URL, json=payload, headers=headers)
        
        if response.status_code == 200:
            st.success('Bill summary generated successfully!')
            pdf_file = BytesIO(response.content)
            st.download_button(label="Download PDF", data=pdf_file, file_name="bill_summary.pdf", mime="application/pdf")
        else:
            st.error(f'Failed to generate summary: {response.text}')
    else:
        st.error('Please enter a valid bill URL.')

# Add a horizontal line
# st.markdown("<hr>", unsafe_allow_html=True)

# Add a heading 2
st.title('GitHub Repo for FastAPI & Streamit')
st.write("Created by Alex Sciuto - AI Engineering Intern @ DDP")

#if st.button('FastAPI Repo'):
#    webbrowser.open_new_tab("https://github.com/DataWithAlex/Digital_Democracy_API")

st.markdown('[FastAPI Repo](https://github.com/DataWithAlex/Digital_Democracy_API)')
st.markdown('[Streamlit App Repo](https://github.com/DataWithAlex/DDP-Bill-Webform)')

#if st.button('Streamlit App Repo'):
#    webbrowser.open_new_tab("https://github.com/DataWithAlex/DDP-Bill-Webform")



# 