import streamlit as st
from model_predict import prediction

st.title("Casting Defect Detection")
label=None
casting_image=st.file_uploader("Upload an image", type=["jpg", "jpeg"])
if casting_image is not None:
    st.image(casting_image, caption="Uploaded Image", use_container_width=True)
    st.write("Image uploaded successfully!")
    with open('casting_image.jpg', 'wb') as f:
        f.write(casting_image.getbuffer())
    st.write("Label:",prediction("casting_image.jpg"))

    



    
