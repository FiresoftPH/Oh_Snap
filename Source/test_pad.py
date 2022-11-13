test_var = 0

def changeVar(value):
    test_var = value
    return test_var

for x in range(10):
    changeVar(x)
    print(test_var)