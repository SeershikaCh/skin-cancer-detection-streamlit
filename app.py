import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

st.title("Skin Cancer Detection App")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("your_model.h5")

model = load_model()

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img = image.resize((224,224))
    img_array = np.array(img)/255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    if prediction[0][0] > 0.5:
        st.error("Prediction: Malignant")
    else:
        st.success("Prediction: Benign")
