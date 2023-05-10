def bubble_sorted(arr:list):
    while True:
        for i in range(0,len(arr)-1):
            count = 0
            if arr[i] > arr[i+1]:
                count += 1
                arr[i], arr[i+1] = arr[i+1], arr[i]
        if count == 0:
            break
    return arr
arr = [30,20,80,40,50,10,60,70,90]
print(bubble_sorted(arr))
#[20, 30, 40, 50, 10, 60, 70, 80, 90]
