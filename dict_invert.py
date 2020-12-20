from pprint import pprint
din = {
    'apple': ['malum', 'pomum', 'popula'],
    'fruit': ['baca', 'bacca', 'popum'],
    'punishment': ['malum', 'multa']
}
dout = {}

for i in din.keys():
    for j in din.get(i):
        dout.setdefault(j)
        if dout[j]: dout[j] = dout[j], i
        else: dout[j] = i
pprint(dout)
