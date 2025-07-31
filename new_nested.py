import math

x = [[1,2,3,4,5,6], 
     [5,6,7,8,6,7],
     [9,10,11,12,7,8],
     [13,14,15,16,8,9],
     [16,17,18,19,9,10]] #14.0 24.0 34.0 44.0 111.833333333333344.0 64 


col = len(x[0])
row = len(x)


row_sum_list = []

for i in range(len(x)):
    row_sum = 0
    for j in range(len(x[i])):
        row_sum += x[i][j]
        row_sum_avg =  row_sum/len(x[0])
    print(row_sum_avg)
    row_sum_list.append(row_sum_avg)

print(row_sum_list)

total_avg = 0

for i in range(len(row_sum_list)):
    total_avg += row_sum_list[i]

print(total_avg)




for i in range(len(x)):
    for j in range(len(x[i])):
     mean_row = ((len(x[i]))/2)+1   
     round_mean = math.ceil(mean_row)
     x[i][round_mean] = total_avg
     print(f"{x[i][j]:3.2f}", end=" ")
    print()
    
    
     




# for row in x:
#      mean_row = statistics.mean(row)
#      round_mean = math.ceil(mean_row)
#      print(round_mean)

    
       

      









