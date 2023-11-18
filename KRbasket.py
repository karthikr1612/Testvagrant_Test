basket = []
discountitems = []
wdprices = []
prices=[]
newlist = []
newvalue = []
basket[0] = ["leather wallet",1100,18,1] #[name,unit price, GST, quantity]
basket[1] = ["umbrella",900,12,4]
basket[2] = ["cigarette",200,28,3]
basket[3] = ["honey",100,0,2] 

for i in range(4):
    if basket[i][1]>500:
        for j in range(4):
            if(j==2):
                newvalue[j]=basket[i][j]-5  #alternate method discountitems+=[basket[i][0],basket[i][1]-5,[basket[i][2],[basket[i][3]] 
            else:
                newvalue[j]=basket[i][j]
            
        discountitems+= newvalue
    else:
        discountitems+= []
for i in range(4):
    wdprices[i] = (basket[i][1]*basket[i][3])*(basket[i][2]/100)

for i in range(4):
    if basket[i] == discountitems[i]:
        newlist+=discountitems[i]
    else:
        newlist+=basket[i]

for i in range(4):
    prices[i] = (newlist[i][1]*newlist[i][3])*(newlist[i][2]/100)

totalprice = prices.sum()
highestamount = max(wdprices)
for i in range(4):
    if wdprices[i] == highestamount:
        indexi = i

print("The product for which the customer paid maximum GST amount is: %s",basket[indexi][0])
print("The total amount to be paid is: %f",totalprice)

        