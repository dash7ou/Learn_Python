from pathlib import Path

# there are two different of paths absolute path and relative path
# Absolute path => /usr/local/bin

path = Path('pythonPackages')
print(path.exists())

another_path = Path("./pythonPackages1000")
print(another_path.exists())

# make dir
third_path = Path("email")
third_path.mkdir()

# remove dir
third_path.rmdir()


path = Path()
for filee in path.glob('*.py'):
    print(filee)
