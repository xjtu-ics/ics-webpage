import os
import zipfile
import json
import argparse
import shutil
import locale

default_pic_url = 'docs/assets/default.png'
pic_path_map = {}

def unzip_files(source_folder):
    """
    解压缩指定文件夹下的所有 ZIP 文件，并将文件名改为与 ZIP 文件同名（不包含扩展名）。
    :param source_folder: 包含 ZIP 文件的文件夹路径
    :param extract_folder: 提取的目标目录
    :return: 解压缩后的文件夹列表
    """

    # 确保目标目录存在
    if not os.path.exists(source_folder):
        os.makedirs(source_folder)

    # 遍历 source_folder 下的所有文件和子文件夹
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.zip'):
                zip_file_path = os.path.join(root, file)
                zip_file_name = os.path.splitext(os.path.basename(zip_file_path))[0]  # 获取 ZIP 文件名（不包含扩展名）

                with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                    # 解压到指定目录
                    zip_ref.extractall(source_folder)

                    # 遍历解压后的文件
                    for zip_info in zip_ref.infolist():
                        original_file_name = zip_info.filename
                        original_file_ext = os.path.splitext(original_file_name)[1]
                        new_file_name = f"{zip_file_name}{original_file_ext}"  # 新文件名与 ZIP 文件同名
                        new_file_path = os.path.join(source_folder, new_file_name)

                        # 重命名文件
                        original_file_path = os.path.join(source_folder, original_file_name)
                        os.rename(original_file_path, new_file_path)
                        
def mv_picture(source_folder):
    supported_extensions = {'.jpg', '.jpeg', '.png', '.gif'}

    # 遍历文件夹及其子文件夹
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # 检查文件扩展名是否为支持的图片格式
            if os.path.splitext(file)[1].lower() in supported_extensions:
                old_pic_path = os.path.join(root, file)
                new_pic_path = os.path.join(pic_extract_folder, file)
                new_pic_path_withour_ext = os.path.splitext(new_pic_path)[0]
                pic_path_map[new_pic_path_withour_ext] = new_pic_path
                shutil.copy2(old_pic_path, new_pic_path)


def read_and_merge_json(source_folder, pic_extract_folder, target_json_path):
    """
    读取指定文件夹下所有解压缩文件夹中的 JSON 文件，添加 pic_url 字段，并将其内容添加到目标 JSON 文件中
    :param source_folder: 指定文件夹的路径
    :param pic_extract_folder: 图片提取的目标目录
    :param target_json_path: 目标 JSON 文件的路径
    """
    all_json_data = []
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.json'):
                json_file_path = os.path.join(root, file)
                try:
                    with open(json_file_path, 'r', encoding='utf-8') as json_file:
                        json_data = json.load(json_file)
                        # 为 JSON 数据添加 pic_url 字段
                        pic_name = os.path.splitext(file)[0]
                        pic_url = os.path.join(pic_extract_folder, pic_name)
                        pic_url = pic_path_map.get(pic_url, default_pic_url)
                        parts = pic_url.split('/')
                        pic_value = '/'.join(parts[1:])
                        json_data['pic_url'] = f'../{pic_value}'
                        all_json_data.append(json_data)
                        print(f"merge {pic_name}")
                except json.JSONDecodeError:
                    pass
                except IndexError:
                    pass

    if all_json_data:
        try:
            locale.setlocale(locale.LC_COLLATE, 'zh_CN.UTF-8')
            sorted_json_data = sorted(all_json_data, key=lambda x: locale.strxfrm(x.get('name', '')))
            with open(target_json_path, 'w', encoding='utf-8') as target_file:
                json.dump(sorted_json_data, target_file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(e)
            pass


def delete_zip_files(folder_path):
    """
    删除指定文件夹下的所有 .zip 文件
    :param folder_path: 要清理的文件夹路径
    """
    # 确保路径存在
    if not os.path.exists(folder_path):
        print(f"路径不存在：{folder_path}")
        return

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件扩展名是否为 .zip
        if filename.endswith(".zip"):
            file_path = os.path.join(folder_path, filename)
            try:
                os.remove(file_path)  # 删除文件
                print(f"已删除文件：{file_path}")
            except Exception as e:
                print(f"删除文件时出错：{file_path}，错误信息：{e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='解压缩 ZIP 文件，合并 JSON 文件，提取图片并添加 pic_url 字段')
    parser.add_argument('source_folder', type=str, help='包含 ZIP 文件的文件夹路径')
    parser.add_argument('pic_extract_folder', type=str, help='图片提取的目标目录')
    parser.add_argument('target_json', type=str, help='目标 JSON 文件的路径')

    args = parser.parse_args()
    source_folder = args.source_folder
    pic_extract_folder = args.pic_extract_folder
    target_json = args.target_json

    # 创建图片提取目录
    if not os.path.exists(pic_extract_folder):
        os.makedirs(pic_extract_folder)

    # 解压缩 ZIP 文件并记录解压缩后的文件夹
    unzip_files(source_folder)
    mv_picture(source_folder)
    # 读取并合并 JSON 文件，添加 pic_url 字段
    read_and_merge_json(source_folder, pic_extract_folder, target_json)
    # 删除解压缩产生的文件夹
    delete_zip_files(source_folder)