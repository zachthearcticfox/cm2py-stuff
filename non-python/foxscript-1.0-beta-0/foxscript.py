import re

with open('main.fox', 'rt+') as f:
    code = f.read()

def tokenize():
    lines = code.split('\n')
    for ln in lines:
        cc = ''
        for char in ln:
            cc = char