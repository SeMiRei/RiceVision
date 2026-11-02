import streamlit as st


st.title("📊 ข้อมูลโครงการ")

st.write(
    "Multi-Source Rice Leaf Disease Classification"
)

st.divider()

# ==========================================
# Statistics
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Classes",
        "6"
    )

with col2:

    st.metric(
        "Images",
        "4,494"
    )

with col3:

    st.metric(
        "Sources",
        "2"
    )

with col4:

    st.metric(
        "Images / Class",
        "749"
    )

st.divider()

# ==========================================
# Dataset Sources
# ==========================================

st.header("📚 แหล่งข้อมูล")

st.subheader(
    "Mendeley Data"
)

st.write(
    "Rice Leaf Disease Image Samples"
)

st.write(
    "**จำนวนภาพที่นำมาใช้:** 2,249 ภาพ"
)

st.subheader(
    "Kaggle"
)

st.write(
    "Rice Leaf Disease Dataset"
)

st.write(
    "**จำนวนภาพที่นำมาใช้:** 2,245 ภาพ"
)

st.divider()

# ==========================================
# Classes
# ==========================================

st.header("🌾 Classes")

classes = [
    "Healthy",
    "Bacterial Leaf Blight",
    "Brown Spot",
    "Leaf Blast",
    "Leaf Scald",
    "Tungro"
]

for i, class_name in enumerate(classes, 1):

    st.write(
        f"**{i}.** {class_name}"
    )

st.divider()

# ==========================================
# Dataset Split
# ==========================================

st.header("📦 Dataset Split")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Training",
        "3,144"
    )

with col2:

    st.metric(
        "Validation",
        "678"
    )

with col3:

    st.metric(
        "Testing",
        "672"
    )

st.caption(
    "Train / Validation / Test = 70% / 15% / 15%"
)