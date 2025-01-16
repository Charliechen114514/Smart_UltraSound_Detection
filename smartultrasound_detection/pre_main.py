import os

# 设置目标路径
rc_py_dir = 'runtimes_middlewares/rc_py'

def create_if_not_exsited(dir_path: str):
    # 检查路径是否存在，如果不存在则创建
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"[logging]: Directory '{dir_path}' created as is requried")
    else:
        print(f"[logging]: Directory '{dir_path}' already exists. jump the creations...")

create_if_not_exsited(rc_py_dir)