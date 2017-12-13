
def main(input_string):
    import re, sys
    # input_string = sys.stdin.read()
    regex = r'question-summary-(\d+)\">.*?question-hyperlink\">([\w\s]+).*?class=\"relativetime\">([\w\s]+)<'
    for x in re.findall(regex, input_string, re.DOTALL):
        print(';'.join(x))


if __name__ == '__main__':
    with open('/home/matteo/ALL/hackerrank/regex/07_Applications/stack_exchange_scraper/test.html', 'r') as f:
        main(f.read())
