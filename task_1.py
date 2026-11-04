temporal_meanings = '1h 45m,360s,25m,30m 120s,2h 60s'
minuts = 0 

replaced_symbols = [','] 

for s in replaced_symbols:
    temporal_meanings = temporal_meanings.replace(s, ' ') 

meanings = temporal_meanings.split(' ')

for meaning in meanings:
    if 'h' in meaning:
        meaning = meaning.split('h')
        minuts += int(meaning[0]) * 60

    if 'm' in meaning:
        meaning = meaning.split('m')
        minuts += int(meaning[0])

    if 's' in meaning:
        meaning = meaning.split('s')
        minuts += int(meaning[0]) / 60

print(minuts)