#1.提醒用户输入自己的英文名字，然后保存到字典中（以name为key）,将用户输入的英文名字翻转，继续保存到刚才的字典中
# （以new_name为key）将字典中用户的正常的英文姓名赋值给变量real_name,告知客户“您的英文名字是：” + 变量,“您
#  的英文名字翻转是：” + 字典里获取
# Englishname=input('请输入你的英文名字：')
# zidian={'name':Englishname}
# zidian['new_name']=Englishname[::-1]
# real_name=Englishname
# print('您的英文名字是：'+real_name+','+'您的英文名字的翻转是:'+zidian['new_name'])

# a=input('请输入您的英文名字：')
# zd={'name':a,'new_name':a[::-1]}
# print('您的英文名字是：'+zd['name']+','+'您的英文名字的翻转是:'+zd['new_name'])

#2.提醒用户依次输入数学、语文、英语、综合四门的成绩，按照输入的成绩排序，告诉用户“您的最高的一门成绩
# 是：”xx （不用告诉用户是哪一科）
# score=input('请依此输入数学、语文、英语、综合四门的成绩:')
# scores=score.split(' ')
# cj=sorted(scores)
# print('您的最高的一门成绩是：'+cj[-1])

#3.使用input让用户依次输入两个数字, 计算两个数字的和并显示.
# num=input('请依此输入两个数字')
# nums=num.split(' ')
# #print(nums)
# sum=int(nums[0])+int(nums[1])
# #print(sum)
# print('求和：%d'%sum)

#4.用python输出九九乘法表
for i in range(1,10):
   for n  in range(1,i+1):
     print('%d*%d=%d\t'%(n,i,n*i),end='')
   print()

#5.打印时间
import datetime
nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在
pastTime = (datetime.datetime.now()-datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')#过去一小时时间
afterTomorrowTime = (datetime.datetime.now()+datetime.timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S')#后天
tomorrowTime = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')#明天
print('\n',nowTime,'\n',pastTime,'\n',afterTomorrowTime,'\n',tomorrowTime)
