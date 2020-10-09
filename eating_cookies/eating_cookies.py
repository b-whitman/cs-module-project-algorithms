'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    if n == 0:
        return 1

    arr = [1,2,4]
    i = 3
    while len(arr) <= n:
        arr.append(arr[i-3]+arr[i-2]+arr[i-1])
        i += 1

    return arr[n-1]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 500

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
