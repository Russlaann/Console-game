from os import environ
import pprint
for i in environ:
    print(f'{i}: {environ[i]},')