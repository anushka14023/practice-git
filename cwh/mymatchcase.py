x =4                
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 1:
        print(x,"case is 1")
    # case with if-condition
    case 2:
        print(x,"case is 2")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x,"ji")

  
