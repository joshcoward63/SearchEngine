import json

data = {}
data['headercontent'] = []
data['headercontent'].append({
    'name': 'some name',
    'website': 'some website',
    'from': 'some content'
})
data['headercontent'].append({
    'name': 'some name',
    'website': 'some website',
    'from': 'some content'
})
data['headercontent'].append({
    'name': 'some name',
    'website': 'some website',
    'from': 'some content'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
