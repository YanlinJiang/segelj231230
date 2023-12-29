import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import cv2
import io
from pages.algorithm import NRSS2
from pages.algorithm.NRSStest import NRSS
from skimage.metrics import structural_similarity as compare_ssim



def executeFR(img):
    Algorithm = st.multiselect(
        'Step-3, Choose an algorithm:',
        ['1.SSIM',
         '2.PSNR',])
    buttonEx = st.button("Execute")
    if buttonEx:
        #st.write(Algorithm)
        if img is None:
            st.write("No Image File is Uploaded")
        elif not Algorithm:
            st.write("Please select an algorithm first")
        else:
            image_details = {"file_name": img.name,
                            "file_type": img.type,
                            "file_size": img.size}
            st.write(image_details)
            # To View Uploaded Image
            image_data = img.read()
            image = Image.open(io.BytesIO(image_data))
            st.image(image, width=250)
            if '1.SSIM' in Algorithm:
                st.write(NRSS2(img).NRSS())


def executeNR(img):
    Algorithm = st.multiselect(
        'Step-3, Choose an algorithm:',
        ['1.NRSS',
         '2.尚无',])
    buttonEx = st.button("Execute")
    if buttonEx:
        #st.write(Algorithm)
        if img is None:
            st.write("No Image File is Uploaded")
        elif not Algorithm:
            st.write("Please select an algorithm first")
        else:
            image_details = {"file_name": image_file.name,
                            "file_type": image_file.type,
                            "file_size": image_file.size}
            st.write(image_details)
            # To View Uploaded Image
            image_data = image_file.read()
            image = Image.open(io.BytesIO(image_data))
            st.image(image, width=250)
            if '1.NRSS' in Algorithm:
                temp=NRSStest(img)
                st.write(temp.process_image())



st.header("""Multiple Modules Image Processing""")
st.caption("-You can choose what function you like and processing image here.")

#第一步，上传图片
image_file = st.file_uploader("Step-1, Upload an Images",type=["png","jpg","jpeg"])

#第二步，选择FR/RR/NR
#st.write("Step-1, Choose an type for image processing:")
step1Button = st.selectbox('Step-2, Choose an type for image processing:',
             ('Full Reference(FR)','Reduce Reference(RR)','None Reference(NR)','Click to select'),index=3)
if step1Button=='Full Reference(FR)':
    # 第三步，选择算法
    executeFR(image_file)
elif step1Button=='Reduce Reference(RR)':
    # 第三步，选择算法
    Algorithm = st.multiselect(
        'Step-3, Choose an algorithm:',
        ['A算法', 'B算法', 'C算法',
         'D算法', 'E算法', 'F算法'])
    buttonEx = st.button("Execute")
elif step1Button=='None Reference(NR)':
    # 第三步，选择算法
    executeNR(image_file)






