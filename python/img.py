from PIL import Image
import matplotlib.pyplot as plt


# 显示图片
img_path = "E:/image/icon_google.png"
# img_path = "D:\\cloudNote\\github\\jupyter-notebook\\quanju_v_1.tmp"
img=Image.open(img_path)
plt.figure("dog")
plt.imshow(img)
plt.show()