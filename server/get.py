from .local_data import category
from .data_matrix import matrix

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
    print(output)
    print("adawd")
    return output

def entertainment():
    output = []
    keys = []
    for key, attribute in matrix.items():
        if attribute[1]:
            keys.append(key)
    for place in keys:
        if place in category:
            output.append(category[place])
    return output

def cultural():
    output = []
    keys = []
    for key, attribute in matrix.items():
        if attribute[2]:
            keys.append(key)
    for place in keys:
        if place in category:
            output.append(category[place])
    return output

def outdoor():
    output = []
    keys = []
    for key, attribute in matrix.items():
        if attribute[3]:
            keys.append(key)
    for place in keys:
        if place in category:
            output.append(category[place])
    return output

def trips():
    output = []
    keys = []
    for key, attribute in matrix.items():
        if attribute[4]:
            keys.append(key)
    for place in keys:
        if place in category:
            output.append(category[place])
    return output

def drunk():
    output = []
    keys = []
    for key, attribute in matrix.items():
        if attribute[5]:
            keys.append(key)
    for place in keys:
        if place in category:
            output.append(category[place])
    return output

def student():
    output = []
    keys = []
    for key, attribute in matrix.items():
        if attribute[6]:
            keys.append(key)
    for place in keys:
        if place in category:
            output.append(category[place])
    return output

def friends():
    output = []
    keys = []
    for key, attribute in matrix.items():
        if attribute[7]:
            keys.append(key)
    for place in keys:
        if place in category:
            output.append(category[place])
    return output

def family():
    output = []
    keys = []
    for key, attribute in matrix.items():
        if attribute[8]:
            keys.append(key)
    for place in keys:
        if place in category:
            output.append(category[place])
    return output

def couples():
    output = []
    keys = []
    for key, attribute in matrix.items():
        if attribute[9]:
            keys.append(key)
    for place in keys:
        if place in category:
            output.append(category[place])
    return output

def tourists():
    output = []
    keys = []
    for key, attribute in matrix.items():
        if attribute[10]:
            keys.append(key)
    for place in keys:
        if place in category:
            output.append(category[place])
    return output