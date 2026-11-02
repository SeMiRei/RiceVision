import streamlit as st


st.title("ℹ️ เกี่ยวกับ RiceVision")

st.write(
    """
    RiceVision เป็นระบบต้นแบบสำหรับช่วยจำแนกโรคใบข้าว
    จากภาพด้วยเทคนิค Deep Learning
    """
)

st.divider()

st.header("🎯 วัตถุประสงค์")

objectives = [
    "รวบรวมข้อมูลภาพใบข้าวจากหลายแหล่ง",
    "เตรียมและทำความสะอาดข้อมูลภาพ",
    "พัฒนาโมเดลสำหรับจำแนกโรคใบข้าว",
    "ประเมินประสิทธิภาพของโมเดล",
    "พัฒนาระบบต้นแบบสำหรับนำโมเดลไปใช้งาน"
]

for objective in objectives:

    st.write(
        f"• {objective}"
    )

st.divider()

st.header("🌾 โรคที่ระบบรองรับ")

classes = [
    "Healthy",
    "Bacterial Leaf Blight",
    "Brown Spot",
    "Leaf Blast",
    "Leaf Scald",
    "Tungro"
]

for class_name in classes:

    st.write(
        f"• {class_name}"
    )

st.divider()

st.header("⚠️ ข้อจำกัดของระบบ")

st.warning(
    """
    ผลการวิเคราะห์จากระบบเป็นการคัดกรองเบื้องต้น
    ไม่ควรใช้แทนการวินิจฉัยจากผู้เชี่ยวชาญ
    """
)

st.divider()

st.caption(
    "RiceVision | Multi-Source Rice Leaf Disease Classification"
)