import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image

#编辑网页标题
st.header("""Welcome to Image Processing System""")

#网页步骤介绍
st.subheader("Operating Steps:")
st.image('exFile/step.GIF')

#编辑网页简介
st.subheader("Function Introduction:")
st.write("-Full Reference(FR) image processing:")
st.caption("Frequency Resolution (FR) image processing is an advanced technique that analyzes and manipulates images based on their frequency characteristics. This method is particularly effective for noise reduction, image quality enhancement, and image restoration.")
st.write("-Reduce Reference(RR) image processing:")
st.caption("Range Resolution (RR) image processing is a technique focused on enhancing the spatial resolution of images, particularly in applications where depth or distance accuracy is crucial. ")
st.write("-None Reference(NR) image processing:")
st.caption("Noise Reduction (NR) image processing is a key technique used to improve image quality by removing unwanted random variations, or 'noise,' from images. This noise can arise from various sources, such as sensor imperfections, environmental conditions, or transmission interference.")