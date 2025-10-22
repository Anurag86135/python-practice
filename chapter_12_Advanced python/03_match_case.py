# def http_status(status): # match case
#     match status:
#         case 200:
#             return "ok"
#         case 404:
#             return "Not found"
#         case 500:
#             return "International server Error"
#         case _ :
#             return "Unknown status"
        
# print(http_status(500))

# merge dictionary

dict1={'a':1,'b':2}
dict={'b':3,'c':4}

merged =dict1|dict

print(merged)
# output : {'a': 1, 'b': 3, 'c': 4}