#1.	Write a Python Program to find sum of array?
class Assignment7:
    def sum_of_array(self):
        arr = eval(input("Enter the array"))
        sum = 0
        for i in arr:
            sum = sum +i
        return sum
    #2.	Write a Python Program to find largest element in an array?
    def LEArray(self):

        LEarr = eval(input("Enter the array"))
        n = len(LEarr)
        max = LEarr[0]
        for i in range(1,n):
            if LEarr[i]>max:
                max= LEarr[i]
        return max
    #3.	Write a Python Program for array rotation?
    def array_rotation(self):
        arrotation = eval(input("Enter the array"))
        return arrotation[::-1]

    #4.	Write a Python Program to Split the array and add the first part to the end?
    def split_array(self):
        SA = eval(input("Enter the array"))
        return SA[0]+SA[-1]
    #Write a Python Program to check if given array is Monotonic
    def checkMonotonic():
        in_arr = eval(input("Enter the Array: "))
        if (all(in_arr[i] <= in_arr[i + 1] for i in range(len(in_arr) - 1)) or all(
                in_arr[i] >= in_arr[i + 1] for i in range(len(in_arr) - 1))):
            return f'Array {in_arr} is Monotonic'
        else:
            return f'Array {in_arr} is Not Monotonic'







a = Assignment7
#a.sum_of_array
#print(a.sum_of_array(""))
#a.LEArray
#print(a.LEArray(""))
#a.array_rotation
#print(a.array_rotation(""))
#a.split_array
#print(a.split_array(""))
a.checkMonotonic
print(a.checkMonotonic())