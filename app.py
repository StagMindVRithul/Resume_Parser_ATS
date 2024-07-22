from dotenv import load_dotenv

load_dotenv()

import streamlit as st 
import os 
from PIL import Image
import pdf2image
import google.generativeai as genai
import io
import base64

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_content,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert the PDF to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No File Uploaded")
    
def extract_resume_details(input_text, pdf_content,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_text, pdf_content[0],prompt])
    return response.text
    
## Streamlit App

st.set_page_config(page_title="Resume_Parser_and_ATS")
st.header("Resume Parser and ATS")
input_text = st.text_area("Job Description: ",key="input")
uploaded_file = st.file_uploader("Upload Your Resume(PDF)...",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Tell me about the Resume!")
submit2 = st.button("Percentage Match!")
submit3 = st.button("Extract Resume Details")

input_prompt1 = """
You are an experienced HR with Tech Experience in the field of Data Science, Full stack Web development, Big Data Engineering, DEVOPS, Data Analyst,
your taks is to review the provided resume against the job description for this profiles.
Please share your professional evaluation on whether the candidate's profile aligns with the role.
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding ofData Science, Full stack Web development, Big Data Engineering, DEVOPS, Data Analyst and deep ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

input_prompt3 = """
You are an AI specialized in extracting relevant information from resumes. Please extract the following details from the provided resume properly:
    - First Name
    - Last Name
    - Full Name
    - Email Address
    - Phone Number
    - Location
    - LinkedIn URL
    - University Name
    - Education Level
    - Graduation Year and Month
    - Majors
    - GPA
    - Job Title
    - Company Name
    - Job Location
    - Job Duration
    - Skills
    - Certifications
    Provide the extracted information in a structured format.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")
elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = extract_resume_details(input_text, pdf_content,input_prompt3)
        st.subheader("Extracted Resume Details")
        st.write(response)
    else:
        st.write("Please upload the resume")