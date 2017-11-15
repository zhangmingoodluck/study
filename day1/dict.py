#Author Mike
#-----------utf-8--------------

dict={'name':'mike','age':'27','class':'4'}
print (dict['age'])                 #显示字典中的key对应的value
dict['age']=25                      #修改key对应的value
print (dict['age'])
dict['school']='oye'               #新增一个不存在的value
print (dict['school'])
#del dict['school']                 #删除一个key
#print (dict['school'])
#dict.clear()                         #清空字典
#print (dict['age'])
#del dict                            #删除字典
#print (dict['age'])
print (len(dict))
print (dict.get('name'))
print (dict.get('fuck'))
print (dict.items())
print (dict.keys())
dict.setdefault('fuck',default=None)
print (dict.get('fuck'))