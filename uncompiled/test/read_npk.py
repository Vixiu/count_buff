import struct
import zlib
from PIL import Image

# 定义NPK文件头部的结构
NPK_Header_Format = '16sI'
NPK_Header_Size = struct.calcsize(NPK_Header_Format)

# 定义NPK文件索引的结构
NPK_Index_Format = 'II256s'
NPK_Index_Size = struct.calcsize(NPK_Index_Format)

# 定义NImgF文件头部的结构
NImgF_Header_Format = '16sIIIi'
NImgF_Header_Size = struct.calcsize(NImgF_Header_Format)

# 定义NImgF文件索引的结构
NImgF_Index_Format = 'IIiiiiiiii'
NImgF_Index_Size = struct.calcsize(NImgF_Index_Format)

# 读取NPK文件头部
with open('your_file.npk', 'rb') as file:
    header_data = file.read(NPK_Header_Size)
    flag, count = struct.unpack(NPK_Header_Format, header_data)

    # 读取NPK文件索引
    for _ in range(count):
        index_data = file.read(NPK_Index_Size)
        offset, size, name = struct.unpack(NPK_Index_Format, index_data)
        decoded_name = bytes([a ^ b for a, b in zip(name, decord_flag)]).rstrip(b'\x00').decode('utf-8')

        # 在这里可以根据offset和size读取IMG文件
        with open(decoded_name, 'wb') as img_file:
            file.seek(offset)
            img_file.write(file.read(size))

# 读取IMG文件
with open('your_img_file.img', 'rb') as img_file:
    header_data = img_file.read(NImgF_Header_Size)
    flag, index_size, unknown1, unknown2, index_count = struct.unpack(NImgF_Header_Format, header_data)

    # 读取IMG文件索引
    for _ in range(index_count):
        index_data = img_file.read(NImgF_Index_Size)
        dwType, dwCompress, width, height, size, key_x, key_y, max_width, max_height = struct.unpack(NImgF_Index_Format, index_data)

        # 读取图片数据
        img_data = img_file.read(size)

        # 解压缩图片数据
        if dwCompress == 6:
            img_data = zlib.decompress(img_data)

        # 处理图片数据，这里假设你已经有了一个适当的处理函数
        processed_data = process_image_data(img_data)

        # 保存处理后的图片
        img = Image.frombytes('RGBA', (width, height), processed_data)
        img.save(f'image_{_}.png')
