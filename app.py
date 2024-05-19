import streamlit as st
from rembg import remove
from PIL import Image
import io

# Title of the application
st.title("Background Removal Web Application")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    input_image = Image.open(uploaded_file)
    st.image(input_image, caption="Uploaded Image", use_column_width=True)

    # Remove the background
    st.write("Removing background...")
    output_image = remove(input_image)

    # Convert the result to a format that can be displayed by Streamlit
    output_buffer = io.BytesIO()
    output_image.save(output_buffer, format="PNG")
    output_buffer.seek(0)
    
    # Display the output image
    st.image(output_image, caption="Image with Background Removed", use_column_width=True)

    # Provide a download link for the result
    st.download_button(
        label="Download Image",
        data=output_buffer,
        file_name="remove.png",
        mime="image/png"
    )
