import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='papa', charset='utf8')
cursor = conn.cursor()

cursor.execute("select url from t_url where zt='1'")
a1 = cursor.fetchall()
# # print(a1)
# # c=a1[2][0]
# # print(c)
#
for i in range(len(a1)):
    # print(i)

    sql2="update t_url set zt='0' where url=('%s')"%a1[i][0]
    cursor.execute(sql2)
    conn.commit()

# a='https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-15436921628.119.3eea658bzBf2kN&id=589760335477&rn=3cc2c9c58e867db7b8591f8a98938a72&abbucket=10'
# print(len(a))

for i in range(5):
    print(i)
for j in range(5,10):
    print(j)






