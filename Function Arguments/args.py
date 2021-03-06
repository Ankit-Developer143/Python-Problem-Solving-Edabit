def function(named_arg, *args):
   print(named_arg)
   print(args)

function(1, 2, 3, 4, 5)


""" 
op:-
1
(2, 3, 4, 5)
 """
 
 
 
 
 
#  Tuple Unpacking

# A variable that is prefaced with an asterisk (*) takes all values from the iterable that are left over from the other variables.
# Example:
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

""" 
op:-
1
2
[3, 4, 5, 6, 7, 8]
9

 """