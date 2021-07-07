import os

script = os.path.realpath(__file__)
print("Script path:", script)

script = os.path.dirname(script)
print("Script path:", script)