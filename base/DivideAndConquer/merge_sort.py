def merge_sort(arr):

    length = len(arr)

    if length == 1:
        return
    
    #divide arr first
    q, r = divmod(length, 2)
    left = arr[: (q - r)]
    right = arr[-(q - r) :]
    print("left divided", left)
    print("right divided", right)
    arr.clear()
  
    merge_sort(left)
    merge_sort(right)

    print("Begin to merge:", left, right)
    while left and right:
        if left[0] <= right[0]:
            arr.append(left[0])
            del left[0]
        else:
            arr.append(right[0])
            del right[0]
        print("merged left and right", arr, left, right)
    while left:
        arr.append(left[0])
        del left[0]
        print("merged only left", arr, left)
    while right:
        arr.append(right[0])
        del right[0]
        print("merged only right", arr, right)
       
if __name__ == '__main__':
    main()

main()

def main():
    arr = [7,4,6,5]
    merge_sort(arr)
    print(arr)

    
    
    
    
