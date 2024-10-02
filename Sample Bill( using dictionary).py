price={
    "noodles":120,
    "biriyani":140,
    "porotta with beef combo": 180,
    "meals":80
}
quantity={
     "noodles":2,
     "biriyani":2,
     "porotta combo": 3,
     "meals":2
}
total=0
for i in price:
    total=total+(price[i]*quantity[i])
    
print("the bill is :",total)
