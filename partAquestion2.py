die_a=[1,2,3,4,5,6] 
die_b=[1,2,3,4,5,6]
print("\nDistribution of all possible combinations\n")
for i in die_a:
    for j in die_b:
        print("("+str(i)+","+str(j)+")",end=" ")
    print()