import os
import zipfile
import json
import argparse
import shutil

default_pic_url = 'docs/assets/default.png'
pic_path_map = {}

def unzip_files(source_folder, pic_extract_folder):
    """
    解压缩指定文件夹下的所有 ZIP 文件，提取图片到指定目录，并返回解压缩后的文件夹列表
    :param source_folder: 包含 ZIP 文件的文件夹路径
    :param pic_extract_folder: 图片提取的目标目录
    :return: 解压缩后的文件夹列表
    """
    unzipped_folders = []
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.zip'):
                zip_file_path = os.path.join(root, file)
                with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                    # 创建与 ZIP 文件同名的文件夹用于解压缩
                    extract_folder = os.path.splitext(zip_file_path)[0]
                    zip_ref.extractall(extract_folder)
                    unzipped_folders.append(extract_folder)
                    # 获取 ZIP 文件的名称（不包含扩展名）
                    zip_file_name = os.path.splitext(os.path.basename(zip_file_path))[0]
                    # 提取图片到指定目录并改名
                    for zip_info in zip_ref.infolist():
                        if zip_info.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                            # 获取图片的扩展名
                            ext = os.path.splitext(zip_info.filename)[1]
                            # 构造新的图片文件名
                            new_pic_name = f"{zip_file_name}{ext}"
                            new_pic_path = os.path.join(pic_extract_folder, new_pic_name)
                            new_pic_path_withour_ext = os.path.splitext(new_pic_path)[0]
                            pic_path_map[new_pic_path_withour_ext] = new_pic_path
                            with zip_ref.open(zip_info) as source, open(new_pic_path, 'wb') as target:
                                target.write(source.read())
                     # 提取 JSON 文件到指定目录并改名
                    for zip_info in zip_ref.infolist():
                        if zip_info.filename.lower().endswith('.json'):
                            # 构造新的 JSON 文件名
                            new_json_name = f"{zip_file_name}.json"
                            new_json_path = os.path.join(extract_folder, new_json_name)
                            with zip_ref.open(zip_info) as source, open(new_json_path, 'w', encoding='utf-8') as target:
                                target.write(source.read().decode('utf-8'))
                            # 删除原 JSON 文件
                            original_json_path = os.path.join(extract_folder, zip_info.filename)
                            if os.path.exists(original_json_path):
                                os.remove(original_json_path)
    return unzipped_folders


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
                        json_data['pic_url'] = f'/{pic_value}'
                        all_json_data.append(json_data)
                        print(f"merge {pic_name}")
                except json.JSONDecodeError:
                    pass
                except IndexError:
                    pass

    if all_json_data:
        try:
            with open(target_json_path, 'w', encoding='utf-8') as target_file:
                json.dump(all_json_data, target_file, ensure_ascii=False, indent=4)
        except Exception:
            pass


def delete_unzipped_folders(folders):
    """
    删除指定的解压缩文件夹
    :param folders: 解压缩文件夹的列表
    """
    for folder in folders:
        if os.path.exists(folder):
            try:
                shutil.rmtree(folder)
            except Exception:
                pass


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
    unzipped_folders = unzip_files(source_folder, pic_extract_folder)
    # 读取并合并 JSON 文件，添加 pic_url 字段
    read_and_merge_json(source_folder, pic_extract_folder, target_json)
    # 删除解压缩产生的文件夹
    delete_unzipped_folders(unzipped_folders)