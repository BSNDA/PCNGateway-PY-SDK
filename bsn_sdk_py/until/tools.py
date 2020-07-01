import os
import base64


def nonce_str():
    return str(base64.b64encode(os.urandom(24)), encoding = "utf-8")

def array_sort(ls: list):
    l_str = ''
    for i, l in enumerate(ls):
        if isinstance(l, dict):
            l_str = l_str + obj_sort(l)
        elif isinstance(l, list):
            l_str = l_str + array_sort(l)
        else:
            l_str = l_str + str(l)
    return l_str


def map_sort(ds: dict):
    d_str = ''
    for (k, v) in ds.items():
        d_str = d_str +'{}{}'.format(k, v)
    return d_str


def obj_sort(oos):
    d_str = ''
    for (k, v) in oos.items():
        d_str = d_str + '{}'.format(v)
    return d_str

if __name__ == '__main__':
    # print(array_sort(['html', 'js', 'css', 'python']))
    # print(map_sort({"a":"111","b":"222","o":"333"}))
    print(array_sort([{"a":"111","b":"222","c":"333|||"},
                      {"d": "444", "e": "555", "f": "666"}]))
