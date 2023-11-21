#=========#
#METHOD 1#
#========#

house_rent= 1000000
# #print(type(house_rent))
good_credit=True
# put=(house_rent*10)/100;
# give=(house_rent*20)/100;

# if(good_credit==True):
#     print("The price of the house is "+ str(put))
# else:print("The price of the house is "+ str(give))

# print("On the way to get your new home")


#=========#
#METHOD 2#
#========#
if(good_credit==True):
    down_payment=.1*house_rent
else:
     down_payment=.2*house_rent
print(f"On the way to get your new home...\nDown Payment: ${down_payment}")
    
