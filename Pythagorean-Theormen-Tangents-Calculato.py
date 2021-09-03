A = int(input("What is side A? "))
C = int(input("What are you given of side C? "))
B = C - A + 1

AS = A*A
BS = B*B
C2 = B+C
CS = C2*C2
AB = AS+BS

while AB != CS:
    B = B+1
    AS = A * A
    BS = B * B
    C2 = B + C
    CS = C2 * C2
    AB = AS + BS

print("Your answer is " + str(B))