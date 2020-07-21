import yaml

file = open('search.yaml', encoding='utf-8')
testdata = yaml.load(file, Loader=yaml.FullLoader)#或者yaml.full_load()
#print(type(testdata))
print(testdata)

