die_a=[1,2,3,4,5,6] 
die_b=[1,2,3,4,5,6]
sum_of_combinations={}
x=36 
print("\nProbability of all Possible Sums\n")
for i in die_a:
    for j in die_b:
        pair="("+str(i)+","+str(j)+")"
        sum_of_pair=i+j
        sum_of_combinations[pair]=sum_of_pair
for i in range(2,13):
    count=0
    for j in sum_of_combinations:
        if sum_of_combinations[j]==i:
            count+=1
    print("P("+str(i)+") = "+str(count)+"/"+str(x)+  " = "+str(int(count)/int(x)))