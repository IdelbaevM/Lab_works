def count(input_string):
    upper=0
    lower=0
    for char in input_string:
        if char.isupper():
            upper +=1
        elif char.islower():
            lower +=1
    return upper,lower
example="I am so tired,i do not want to go to the movieS"
upper , lower=count(example)
print(f"Upper case letter number:{upper}")
print(f"Lower case letter number:{lower}")
