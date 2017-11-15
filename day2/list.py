#Author Mike
#-----------utf-8--------------
#names ="zhangyang guyan xihuan" #无法取单个学生的名字，只能用分隔符，或者正则等麻烦的方式读取，修改也非常麻烦
import copy
names=["zhangyang","guyan","xihuan","fuck",["jack","peter","mike"],"oye","oye","oye"]
for index,i in enumerate(names):
    print(index,i )
'''
print(names)
#names.reverse()#反转列表要素顺序
#print(names)
names1=["4a","aa","Aa","#a"]
print(names1)
names1.sort()#按ascii码排序
print(names1)
print(names[0],names[2])
print(names[0:2])#从第一位开始连续取2个字符，顾头不顾尾，也就是最后一位取不到，也叫切片
print(names[:3])#第一位开始取3个
print(names[-1])#取最后一位
print(names[-4])#取最后第二位
print(names[-2:])#取最后二位
names.append("last") #追加list要素
print(names)
print(names[-1])#取最后一位
names.insert(1,"insert")#插入一位要素
print(names)
print(names[1])#取下标为1的要素
names[2]="修改"#修改list的要素
print(names)
print(names[2])
names.remove("oye")#删除要素
print(names)
del names[0]
print(names)
names.pop()#默认删除最后一个，如果有下标则与del相同
print(names)
print(names.index("xihuan"))#查找要素的下标
print(names[names.index("xihuan")])
print(names.count("oye"))#统计list内的相同要素的数量
names.extend(names1)#合并2个list
print(names,names1)
names2=names.copy()
print(names,names2)
names.clear()#清除list内的要素
del names

print(names)
names2=copy.deepcopy(names)
names[1]="99"
names[4][2]="edit"
print(names)
print(names2)
'''
'''
print(names)
#for i in names:
    #print (i)
print(names[0:-1:2])#从第一个显示到最后一个，步长为2，只显示奇数编号的要素
print(names[::2])#0，或-1可以省略

names2=names.copy()
names3=names[:]
names4=list(names)
print(names)
print(names2)
print(names3)
print (names4)

person=['name',['saving',100]]
p1=person.copy()
p2=person.copy()
p1[0]="老公"
p2[0]="老婆"
p1[1][1]=50
print(p1)
print(p2)names=["zhangyang","guyan","xihuan","fuck","oye","oye","oye"]
print(names)
print(names[-2:])#取最后2位
'''
