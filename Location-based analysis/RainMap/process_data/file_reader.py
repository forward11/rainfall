import os

def get_all_files(directory):
    files = []
    file_list = os.listdir(directory)
    for i in range(0, len(file_list)):
        path = os.path.join(directory, file_list[i])
        if os.path.isdir(path):
            files.extend(get_all_files(path))
        if os.path.isfile(path):
            files.append(path)

    return files


if __name__ == '__main__':
    wsl_path = "E:\\rainfall\\Location-based analysis\\RainMap\\data"
    files = get_all_files(wsl_path)