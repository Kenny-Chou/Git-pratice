count_TP = 0
count_FP = 0

prescision = count_TP / (count_TP + count_FP) if (count_TP + count_FP)!= 0 else 0
print("precision=", prescision)
