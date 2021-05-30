filename = 'student_txt'


def insert():
    student_list=[]

    # Add student info
    while True:
        id = input('请输入ID：')
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩'))
            python = int(input('请输入python成绩：'))
        except:
            print('输入无效，请重新输入：')
            continue
        student = {'id':id,'name':name,'english':english,'python':python}
        student_list.append(student)
        a=input('是否继续添加y/n?')
        if a == 'y':
          continue
        else:
          break

    save(student_list)


def save(student_list):
    try:
        stu_txt = open(filename,'a',encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
        pass

    for student in student_list:
        stu_txt.write(str(student) + '\n')

    stu_txt.close()
