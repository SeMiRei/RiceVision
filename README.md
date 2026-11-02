# RiceVision

### การจำแนกโรคใบข้าวด้วยเทคนิคการเรียนรู้เชิงลึก

RiceVision เป็นโครงงานที่พัฒนาแบบจำลอง **Deep Learning** สำหรับจำแนกโรคใบข้าวจากภาพ โดยรวบรวมข้อมูลภาพจากหลายแหล่ง ได้แก่ **Mendeley Data และ Kaggle** เพื่อใช้ในการฝึกและทดสอบแบบจำลอง

## วัตถุประสงค์

พัฒนาแบบจำลองที่สามารถจำแนกภาพใบข้าวออกเป็น 6 ประเภท และนำแบบจำลองมาใช้งานผ่าน Web Application

## ประเภทที่จำแนก

1. Healthy
2. Bacterial Leaf Blight
3. Brown Spot
4. Leaf Blast
5. Leaf Scald
6. Tungro

## Dataset

ข้อมูลที่ใช้มาจาก 2 แหล่ง ได้แก่

- **Mendeley Data**: Rice Leaf Disease Image Samples
- **Kaggle**: Rice Leaf Disease Dataset

หลังจากคัดเลือกและปรับสมดุลข้อมูล ได้ทั้งหมด **4,494 ภาพ**  
แบ่งเป็น 6 Classes โดยแต่ละ Class มี **749 ภาพ**

แบ่งข้อมูลเป็น

- Training Set: 70% → 3,144 ภาพ
- Validation Set: 15% → 678 ภาพ
- Test Set: 15% → 672 ภาพ

## MODEL

มีการทดลองใช้แบบจำลอง Deep Learning ได้แก่

- DenseNet121
- EfficientNetV2-B0
- EfficientNetV2-S
- MobileNetV3-Large

ผลการทดสอบที่ดีที่สุดในขณะนี้คือ

**EfficientNetV2-S — Test Accuracy 99.55%**

## Web Application

พัฒนาด้วย **Streamlit** โดยผู้ใช้สามารถ

- อัปโหลดภาพใบข้าว
- วิเคราะห์ประเภทของโรค
- ดูค่า Confidence
- ดูข้อมูลและอาการของโรค
- ดูแนวทางการจัดการเบื้องต้น

## โครงสร้างโฟลเดอร์

```text
RiceVision/
├── app.py
├── requirements.txt
├── disease_info.py
├── model/
│   └── model.h5
├── pages/
│   ├── home.py
│   ├── rice_leaf_disease_classification.py
│   ├── disease_guide.py
│   ├── overview.py
│   └── about.py
├──.streamlit
    └── config.toml