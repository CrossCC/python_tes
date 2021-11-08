import sys
import os

def parse_file(path):
    """
    用于分析文件，返回文件中空格、制表符和行数
    path：分析的文件路径
    return：包含空格数、制表符数和行数的元组
    """
    with open(path) as f:
        i = 0
        spaces = 0
        tabs = 0
        for i,line in enumerate(f):
            spaces += line.count(' ')
            tabs += line.count('\t')

    return spaces,tabs,i+1


def main(path):
    """
    用于打印分析结果
    若文件不存在返回False
    """
    if os.path.exists(path):
        spaces,tabs,lines = parse_file(path)
        print("Spaces{},Tabs{},Lines{}".format(spaces,tabs,lines))
        return True
    else:
        return False

if __name__ == '__main__':
   #是否有参数
    if len(sys.argv) > 1:
        main(sys.argv[1])

    else:
        sys.exit(-1)

    sys.exit(0)
