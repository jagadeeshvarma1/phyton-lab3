#copy , remove duplicates , delete at k th index , search an item , display
def copy(listo,n):
    list2=[]
    list2=listo
    print("copied list is",list2)
def remove(list1):
    list1 = list(dict.fromkeys(list1))
    print(list1)
def delete(listo):
    k=int(input("enter an index to remove:"))
    listo.pop(k)
    print(listo)
def search(listo):
    m=int(input("enter the element to search:"))
    for i in range(0,len(listo)):
        if(listo[i]==m):
            print(m,"is found in",i,"th index")
            break
def display(listo):
    print(listo)
n=int(input("enter size of array:"))
listo=[]
for i in range(n):
    a=int(input())
    listo.append(a)
m=int(input("enter 1 to 5 to perform respective function:"))
if(m==1):
    copy(listo,n)
elif(m==2):
    remove(listo)
elif(m==3):
    delete(listo)
elif(m==4):
    search(listo)
elif(m==5):
    display(listo)
else:
    print("enter nor btwn 1 to 5")
