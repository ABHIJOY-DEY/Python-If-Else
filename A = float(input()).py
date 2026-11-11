A = float(input())
B = float(input())
C = float(input())

if A == B == C:
    print("The triangle is classified as Equilateral")
    
elif A == B or B == C or C == A:
    print("The triangle is classified as Isosceles")

else:
    print("The triangle is classified as Scalene")