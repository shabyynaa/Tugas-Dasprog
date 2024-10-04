# input Healthy Poin 
U = int(input())

# input banyaknya Knight Ibis
K = int(input())

# input banyaknya minion Ibis
M = int(input())

# calculate Attack point
AP_knight = ((K // 2) * 5) * 5
AP_minion = (M // 2) * 2
AP_raja = 1000 

attack_point = AP_knight + AP_minion + AP_raja

# calculate sisa Healthy Point 
healthy_point = U - attack_point

if healthy_point >= 0:
    print("Yey! Ucup Menang! HP tersisa:", healthy_point)

else:
    print("Yah! Ucup Meninggoy.")