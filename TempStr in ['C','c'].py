#TempConvert.py
TempStr = input("请输入带有符号的温度值:")
#设置一个变量，input为字符串格式
if TempStr[-1] in ['F','f']:         #检测字符串最后一个字符是C or F判断华氏度和摄氏度，进行温度转换,
    C = (eval(TempStr[0:-1]) - 32)/1.8        #这里是计算过程，用eval函数,取第一位到倒数第二位(不包括最后的单位)
    print("转换后的温度是{:.2f}C".format(C))   #format格式处理 {:.2f是小数点后两位 f= float 浮点数}
if TempStr[-1] in {'C','c'}:
        F = 1.8*eval(TempStr[0:-1]) + 32
        print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")            #防止出bug写个else 
    