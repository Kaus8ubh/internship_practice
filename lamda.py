#square no
# square= lambda x: x**2
# print(square(2))


# list=[1,2,3,4,5,6,7,8,9]
# max=lambda x,y: x if x>y else y 
# print(max(2,12))


list1=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda x: x%2==0,list1))
print(evens)
