import os

def disk(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk(childpath)
    print('{0:<3}'.format('total'), path)
    return total

print(disk("C:/Users/harsh/Downloads/python-prep"))

