grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  #Список:
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}                        #Множество:
a = sorted(students)
z = grades[0]
z_1 = sum(z) / len(z)
x = grades[1]
x_1 = sum(x) / len(x)
c = grades[2]
c_1 = sum(c) / len(c)
v = grades[3]
v_1 = sum(v) / len(v)
b = grades[4]
b_1 = sum(b) / len(b)
School = {a[0]: z_1, a[1]: x_1, a[2]: c_1, a[3]: v_1, a[4]: b_1}
print(School)
