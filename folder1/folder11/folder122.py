from folder111 import folder11_m        # 当前文件运行不行，
# from folder11.folder111 import folder11_m   # 当前文件运行还是不行
# from folder111 import folder11_m   # 当前文件运行可以，但是上层文件夹调用不行

def aa2():
    folder11_m()

if __name__ == '__main__':
    aa2()