import os
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def main():
    regex = r'href="(.+)"'
    with open(os.path.join(__location__, 'test.html')) as f:
        for x in re.findall(regex, f.read(), re.DOTALL):
            print(','.join(x))

if __name__ == '__main__':
    main()


