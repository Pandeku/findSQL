# coding=utf-8
import os
import configparser
JISHU = 0


# 在日志里查找SQL，通过将SQL列表传入，逐个文件打开查找
def log_find_sql(file, lists):
    key = 0
    count = 0
    f = open(file, 'r', encoding='UTF-8-sig')
    for line in f:
        if lists[key] in line:
            key = key + 1
            if key == len(lists):
                count = count + 1
                key = 0
        else:
            key = 0
    return count


# 打开文件夹，打开每一个文件，调用log_find_sql 函数查找
def get_file_path(dir_path):
    global JISHU
    result = 0
    dirs = os.listdir(dir_path)
    for sub_dir_path in dirs:
        file_path = os.path.join(dir_path, sub_dir_path)
        if os.path.isfile(file_path):  # 判读是否为文件，若是返回文件路径
            file_count = log_find_sql(file_path, get_sql_list())
            print(file_path, "计数：", file_count)
            result = result + file_count
        if os.path.isdir(file_path):  # 判断是否为目录，若是则继续遍历
            JISHU = JISHU+get_file_path(file_path)
    return result


# 读取SQL文件，去掉'\n,\t'，将其转化为列表,并返回
def get_sql_list():
    list_sql = []
    sql_list = open(csv_sql_path, encoding='UTF-8-sig')
    for line in sql_list:
        line=line.strip("\n")
        line = line.strip("\t")
        list_sql.append(line)
    return list_sql


# 主函数，设置SQL文件和log文件夹
if __name__ == '__main__':

    config = configparser.ConfigParser()
    config.read("path.ini")  # 读配置文件
    dirs_path = config.get("File_Path", "Dirs_path")
    csv_sql_path = config.get("File_Path", "Csv_sql_path")
    print("开始计数:", get_sql_list())
    get_file_path(dirs_path)
    print("在所有记录里共查到记录：", JISHU)

