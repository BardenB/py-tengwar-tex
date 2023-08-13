''' PYngwar Transcriber version 0.2
Mar 1, 2016
Ondo Carniliono - Pedro Bernardinelli
ondo@quenya101.com

Current problems: possible final vowel being deleted?

Usage: the load_and_transcribe function gets a text in Roman alphabet and transcribe for the Tengwar LaTeX codes.
the main function outputs to a file. It isn't needed for the usage of the script.

This version is specific for the English General Use Orthographic Spelling. This is not meant to work for phonemic spelling.
'''

from TecendilJSON_EN import preprocess, map, replace_patterns, vowels
import re

vowels = ["a", "e", "i", "o", "u"]

accented_vowels = vowels +  ["á", "é", "í", "ó", "ú", "ë", "ä", "ö"]


def replacer(text):
	''' (str) -> str
	Takes special characters (doubled consonants, consonants like nt or th, nuquerna cases)
	and substitutes for the single characters in letters_change
	'''
	cons_keys = list(preprocess.keys())

	text = " " + text.lower()

	for i in range(0, len(cons_keys)):
		text = text.replace(cons_keys[i], preprocess[cons_keys[i]])


	#for i in range(0, len(vowels)):
	#	esse = "z" + vowels[i]
	#	esse_nuquerna = "Z" + vowels[i]
	#	text = text.replace(esse, esse_nuquerna)

#	for i in range(0, len(accented_vowels)):
#		romen = "r" + accented_vowels[i]
#		romen_change = "R" + accented_vowels[i]
#		text = text.replace(romen, romen_change)

	return text[1:]

valid_groupings = list(map.keys())

def character_by_character_approach(input_str):
    def rearrange_word(word):
        positions_to_skip = set()

        for grouping in valid_groupings:
            pos = 0
            while pos < len(word):
                if word[pos:pos+len(grouping)] == grouping:
                    for i in range(pos, pos+len(grouping)):
                        positions_to_skip.add(i)
                    pos += len(grouping)
                else:
                    pos += 1

        word = list(word)
        rearranged_word = []

        pos = 0
        while pos < len(word):
            if pos in positions_to_skip:
                if pos + 1 < len(word):
                    rearranged_word.append(''.join(word[pos:pos+2]))
                    pos += 2
                else:
                    rearranged_word.append(word[pos])
                    pos += 1
            elif word[pos] in vowels:
                if pos + 1 < len(word) and word[pos + 1] not in vowels and word[pos:pos+2] not in valid_groupings:
                    rearranged_word.append(word[pos + 1] + word[pos])
                    pos += 2
                else:
                    rearranged_word.append(word[pos])
                    pos += 1
            else:
                rearranged_word.append(word[pos])
                pos += 1

        return ''.join(rearranged_word)

    rearranged_chars = []
    word_buffer = []

    for char in input_str:
        if char in vowels:
            word_buffer.append(char)
        else:
            if word_buffer:
                word = ''.join(word_buffer)
                if any(char in word for char in vowels):
                    rearranged_word = rearrange_word(word)
                    rearranged_chars.append(rearranged_word)
                else:
                    rearranged_chars.append(word)
                word_buffer = []
            rearranged_chars.append(char)

    if word_buffer:
        word = ''.join(word_buffer)
        if any(char in word for char in vowels):
            rearranged_word = rearrange_word(word)
            rearranged_chars.append(rearranged_word)
        else:
            rearranged_chars.append(word)

    return ''.join(rearranged_chars)


def transcriber(text):
    a = ""
    current_word = ""

    for char in text:
        if char == " ":
            if current_word:
                a += transcribe_word(current_word) + " " + map[" "] + " "
                current_word = ""
            else:
                a += map[" "] + " "
        else:
            current_word += char

    if current_word:
        a += transcribe_word(current_word)

    return a.strip()

def transcribe_word(word):
    transcribed_word = ""
    i = 0

    while i < len(word):
        for length in range(100, 1, -1):
            if i + length <= len(word) and word[i:i+length] in map:
                transcribed_word += map[word[i:i+length]]
                i += length
                break
        else:
            transcribed_word += map.get(word[i], "")
            i += 1

    return transcribed_word
	
def tengwar_roman_to_tex(text):
	StringsToSearch = ["\TTthreedots", "\TTdot", "\TTacute", "\TTrightcurl", "\TTleftcurl", "\TTcaron", "\TTbreve", "\TTdoubleacute", "\TTdoublerightcurl", "\TTdoubleleftcurl", "\TTtwodots", "\TTtilde", "\TTlefttilde", "\TTnasalizer", "\TTdoubler", "\TTdotbelow","\TTtwodotsbelow", "\TTlefttwodotsbelow", "\TTthreedotsbelow", "\TTdoubleacutebelow", "\TTrightcurlbelow", "\TTleftcurlbelow", "\TTverticalbarbelow"]
	a = replacer(text)
	tengwar = transcriber(a)
	texs = insert_string_between(tengwar, StringsToSearch, "\Ttelco")
	return texs

def insert_string_between(text, search_strings, new_string):
	result = text
	for i in range(len(search_strings)-1):
		string1 = search_strings[i]
		result = result.replace(str(string1 + " " + string1), string1 + new_string + string1)
	return result

def load_and_transcribe():
	file_name = input("Enter the input file name: ")
	scribe = ''

	with open(file_name, 'r', encoding='utf-8') as input_file:
		for line in input_file:
			text = character_by_character_approach(line)
			scribe = scribe +  tengwar_roman_to_tex(text)
			print('scribe ', scribe)
	return scribe

def save(text):
	file_names = input("Enter the output file name: ")

	with open(file_names, "w", encoding='utf-8') as output_file:
		output_file.write(text)

def main():
	text = load_and_transcribe()
	for pattern, replacement in replace_patterns:
		text = re.sub(pattern, replacement, text)
	save(text)

if __name__ == "__main__":
	main()