#
import pandas as pd
#
# products=['apple','bananas','oranges','grapes','pineaples']
#
# sales=[15,20,18,9,6]
#
# sales_siries=pd.Siries(sales,index=products)
# print(sales_siries)
#
# print(sales_siries['grapes'])
#
# total_sales=sales_siries.sum()
# print(total_sales)
#
# best_sell=sales_siries.idxmax()
# print(best_sell)

data={
    'name':['alice','bob','charlie']
    'age':[23,30,22]
    'city':['new york','berlin','vien']
}

df=pd.DataFrame(data)
print(df)