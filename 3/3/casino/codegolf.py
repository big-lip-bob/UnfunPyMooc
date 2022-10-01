P=int(input())
T=int(input())
print((((T!=0)&((T<11)^T^P),(T^P)&1)[P<15]*20,(T==P)*120)[P<13])