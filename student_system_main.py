def main():
    while True:
        menu()
        a=int(input('请输入：'))
        if a==1:
            insert()


def menu():
    print('学生信息管理系统')
    print('功能菜单')
    print('1.录入学生信息')
    print('2.查找学生信息')
    print('3.删除学生信息')
    print('4.修改学生信息')
    print('5.排序')
    print('6.统计学生总人数')
    print('7.显示所有学生信息')
    print('0.退出学生系统')


if __name__ == '__main__':
        main()
