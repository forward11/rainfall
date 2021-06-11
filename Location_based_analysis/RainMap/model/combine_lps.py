import cv2
from file_reader import get_all_files

# 加载图像
wind_imgs = get_all_files('E:\\rainfall\\Location_based_analysis\\under_wind\\plot\\lps_wind_last')
rain_imgs = get_all_files('E:\\rainfall\\Location_based_analysis\\under_wind\\plot\\lps_rain_last')
for i in range(len(wind_imgs)):
    rain_img = cv2.imread(rain_imgs[i])
    wind_img = cv2.imread(wind_imgs[i])

    rows, cols = wind_img.shape[:2]
    # print(rows, cols)
    # rows, cols = rain_img.shape[:2]
    # print(rows, cols)
    # exit()
    roi = rain_img[800:800+rows, -cols-800:-800]
    dst = cv2.addWeighted(wind_img, 0.8, roi, 0.2, 0)
    add_img = rain_img.copy()
    add_img[800:800+rows, -cols-800:-800] = dst
    cv2.imwrite('E:\\rainfall\\Location_based_analysis\\under_wind\\plot\\lps_last\\'+wind_imgs[i].split('\\')[-1], add_img)
