def convert_list(items):
    if type(items)==str or type(items)==dict or type(items)==tuple or type(items)==set:
        list1=[i for i in items]
        return list1
    else:
        return None
print(convert_list((1,2,3,4,5)))
print(convert_list({1,2,3,4,5}))
print(convert_list('12345'))
print(convert_list({1:10,2:20,3:30,4:40,5:50}))
print(convert_list('50'))


