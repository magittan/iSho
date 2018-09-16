import json

with open('peers.json', 'r') as f:
    data = json.load(f)
    tickers = [i['id'] for i in data['nodes']]
    ticker_dict = dict(zip(tickers,[0 for i in range(len(tickers))]))
    for i in data['links']:
        ticker_dict[i['source']]+=1
    for i in data['nodes']:
        i['label'] = i['id']
        i['r'] = ticker_dict[i['id']]

with open('modified_peers.json', 'w') as g:
    json.dump(data,g)