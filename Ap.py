ap = str(input("Please enter the first four terms of an AP without space or underscore: "))
wtd = input("What you want to find? nth_term, sum_of_terms, first_term, common_differnce? ")
a = int(ap[0])
d = int(ap[1]) - int(ap[0])

def first_term():
    print("The first term of the given arthmetic progression is: " + str(a))

def common_difference():
    print("The common difference of the given arthmetic progression is: " + str(d))

def nth_term():
    n = int(input("Please enter the nth term that you have to find: "))
    nth_term = a + (n - 1)*d
    print("The nth term of this arthmetic progression is: " + str(nth_term))

def sum_of_terms():
    n = int(input("Please enter the nth term that you have to find its sum: "))
    sum_of_terms = n/2*(2*a + (n-1)*d)
    print("The sum of nth term of this arthmetic progression is: " + str(sum_of_terms))

if wtd == "first_term":
    first_term()
elif wtd == "common_difference":
    common_difference()
elif wtd == "nth_term":
    nth_term()
elif wtd == "sum_of_terms":
    sum_of_terms()