import tkinter as tk
from tkinter import filedialog
import os
import re
import shutil


def directory_selector_gui():
    root = tk.Tk()
    root.withdraw()
    dir_path = filedialog.askdirectory(
        initialdir='C:/Users/USER/Desktop/compare', title="選擇資料夾")
    return dir_path


def compare_file(dir_path, origin_file, target_file, sameFile_dir):
    abs_origin_file = os.path.join(dir_path, origin_file)
    abs_target_file = os.path.join(dir_path, target_file)

    # 打开第一个文件以读取字符串内容
    with open(abs_origin_file, "r") as ofile:
        of_txt = ofile.read()
    with open(abs_target_file, "r") as tfile:
        tf_txt = tfile.read()

    # 忽略多個空白和換行符號
    of_txt = re.sub(r"\s+", "", of_txt)
    tf_txt = re.sub(r"\s+", "", tf_txt)

    # 若有同樣的檔案，則複製到sameFile資料夾
    if (of_txt == tf_txt):
        shutil.copy(abs_origin_file, os.path.join(sameFile_dir,origin_file))
        shutil.copy(abs_target_file, os.path.join(sameFile_dir,target_file))
        return True
    return False


dir_path = directory_selector_gui()
sameFile_dir = os.path.join(dir_path, "sameFile")

# 讀檔案和創建sameFile資料夾
if os.path.exists(sameFile_dir):
    shutil.rmtree(sameFile_dir)

files = os.listdir(dir_path)
os.makedirs(sameFile_dir, exist_ok=True)

for i, origin_file in enumerate(files):
    print(f"\n[{i}] {origin_file}\n")
    for j in range(i+1, len(files)):
        target_file = files[j]
        isSame = compare_file( dir_path, origin_file, target_file, sameFile_dir)
        print(f"compare: {target_file}..... {isSame}")
    print("="*50)
