import cv2
import numpy as np
import streamlit as st

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

