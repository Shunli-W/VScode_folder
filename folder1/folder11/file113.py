import sys
def aa():
    bb()

if __name__ == '__main__':
    sys.path.append(r"F:\VScode_folder\folder1")
    from ..file2 import bb 
    aa()
    bb()
else:
    from file2 import bb 
    aa()
    bb()
