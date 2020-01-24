
import os
from random import choice
from tempfile import NamedTemporaryFile

"""Generate N random files and dirs with random suffix"""

files = int(input("Entry quantity of files: "))
dirs = int(input("Entry quantity of dirs: "))
suffixes = ['.txt', '.jpg', '.png', '.bmp', '.tff', '.gif', '.pdf',
            '.doc', '.xls', '.ppt', '.c', '.py', '.dat']

test_path = 'test'
os.makedirs(test_path, exist_ok=True)

for i in range(files):
    NamedTemporaryFile('w', delete=False, suffix=choice(suffixes),
                       dir=test_path).close()

for i in range(1, dirs):
    dirpath = os.path.join(test_path, 'dir'+str(i))
    os.makedirs(dirpath, exist_ok=True)
    for i in range(files):
        NamedTemporaryFile('w', delete=False, suffix=choice(suffixes),
                           dir=dirpath).close()
