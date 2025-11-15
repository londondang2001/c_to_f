# 摄氏(celsius) 转换为华氏(fahrenheit) 程式

# 让使用者输入 摄氏温度
# 然后印出 华氏温度

c = input('请输入摄氏温度：')
c = float(c)
f = c * 1.8 + 32
print('华氏温度为：', f, 'F')