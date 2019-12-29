import random

def quick_sort(arr):
    if len(arr) < 2:
        return arr

    #pick a random number from current list
    compared_number = random.choice(arr)
    
    less = [i for i in arr if i < compared_number]
    greater = [i for i in arr if i > compared_number]

    return quick_sort(less) + [compared_number] + quick_sort(greater)
    
def main():
    arr = [7,4,6,5,2,3]
    print(quick_sort(arr))
       
if __name__ == '__main__':
    main()

main()
