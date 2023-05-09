from .local_data import category
from .data_matrix import matrix

#
def food():
    output = dict()
    keys = []
    for key, attribute in matrix.items():
        if attribute[0]:
            keys.append(key)
    id = 0
    for place in keys:
        if place in category:
            output[id] = category[place]
            id += 1
    return output

def entertainment():
    output = dict()
    keys = []
    for key, attribute in matrix.items():
        if attribute[1]:
            keys.append(key)
    id = 0
    for place in keys:
        if place in category:
            output[id] = category[place]
            id += 1
    return output

def cultural():
    output = dict()
    keys = []
    for key, attribute in matrix.items():
        if attribute[2]:
            keys.append(key)
    id = 0
    for place in keys:
        if place in category:
            output[id] = category[place]
            id += 1
    return output

def outdoor():
    output = dict()
    keys = []
    for key, attribute in matrix.items():
        if attribute[3]:
            keys.append(key)
    id = 0
    for place in keys:
        if place in category:
            output[id] = category[place]
            id += 1
    return output

def trips():
    output = dict()
    keys = []
    for key, attribute in matrix.items():
        if attribute[4]:
            keys.append(key)
    id = 0
    for place in keys:
        if place in category:
            output[id] = category[place]
            id += 1
    return output

def drunk():
    output = dict()
    keys = []
    for key, attribute in matrix.items():
        if attribute[5]:
            keys.append(key)
    id = 0
    for place in keys:
        if place in category:
            output[id] = category[place]
            id += 1
    return output

def student():
    output = dict()
    keys = []
    for key, attribute in matrix.items():
        if attribute[6]:
            keys.append(key)
    id = 0
    for place in keys:
        if place in category:
            output[id] = category[place]
            id += 1
    return output

def friends():
    output = dict()
    keys = []
    for key, attribute in matrix.items():
        if attribute[7]:
            keys.append(key)
    id = 0
    for place in keys:
        if place in category:
            output[id] = category[place]
            id += 1
    return output

def family():
    output = dict()
    keys = []
    for key, attribute in matrix.items():
        if attribute[8]:
            keys.append(key)
    id = 0
    for place in keys:
        if place in category:
            output[id] = category[place]
            id += 1
    return output

def couples():
    output = dict()
    keys = []
    for key, attribute in matrix.items():
        if attribute[9]:
            keys.append(key)
    id = 0
    for place in keys:
        if place in category:
            output[id] = category[place]
            id += 1
    return output

def tourists():
    output = dict()
    keys = []
    for key, attribute in matrix.items():
        if attribute[10]:
            keys.append(key)
    id = 0
    for place in keys:
        if place in category:
            output[id] = category[place]
            id += 1
    return output