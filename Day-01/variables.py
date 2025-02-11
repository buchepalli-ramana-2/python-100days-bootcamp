
#Swap the below variable values using three line code
glass1 = "milk"
glass2 = "juice"

print("Before swap")
print("glass1: ",glass1 +"\n"+ "glass2: ",glass2 +"\n")

switch = glass1
glass1 = glass2
glass2 = switch

#print(glass1,glass2)

glass1 = glass1 + glass2
#print(len(glass1))
glass2=glass1[len(glass2)+1:len(glass1)]
#print(glass2)
glass1=glass1[:-len(glass2)]
print("After swap")
print("glass1: ",glass1 +"\n"+ "glass2: ",glass2)