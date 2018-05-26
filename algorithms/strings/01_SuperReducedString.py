def remove_double_characters(string):
    index_to_ignore = None

    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            index_to_ignore = i
            break

    if index_to_ignore is None:
        return string

    ris = ''
    for i in range(len(string)):
        if i in [index_to_ignore, index_to_ignore + 1]:
            continue
        ris += string[i]

    print('Input was {} --> {}'.format(string, ris))
    return ris

def super_reduced_string(string):
    string_rip = remove_double_characters(string)
    while string_rip != remove_double_characters(string_rip):
        string_rip = remove_double_characters(string_rip)
    return string_rip

if __name__ == '__main__':
    examples = ['aaabccddd']

    for s in examples:
        result = super_reduced_string(s)
        print('For string {}, result is {}'.format(s, result))