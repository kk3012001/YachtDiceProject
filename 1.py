class A:
    q = 1
    w = 2
    def a():
        A.q = 2
    def b():
        A.q = 1
        
class B:
    def a():
        A.q =4

A.a()
print(A.q)
B.a()
print(A.q)
        