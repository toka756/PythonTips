def merge_sort(arr):

    length = len(arr)

    if length == 1:
        return
    
    #divide arr first
    q, r = divmod(length, 2)
    left = arr[: (q + r)]
    right = arr[-(q) :]
    print("left divided", left)
    print("right divided", right)
    arr.clear()
  
    #divide until only 1 number in list
    merge_sort(left)
    merge_sort(right)

    #onquer: merge 
    print("Begin to merge: left: %s right: %s" % (left, right))
    while left and right:
        if left[0] <= right[0]:
            arr.append(left[0])
            del left[0]
        else:
            arr.append(right[0])
            del right[0]
        print("Merged left and right: %s, left: %s, right: %s" % (arr, left, right))
    while left:
        arr.append(left[0])
        del left[0]
        print("Merged only left: %s, left: %s" % (arr, left))
    while right:
        arr.append(right[0])
        del right[0]
        print("Merged only right: %s, right: %s" % (arr, right))
       
if __name__ == '__main__':
    main()

main()

def main():
    arr = [7,4,6,5,2,3]
    merge_sort(arr)
    print(arr)

    
    
    
    
