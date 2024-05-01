#typing = int(input("Son; "))

#def check(lst):
#
#    if typing in lst:
#        return True
#   else:
#        return False
#
#print(check([1, 2, 3, 4, 5]))



#def list_less_than_100(lst):
#    for x in lst:
#        if x < 100:
#            return True

#            return False
#
#print(list_less_than_100([45 + 50]))
#print(list_less_than_100([60 + 60]))
#print(list_less_than_100([20 + 30]))

def max_total(lst):
    lst.sort(reverse=True)


lst = [3, 5, 7, 4, 5, 10]
print(max_total(lst))

#print(max_total([0, 0, 0, 0, 0, 100]))
#print(max_total([1, 6, 0, 15, 8, 10]))

