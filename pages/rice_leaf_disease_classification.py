import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

from disease_info import disease_info


st.title("🔍 ทายผลโรคใบข้าว")

st.write(
    "อัปโหลดภาพใบข้าวเพื่อเข้าสู่กระบวนการวิเคราะห์"
)

st.divider()


MODEL_PATH = "best.keras"

# =========================================================
# Class Names
# =========================================================

CLASS_NAMES = [
    "Bacterial Leaf Blight",
    "Brown Spot",
    "Healthy",
    "Leaf Blast",
    "Leaf Scald",
    "Tungro",
]

# =========================================================
# Load Model
# =========================================================

@st.cache_resource
def load_classification_model():
    return load_model(
        MODEL_PATH,
        compile=False
    )


try:

    model = load_classification_model()

except Exception as e:

    st.error("❌ ไม่สามารถโหลด Model ได้")

    st.info(
        "กรุณาตรวจสอบว่าไฟล์ model อยู่ในโฟลเดอร์ "
        "`model` และชื่อไฟล์ถูกต้อง"
    )

    st.code(MODEL_PATH)

    st.stop()

# =========================================================
# Upload Image
# =========================================================

uploaded_file = st.file_uploader(
    "เลือกภาพใบข้าว",
    type=[
        "jpg",
        "jpeg",
        "png"
    ]
)


if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    col1, col2 = st.columns(2)

    # =====================================================
    # Image
    # =====================================================

    with col1:

        st.subheader("📷 ภาพที่อัปโหลด")

        st.image(
            image,
            use_container_width=True
        )

    # =====================================================
    # Prediction
    # =====================================================

    with col2:

        st.subheader("การวิเคราะห์")

        st.info(
            "กดปุ่มเพื่อให้ Model วิเคราะห์ภาพใบข้าว"
        )


        if st.button(
            "🔍 วิเคราะห์ภาพ",
            use_container_width=True
        ):

            # -------------------------------------------------
            # Prepare Image
            # -------------------------------------------------

            # อ่านขนาด Input ของ Model
            input_height = model.input_shape[1]
            input_width = model.input_shape[2]

            # Resize ภาพ
            img = image.resize(
                (input_width, input_height)
            )

            # แปลงเป็น NumPy Array
            img_array = np.array(img)

            # เพิ่ม Batch Dimension
            img_array = np.expand_dims(
                img_array,
                axis=0
            )

            # -------------------------------------------------
            # Preprocessing
            # -------------------------------------------------

            # Normalize ค่า Pixel
            img_array = img_array.astype("float32") / 255.0


            # -------------------------------------------------
            # Prediction
            # -------------------------------------------------

            predictions = model.predict(
                img_array,
                verbose=0
            )[0]


            # -------------------------------------------------
            # Get Top 3
            # -------------------------------------------------

            top_indices = np.argsort(
                predictions
            )[::-1][:3]


            # Class ที่มี Probability สูงสุด
            predicted_index = top_indices[0]

            prediction = CLASS_NAMES[
                predicted_index
            ]

            confidence = predictions[
                predicted_index
            ]

            # -------------------------------------------------
            # Save Result
            # -------------------------------------------------

            st.session_state["prediction"] = prediction

            st.session_state["confidence"] = confidence

            st.session_state["predictions"] = predictions

            st.session_state["top_indices"] = top_indices

# =========================================================
# Result
# =========================================================

if "prediction" in st.session_state:

    prediction = st.session_state["prediction"]

    confidence = st.session_state["confidence"]

    predictions = st.session_state["predictions"]

    top_indices = st.session_state["top_indices"]

    info = disease_info[prediction]


    st.divider()

    st.header("🎯 ผลการทำนาย")

    col1, col2 = st.columns(2)

    # =====================================================
    # Prediction Result
    # =====================================================

    with col1:

        st.success(
            f"**{prediction}**"
        )

        st.write(
            f"ชื่อภาษาไทย: "
            f"**{info['name_th']}**"
        )

    # =====================================================
    # Confidence
    # =====================================================

    with col2:

        st.metric(
            "Confidence",
            f"{confidence * 100:.2f}%"
        )

        st.progress(
            float(confidence)
        )

    # =====================================================
    # Disease Information
    # =====================================================

    st.divider()

    st.subheader("🌱 ข้อมูลโรค")

    st.write(
        f"**อาการ:** {info['description']}"
    )

    # =====================================================
    # Management
    # =====================================================

    st.subheader("🧑‍🌾 แนวทางการจัดการ")

    for item in info["management"]:

        st.write(
            f"• {item}"
        )

    # =====================================================
    # Top 3 Predictions
    # =====================================================

    st.divider()

    with st.expander("📊 ผลการทำนาย Top 3"):

        for rank, index in enumerate(
            top_indices,
            start=1
        ):

            class_name = CLASS_NAMES[index]

            probability = predictions[index]

            st.write(
                f"**อันดับ {rank}: {class_name}** "
                f"({probability * 100:.2f}%)"
            )

            st.progress(
                float(probability)
            )