from insert import filename
import os
def search():
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按ID查找请输入1，按姓名查找请输入2：')
            if mode=='1':
                id=input('请输入学生ID:')
            elif mode=='2':
                name=input('请输入学生姓名：')
            else:
                print('您的输入有误，请重新输入')
                search()
            with open(filename,'r',readline='utf-8') as rfile:
                student=rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id !='':
                        if id == d['id']:
                            student_query.append()
                    if name !='':
                        if name == d['name']:

                            student_query.append()
            show_student(student_query)
            student_query.clear()
            y=input('是否继续查询：y/n')
            if y == 'y':
                continue
            else:
                break
