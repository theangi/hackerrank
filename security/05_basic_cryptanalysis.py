def decrypt_adaptively():
    """
    This tries to decrypt the text in an evolutive/adaptive process.
    This is surely slower than a pure mathematical approach.
    """
    import string

    correspondances = dict.fromkeys(string.ascii_lowercase, 0)

    dictionary = []
    with open('/home/matteo/ALL/hackerrank/security/dictionary.lst') as f:
        _ = [dictionary.append(x.replace('\n', '')) for x in f]

    row_input = 'lhpohes gvjhe ztytwojmmtel lgsfcgver segpsltjyl vftstelc djfl rml catrroel jscvjqjyfo mjlesl lcjmmfqe egvj gsfyhtyq sjfgver csfaotyq lfxtyq gjywplesl lxljm dxcel mpyctyq ztytwojmmtelel mfcgv spres mjm psgvty bfml ofle mjlc dtc tygfycfctjy dfsyl zpygvel csfao yealqsjpml atyl lgsjql qyfsotelc fseyf ojllel gjzmselltyq wpyhtelc zpltgl weygel afyher rstnesl aefleo rtyhes mvflel yphe rstnes qojder dtwwer lojml mfcgvel reocfl djzder djpygtyq gstmmoeafsel reg cpdel qspyqe mflctel csflvtyq vfcl avfghtyq vftsdfool mzer rsjye wjjol psol mplvtyq catrroe mvfqe lgseey leqzeycer wjseqsjpyrer lmjtoes msjwtoel docl djpyger cjpstlcl goefy gojddesl mjrl qjddoe gjy gpdtyql lyftotyq rjayojfr swgl vjle atrqec gjzmfgces frfl qotcgver gspzd zftodjzdl lyfsh'

    input_data = row_input.split()
    sorted_input = sorted(input_data, key=lambda x: len(x), reverse=True)
    dictionary = sorted(dictionary, key=lambda x: len(x), reverse=True)

    def check_same_letter_everywhere(first, second):
        for i, x in enumerate(first):
            pos = get_positions_letter_in_word(first, x)
            x1 = second[i]
            pos1 = get_positions_letter_in_word(second, x1)

            if len(pos) != len(pos1) or pos != pos1:
                return False
        return True

    def get_words_same_length_and_shape(value):
        return [x for x in dictionary if len(x) == len(value) and check_same_letter_everywhere(value, x)]

    def update_mapping(cryped, decrypted):
        for i, _ in enumerate(cryped):
            if correspondances[cryped[i]] == 0:
                correspondances[cryped[i]] = decrypted[i]

    def get_positions_letter_in_word(word, letter):
        return [pos for pos, char in enumerate(word) if char == letter]

    def matches_using_current_data(first, second):
        for i, _ in enumerate(first):
            if correspondances[first[i]] != 0 and correspondances[first[i]] != second[i]:
                return False
        return True

    def do_stuff(something):
        longest_input_word = min(something, key=lambda x: len(get_words_same_length_and_shape(x)))
        to_be_used_as_cipher = get_words_same_length_and_shape(longest_input_word)

        if len(to_be_used_as_cipher) == 1:
            # print('Moment of thruth! {} could be only {}'.format(longest_input_word, to_be_used_as_cipher))
            update_mapping(longest_input_word, to_be_used_as_cipher[0])
        else:
            for x in to_be_used_as_cipher:
                if matches_using_current_data(longest_input_word, x):
                    # print('Found by previous knowledge! {} --> {}'.format(longest_input_word, x))
                    update_mapping(longest_input_word, x)
                    break

        something.remove(longest_input_word)

    while len(sorted_input) > 1 or 0 not in correspondances.values():
        do_stuff(sorted_input)

    result = []

    print('Dictionary now: {}'.format(correspondances))
    for x in row_input:
        result.append(correspondances[x]) if x is not ' ' else result.append(' ')

    print(*result, sep='')
