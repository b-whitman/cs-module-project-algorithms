'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    arr.sort()
    
    if arr[-1] != arr[-2]:
        return arr[-1]

    i = 0
    while i < len(arr):
        num = arr[i]
        next = arr[i+1]
        if num == next:
            i += 2
        else:
            return arr[i]
    
    # Original Solution

    # for i in range(len(arr))[::2]:
    #     if arr[i] == arr[-1]:
    #         return arr[i]
    #     if arr[i] == arr[i+1]:
    #         continue
    #     else:
    #         return arr[i]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
