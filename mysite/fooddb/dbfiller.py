import openfoodfacts

categories = openfoodfacts.facets.get_categories({
    'country':'france'
})

for category in categories:
    print(category['name'])


search_result = openfoodfacts.products.advanced_search({
  'search_terms':'Nutella',
  'country':'france',
  'language'
  "sort_by":"product_name",
  "page_size":"10",
  'pages':'1',
})

print(search_result)
print(search_result[1])
print(search_result['products'][1])
print(search_result['products'][1]['product_name'])
print(search_result['products'][1]['categories'])
print(search_result['products'][2]['categories'])
print(search_result['products'][3]['categories'])
print(search_result['products'][4]['categories'])


for item in search_result:
    print(item)

for x in search_result['products']:
    print(x)

for x in search_result['products']:
    print(x['product_name'])