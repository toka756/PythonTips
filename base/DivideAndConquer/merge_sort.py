def merge_sort(arr):

    length = len(arr)
    if length == 1:
        return

    #divide arr first
    q, r = divmod(length, 2)
    left = arr[: (q + r)]
    right = arr[-q :]

    print("Divid left to: ", left)
    print("Divid right to:", right)
    arr.clear()

    #divide until only 1 number in list
    merge_sort(left)
    merge_sort(right)

    #conquer: merge
    print("Begin to merge: left: %s right: %s" % (left, right))
    while left and right:
        if left[0] <= right[0]:
            arr.append(left[0])
            del left[0]
        else:
            arr.append(right[0])
            del right[0]
            print("Merged left and right: %s, left after merge: %s, right after merge: %s" % (arr, left, right))
    while left:
        arr.append(left[0])
        del left[0]
        print("Merged left only: %s, left after merge: %s" % (arr, left))
    while right:
        arr.append(right[0])
        del right[0]
        print("Merged right only: %s, right after merge: %s" % (arr, right))

def main():
    arr = [7,4,6,5,2,3]
    merge_sort(arr)
    print(arr)
       
if __name__ == '__main__':
    main()

main()

    
    
    
    
