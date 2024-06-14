'''
1）搜索路径的顺序
搜索「内置模块」（built-in module）：time，os，sys等等
搜索 sys.path 中的路径
而sys.path中路径顺序又如下：

当前执行的.py文件所在目录；
环境变量 PYTHONPATH中列出的目录；
第三方库site-packages：像conda，pip安装的库都在这里；

2）相对和绝对的导入方法
程序猿有两种方法导入模块，相对导入和绝对导入
无论绝对导入还是相对导入都有参照物。
绝对导入的参照物是当前执行的入口.py文件所在的文件夹，相对导入的参照物是当前模块所在位置。
绝对导入
└── D:\workplace\python\import_test
    ├──main.py
    ├── pack1
    │   ├── module1.py

# main.py
from pack1 import module1
执行main.py，正常运行，此时绝对导入的参照物是main.py所在目录，即D:\workplace\python\import_test

现在把main.py移到package1目录下
└── D:\workplace\python\import_test
    ├── pack1
    │   ├── module1.py
    │   ├── main.py

# main.py
from pack1 import module1
执行main.py，报错ModuleNotFoundError: No module named 'pack1'，因为此时绝对导入的参照物是main.py所在目录，即D:\workplace\python\import_test\pack1，不存在D:\workplace\python\import_test\pack1\pack1，自然报错。

2.2相对导入
在python中相对导入，又分隐式相对导入和显式相对导入。
# 文件结构
└── D:\workplace\python\import_test
    ├──main.py
    ├── pack1
    │   ├── module1.py
    │   ├── module2.py

# module1.py
import pack1.module2 # 绝对导入
import  module2 # 隐式相对导入
from . import module2 # 显式相对导入

# main.py
from pack1 import module1 # 绝对导入

================================
执行入口的.py文件不可以使用相对导入
常常会报这样的错误：ImportError: attempted relative import with no known parent package。
当输入命令行python main.py或者IDE运行main.py时，main.py中不可以使用相对导入。因为python会把执行.py文件的__name__改为"__main__"，
此时就找不到__main__.pack1。

top-level顶层文件夹不能作为包
常常会报这样的错误：ValueError: attempted relative import beyond top-level package。
因为你把顶层文件夹当成包在使用。什么是top-level？当前执行入口.py文件所在的文件夹，也就是绝对导入的参照物。
不可以把top-level文件夹作为包package，自然也就不能导入了。

# 文件结构
└── D:\workplace\python\import_test
    ├──main.py
    ├── pack1
    │   ├── module1.py
    │   ├── module2.py

# module1.py
from .. import module2 #  报错!!!!此时..是顶层文件夹D:\workplace\python\import_test，
不可以把它作为包，自然就不能导入它

# main.py
from pack1 import module1 # 绝对导入
================================
https://zhuanlan.zhihu.com/p/432503792

jin
'''
import sys
# import os
# print(os.getcwd())

# 正常从上往下的绝对路径进行引用
from file2 import bb
from folder11.folder111 import folder11_m
bb()
folder11_m()

# 当前主运行文件调用同级目录的子文件d，子文件d中调用当前主运行文件的同级文件（子文件中的引用，直接from 同级文件名 import ..）
# 也就是说入口文件folder1.py可以引用同一目录下的所有文件，其调用的子文件也可以直接引用入口文件同目录下的文件
from folder11.file113 import aa
aa()

# 当前主运行文件调用同级目录的子文件，子文件中调用子文件的同级文件
# 解决方法（1）子文件中使用相对引用点（.）引用同级目录, 这个(.)相当于将引用调到入口文件的同级目录
from folder11.folder12 import aa
aa()

# 解决方法（2）引入搜索路径sys， 最主要的解决方法
sys.path.append(r"F:\VScode_folder\folder1\folder11")
print(sys.path)
from folder11.folder122 import aa2
aa2()