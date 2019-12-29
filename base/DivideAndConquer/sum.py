def sumArray(arr: []):
    if len(arr) == 1:
       return arr[0] 
    else:
       return arr[0] + sumArray(arr[1:])

def main():
    sumResult = sumArray([1,2,10])
    print(sumResult)
    
if __name__ == "__main__":
    main()

main()

   


