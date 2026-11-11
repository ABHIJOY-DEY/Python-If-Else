N = int(input())
sumo,sume = 0,0
for i in range(1,N+1,2):
    sumo = sumo+i
for j in range(2,N+1,2):
    sume = sume + j

print("Sum of even numbers from 1 to",N,"is",sume)
print("Sum of odd numbers from 1 to",N,"is",sumo)