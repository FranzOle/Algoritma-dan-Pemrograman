jawa = {'satu': 'setunggal', 'dua': 'kalih', 'tiga': 'tiga telu', 'empat': 'sekawan'}
print(jawa['satu'])  #setunggal
print(jawa)
print(jawa['tiga'])  #tiga telu

vals = list(jawa.keys())
print(vals) 

for key in jawa:
    print(f'Key: {key}, Value: {jawa[key]}')    
    