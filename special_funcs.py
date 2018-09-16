import json

class GraphDB:
    nodes = {}
    def __init__(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            for link in data['links']:
                if link['source'] not in self.nodes.keys():
                    self.nodes[link['source']] = []
                if link['target'] not in self.nodes.keys():
                    self.nodes[link['target']] = []
                if link['target'] not in self.nodes.keys():
                    self.nodes[link['source']].append(link['target'])
                if link['source'] not in self.nodes.keys():
                    self.nodes[link['target']].append(link['source'])
    
    def find_greatest_degree(self):
        best = ('', 0)
        for key in nodes.keys():
            if self.nodes[key] > best[1]:
                best = (key, self.nodes[key])
        return best
    
    def find_degree(self, _id):
        return len(self.nodes[_id])

data = None
with open('peers.json', 'r') as f:
    data = json.load(f)
tickers = [i['id'] for i in data['nodes']]
ticker_dict = dict(zip(tickers,[0 for i in range(len(tickers))]))
gdb = GraphDB('peers.json')
neighbor_dict = gdb.nodes
for i in data['links']:
    ticker_dict[i['source']]+=1
for i in data['nodes']:
    i['label'] = i['id']
    i['r'] = ticker_dict[i['id']]
    i['neighbors'] = neighbor_dict[i['id']]

with open('modified_peers.json', 'w') as g:
    json.dump(data,g)