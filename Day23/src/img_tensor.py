import cv2 as cv
import psycopg2
import torchvision.transforms as transforms

# 数据库连接配置
db_config = {
    'dbname': 'user_tZGjBb',
    'user': 'user_tZGjBb',
    'password': 'password_fajJed',
    'host': '10.0.201.34',
    'port': '5432'
}


def insert_image_record(image_path, image_shape, tensor_shape, image_data, tensor_data):
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    query = """
    INSERT INTO image_records (image_path, image_shape, tensor_shape, image_data, tensor_data)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (image_path, image_shape, tensor_shape, image_data, tensor_data))

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    img_path = 'D:\\download\\PixPin_2024-05-11_18-33-28.png'
    img = cv.imread(img_path)
    print("img: ", img.shape)  # numpy数组格式为（H,W,C）

    transf = transforms.ToTensor()
    img_tensor = transf(img)  # tensor数据格式是torch(C,H,W)
    print("img_tensor: ", img_tensor.size())

    # 将图片和Tensor转换为二进制数据
    _, img_encoded = cv.imencode('.jpg', img)
    img_data = img_encoded.tobytes()
    tensor_data = img_tensor.numpy().tobytes()

    # 插入记录到数据库
    insert_image_record(
        img_path,
        str(img.shape),
        str(img_tensor.size()),
        img_data,
        tensor_data
    )
