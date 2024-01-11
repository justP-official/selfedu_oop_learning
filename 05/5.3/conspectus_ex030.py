def func2():
    try:
        return 1 / 0
    except:
        print("func2 error")

def func1():
    try:
        return func2()
    except:
        print("func1 error")

print("Lorem")
print("Lorem")
print("Lorem")
try:
    func1()
except:
    print("func1 error")
print("Lorem")
print("Lorem")
print("Lorem")
print("Lorem")
