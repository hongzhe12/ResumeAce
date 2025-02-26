import os

def encrypt_python_files():
    # 获取当前工作目录
    current_directory = os.getcwd()
    # 列出当前目录下的所有文件
    files = os.listdir(current_directory)
    for file in files:
        # 检查文件是否为 .py 文件
        if file.endswith('.py'):
            # 构建文件的完整路径
            file_path = os.path.join(current_directory, file)
            # 构建 pyarmor 加密命令
            command = f'pyarmor gen "{file_path}"'
            try:
                # 执行 pyarmor 加密命令
                os.system(command)
                print(f"Successfully encrypted {file_path}")
            except Exception as e:
                print(f"Failed to encrypt {file_path}: {e}")

if __name__ == "__main__":
    encrypt_python_files()