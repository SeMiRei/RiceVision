import streamlit as st

# ==========================================
# Header
# ==========================================

st.title("🌾 RiceVision")

st.subheader(
    "ระบบช่วยจำแนกโรคใบข้าวด้วยเทคนิคการเรียนรู้เชิงลึก"
)

st.write(
    "ระบบต้นแบบสำหรับช่วยคัดกรองโรคใบข้าวจากภาพ "
    "พร้อมแสดงข้อมูลโรคและแนวทางการจัดการเบื้องต้น"
)

st.divider()

# ==========================================
# Welcome
# ==========================================

st.header("ยินดีต้อนรับสู่ RiceVision")

st.write(
    """
    RiceVision เป็นระบบต้นแบบที่พัฒนาขึ้นเพื่อช่วยจำแนก
    โรคใบข้าวจากภาพด้วยเทคนิค Deep Learning

    ระบบรองรับโรคใบข้าวทั้งหมด 6 Classes ได้แก่
    Healthy, Bacterial Leaf Blight, Brown Spot,
    Leaf Blast, Leaf Scald และ Tungro
    """
)

# ==========================================
# Project Overview
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "จำนวน Classes",
        "6"
    )

with col2:
    st.metric(
        "จำนวนภาพ",
        "4,494"
    )

with col3:
    st.metric(
        "แหล่งข้อมูล",
        "2 Sources"
    )

st.divider()

# ==========================================
# How to use
# ==========================================

st.header("🚀 วิธีใช้งาน")

step1, step2, step3 = st.columns(3)

with step1:
    st.subheader("1️⃣ Upload")
    st.write(
        "อัปโหลดภาพใบข้าวที่ต้องการวิเคราะห์"
    )

with step2:
    st.subheader("2️⃣ Analyze")
    st.write(
        "ระบบจะวิเคราะห์ภาพและจำแนกประเภทโรค"
    )

with step3:
    st.subheader("3️⃣ Management")
    st.write(
        "ดูข้อมูลโรคและแนวทางการจัดการเบื้องต้น"
    )

st.divider()

st.info(
    "💡 เลือกเมนูจาก Sidebar เพื่อเริ่มใช้งาน RiceVision"
)

st.caption(
    "RiceVision | Multi-Source Rice Leaf Disease Classification"
)