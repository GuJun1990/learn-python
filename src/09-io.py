# -*- coding: UTF-8 -*-


def read_all():
    with open('/Users/gujun/PycharmProjects/learn-python/data/input.txt', 'r') as f:
        print(f.read())


def read_line_by_line():
    with open('/Users/gujun/PycharmProjects/learn-python/data/input.txt', 'r') as f:
        for line in f.readlines():
            print(line.strip())  # 把末尾的'\n'删掉


def write_file():
    with open('/Users/gujun/PycharmProjects/learn-python/data/output.txt', 'w') as f:
        f.write("Hello, world!\n")


if __name__ == '__main__':
    # read_all()
    # read_line_by_line()
    write_file()

