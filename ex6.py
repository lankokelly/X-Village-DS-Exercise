import json

with open( 'ptt_0726_s.json', 'r' , encoding='utf-8-sig' ) as f:

    data = json.load(f) #list
    Null_Dict = {}
    s = 'h_推文總數'

    def get_key(d):
        if (d[s] == Null_Dict):
            d[s].update({"all":0})
            return d[s]['all']
        else:
            return d[s]['all']
    data.sort(key = get_key , reverse=True) 
    print(data)
