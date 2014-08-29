import json

f = open('moves.json','r')
data = f.read()

content = json.dumps(data)
moves = json.loads(content)

#print(moves)
moves_items = moves[0]
print(moves_items)
'''
for move in moves_items:
    print(move['details'])
    i = 0
    for detail in move['details']:
        
        print(detail)
        i = i + 1
'''