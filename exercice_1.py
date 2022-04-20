def get_indexes(my_list, value_to_get):
    indexes=[]
    for i in range(0,len(my_list)):
        if my_list[i]==value_to_get:
           indexes.append(i)
    
    print(indexes)
      
my_list=[1,2,3,4,5,1]

get_indexes(my_list,1)
