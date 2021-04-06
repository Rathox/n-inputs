#for defining n inputs from the user
print('enter 0 to stop.\n')

def enter(x):
	list=[]
	while x:
		list.append(x)
		x=float(input())
	print(list)
	print('Shorting them we get.')
	
	while list:
		y=(min(list))
		num=[]
		while y in list:
			o=list.remove(y)
			num.append(o)
		g=len(num)
		print(y,'×',g)

b=float(input())
enter(b)
#------------------ done ---------------------------

