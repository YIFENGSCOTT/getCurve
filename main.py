from PIL import Image
import numpy as np

for cnt in range(3):  # 把图片读进来
    name = str(cnt) + ".jpg"
    from_path = "from/" + name
    to_path = "to/" + name
    ori_pic = Image.open(from_path)
    ori_array = np.asarray(ori_pic)
    print("Original shape: ")
    print(ori_array.shape)

    cut_array = ori_array.copy()

    for pre_i in range(int(ori_array.shape[0] * .5)):  # 上部的彩色图片中有橙色部分，不需要所以截掉
        for pre_j in range(ori_array.shape[1]):
            cut_array[pre_i][pre_j] = [0,0,0]

    res_array = cut_array.copy()

    for i in range(ori_array.shape[0]):
        for j in range(ori_array.shape[1]):
            cur_RGB = cut_array[i][j]
            if cur_RGB[0] > 120:
                if (cur_RGB[1] > 100) and (cur_RGB[1] < 130):
                    if cur_RGB[2] < 30:
                        res_array[i][j] = [0,0,0]  # 如果RGB值在上述区间，把res中的颜色换成黑的， 不然换成白的
                    else: res_array[i][j] = [255,255,255]
                else: res_array[i][j] = [255,255,255]
            else: res_array[i][j] = [255,255,255]

    res_pic = Image.fromarray(res_array).convert('RGB')  # 数组->图
    res_pic.save(to_path)  # 保存图片



