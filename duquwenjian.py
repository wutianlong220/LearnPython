from pathlib import Path

path = Path('../k/pi_million_digits.txt')

contents = path.read_text()


new = ''

for line in contents.splitlines():
    ##print(line)
    new += line.lstrip()

print(new)