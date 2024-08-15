def currySoma(a):
    def somar_b(b):
        def somar_c(c):
            return a + b + c
        return somar_c
    return somar_b

print(currySoma(1)(2)(3))