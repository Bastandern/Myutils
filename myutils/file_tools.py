import hashlib
import os
from pathlib import Path

def calculate_hash(file_path: Path, algorithm: str = 'sha256') -> str:
    """计算指定文件的哈希值"""
    if not file_path.is_file():
        return f"错误: {file_path} 不是一个有效文件。"

    hash_func = getattr(hashlib, algorithm, None)
    if hash_func is None:
        return f"错误: 不支持的算法 {algorithm}"

    h = hash_func()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def list_tree(dir_path: Path, max_depth: int = 2, current_depth: int = 0):
    """(简易版) 打印目录树"""
    if not dir_path.is_dir():
        print(f"错误: {dir_path} 不是一个有效目录。")
        return

    if current_depth > max_depth:
        return

    items = sorted(dir_path.iterdir(), key=lambda x: (x.is_file(), x.name))

    for i, item in enumerate(items):
        prefix = "│   " * current_depth
        connector = "└── " if i == len(items) - 1 else "├── "

        print(f"{prefix}{connector}{item.name}")

        if item.is_dir():
            list_tree(item, max_depth, current_depth + 1)