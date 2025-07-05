# Scope Example
x = "global"  # Global variable

def outer():
    x = "enclosed"  # Enclosed scope

    def inner():
        x = "local"  # Local scope
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()
print("Global:", x)
