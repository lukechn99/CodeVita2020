# an employer is distributing gifts to employees
# each employ receives at least one gift and employees
# are denoted a level of importance, most important 
# employees must receive more gifts than their 
# adjacent employees
#
# example input
# 2                 # of cases
# 6                 case 1: # of employees
# 1 2 3 2 3 1       case 1: employees
# 4                 case 2: # of employees
# 1 2 1 2           case 2: employees
#
# example output
# 10                case 1: because [1, 2, 3, 1, 2, 1]
# 6                 case 2: because [1, 2, 1, 2]

# current minimum
# assign the first employee 1 gift
# if the next employee is more important, give 2
# keep track of least important
