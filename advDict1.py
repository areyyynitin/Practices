items = [
    {'name':'Apple','category':'fruit'},
    {'name':'banana','category':'fruit'},
    {'name':'carrot', 'category':'vegetable'},
    {'name':'broccoli','category':'vegetable'},
    {'name':'chicken','category':'meat'}
]

category_items = {
    category: [item['name'] for item in items if item['category']== category]
    for category in {item['category'] for item in items}
}
for i,j in category_items.items():
    print(i,j)