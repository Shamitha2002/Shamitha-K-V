class Calculator:
    def __init__(self, a, b, op):
        self.a=float(a)
        self.b=float(b)
        self.op=str(op).lower()

    def result(self):
        if self.op=="add":
            return self.a+self.b
        if self.op=="subtract":
            return self.a-self.b
        if self.op=="multiply":
            return self.a*self.b
        if self.op=="divide":
            return "Err: /0" if self.b==0 else self.a/self.b
        return "Invalid"

a=input("Enter number 1: ")
b=input("Enter number 2: ")
o=input("Choose Operation (add/subtract/multiply/divide): ")

print("Result:", Calculator(a, b, o).result())
