# search_function
def search(arr, N, x):
 
    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1
 
#udayipp T-shirt function
# Driver Code below
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40, 60, 152, 200, 450]
    x = 10
    N = len(arr)
 
    # Function call
    result = search(arr, N, x)
    if(result == -1):
        print("Element is not present in array :  ")
      
    else:
        print("Element is present at index : ", result)

      # End Now
