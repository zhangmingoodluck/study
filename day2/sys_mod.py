#Author Mike
#-----------utf-8--------------
'''import os
cmd_res=os.system("dir")#执行命令，不保存结果
cmd_res=os.popen("dir")#执行命令，保存结果,只有内存路径
cmd_res=os.popen("dir").read()#执行命令，保存结果
print ("--",cmd_res)
os.mkdir("new_dir")
print (type(2**32))
print (type(2**64))
print (type(2**1024))'''
msg="我是帅哥"
print (msg)
print(msg.encode('utf-8'))
print(msg.encode('utf-8').decode())
