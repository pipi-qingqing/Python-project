from insert import filename
import os

def delete():
   while True:
       student_id = input('请输入要删除的学生ID:')
       if student_id != ' ':
           if os.path.exists(filename):
               with open(filename,'r',encoding='utf-8') as file:
                   student_old = file.readline()
           else:
               student_old = []
           flag=False
           if student_old:
               with open(filename,'w',encoding='utf-8') as wfile:
                   d={}
                   for item in student_old:
                       d=dict(eval(item))
                       if d['id'] != student_id:
                           wfile.write(str(d)+'\n')
                       else:
                           flag = True
                   if flag:
                       print('已删除ID为student_id的学生信息')
                   else:
                       print('未找到学生信息')

           else:
               print('无学生信息')
           answer = input('是否继续删除：y/n')
           if answer == 'y':
               continue
           else:
               break
