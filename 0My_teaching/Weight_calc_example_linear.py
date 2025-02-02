import numpy as np 
import matplotlib.pyplot as plt

#function to fit
x=np.arange(1,11) #input x=[1,2,...10]
y=2.*x	#output

#learning rate
alpha=0.01

#criteria for cost function J
J_CRIT=0.01

#def cost function
def J_calc(a,y):
	J=0.5*np.mean( (a-y)**2. ) #Mean Squared Error
	return J

#Step 1: Initate w (weight), b (bias)
w=1
b=0

g=1 #linear activation function

J=100
w_list=[w]
b_list=[b]

while J>J_CRIT:
	#Step 2: Propage 
	a2=g*(w*x+b)

	#Step 3: calculate cost function
	J=J_calc(a2,y)

	#Step 4: calculate the gradient
	#4.1.1 dJ_dw=dJ/dw
	dJ_dw=np.mean((a2-y)*x)
	#4.1.2 dw=-alpha*(dJ/dw)
	dw=-alpha*dJ_dw

	#4.2.1 dJ_db=dJ/db
	dJ_db=np.mean(a2-y)
	#4.2.2 db=-alpha*(dJ/db)
	db=-alpha*dJ_db

	#4.3 update w and b
	w=w+dw
	b=b+db 

	w_list.append(w)
	b_list.append(b)
print('w_list: ')
print(w_list)
print('b_list: ')
print(b_list)

x=np.arange(0,11,1) #include 0 to plotting

plt.clf()
for (w,b) in zip(w_list,b_list):
	plt.plot(x,w*x+b,color='blue',alpha=0.3)
plt.plot(x,w_list[-1]*x+b_list[-1],color='blue',label='final fit')
plt.scatter(x,2*x,color='red',label='data')
plt.grid(alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0,10)
plt.ylim(0,20)
plt.legend()
plt.show()