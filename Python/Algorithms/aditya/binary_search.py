line = input('Input line list of numeric items')

line = list(map(int,line.strip().split()))

key = int(input("Enter the key"))

def binary(line,key):
    low=0
    high=len(line)-1
    flag=0
    while(low<=high and flag==0):
        mid=(low+high)//2
        if(key==line[mid]):
            flag=1
            print("the element found at: {} ".format(mid))
            return
        else:
            if(key<line[mid]):
                high=mid-1
            else:
                low=mid+1
    print("Element not found")

binary(line,key)
    
