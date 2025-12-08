#URL

url=input().strip()

query=url.split('?')[1]

parameter=query.split('&')

for i in parameter:
    key,value=i.split('=')
    print(f"{key}: {value}")