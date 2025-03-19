# # import streamlit as st
# # from streamlit_drawable_canvas import st_canvas
# # from PIL import Image
# # import numpy as np
# # import base64
# # from io import BytesIO
# # import google.generativeai as genai
# # from gtts import gTTS
# # import os
# # import time

# # # Configure Gemini API
# # genai.configure(api_key="AIzaSyAWsewWyrj733ImgncO47SwlsKmm-5pDKU")
# # model = genai.GenerativeModel("gemini-2.0-flash")

# # # Streamlit UI
# # st.title("🎨 Paint-like Canvas with Text-to-Speech")
# # st.write("Select a tool and draw on the canvas, or upload your own flowchart!")

# # # File Uploader for Flowchart
# # uploaded_file = st.file_uploader("📤 Upload your flowchart (PNG/JPG)", type=["png", "jpg", "jpeg"])

# # # Tool and Settings
# # tool = st.selectbox("🛠️ Tool", ["Select", "Eraser", "Pencil", "Brush", "Rectangle", "Circle", "Line"])
# # stroke_color = st.color_picker("🎨 Color", "#000000")
# # stroke_width = st.slider("✏️ Brush/Pencil Size", 1, 20, 3)  # Smaller default for Pencil
# # eraser_width = st.slider("🧽 Eraser Size", 1, 50, 20)

# # st.write("Current Tool:", tool)  # Debug

# # # Define drawing mode based on selected tool
# # drawing_mode = None
# # if tool == "Pencil":
# #     drawing_mode = "freedraw"
# #     stroke_width = min(stroke_width, 3)  # Limit to small width for pencil effect
# # elif tool == "Brush":
# #     drawing_mode = "freedraw"
# # elif tool == "Eraser":
# #     drawing_mode = "freedraw"
# #     stroke_color = "#FFFFFF"  # White for erasing
# # elif tool == "Rectangle":
# #     drawing_mode = "rect"
# # elif tool == "Circle":
# #     drawing_mode = "circle"
# # elif tool == "Line":
# #     drawing_mode = "line"
# # elif tool == "Select":
# #     drawing_mode = "transform"

# # # Canvas for drawing (without background_image due to error)
# # canvas_result = st_canvas(
# #     fill_color="rgba(255, 255, 255, 0)",  # Transparent background
# #     stroke_width=eraser_width if tool == "Eraser" else stroke_width,
# #     stroke_color=stroke_color,
# #     background_color="#FFFFFF",
# #     height=600,
# #     width=1000,
# #     drawing_mode=drawing_mode,
# #     key="paint_canvas",
# # )

# # # Display uploaded image if present
# # if uploaded_file is not None:
# #     uploaded_image = Image.open(uploaded_file).convert("RGBA")
# #     st.image(uploaded_image, caption="Uploaded Flowchart", use_column_width=True)
# #     st.write("Flowchart uploaded successfully!")  # Debug

# # st.write("Canvas Data Available:", canvas_result.image_data is not None)  # Debug

# # # User Query Input
# # user_query = st.text_input("🔍 Enter your query related to the drawing")

# # # Convert image to Base64 for processing
# # def encode_image(image_data):
# #     try:
# #         buffered = BytesIO()
# #         image_data.save(buffered, format="PNG")
# #         return base64.b64encode(buffered.getvalue()).decode("utf-8")
# #     except Exception as e:
# #         st.error(f"Image encoding failed: {str(e)}")
# #         return None

# # # Convert text to speech and save as temporary file
# # def text_to_speech(text, filename="response.mp3"):
# #     try:
# #         tts = gTTS(text=text, lang='en')
# #         tts.save(filename)
# #         return filename
# #     except Exception as e:
# #         st.error(f"TTS Error: {str(e)}")
# #         return None

# # # Process canvas and query using Gemini API
# # def analyze_canvas_and_query(canvas_image, query, uploaded_image=None):
# #     parts = []
# #     if uploaded_image is not None:
# #         img_base64 = encode_image(uploaded_image)
# #         if img_base64:
# #             parts.append({"inline_data": {"mime_type": "image/png", "data": img_base64}})
# #     elif canvas_image is not None:
# #         img_base64 = encode_image(canvas_image)
# #         if img_base64:
# #             parts.append({"inline_data": {"mime_type": "image/png", "data": img_base64}})
    
# #     if query:
# #         parts.append({"text": query})
    
# #     try:
# #         response = model.generate_content({"parts": parts})
# #         text_response = response.text if response else "Could not interpret the content."
# #         # Convert response to speech
# #         audio_file = text_to_speech(text_response)
# #         if audio_file:
# #             st.audio(audio_file, format="audio/mp3")
# #             # Add a delay to ensure playback completes before deletion
# #             time.sleep(5)  # Adjust delay as needed based on audio length
# #             try:
# #                 os.remove(audio_file)
# #             except Exception as e:
# #                 st.warning(f"Could not delete audio file: {str(e)}. It may still be in use.")
# #         return text_response
# #     except Exception as e:
# #         st.error(f"API Error: {str(e)}")
# #         return "API connection failed. Please check your API key or network."

# # # Button to trigger analysis
# # if st.button("🔍 Analyze Drawing"):
# #     if canvas_result.image_data is not None or user_query or uploaded_file:
# #         uploaded_image = Image.open(uploaded_file).convert("RGBA") if uploaded_file else None
# #         if canvas_result.image_data is not None:
# #             try:
# #                 canvas_image = Image.fromarray((canvas_result.image_data * 255).astype("uint8"))
# #                 result = analyze_canvas_and_query(canvas_image, user_query, uploaded_image)
# #                 st.subheader("Analysis Result:")
# #                 st.write(result)
# #             except Exception as e:
# #                 st.error(f"Image processing failed: {str(e)}")
# #         elif uploaded_file:
# #             result = analyze_canvas_and_query(None, user_query, uploaded_image)
# #             st.subheader("Analysis Result:")
# #             st.write(result)
# #         elif user_query:
# #             result = analyze_canvas_and_query(None, user_query)
# #             st.subheader("Analysis Result:")
# #             st.write(result)
# #     else:
# #         st.warning("Please draw on the canvas, upload a flowchart, or enter a query for analysis.")

# # # Clear Canvas Button
# # if st.button("🗑️ Clear Canvas"):
# #     st.session_state.background_image = None
# #     st.rerun()

# # st.success("✅ Ready! Select a tool, upload a flowchart, or start drawing.")
# import streamlit as st
# from streamlit_drawable_canvas import st_canvas
# from PIL import Image
# import numpy as np
# import base64
# from io import BytesIO
# import google.generativeai as genai
# from gtts import gTTS
# import os
# import time

# # Configure Gemini API
# genai.configure(api_key="AIzaSyAWsewWyrj733ImgncO47SwlsKmm-5pDKU")
# model = genai.GenerativeModel("gemini-2.0-flash")

# # Custom CSS for Sky-Blue Theme
# st.markdown("""
#     <style>
#     body {
#         background-color: #e0f2fe;
#         font-family: 'Arial', sans-serif;
#     }
#     .stApp {
#         background-color: #e0f2fe;
#         padding: 20px;
#         border-radius: 15px;
#         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#     }
#     h1, h2, h3 {
#         color: #0369a1;
#         text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
#     }
#     .stButton>button {
#         background-color: #0284c7;
#         color: white;
#         border: none;
#         border-radius: 8px;
#         padding: 10px 20px;
#         font-weight: bold;
#         transition: background-color 0.3s;
#     }
#     .stButton>button:hover {
#         background-color: #0369a1;
#     }
#     .stTextInput>input, .stTextArea>textarea {
#         border: 2px solid #7dd3fc;
#         border-radius: 8px;
#         background-color: #f0f9ff;
#         color: #0c4a6e;
#     }
#     .stSelectbox, .stSlider {
#         background-color: #f0f9ff;
#         border: 2px solid #7dd3fc;
#         border-radius: 8px;
#         padding: 5px;
#     }
#     .stFileUploader {
#         background-color: #f0f9ff;
#         border: 2px dashed #7dd3fc;
#         border-radius: 8px;
#         padding: 10px;
#     }
#     .stSuccess, .stWarning, .stError {
#         background-color: #bae6fd;
#         border: 1px solid #7dd3fc;
#         border-radius: 8px;
#         padding: 10px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Streamlit UI with Sky-Blue Theme
# st.title("🎨 Paint-like Canvas with Text-to-Speech")
# st.write("✨ Select a tool, draw on the canvas, or upload your own flowchart in style!")

# # File Uploader for Flowchart
# uploaded_file = st.file_uploader("📤 Upload Your Flowchart (PNG/JPG)", type=["png", "jpg", "jpeg"])

# # Tool and Settings with Decorative Emojis
# st.subheader("🛠️ Drawing Tools & Settings")
# col1, col2 = st.columns(2)
# with col1:
#     tool = st.selectbox("🖌️ Tool", ["Select", "Eraser", "Pencil", "Brush", "Rectangle", "Circle", "Line"])
#     stroke_color = st.color_picker("🎨 Stroke Color", "#0284c7")  # Default sky-blue
# with col2:
#     stroke_width = st.slider("✏️ Brush/Pencil Size", 1, 20, 3)
#     eraser_width = st.slider("🧽 Eraser Size", 1, 50, 20)

# st.write(f"🌟 Current Tool: **{tool}**")  # Debug with decoration

# # Define drawing mode based on selected tool
# drawing_mode = None
# if tool == "Pencil":
#     drawing_mode = "freedraw"
#     stroke_width = min(stroke_width, 3)  # Limit to small width for pencil effect
# elif tool == "Brush":
#     drawing_mode = "freedraw"
# elif tool == "Eraser":
#     drawing_mode = "freedraw"
#     stroke_color = "#FFFFFF"  # White for erasing
# elif tool == "Rectangle":
#     drawing_mode = "rect"
# elif tool == "Circle":
#     drawing_mode = "circle"
# elif tool == "Line":
#     drawing_mode = "line"
# elif tool == "Select":
#     drawing_mode = "transform"

# # Canvas for drawing with increased height
# canvas_result = st_canvas(
#     fill_color="rgba(255, 255, 255, 0)",  # Transparent background
#     stroke_width=eraser_width if tool == "Eraser" else stroke_width,
#     stroke_color=stroke_color,
#     background_color="#FFFFFF",
#     height=800,  # Increased height
#     width=1000,
#     drawing_mode=drawing_mode,
#     key="paint_canvas",
# )

# # Display uploaded image if present
# if uploaded_file is not None:
#     uploaded_image = Image.open(uploaded_file).convert("RGBA")
#     st.image(uploaded_image, caption="📸 Uploaded Flowchart", use_column_width=True)
#     st.write("🎉 Flowchart uploaded successfully!")

# st.write(f"🖼️ Canvas Data Available: **{canvas_result.image_data is not None}**")  # Debug

# # User Query Input
# st.subheader("🔍 Ask About Your Drawing")
# user_query = st.text_input("💬 Enter your query related to the drawing", placeholder="e.g., What does this shape mean?")

# # Convert image to Base64 for processing
# def encode_image(image_data):
#     try:
#         buffered = BytesIO()
#         image_data.save(buffered, format="PNG")
#         return base64.b64encode(buffered.getvalue()).decode("utf-8")
#     except Exception as e:
#         st.error(f"🚫 Image encoding failed: {str(e)}")
#         return None

# # Convert text to speech and save as temporary file
# def text_to_speech(text, filename="response.mp3"):
#     try:
#         tts = gTTS(text=text, lang='en')
#         tts.save(filename)
#         return filename
#     except Exception as e:
#         st.error(f"🚫 TTS Error: {str(e)}")
#         return None

# # Process canvas and query using Gemini API
# def analyze_canvas_and_query(canvas_image, query, uploaded_image=None):
#     parts = []
#     if uploaded_image is not None:
#         img_base64 = encode_image(uploaded_image)
#         if img_base64:
#             parts.append({"inline_data": {"mime_type": "image/png", "data": img_base64}})
#     elif canvas_image is not None:
#         img_base64 = encode_image(canvas_image)
#         if img_base64:
#             parts.append({"inline_data": {"mime_type": "image/png", "data": img_base64}})
    
#     if query:
#         parts.append({"text": query})
    
#     try:
#         response = model.generate_content({"parts": parts})
#         text_response = response.text if response else "Could not interpret the content."
#         # Convert response to speech
#         audio_file = text_to_speech(text_response)
#         if audio_file:
#             st.audio(audio_file, format="audio/mp3")
#             time.sleep(5)  # Adjust delay as needed
#             try:
#                 os.remove(audio_file)
#             except Exception as e:
#                 st.warning(f"⚠️ Could not delete audio file: {str(e)}")
#         return text_response
#     except Exception as e:
#         st.error(f"🚫 API Error: {str(e)}")
#         return "API connection failed. Please check your API key or network."

# # Button to trigger analysis
# if st.button("🔍 Analyze Drawing"):
#     if canvas_result.image_data is not None or user_query or uploaded_file:
#         uploaded_image = Image.open(uploaded_file).convert("RGBA") if uploaded_file else None
#         if canvas_result.image_data is not None:
#             try:
#                 canvas_image = Image.fromarray((canvas_result.image_data * 255).astype("uint8"))
#                 result = analyze_canvas_and_query(canvas_image, user_query, uploaded_image)
#                 st.subheader("🌟 Analysis Result:")
#                 st.write(result)
#             except Exception as e:
#                 st.error(f"🚫 Image processing failed: {str(e)}")
#         elif uploaded_file:
#             result = analyze_canvas_and_query(None, user_query, uploaded_image)
#             st.subheader("🌟 Analysis Result:")
#             st.write(result)
#         elif user_query:
#             result = analyze_canvas_and_query(None, user_query)
#             st.subheader("🌟 Analysis Result:")
#             st.write(result)
#     else:
#         st.warning("⚠️ Please draw on the canvas, upload a flowchart, or enter a query!")

# # Clear Canvas Button
# if st.button("🗑️ Clear Canvas"):
#     st.session_state.background_image = None
#     st.rerun()

# st.success("✅ Ready! Select a tool, upload a flowchart, or start drawing in sky-blue style!")
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np
import base64
from io import BytesIO
import google.generativeai as genai
from gtts import gTTS
import os
import time

# Configure Gemini API (use environment variable for deployment)
genai.configure(api_key=os.environ.get("GEMINI_API_KEY", "AIzaSyAWsewWyrj733ImgncO47SwlsKmm-5pDKU"))
model = genai.GenerativeModel("gemini-2.0-flash")  # Update to correct model if needed

# Custom CSS for Sky-Blue Theme
st.markdown("""
    <style>
    body {
        background-color: #e0f2fe;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background-color: #e0f2fe;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    h1, h2, h3 {
        color: #0369a1;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background-color: #0284c7;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #0369a1;
    }
    .stTextInput>input, .stTextArea>textarea {
        border: 2px solid #7dd3fc;
        border-radius: 8px;
        background-color: #f0f9ff;
        color: #0c4a6e;
    }
    .stSelectbox, .stSlider {
        background-color: #f0f9ff;
        border: 2px solid #7dd3fc;
        border-radius: 8px;
        padding: 5px;
    }
    .stFileUploader {
        background-color: #f0f9ff;
        border: 2px dashed #7dd3fc;
        border-radius: 8px;
        padding: 10px;
    }
    .stSuccess, .stWarning, .stError {
        background-color: #bae6fd;
        border: 1px solid #7dd3fc;
        border-radius: 8px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit UI
st.title("🎨 Paint-like Canvas with Text-to-Speech")
st.write("✨ Select a tool, draw on the canvas, or upload your own flowchart!")

# File Uploader with Custom Label
st.subheader("📤 Upload Your Flowchart")
uploaded_file = st.file_uploader(
    "Drag and drop file here - Limit 1 GB per file • PNG, JPG, JPEG",
    type=["png", "jpg", "jpeg"]
)

# Tool and Settings
st.subheader("🛠️ Drawing Tools & Settings")
col1, col2 = st.columns(2)
with col1:
    tool = st.selectbox("🖌️ Tool", ["Select", "Eraser", "Pencil", "Brush", "Rectangle", "Circle", "Line"])
    stroke_color = st.color_picker("🎨 Stroke Color", "#0284c7")
with col2:
    stroke_width = st.slider("✏️ Brush/Pencil Size", 1, 20, 3)
    eraser_width = st.slider("🧽 Eraser Size", 1, 50, 20)

st.write(f"🌟 Current Tool: **{tool}**")

# Define drawing mode
drawing_mode = None
if tool == "Pencil":
    drawing_mode = "freedraw"
    stroke_width = min(stroke_width, 3)
elif tool == "Brush":
    drawing_mode = "freedraw"
elif tool == "Eraser":
    drawing_mode = "freedraw"
    stroke_color = "#FFFFFF"
elif tool == "Rectangle":
    drawing_mode = "rect"
elif tool == "Circle":
    drawing_mode = "circle"
elif tool == "Line":
    drawing_mode = "line"
elif tool == "Select":
    drawing_mode = "transform"

# Canvas for drawing
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0)",
    stroke_width=eraser_width if tool == "Eraser" else stroke_width,
    stroke_color=stroke_color,
    background_color="#FFFFFF",
    height=800,
    width=1000,
    drawing_mode=drawing_mode,
    key="paint_canvas",
)

# Display uploaded image
if uploaded_file is not None:
    uploaded_image = Image.open(uploaded_file).convert("RGBA")
    st.image(uploaded_image, caption="📸 Uploaded Flowchart", use_column_width=True)
    st.write("🎉 Flowchart uploaded successfully!")

st.write(f"🖼️ Canvas Data Available: **{canvas_result.image_data is not None}**")

# User Query Input
st.subheader("🔍 Ask About Your Drawing")
user_query = st.text_input("💬 Enter your query related to the drawing", placeholder="e.g., What does this shape mean?")

# Image encoding function
def encode_image(image_data):
    try:
        buffered = BytesIO()
        image_data.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode("utf-8")
    except Exception as e:
        st.error(f"🚫 Image encoding failed: {str(e)}")
        return None

# Text-to-speech function
def text_to_speech(text, filename="response.mp3"):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        return filename
    except Exception as e:
        st.error(f"🚫 TTS Error: {str(e)}")
        return None

# Analyze canvas and query
def analyze_canvas_and_query(canvas_image, query, uploaded_image=None):
    parts = []
    if uploaded_image is not None:
        img_base64 = encode_image(uploaded_image)
        if img_base64:
            parts.append({"inline_data": {"mime_type": "image/png", "data": img_base64}})
    elif canvas_image is not None:
        img_base64 = encode_image(canvas_image)
        if img_base64:
            parts.append({"inline_data": {"mime_type": "image/png", "data": img_base64}})
    
    if query:
        parts.append({"text": query})
    
    try:
        response = model.generate_content({"parts": parts})
        text_response = response.text if response else "Could not interpret the content."
        audio_file = text_to_speech(text_response)
        if audio_file:
            st.audio(audio_file, format="audio/mp3")
            time.sleep(5)
            try:
                os.remove(audio_file)
            except Exception as e:
                st.warning(f"⚠️ Could not delete audio file: {str(e)}")
        return text_response
    except Exception as e:
        st.error(f"🚫 API Error: {str(e)}")
        return "API connection failed. Please check your API key or network."

# Analyze button
if st.button("🔍 Analyze Drawing"):
    if canvas_result.image_data is not None or user_query or uploaded_file:
        uploaded_image = Image.open(uploaded_file).convert("RGBA") if uploaded_file else None
        if canvas_result.image_data is not None:
            try:
                canvas_image = Image.fromarray((canvas_result.image_data * 255).astype("uint8"))
                result = analyze_canvas_and_query(canvas_image, user_query, uploaded_image)
                st.subheader("🌟 Analysis Result:")
                st.write(result)
            except Exception as e:
                st.error(f"🚫 Image processing failed: {str(e)}")
        elif uploaded_file:
            result = analyze_canvas_and_query(None, user_query, uploaded_image)
            st.subheader("🌟 Analysis Result:")
            st.write(result)
        elif user_query:
            result = analyze_canvas_and_query(None, user_query)
            st.subheader("🌟 Analysis Result:")
            st.write(result)
    else:
        st.warning("⚠️ Please draw, upload a flowchart, or enter a query!")

# Clear canvas button
if st.button("🗑️ Clear Canvas"):
    st.session_state.background_image = None
    st.rerun()

st.success("✅ Ready! Select a tool, upload a flowchart (up to 1 GB), or start drawing!")