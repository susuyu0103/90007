list1 = score = ['小徐',5,9,6,8,7,10,6]
a=list1[0]
b=max(list1[1:7])
print(a,'最多進了',b,'球')
c=min(list1[1:7])
print(a,'最少進了',c,'球')
d=sorted(list1[1:7][-3:])
print(a,'進球數最多的三回合各投入',d,'球')
e=sorted(list1[1:7][0:3])
print(a,'進球數最少的三回合各投入',e,'球')
f=sum(list1[1:7])/len(list1[1:7])
print(a,'的進球平均球數',f,'球')


# for i in range(1,10):
#     for j in range(1,10):
#         print('%d*%d=%2d' % (i,j,i*j),end=' ')
#     print() 

# import random
# a=random.randint(1,1000)
# b='I love you'
# c='much'
# print(b,end='')
# for i in range(a):
#     print(' so',end='')
# print(' ',c) 
# print('隨機數:',a)