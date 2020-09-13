"""searching an array
jagadeeshvarma 
121910313026"""
def search(list,m):
    for i in range(0,len(list)):
        if(list[i]==m):
            print(m,"is found in",i,"th index")
            break
k=int(input("size of array:"))
list=[]
for i in range(0,k):
    ap=int(input("array elements:"))
    list.append(ap)
m=int(input("element to search:"))   
search(list,m)
