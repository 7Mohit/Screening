"""
Decorators are used to modify the behaviour of another function.
They enable the programmer to wrap an additional functionality 
without modifying the real definition of the function.
In below example: The decorator even checks if all numbers in a list are even.
When added to function calculate_sum(), it modifies the behaviour of function
to calculate sum of list only if all values are even
"""

def even(func):
    """Check if all numbers in list are even"""
    def check_even(num_list):
        for i in num_list:
            if i%2 != 0:
                print("The list contains an odd value")
                return
        return func(num_list)
    return check_even

@even
def calculate_sum(num_list):
    """Calculate the sum of input list"""
    print(f'Sum of list:{sum(num_list)}')

if __name__=='__main__':
    print('Input the numbers space separated to calculate sum:')
    x = [ int(i) for i in input().split()]
    calculate_sum(x)

