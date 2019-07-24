# class A:
#     age=18
#     def fun(self):
#         print(self.age)
#         print(A.age)
#
#
# a=A()
# # a.fun()
#
# print(a.age) # 类属性
# # print(A.age) # 类属性
#
# b=A()
# print(b.age)
#
# a.age=20
# print(a.age)  # 20 实例属性
# print(b.age)  # 18 类属性
#
# A.age=25
# print(a.age) # 20
# print(b.age) # 25


#
#
# class A:
#     age=18
#
#     def hehe(hehe):
#         a.hehe=100
#         print(a.age)
#
#
# a=A()
# a.hehe() # self自动传递当前对象 a.hehe(a)
# a.age
# a.hehe=100



# print(a.age)  # age: 类属性
# print(a.__dict__)
# print(A.__dict__)
#
# a.age=20
# print(a.__dict__)
# print(A.__dict__)



# class A:
#     age=18
#     def hehe(self):
#         print('123')
#         print(self.age)
#
# a=A()
# print(a.__dict__)
# print(A.__dict__)


# import MySQLdb
#
# conn=MySQLdb.Connect(host='localhost',port=3306,
#                                   user='root',password='123456',
#                                   db='crawler',charset='utf8')
# cursor=conn.cursor()
#
# cursor.execute('select ip,port,types from xici where status=1')
# print(cursor.fetchone())
#
#
#



from apscheduler.schedulers.blocking import BlockingScheduler

sched=BlockingScheduler()
def hehe():
    print('123')
sched.add_job(hehe,'cron',second='*/2')
sched.start()











