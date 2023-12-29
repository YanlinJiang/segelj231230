from skimage import (data, img_as_float)
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt

# 示例图像：使用skimage库中的示例图像
image1 = img_as_float(data.camera())
image2 = img_as_float(data.camera())

# 加一些噪声到第二幅图像以模拟图像退化
import numpy as np
noise = np.random.normal(0, 0.1, image1.shape)
image2 = image1 + noise

# 限制图像的值在合理的范围内
image2 = np.clip(image2, 0, 1)

# 计算两幅图像的SSIM
ssim_index = ssim(image1, image2)

# 显示两幅图像和它们的SSIM值
fig, axes = plt.subplots(1, 3, figsize=(10, 4))

axes[0].imshow(image1, cmap=plt.cm.gray)
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(image2, cmap=plt.cm.gray)
axes[1].set_title('Degraded Image')
axes[1].axis('off')

axes[2].text(0.5, 0.5, f'SSIM: {ssim_index:.2f}', fontsize=20, ha='center')
axes[2].axis('off')

plt.tight_layout()
plt.show()
