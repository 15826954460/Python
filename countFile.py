import os
result = []
def get_all(cwd):
    get_dir = os.listdir(cwd)  # 遍历当前目录，获取文件列表
    print(get_dir)
    for i in get_dir:          
        sub_dir = os.path.join(cwd,i)  # 把第一步获取的文件加入路径
        print(sub_dir)
        if os.path.isdir(sub_dir):     # 如果当前仍然是文件夹，递归调用
            get_all(sub_dir)
        else:
            ax = os.path.basename(sub_dir)  # 如果当前路径不是文件夹，则把文件名放入列表
            result.append(ax)
            # print(len(result))   #对列表计数
    return result
lis = ''
if __name__ == "__main__": 
    cur_path = os.getcwd()   #当前目录
    lis = get_all(cur_path)

for item in lis:
    pass
    # print(item)

