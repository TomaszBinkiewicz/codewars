from unittest import TestCase


def send(s):
    words_list = s.split(' ')
    print(words_list)
    for i, word in enumerate(words_list):
        words_list[i] = [str(format(ord(char), 'b')) for char in word]

        for index, char_bin in enumerate(words_list[i]):
            if len(char_bin) < 7:
                words_list[i][index] = ('0' * (7 - len(char_bin))) + words_list[i][index]
        words_list[i] = ''.join(words_list[i])
    for index, word in enumerate(words_list):
        ret_word = ""
        i = 0
        while i < len(word):
            if word[i] == '1':
                try:
                    count = len(word[i:i + word[i:].index('0')])
                    i += word[i:].index('0')
                except ValueError:
                    count = len(word[i:])
                    i = len(word)
                ret_word += f'0 {count * "0"} '
            elif word[i] == '0':
                try:
                    count = len(word[i:word[i:].index('1') + i])
                    i += word[i:].index('1')
                except ValueError:
                    count = len(word[i:])
                    i = len(word)
                ret_word += f'00 {count * "0"} '
        words_list[index] = ret_word.strip()
    print(words_list)
    return ' '.join(words_list)


def receive(s):
    words = s.split(' ')
    binary = ""
    for i, word in enumerate(words):
        if i % 2 == 0 and words[i] == '0':
            words[i + 1] = words[i + 1].replace('0', '1')
        if i % 2 == 1:
            binary += words[i]
    print(binary)
    binary_words = [binary[7 * i:7 * (i + 1)] for i in range(int(len(binary) / 7))]
    print(binary_words)
    return ''.join([chr(int(binary[7 * i: 7 * i + 7], 2)) for i in range(int(len(binary) / 7))])


class Tests(TestCase):
    def test_recieve(self):
        self.assertEqual(receive("0 0 00 0000 0 00"), "C")
        self.assertEqual(receive("0 0 00 0000 0 000 00 0000 0 00"), "CC")
        self.assertEqual(receive("00 0 0 0 00 00 0 0 00 0 0 0"), "%")
        self.assertEqual(receive(
            "0 0 00 0000 0 0000 00 0 0 0 00 000 0 000 00 0 0 0 00 0 0 000 00 000 0 0000 00 0 0 0 00 0 0 00 00 0 0 0 00 00000 0 0 00 00 0 000 00 0 0 00 00 0 0 0000000 00 00 0 0 00 0 0 000 00 00 0 0 00 0 0 00 00 0 0 0 00 00 0 0000 00 00 0 00 00 0 0 0 00 00 0 000 00 0 0 0 00 00000 0 00 00 0 0 0 00 0 0 0000 00 00 0 0 00 0 0 00000 00 00 0 000 00 000 0 0 00 0 0 00 00 0 0 000000 00 0000 0 0000 00 00 0 0 00 0 0 00 00 00 0 0 00 000 0 0 00 00000 0 00 00 0 0 0 00 000 0 00 00 0000 0 0000 00 00 0 00 00 0 0 0 00 000000 0 00 00 00 0 0 00 00 0 0 00 00000 0 00 00 0 0 0 00 0 0 0000 00 00 0 0 00 0 0 00000 00 00 0 0000 00 00 0 00 00 0 0 000 00 0 0 0 00 00 0 0 00 000000 0 00 00 00000 0 0 00 00000 0 00 00 0000 0 000 00 0 0 000 00 0 0 00 00 00 0 0 00 000 0 0 00 00000 0 000 00 0 0 00000 00 0 0 0 00 000 0 00 00 0 0 0 00 00 0 0000 00 0 0 0 00 00 0 00 00 00 0 0 00 0 0 0 00 0 0 0 00 00000 0 000 00 00 0 00000 00 0000 0 00 00 0000 0 000 00 000 0 0000 00 00 0 0 00 0 0 0 00 0 0 0 00 0 0 000 00 0"),
            "Chuck Norris' keyboard has 2 keys: 0 and white space.")

    def test_send(self):
        self.assertEqual(send("C"), "0 0 00 0000 0 00")
        self.assertEqual(send("CC"), "0 0 00 0000 0 000 00 0000 0 00")
        self.assertEqual(send("%"), "00 0 0 0 00 00 0 0 00 0 0 0")
        self.assertEqual(send("Chuck Norris' keyboard has 2 keys: 0 and white space."),
                         "0 0 00 0000 0 0000 00 0 0 0 00 000 0 000 00 0 0 0 00 0 0 000 00 000 0 0000 00 0 0 0 00 0 0 00 00 0 0 0 00 00000 0 0 00 00 0 000 00 0 0 00 00 0 0 0000000 00 00 0 0 00 0 0 000 00 00 0 0 00 0 0 00 00 0 0 0 00 00 0 0000 00 00 0 00 00 0 0 0 00 00 0 000 00 0 0 0 00 00000 0 00 00 0 0 0 00 0 0 0000 00 00 0 0 00 0 0 00000 00 00 0 000 00 000 0 0 00 0 0 00 00 0 0 000000 00 0000 0 0000 00 00 0 0 00 0 0 00 00 00 0 0 00 000 0 0 00 00000 0 00 00 0 0 0 00 000 0 00 00 0000 0 0000 00 00 0 00 00 0 0 0 00 000000 0 00 00 00 0 0 00 00 0 0 00 00000 0 00 00 0 0 0 00 0 0 0000 00 00 0 0 00 0 0 00000 00 00 0 0000 00 00 0 00 00 0 0 000 00 0 0 0 00 00 0 0 00 000000 0 00 00 00000 0 0 00 00000 0 00 00 0000 0 000 00 0 0 000 00 0 0 00 00 00 0 0 00 000 0 0 00 00000 0 000 00 0 0 00000 00 0 0 0 00 000 0 00 00 0 0 0 00 00 0 0000 00 0 0 0 00 00 0 00 00 00 0 0 00 0 0 0 00 0 0 0 00 00000 0 000 00 00 0 00000 00 0000 0 00 00 0000 0 000 00 000 0 0000 00 00 0 0 00 0 0 0 00 0 0 0 00 0 0 000 00 0")
