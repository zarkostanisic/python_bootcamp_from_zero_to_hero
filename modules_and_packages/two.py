import python_bootcamp_from_zero_to_hero.modules_and_packages.one as one

print("TOP LEVEL IN TWO.PY")

one.func()

if __name__ == "__main__":
    print("TWO.PY is being run directly!")
else:
    print("TWO.PY has been imported!")