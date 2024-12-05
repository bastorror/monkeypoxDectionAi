import streamlit as st 
import pandas as pd
import keras 
from PIL import Image
from util import classify        #import libary ที่จำเป็น



st.title('Monkey Pox classification')     # ตั้งชื่อหัวข้อ
st.header('Please upload a monkey pox image') 

file = st.file_uploader('', type=['jpeg', 'jpg', 'png', 'HEIC'])  # ตั้งค่านามสกุลที่เป็น input

# model = keras.models.load_model('model\cnn_model_7.h5') # load model ที่เทรน

# with open('model\labels.txt', 'r') as f:  # เปิดไฟล์ labels เพื่ออ่าน class
#   class_names = [a[:-1].split(' ') for a in f.readlines()]
#   f.close

# if file is not None:      # นำ input มาอ่านและทำนายผลลัพท์
#   image = Image.open(file).convert('RGB')
#   st.image(image, use_column_width=True)

#   class_name, conf_score = classify(image, model, class_names)  

#   st.write("## {}".format(class_name))
#   st.write("### score: {}".format(conf_score))
