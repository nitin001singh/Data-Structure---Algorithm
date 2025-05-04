import math
def gradingStudents(grades):
    output = []
    for grade in grades:

        maxLimit = math.ceil(grade / 5) * 5
        difference = maxLimit - grade
        # print(difference)
        if grade < 38:
            output.append(grade)
        else:
            if difference < 3:
                output.append(maxLimit)
            else:
                output.append(grade)
        
    for val in output:
        print(val, end="\n")
    
    # return output

res = gradingStudents([73,67,38,33])
# print(res)