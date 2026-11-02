import streamlit as st

from disease_info import disease_info


st.title("🌱 ข้อมูลโรคใบข้าว")

st.write(
    "ข้อมูลโรคที่ RiceVision รองรับทั้งหมด 6 Classes"
)

st.divider()

# ==========================================
# Select Disease
# ==========================================

selected_disease = st.selectbox(
    "เลือกโรคที่ต้องการดูข้อมูล",
    list(disease_info.keys())
)

info = disease_info[selected_disease]

# ==========================================
# Disease
# ==========================================

st.header(
    f"🌾 {selected_disease}"
)

st.write(
    f"**ชื่อภาษาไทย:** {info['name_th']}"
)

st.write(
    f"**ลักษณะอาการ:** {info['description']}"
)

st.divider()

# ==========================================
# Management
# ==========================================

st.subheader(
    "🧑‍🌾 แนวทางการจัดการ"
)

for item in info["management"]:

    st.write(
        f"• {item}"
    )

st.divider()

st.caption(
    "ข้อมูลนี้ใช้สำหรับประกอบการคัดกรองและให้ความรู้เบื้องต้น"
)