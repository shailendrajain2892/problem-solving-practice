def lcs(n):
    final_subs=[]
    for idx,i in enumerate(n):
        subs=[i,]
        starting=i
        for j in n[idx:]:
            if j > starting:
                subs.append(j)
        final_subs.append(subs)
    return final_subs

print(lcs([10,9,2,5,3,7,101,18,19,20]))
