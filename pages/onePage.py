import streamlit as st
from PIL import Image
import time
from streamlit_card import card
import base64




def NRSS(file):  # 画质评价算法
    import cv2
    import numpy as np
    from skimage.metrics import structural_similarity as compare_ssim

    image = cv2.imdecode(np.frombuffer(file, np.uint8), cv2.IMREAD_GRAYSCALE)
    Ir = cv2.GaussianBlur(image, (7, 7), 0)

    x = cv2.Sobel(image, cv2.CV_16S, 1, 0)
    y = cv2.Sobel(image, cv2.CV_16S, 0, 1)

    absX = cv2.convertScaleAbs(x)  # 转回uint8
    absY = cv2.convertScaleAbs(y)

    G = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

    x = cv2.Sobel(Ir, cv2.CV_16S, 1, 0)
    y = cv2.Sobel(Ir, cv2.CV_16S, 0, 1)

    absX = cv2.convertScaleAbs(x)  # 转回uint8
    absY = cv2.convertScaleAbs(y)

    Gr = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

    (h, w) = G.shape
    G_blk_list = []
    Gr_blk_list = []
    sp = 6
    for i in range(sp):
        for j in range(sp):
            G_blk = G[int((i / sp) * h):int(((i + 1) / sp) * h), int((j / sp) * w):int(((j + 1) / sp) * w)]
            Gr_blk = Gr[int((i / sp) * h):int(((i + 1) / sp) * h), int((j / sp) * w):int(((j + 1) / sp) * w)]
            G_blk_list.append(G_blk)
            Gr_blk_list.append(Gr_blk)

    sum = 0
    for i in range(sp * sp):
        mssim = compare_ssim(G_blk_list[i], Gr_blk_list[i])
        sum = mssim + sum

    nrss = sum / (sp * sp * 1.0)

    return nrss


@st.cache_data
def load_lottie(url):
    return url


st.markdown("# 画质评价界面")

with open('/Users/jiangyanlin/Downloads/2312_实验室/231226_平台搭建简介/py_project_streamlit/assets/photo/magnifying-glass.jpg', "rb") as f:
    data = f.read()
    encoded = base64.b64encode(data)
data = "data:image/png;base64," + encoded.decode("utf-8")


hasClicked = card(
  title="画质评价",
  text="Image quality evaluation",
  image=data,
  on_click=None,
  url=None,
    styles={
        "card": {
            "width": "450px",
            "height": "350px",
            "float": "left",
            "margin-top": "-30px",
            "margin-left": "-40px",

        },
        "text": {
            "font-family": "STXingKai",
            "font-size": "36px",
        },
        "filter": {
            "background-color": "rgba(255, 255, 244, 255)"  # <- make the image not dimmed anymore

        }
    }
)

st.write("###### 画质评价功能界面。")

st.divider()

st.markdown(
    "### 请上传一张照片:frame_with_picture:"
)

uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])


st.write("#### 图像")
if uploaded_file is not None:
    st.image(uploaded_file, width=500, caption="image")
    file_contents = uploaded_file.read()

button1 = st.button("开始画质评价", key="button1")

# st.image('./assets/description.png',width=600)
st.markdown(
    "### 画质评价分数:100::"
)

if button1:
    if uploaded_file is None:
        st.error('请先上传一张图片！')
    else:
        with st.spinner('正在运行中.....'):
            time.sleep(5)

        output = NRSS(file_contents)
        st.write(f'{round(output,2)}')

        st.success('画质评价成功!')