# -*- coding: UTF-8 -*-

# 操作符
# Python中支持+-* / %(加减乘除取余)这样的操作符
# >>> a= 1
# >>> b= 2
# >>> print(a/b)
# 0.5
# >>> a= 1.0
# >>> b= 2
# >>> print(a* b)
# 2.0
# >>> a=3
# >>> b=2
# >>> print(3%2)
# // 是“地板除"君论操作数类型如何,都会对结果进行取地板运算
# >>> a=1
# >>> b=2
# >>> print a // b
# 0
# **表示乘方运算(记得Python的数据无上限)
# >>> a= 2
# >>> b= 3
# >>> print(a**b)
# 8
print(-5//3)
print(8%5)
print((-2)**4)
2>3
print(3+2)
print(5-1)
print(5*3)
print(-5/3)
print(-5//3) #向下取整
print(8%5) #取余
print(-2**32)
print((-2)**32)

# Python也支持标准的比较运算符. > < >= <= == !=这些运算符的表达式的结果,是一个布尔值
# >>>2<4
# True
# >>> 2== 4
# False
# >>>2>4
# False
# >>>2!=4
# True

# Python也支持逻辑运算符. and or not
# >>> 2<4 and2==4 >>> True and False >>> 1 and 0
# False
# >>> 2>4or 2<4
# True
# >>> not6.2<= 6
# True
# 字符串之间可以使用== != 来判定字符串的内容是否相同
# >>> 'tester' != 'Tester'
# True
# 字符串之间也可以比较大小，这个大小的结果取决于字符串的"字典序"
# >>> 'haha' < 'hehe'
# True
print(2==4,2!=4)
print('a'<'b')
print('A'<'a')
print('Z'<'a')
print('A'<'B')
#0-9 A-Z a-z
print('aza'>'aba')
print(88<123)
print('98'<'A')

import time
nowm=time.strftime('%Y%m%d %H:%M:%S',time.localtime(time.time()))
print(nowm)
import datetime
nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在
pastTime = (datetime.datetime.now()-datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')#过去一小时时间
afterTomorrowTime = (datetime.datetime.now()+datetime.timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S')#后天
tomorrowTime = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')#明天
print('\n',nowTime,'\n',pastTime,'\n',afterTomorrowTime,'\n',tomorrowTime)

a=1
print(type(a))
a=1.0
print(type(a))
a=10+5j
print(type(a))



print('''my name is"man\nba" , hello everyone''')#\n换行符
print('''my name is"man\\ba" , hello everyone''')#\本身用\\表示

#使用索引操作符[]或者切片操作符[:]来获取子字符串(切片操作是一个前闭后开区间).
#字符串的索引规则是:第一个字符索引是0, 最后一个字符索引是-1(可以理解成len-1).
a='iuytrtyuiuhiojok'
print(a[0])
print(a[-1])
print(a[1:4]) #>=1 and <4   左闭右开
print(a[:3])
print(a[2:])
print(a[:])
print(a[::-1]) #等差
print(a[::1])
print(a[::2])
print(a[::3])
print(a[::-2])

# +用于字符串连接运算, *用于字符串重复.
a='tester'
b='-soft'
c=a+b
print(c)   #tester-soft
d=a*4
print(d)  #testertestertestertester

#Python没有"字符类型"这样的概念单个字符也是字符串.
a= 'tester'
print(type(a[0]))  #<class 'str'>
c='www'
a='bcbx'
b='home'
d='com'
e=888
f='100.5'
print (e+float(f))
print(c+'.'+a+b+'.'+d+str(e))
print (a*2)

# 输入输出
# print函数将结果输出到标准输出(显示器)上.
# input函数从标准输入中获取用户输入。
# >>> name = input("Enter name:")
# Enter name:aaa
# >>> print (name)
# aaa
# name=input('enter name:')
# print(name)
# input返回的结果只是一个字符串. 如果需要获得一个数字， 需要使用int函数把字符串转换成数字.
# >>>num=input("please input a num")
# please input a num>? 5
# >>>print(num+2)
# Traceback (most recent call last):
# File "<input>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str
# 使用int函数
# >>>print(int(num)+2)
# 7
# num=input('please input a num')
# #print(num+2)错误
# print(int(num)+2)
print(len('abcdef'))

#占位符
#    %d 整数，%f浮点数，%.xf精确到小数点后x位，%s字符串
name='fzq'
age=25
money=55.63
print('我的名字是%s，我的年龄%d,我有%.9f钱'%(name,age,money))
# 1.%d　　整数占位符
# >>>'我考了%d分' % 20
# '我考了20分'
# >>>'我考了%d分' % 20.5
# '我考了20分'
# >>>"我考了%d分，进步了%d分" % (50,10)
# "我考了50分，进步了10分"
# %d只能占位整数，即使是原数字为浮点数他也会强制转换变成整数。
# 2.%f　　浮点数占位符
# >>>"我考了%f" % 66.666
# "我考了66.666000"
# >>>'我考了%f' % 66
# ‘我考了66.000000'
# >>>"我考了%f，进步了%.2f" % (66,12.369)
# "我考了66.000000，进步了12.36"
# %f只能占位浮点数，%.xf 则是精确至小数点后x位。
# 　　3.%s　　字符串占位符
#  >>>'%s' % Ture
#  'Ture'
#  >>>'%s,%s' % (123,abc)
#  '123,abc'
# %s占位字符串，应用最多。

#布尔值表示的是一个表达式的的"真" 和"假"~
#Python中用True和False来表示布尔值(注意,第一个字符大写).
a = True
print (a)
#True
print (type(a))
#<class 'bool'>
#布尔类型的变量,也是一种特殊的整数类型.在和整数进行运算时, True被当做1, False被当做0.
a = True
b=a+ 1
print (b)
print(type(True))
a='956'
print(int(a))  #int整数
b='23.23'
print(float(b))
print('数字是%d' %int(a),end='***')
print('kfj',end='end')
print()
# 函数
# 我们实现一个打印日志的函数.这个函数第一个参 数是一条日志的前缀,后续可能有N个参数, N个参
# 数之间使用 \t分割 .join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
def Log(prefix, *data):
    print (prefix + '\t'.join(data))
Log('[Notice]','hello','world')
# 通过在参数名前加两个星号**.星号后面的部分表示传入的参数是一个字典.这时候调用函数就可
# 以按照关键字参数的方式传参了.
def Log(prefix, **data):
    print (prefix + '\t'.join(data.values()))
Log('[Notice]', ip = '127.0.0.1', port = '80', userid = '1234')

#查看系统默认编码方式
import sys
print(sys.getdefaultencoding())
#如果要包含中文,默认不是utf-8的话,需要在代码文件最开头的地方注明
#-*- coding: UTF-8 -*-

# 原始字符串(raw strings)
# 有的时候,我们需要有\n这样的字符作为转义字符.但是有些时候我们又不希望进行转义，
# 需要原始的\n作为字符串的一部分.
# 举个例子, QQ发消息时,有一个"表情快捷键"的功能这个功能就相当于"转义字符".
# 当开启了这个功能之后，在输入框中输入/se就会被替换成一个表情比如我给同事发-个目录
# /search/tester(这本来是表示linux上的一个目录)
# 这种情况下，我们需要关闭"表情快捷键"功能对于Python来说我们就可以使用原始字符串来解决
# 这个问题.
print(r'hello\nworld')

'''列表/元组'''
# ●列表和元组类似于c语言中的数组.
# 使用[]来表示列表,使用()来表示元组.
# >>> alist=[1,2, 3, 4]
# >>> alist
# [1,2,3,4]
# >>> atuple= (1,2,3, 4)
# >>> atuple
# (1,2,3,4)
# ●列表和元组能保存任意数量任意类型的Python对象
# >>>a= [1, 'haha']
# >>> a
# [1, "haha']
# ●可以使用下标来访问里面的元素,下标从0开始.最后一个下标为-1
# >>> a[0]
# 1
# >>> a[-1]
new_list=[]
print(type(new_list))
new_yuanzu =()
print(type(new_yuanzu))
new_list=[124, 6.66,'abcd', True]
print(new_list[0:2])
new_list[0]=200
print(new_list)

'''排序'''
# sorted:排序这是一个非常有用的函数.返回一个有序的序列(输入参数的副本).
# a =[1，3, 4, 2]
# print(sorted(a))
# #执行结果
# [1, 2, 3，4]
# sorted可以支持自定制排序规则
# 例子1:逆序排序
# a =[1，3, 4，2]
# print(sorted(a, reverse=True))
# #执行结果
# [4, 3, 2，1]
# 例子2:按字符串的长度排序
a = ['aaa', 'bbb', 'cc', 'd']
print(sorted(a, key = len))
# #执行结果
# ['d', 'cc', 'bbb', 'aaaa']

'''理解元组的"不可变" '''
# ●元组的 “不可变"指的是元组元素的id不可变就是说一个元组包含了几个对象然后不可以给这
# 个元组再添加或者删除其中的某个对象也不可以将某个对象改成其他的对象
# ●如果元组中的某个元素是可变对象(比如列表或字典),那么仍然是可以修改的.
a= ([1, 2, 3], [4, 5, 6])
a[0][0] = 100
print (a)
#执行结果
#([100, 2, 3], [4, 5, 6])
new_list=(124,6.66,'abcd',True,[1, 1.5,'test'])
new_list[-1][-1] = 100
print(new_list)
print(new_list[1:3])
# ●可以使用1:切片操作得到列表或元组的子集这个动作和字符串操作是一样的
# >>> a[:]
# [1, 'haha']
# ●列表和元组唯一的区别是, 列表中的元素可以修改,但是元组中的元素不能修改.
# >>>a=[1,2,3,4]
# >>> a[0]= 100
# >>> a
# [100,3,3,4]

# >>> a=(1,2,3, 4)
# >>> a[0]= 100
# Traceback (most recent call last):
# File "<input>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment

'''字典'''
# ●字典是Python中的映射数据类型.存储键值对(key-value).
# ●几乎所有类型的Python对象都可以用作键,不过一般还是数字和字符串最常用.使用{}表示字典
# >>> a = {'ip’: 127.0.0.1'} #创建字典
# >>> a['ip']  #取字典中的元素
# '127.0.0.1'
# >>> a['port'] = 80 #插入新键值对
# >>> a
# {'ip': 127.0.0.1', 'port': 80}
zidian = {}
print (type (zidian))
zidian= {'ip':' 127.0.0.1'}
print (zidian)
zidian['user_name' ]= 'root'
print (zidian)
zidian['user_name' ] = 'bcbx14'
print (zidian)
'''创建字典'''
# 使用{}的方法，我们前面已经介绍过了使用工厂方dict
a = dict((['x', 1],['y', 2]))
print(a)
# 使用字典的内建方法fromkeys
a={}.fromkeys(('x','y'), 0)
print(a)
# #执行结果
# {'x':0， 'y':0}
b={}.fromkeys('xyc发',123)
print(b) #{'x': 123, 'y': 123, 'c': 123, '发': 123}
c={}.fromkeys(('xy',),123)
print(c)  #{'xy': 123}
d={}.fromkeys(('xy'),123)
print(d)  #{'x': 123, 'y': 123}

# ●注意 字典中的键值对,顺序是不确定的
# ● 修改字典元素使用[]可以新增/修改字典元素
# 如果key不存在就会新增;如果已经存在就会修改
# a={}
# a[1] = 100
# print (a)
# a[1] = 200
# print (a)
# #执行结果
# {1:100}
# {1:200}

'''zip'''
# zip:这个函数的功能不太好用语言表达，我们看代码.
# x=[1,2,3]
# y=[4,5,6]
# z=[7,8,9,10]
# print(list(zip(x, y, z)))
# #执行结果
# [(1, 4, 7)，(2, 5, 8)，(3, 6, 9)]
# ●zip其实可以理解成矩阵的 行列互换
# d = dict(zip(key, value))
# print (d)
# #执行结果
# {'score': 60, 'name': manba',' 'id': 1234}
key_list = ['name' ,'age' ,'score']
value_list = ['manba' , 18, 100]
print(dict(zip(key_list, value_list)))
newzd=dict(zip(key_list, value_list))
print(newzd)
#{'name': ' manba', ' age': 18, ' score': 100}

# newzd.clear()    #1.清除字典
# print(newzd)
# myage=newzd.pop('age') #2.删除然后备份
# print(newzd)
# print(myage)
# 3.使用del来删除某一个键值对
# a = {1:100}
# del a[1]
# print (a)
# #执行结果
# {}

# keys:返回一个列表包含字典的所有的key
# values:返回一个列表包含字典的所有value
# items:返回一个列表每一个元素都是一个元组， 包含了key和value
# a = {'x':0， 'y':1}
# print (a.items())
# #执行结果
# dict_items([('x', 0), ("y", 1)])
print(newzd.keys())    #dict_keys(['name', 'age', 'score'])
print(newzd.values())   #dict_values(['manba', 18, 100])
print(newzd.items())   #dict_items([('name', 'manba'), ('age', 18), ('score', 100)])



'''字符串合并和拆分'''
#将序列中的字符串合并成一个字符串.
b='-'
a = ['aa', 'bb', 'cc', 'dd']
print (b.join(a)) #执行结果 aa-bb-cc-dd
#按空格将字符串分割成列表
a='aa bb cc dd'
print (a.split(' ')) #执行结果 ['aa'， 'bb', 'cc', 'dd']
b='aaa,bbb,ccc'
print (b.split(','))
print (b.split(',')[0])

'''字符串常用函数'''
#判定字符串开头结尾
a = 'hello world my name is manba'
print(a.startswith('hel'))
print(a.endswith( 'ba'))
#执行结果 True True
#去除字符串开头结尾的空格制表符
a='   hello world '
print(a)
print (a.strip())
#执行结果 hello world

#左对齐/右对齐
a =' hello world '
print (a.ljust(20,'*'))
print (a.rjust(20,'*'))
print (a.center(20,'*'))
#执行结果:
#hello world*********
#*********hello world
#****hello world*****
#查找子串
a = 'hello world'
print (a.find('ld'))  #下标从0开始数
#执行结果 9
wel ='hello bcbx14 everyone welcome to bcbx13, I am maba'
num_start = wel.find('bcbx')
print(num_start)
print(wel[num_start:num_start+8])
print(wel)

print(len('man\tba')) #6

# 替换子串(记得字符串是不可变对象只能生成新字符串).
# a='hello world'
# print (a.replace( 'world', 'python' ))
# #执行结果
# hello python
# 判定字符串是字母/数字
# str.isalpha如果字符串至少有一个字符并且所有字符都是字母则返回True,否则返回False
# str.isdigit如果字符串只包含数字则返回True否则返回False.
# a = 'helloworld'
# print (a.isalpha())
# a='1234'
# print (a.isdigit())
# #执行结果
# True True

'''列表常用操作'''
# append:追加元素
# a = [1,2]
# a.append(3)
# print (a)
# #执行结果 [1, 2, 3]
# 删除指定下标元素
# a=[0,1,2]
# del a[0]
# print (a)
# #执行结果 [1, 2]
# 按值删除元素
# a=[1,2,3]
# a.remove(1)
# print (a)
# #执行结果 [2,3]

# 列表比较操作: ==/!=为判定所有元素都相等,则认为列表相等;< <= > >=则是两个列表从第一
# 个元素开始依次比较直到某一方胜出
# a = ['abc', 123]
# b = ['xyz', 789]
# c = ['abc', 123]
# print (a < b)
# print (b < c)
# print(b>c and a==c)
# #执行结果
# True
# False
# True

'''对象三要素 id  type(类型)  value(具体的值)'''
#'bcbx'
print (id('bcbx' ), type('bcbx' ),'bcbx' )
#88
print (id(88), type(88), 88)
#99.99
print (id(99.99), type(99.99), 99.99)
#[1, 'tester',I. 5]
print(id([1,'tester' , 1.5]), type([1,'tester' ,1.5]),[1,'tester' ,1.5])
a ='bcbx'
a=88
a=99.99
b=99.99
print(id(a), type(a),a)
print(id(b), type(b), b)

'''理解“引用" '''
# Python中可以用 id这个内建函数查看变量的“地址".
# >>> a= 100
# >>> id(a)
# 24187568
# >>> a= 200
# >>> id(a)
# 24191144
# >>> b=a
# >>> id(b)
# 24191144
# >>>b=300
# >>> id(b)
# 25094648
# ●给a重新赋值成200, 相当于新创建了一个200这样的对象然后将变量名a重新绑定到200这个对象，上
# ●将a赋值给b, 其实相当于又创建了一个变量名b,并将b这个名字和200这个对象绑定到-起
# ●再次修改b的值, 可以看到其实是又创建了一个300这样的对象将b绑定到300这个对象上.
# ●像创建的a, b这样的变量名，其实只是一个对象的别名.或者叫做变量的“引用”

'''if语句'''
# ●标准的if条件语句语法为如下，
# ●如果表达式的值非0或者为布尔值True,则执行do.something,否则执行下一条语句.
# if expression:
#    do_something1
#    do_something2
# next_something
# ●Python也支持else语句
# if expression:
#   do_something1
# else:
#   do_something2
# ●Python里还有神奇的的elif(意思是else-if)
# if expression1:
#   do_something1
# elif expression2:
#   do_something2
# else:
#   do.something3

if False:
    print('yes' )
else:
    print('bcbx' )
print('no' )

'''条件表达式'''
x, y, smaller= 3, 4, 0
if x<y:
    smaller = x
else:
    smaller=y
#上面这一段代码, 用条件表达式写作
smaller=x if x<y else y

# num= int (input('请输入你的成绩(整数):' ))
# if num>85 and num<=100:
#     print('你的成绩是优秀')
# elif num<=85 and num>70:
#     print('你的成绩是良好')
# elif num>=60 and num<=70:
#     print('你的成绩是及格')
# else:
#     print('你的成绩是不及格')

'''while循环'''
#while循环语句和if语句语法类似。只要表达式的值非0或者为True,就会循环执行do_something
# while expression:
#     do_something
#循环执行三次print
counter = 0
while counter < 3:
    print ('loop %d' %counter)
    counter += 1
n=1
while n<10:
    print('test' , n)
    n+= 1

'''for循环'''
# ●Python中的for循环和传统的for循环不太一样.
# ●for循环接收可迭代对象(序列或者迭代器)作为参数每次迭代其中的一个元素
#遍历字符串中的每一个字符
a= 'test'
for c in a:
    print (c)
#执行结果
# t
# e
# s
# t
#遍历列表中的每一个元素
a=[1,2,3,4]
for item in a:
    print (item)
#执行结果
# 1
# 2
# 3
# 4

#遍历字典中的所有key-value
a = {'ip':'192.168.1.1', 'port' :80}
for key in a:
    print (key, a[key])
#执行结果
# ip 192.168.1.1
# port 80
#内建函数range能够生成一个数字组成的列表，方便进行for循环遍历
zidian ={'name' :'manba' ,'age' :18}
for n in zidian:
    print (n)
for n in zidian.keys():
    print (n)
for n in zidian.values():
    print (n)
for key, value in zidian.items():
    print (key, value)

'''和循环搭配的else'''
#else不光可以和if搭伙 还能和while, for搭伙,
#实现一个函数，从列表中查找指定元素，返回下标.
def Find(input_list, x):
    for i in range(0, len(input_list)):
        if input_list[i] == x:
            return i
        else:
            return None
a=Find([1,2,3,5],4)
print(a)

'''内建函数range'''
#内建函数range能够生成一 个数字组成的列表方便进行for循环遍历.
# for循环执行三次打印
for i in range(0, 3):   #前闭后开
  print ('num%d' %i)
#执行结果
# num 0
# num 1
# num 2
# range函数其实有3三个参数.前两个参数分别表示了一个前闭后开的区间.第三个参数表示step,每次
# 迭代的步长
#遍历[0, 100)区间中的偶数
for i in range(0, 100, 2):
  print (i)

'''常用内置函数/模块'''
# abs:求一个数的绝对值.
# divmod: 返回一个元组，同时计算商和余数
a=10
b=-10
print(abs(a))
print(abs(b))
#执行结果
# 10
# 10
a, b = divmod(10,3)
print (a, b)
#执行结果
# 3 1

#str:将数字转换成字符串.int list dict
#round:对浮点数进行四舍五入。round有两个参数
#第一个是要进行运算的值,第二个是保留小数点后多少位 round（2.336，2）
import math
for i in range(0, 10):
    print ( round(math.pi, i) )
#执行结果
# 3.0
# 3.1
# 3.14
# 3.142
# 3.1416
# 3.14159
# 3.141593
# 3.1415927
# 3.14159265
# 3.141592654

'''Break、continue和pass'''
###使用break语句跳出当前循环;
#查找[1, 100)第一个3的倍数
for i in range(1, 100):
    if i%3== 0:
        print(i)
        break
###使用continue语句, 回到循环顶端,判定循环条件;
#循环条件满足,则执行下一次循环;
#打印[1, 100)所有3的倍数
for i in range(1, 100):
    if i%3 !=0:
        continue
    print (i)
    break
#pass语句,有时候需要用到 空语句 这样的概念什么都不做.由于没有{},需要有一个
#专门的语句来占位要不缩进就混乱了.
if x%2 ==0:
  pass

'''生成列表'''
#使用for循环将生成的值放在一个列表中
#生成[0, 4)的数字的平方列表
squared = [x ** 2 for x in range(4)]
print (squared)
#执行结果
# [0, 1, 4, 9]
#这个过程还可以搭配使用if语句
#获取[0, 8)区间中的所有的奇数
evens = [x for x in range(0, 8) if x%2==1]
print (evens)

#squared = [x ** 2 for x in range(2, 7)]
squared=[]
for x in range(2, 7):
    squared.append(x**2)
print (squared)

'''函数'''
#一些可以被重复使用的代码,可以提取出来放到函数中.
#Python使用def来定义一个函数. 使用return来返回结果.
def Add(x, y):
    return x+ y
#调用函数
print (Add(1, 2))
#理解"形参"和“实参":形参相当于数学中"末知数”这样的概念,实参就是给末知数确定具体的数值
#Python中相同名字的函数,后面的会覆盖前面的.
def Func():
    print ( 'aaaa' )
def Func():
    print ( 'bbb' )
Func()
#执行结果 bbbb

def yunsuan(x, y):
    money=x-5000-y
    return money

def shui (money=5000):
    if money<=3000:
        shui_price=money*0.03
    elif money<=10000:
        shui_price=money*0.1-231
    return shui_price
nashuiprice=yunsuan (9000, 1500)
shui_my = shui (nashuiprice)
print(shui_my)

#Python支持默认参数 函数的参数可以具备默认值.
def Func(debug=True):
  if debug:
    print ('in debug mode' )
  else:
    print ('done')
Func()
Func(False)
#Python解包(unpack)语法,函数返回多个值.
def GetPoint():
    return 100, 200
x, y= GetPoint()
#假如我只关注y,不想关注x可以使用_作为占位符.
# _, y=GetPoint()

def dayitong(x, y):
    money=x-5000-y
    if money <= 3000:
        shui_price=money*0.03
    elif money<=10000:
        shui_price=money*0.1-231
    return money, shui_price
a,b = dayitong(10000, 1000)
print(a)
print (b)

def show_names(*names):      # *一星元组
    for name in names:
        print('名字是:'+name)

show_names('manba','zengjun','fzq','123')

def show_my_info(**infos):   # ** 两星字典
    '''展示信息'''
    print (infos)
    for k,v in infos.items():
        print('我的{}是: {}. '.format(k, v))
show_my_info(name='manba', age=18, weight='90kg',sex='男')
print(show_my_info.__doc__)
help(show_my_info)

'''作用域'''
#Python中, def, class(我们后面会讲),会改变变量的作用域
#if, else, elif, while, for, try (我们后面会讲)不会改变变量的作用域
for i in range(0, 10):
    print (i)
print(i)  #即使出了for循环语句块,变量i仍然能访问到i变量.

def func():
    x=1
    print (x)
print(x)  #出了def的函数语句块,就不再能访问到x变量了.

'''文档字符串'''
#写注释对于提升程序的可读性有很大的帮助.前面我们介绍了#来表示单行注释.
#对于多行注释,我们可以使用 三引号('''/''')在函数/类开始位置表示.这个东西也被称为文档字符串
def Add(x, y):
    '''define function for add two number'''
    return x + y
#使用对象的doc属性就能看到这个帮助文档了(别忘了,函数也是对象).
print (Add.__doc__)
#执行结果
#define function for add two num
#或者使用内建函数help也可以做到同样的效果.
help(Add)
#执行结果
#define function for add two num
#文档字符串一定要放在函数/类的开始位置.否则就无法使用__doc__ 或者 help来访问了.


'''文件操作'''
#使用内建函数open打开 一个文件
# handle = open(file_name, 'r')

#file_name是文件的名字.可以是一个绝对路径,也可以是相对路径.
# handle = open('test.txt','r')

#或者
# handle = open(r'E:\aT\tester\test.txt,'r'')
#第二个位置是文件的打开方式.选项有以下几种：
# 'r' :只读
# 'w' :覆盖写
# 'a' :追加写

# handle是一个文件句柄,是一个可迭代的对象.可以直接使用for循环按行读取文件内容.
# for line in handle:
#     print (line)
#handle使用完毕，需要close掉.否则会引起资源泄露(一个进程能打开的句柄数目是有限的).
# handle.close()
read_test=open('test.txt','r',encoding='utf-8')
for line in read_test:
    print(line.strip()) #print(line,end='')

'''读文件'''
# read:读指定长度字节数的数据,返回一个字符串(不是很常用).
# readline:读取一行数据，返回一个字符串，
# readlines:读取整个文件,返回一个列表.列表中的每一项是一个字符串,代表了一行的内容.
# 直接使用for line in f 的方式循环遍历每一行. 功能和readline类似, 一次只读一行，
# 相比于readlines占用内存少.
# f = open('test.txt', 'r')
#     print (f.readlines())
# 注意readline或者readlines这些函数仍然会保留换行符.所以我们往往需要写这样的代码来去掉换行符.
# for line in f.readlines():
#     print (line.strip())
# #或者
# data = [line.strip() for line in f.readlines()]
read_test=open('test.txt','r',encoding='utf-8')
print(read_test.read(6))
print(read_test.readline())
print(read_test.readlines())
read_test.close()

# write_to_file = open('menba02.txt,'w',encoding='utf-8' )
# for n in range(1, 10):
#    write_to_file.write('199%d年七夕快乐\n'%n)
with open('manba02.txt','a',encoding=' utf-8') as write_to_file:
    for n in range(1, 10):
        write_to_file.write('199%d年七夕快乐\n' %n)


'''认识异常'''
# 在我们前面经常提到"程序运行出错"这样的概念实际上,这是Python解释器抛出了一个异常
# 异常的基本概念
# 我们故意将print敲错,解释器抛出了一个 SyntaxError异常
# >> print (hello world")
# File "<input>", line 1|
# I
# print (hello world')
# SyntaxError: invalid syntax

# ● 我们故意访问-一个下标越界的列表,解释器抛出了-一个IndexError异常
# a = [1,2，3]
# print (a[100])
# #执行结果
# Traceback (most recent call last): File "test.py", line 4，in <module>
# print (a[100])
# IndexError: list index out of range
# ●我们故意打开一一个不存在的文件,解释器抛出一一个FileNotFoundError异常
# f = open('aaaaaaaaaaaaaaa.txt')
# #执行结果
# Traceback (most recent call last): File "test.py", line 3，in <module>
# f = open('aaaaaaaaaaaaaa.txt')
# FileNotFoundError: [Errno 2] No such file or directory: ' aaaaaaaaaaaaaa. txt '

'''处理异常'''
# 我们使用try 语句来捕捉异常(可能触发异常的代码放到try中).使用except来具体处理异常.如果
# 异常能够被except捕捉到,则不会影响程序继续执行.
# IndexError, e相当于捕捉到的这个异常对象的名字为e.这个异常对象中包含了异常的具体信息.
# a =[1, 2，3]
# try:
#   print (a[100]) .
#   print ('hello1')
# except IndexError as e :
#   print (type(e))
#   print (e)
# print ('hello')
# #执行结果
# <class 'IndexError'>
# list index out of range
# hello

print('hello python' )
print('我是曼巴')
# try:
#     open_not_eist_file = open('manba008.txt' ,'r' )
# except FileNotFoundError:
#     print('打开文件出错')
try:
    #open_not_eist_file = open('manba008.txt', 'r')
    #list=[1,2,'test']
    #print(list[9])
    print(namce)
except FileNotFoundError as error:
    print(id(error),error,type(error))
    print('打开文件出错')
    with open('error.txt','a',encoding='utf-8') as errors:
        errors.write('打开文件出错\n')
except IndexError:
    print('列表索引超出范围')
    with open('error.txt', 'a', encoding='utf-8') as errors:
        errors.write('列表索引超出范围\n')
except NameError:
    print('变量没有赋值')
    with open('error.txt', 'a', encoding='utf-8') as errors:
        errors.write('变量没有赋值\n')


except Exception:
    print('出错了')


except:
    print('911-926出错了')
print('我是小尾巴')

'''模块'''
# Python模块初识
# 当代码量比较大的时候,我们最好把代码拆分成-些有组织的代码片段.
# 每个代码片段里面包含-组逻辑上有关联的函数或者类.
# 每一个片段里放在一个独立的文件中. 这样的片段就称为模块(module)
# 使用import可以在一个Python文件中引入其他的模块.
# Import os
# print type(os)
# I
# print id(os)
# #执行结果
# <class 'module'>
# 39920328

'''模块导入'''
# 记住,既然模块也是一个对象，那么也可以给这个对象赋值(相当于定义别名).
# import os.path
# p = os.path
# print (p.exists('test.py'))
# 实际上使用import-as可以更方便的完成这个动作
# import os.path as p
# print p.exists('test.py')
# #这样可以一定程度上简化我们的代码(敲-个字符p肯定比敲--串字符os.path要方便).
# from import语句
# import语句是直接导入一个模块而有时候我们只需要用到模块中的某-个或几个函数
# 就可以使用from-import
# from os.path import exists
# print (exists('test.py'))
# #这个时候不需要敲os.path了.

'''特殊标识符'''
# Python使用下划线( )作为变量的前缀和后缀来表示特殊的标识符.
# _xxx_表示一个“私有变量",使用from module import * 无法导入.
# # add.py
# def_Add(x, y):
#  return x+ y
# # test.py
# from add import *
# _Add(1, 2)
# #执行结果
# Traceback (most recent call last): File "test.py", line 3, in <module>
# _Add(1, 2)
# NameError: name ' Add' is not defined
# _xxx_ (前后-个下划线),__xxx__ (前后两个下划线)一般是系统定义的名字.我们自己在给变量命名时要
# 避开这种风格.防止和系统变量冲突.

'''模块导入'''
# 导入模块意味着 "被执行”
# #我们此处有两个Python文件: test.py和add.py
# # add.py
# print ( 'hello' )
# # test.py
# import add
# #执行结果
# hello
#
# 这往往不是我们期望的结果(此如导入模块是打印了一些奇怪的日志)，
# 我们只是想使用模块中的一些函数和变量
# 因此往往我们在实现一个模块时,只将函数定义/类定义放到顶层代码中.

'''理解"导入"和"加载" '''
# 我们写import module时，其实有两个大的阶段,先将这个模块的文件加载到内存中，并创建一个对象
# 来表示;然后通过一个变量名来将这个模块引入到当前的命名空间中.
# 如果同一个模块(例如sys这样的常用模块)被import了多次其实加载动作只进行了一次(也就是说内
# 存中只有一份sys的代码), 执行动作也只进行了一次.
# # add.py
# print( 'hello')
# # test.py
# import add
# import add
# #执行结果
# Hello
# import importlib
# import test21_second
# importlib.reload(test21_second)

'''包(Package)'''
# 当我们代码量进一步变大时, 光拆分成多个文件已经不足以满足需求还需要能按照-定的目录结构
# 层次化的组织这些模块.同时包也可以解决模块之间的名字冲突问题.
# 例如我们以下面的方式组织代码结构:
# test.py
# bao_package/
#     add.py
#     divide.py
#     _init_.py
#
# 在bao_package目录中增加一个_init_.Py 文件, bao.package这个目录就成了包(Package).
# 可以在test.py中import bao_package中的模块了.
# import bao_package.add
# print (bao_package.add.Add(1, 1))
# _init_.py 是在包加载的时候会进行执行，负责一些包的初始化操作.一般是空文件即可.

'''类'''
# 抽象
# 抽象是指对现实世界问题和实体的本质表现行为,特征进行建模;抽象的反义词是"具体”
# 抽象的本质是抓住我们重点关注的主体而忽略-些我们不需要关注的细节;
# 写程序也是-样,我们不可能把一个现实事物所有的信息都在程序中表示出来 而是只表示我们需
# 要用到的.
#
# 类和实例
# 类是施工图纸里面有房子的重要信息(户型,面积，朝向,层高等等).
# 实例是造好的房子，房子造好了,才能住进去,才能娶到媳妇.如果房子烂尾了,美好生活就只是在
# YY~
# 通过同- -张图纸可以建造出N个相同格局的房子，那么这N个实例就都是属于同一个类

'''创建类和实例化类'''
#创建一个新的类
class Tester():
    '我的第一个类'
    a ='tester'
    def test(self):
        return 'hello tester'
#实例化类
x= Tester()
#访问类的属性和方法
print("Tester类的属性a为:",x.a)
print("MyClass类的方法test输出为: ", x.test())
#执行结果
# Tester类的属性a为: tester
# MyClass类的方法test输出为:  hello tester

class My_first_class():
    kaifangshang='中海'
    def house_price(self):
        print('房屋均价2万')

zengjun= My_first_class()
print(zengjun.kaifangshang)
zengjun.house_price()

guoxu = My_first_class()
print (guoxu.kaifangshang)
guoxu.house_price()

'''类的特殊方法'''
#类有一个名为__init__()的特殊方法(构造方法) ,该方法在类实例化时会自动调用。
def __init__(self,a):
    self.data=a
class introduce():
    def __init__(self,yourname,yourage):
        self.name=yourname
        self.age=yourage
me=introduce('manba',18)
print('我的名字叫:',me.name)
print('我的年龄是',me.age)
#执行结果
#我的名字叫:manba
#我的年龄是 18



zidian ={'name' :'manba' ,'age' :18}
for n in zidian:
    print (n)
for n in zidian.keys():
    print (n)
for n in zidian.values():
    print (n)
for key, value in zidian.items():
    print (key, value)
print(list(zidian))
print(list(zidian.keys()))