import cv2
import os

# 设置图片文件夹路径
images_folder = './mydata_augmented/images/train'  # 请替换为你的图片文件夹路径
output_folder = './mydata_augmented/images/filtered'  # 输出文件夹路径，如果不存在会自动创建

# 创建输出文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 高斯滤波核大小
kernel_size = 5

# 遍历文件夹内的图片并进行高斯滤波
for i in range(1, 207):  # 范围从1到206
    # 构造原图片的完整路径
    image_path = os.path.join(images_folder, f'{i:03d}.jpg')

    # 读取图片
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # 检查图片是否正确加载
    if image is None:
        print(f"图片 {i:03d}.jpg 无法加载，请检查图片路径。")
        continue

    # 应用高斯滤波
    filtered_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    # 构造输出图片的完整路径，保持文件名不变
    output_path = os.path.join(output_folder, f'{i:03d}.jpg')

    # 保存处理后的图片
    cv2.imwrite(output_path, filtered_image)
    print(f"图片 {i:03d}.jpg 已进行高斯滤波并保存至 {output_folder}")

print("所有图片已处理完毕。")
