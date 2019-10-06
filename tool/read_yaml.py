import yaml


def read_yaml(filename):
    with open("./data/" + filename, encoding="utf-8")as f:
        arr = []
        for i in yaml.load(f).values():
            arr.append(tuple(i.values()))
        return arr


def read_yaml1(filename):
    with open("./data/" + filename, encoding="utf-8")as f:
        return yaml.load(f)