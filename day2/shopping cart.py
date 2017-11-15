#Author Mike
#-----------utf-8--------------
# 启动程序后，让用户输入工资，然后打印商品列表
#允许用户根据商品编号购买商品
#用户选择商品后，检测用户余额是否够，够就扣款，不够则提醒
#可以随时退出，退出时打印已购买的商品和余额

while True:
    amt=input("please input your amount:")
    if amt.isdigit():
        amt=int(amt)
        shopcart = []
        commodity = [("commodity1", 10), ("commodity2", 20), ("commodity3", 30), ("commodity4", 40), ("commodity5", 60),
                     "if you input 'q' that means quit"]
        while True:
            # for i in commodity:
            #    print(commodity.index(i),i)
            for index, item in enumerate(commodity):
                print(index, item)
            purchasecommodity = input("please input your commdity's number")
            if purchasecommodity.isdigit():
                purchasecommodity=int(purchasecommodity)
                if purchasecommodity > int(len(commodity))-2 or purchasecommodity <0:
                    print("product is not exist!")
                else:
                    price = commodity[purchasecommodity][-1]
                    if amt >= price:
                        amt = amt - commodity[purchasecommodity][-1]
                        shopcart.append(commodity[purchasecommodity])
                        print( "\033[32;1m%s\033[0m is added to your shop cart,your balance is \033[31;1m%s\033[0m"%(commodity[purchasecommodity][0],amt))
                    else:
                        print("your balance is not enough")
            elif purchasecommodity == "q":
                print("your balance is \033[31;1m%s\033[0m" % (amt))
                print("your shop cart:")
                # for i in shopcart:
                #    print(i)
                for index, item in enumerate(shopcart):
                    print(index, item)
                exit()
            else:
                print("please input number")
    elif amt=="q":
        print("bye")
        exit()
    else:
        print("please input digit")



