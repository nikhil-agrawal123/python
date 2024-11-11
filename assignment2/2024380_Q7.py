file_dict = {}

def re(x):
    if '.' in x:
        return x.removesuffix('.')
    else:
        return x.removesuffix(',')

def reference_extractor(text):
    reference = []
    words = text.split()
    for word in words:
        if word.startswith('URL'):
            reference.append(word)
    return reference    

with open('pages.txt', 'r') as f:
    for line in f:
        line = line.strip().split(':')
        y = line[0].split(',')
        url = y[0].strip()
        init_importance = float(y[1].strip())
        if len(line) > 1:
            references = reference_extractor(line[1])
        else:
            references = []
        
        file_dict[url] = {
            'init_imp': init_importance,
            'overall_imp': 0.0,
            'references': references
        }

for i in file_dict.values():
    new_l= []
    for j in i['references']:
        new_l.append(re(j))
    i['references'] = new_l

for url, data in file_dict.items():
    for ref in data['references']:
        if ref in file_dict:
            file_dict[ref]['overall_imp'] += data['init_imp'] / len(data['references'])

N = int(input("Enter the integer number of pages to display: "))

sorted_pages = sorted(file_dict.items(), key=lambda x: x[1]['overall_imp'], reverse=True)

for url, data in sorted_pages[:N]:
    print(f"{url}: {data['overall_imp']}")

def test():
    assert re('abc,') == 'abc'
    assert re('abc.') == 'abc'

test()