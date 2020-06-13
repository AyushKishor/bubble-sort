var = []
n = int(input("Enter the number of element you would like to sort\n"))
for i in range(n):
	num = int(input("Enter a number: "))
	var.append(num)

def sort(arr):
	while True:
		corrected = False
		for i in range(len(arr)- 1):
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
				corrected = True
		if corrected == False:
			return arr		



print(sort(var))
