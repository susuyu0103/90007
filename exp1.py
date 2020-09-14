print('解一元二次方程式')
a = int(input('輸入 a: '))
b = int(input('輸入 b: '))
c = int(input('輸入 c: ')) 
d = (b**2) - (4*a*c) 

x = int(-b-d**0.5)/(2*a)
y = int(-b+ d**0.5)/(2*a) 
print('一元二次方程式解為',x,y)
