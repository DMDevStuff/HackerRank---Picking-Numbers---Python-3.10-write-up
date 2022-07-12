##    https://www.hackerrank.com/challenges/picking-numbers/problem

##    Given an array of integers, find the longest subarray where the absolute
##    difference between any two elements is less than or equal to 1.

##### ##### ##### #####

#   O(n)
#   n is the number of elements in a
#   Even though subarrays are brought up in the problem statment,
#   the key to solving this problem easily and efficiently does not
#   involve actually generating any subarrays.

#   Algo:
#       1. Initiate a dictionary that will be used to store integers as keys
#           and the number of times they occur as the value pair. => O(1)
#       2. Initiate a variable that will be used to store the
#           'longest subarray found'. => O(1)
#       3. Iterate over array a.  For each element check for its existence in
#           our initiated dictionary.  Increment value or create key as needed. => O(n)
#       4. Iterate over initiated dictionary.  For each key, look for key+1.  If it exists,
#           sum the values and check if this sum is greater than our
#           'longest subarray found' value.  If it is, assign the new value. => O(n)
#       5. Return 'longest subarray found' => O(1)

def pickingNumbers(a):
    
    occurrence_table = dict()
    longest_subarray_found = 0
    
    for integer in a:
        
        try:
            occurrence_table[integer] += 1
            
        except:
            occurrence_table[integer] = 1
            
    for integer in occurrence_table:
        
        try:
            current_subarray = occurrence_table[integer] + occurrence_table[integer+1]
            
        except:
            current_subarray = occurrence_table[integer]
            
        if current_subarray > longest_subarray_found:
            
            longest_subarray_found = current_subarray
            
    return longest_subarray_found
