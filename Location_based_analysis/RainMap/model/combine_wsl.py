import cv2
from file_reader import get_all_files

# 加载图像
wind_imgs = get_all_files('E:\\rainfall\\Location_based_analysis\\RainMap\\plot\\wsl\\wind')
rain_imgs = get_all_files('E:\\rainfall\\Location_based_analysis\\RainMap\\plot\\wsl\\rain')
for i in range(len(wind_imgs)):
    rain_img = cv2.imread(rain_imgs[i])
    wind_img = cv2.imread(wind_imgs[i])

    rows, cols = wind_img.shape[:2]
    # print(rows, cols)
    # rows, cols = rain_img.shape[:2]
    # print(rows, cols)
    # exit()
    roi = rain_img[1000:1000+rows, -cols-300:-300]
    dst = cv2.addWeighted(wind_img, 0.8, roi, 0.2, 0)
    add_img = rain_img.copy()
    add_img[1000:1000+rows, -cols-300:-300] = dst
    cv2.imwrite('E:\\rainfall\\Location_based_analysis\\RainMap\\plot\\wsl\\rain&wind\\'+rain_imgs[i].split('\\')[-1], add_img)
