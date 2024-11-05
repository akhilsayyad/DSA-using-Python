# def Bubblesort(data_list):
#     for r in range(1,len(data_list)):
#         for i in range(0,len(data_list)-r):
#             if data_list[i]>data_list[i+1]:
#                 data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
# listt=[19,12,13,10,15,18,11,14,17,16,20]

# Bubblesort(listt)
# print(listt)




def bubblesort(list1):
    for r in range(1,len(list1)):
        for i in range(0,len(list1)-r):
            if list1[i]>list1[i+1]:
                list1[i],list1[i+1]=list1[i+1],list1[i]
    return list1
print(bubblesort([16,12,11,14,15,13]))