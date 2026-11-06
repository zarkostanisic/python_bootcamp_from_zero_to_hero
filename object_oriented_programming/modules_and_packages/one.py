#one.py

def func():
    print("FUNC() IN ONE.PY")

def func1():
    print("FUNC1()")

def func2():
    print("FUNC2()")

print("TOP LEVEL IN ONE.PY")

if __name__ == "__main__":

    print("ONE.PY is being run dirrectly!")

    # RUN THE SCRIPT
    func1()
    func2()
else:
    print("ONE.py has been imported!")