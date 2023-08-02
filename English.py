''' PYngwar Transcriber version 0.2
Mar 1, 2016
Ondo Carniliono - Pedro Bernardinelli
ondo@quenya101.com

Current problems: possible final vowel being deleted?

Usage: the load_and_transcribe function gets a text in Roman alphabet and transcribe for the Tengwar LaTeX codes.
the main function outputs to a file. It isn't needed for the usage of the script.

This version is specific for the English General Use Orthographic Spelling. This is not meant to work for phonemic spelling.
'''

letters_change = {"\n": "\n ", #comments are for values
		  		"tt": "T", #checked.
		  		"pp" : "P", #checked.
		  		"k" : "c", 
		  		"kk" : "C", 
		  		"cc" : "C",
				"ch" : "*", 
		  		"qu" : "q",  
		  		"nd" : "d", 
		  		"mb" : "b", 
		  		"ngw" : "G", #can keep as G if needed.
		  		"ng" : "Ñ", #remapped to be okay.
		  		"th" : "1", #y
		  		"ff" : "F", #checked.
		  		"hw" : "2", #CH as hard k such as echo; not sure how to represent this.
		  		"nt" : "3", #th as this 
		  		"mp" : "4", #checked.
		  		"nc" : "5", #special use case
		  		"gh" : "6", #gh as ghost, checked.
				"sh" : "+",
				"ph" : "=",
		  		'nn' : "N", 
		  		'mm' : "M", 
		  		"ng" : "Ñ", #checked.
		  		"rd" : "7", 
		  		"ll" : "L", #checked.
		  		"ld" : "8", #not correct. remapped incorrectly.
		  		"ss" : "z", 
		  		"hy" : "9", 
		  		" r" : " R", #r before vowel
		  		"hl" : "#l", 
		  		"hr" : "#R", 
		  		#" h" : " H",  #delete I believe.
		  		#"ë" : "e", #not in english.
		  		"ai" : "Ya", #checked.
		  		"ei" : "Ye", #checked.
		  		"oi" : "Yo", #checked.
		  		"ui" : "Yu", #checked.
		  		"au" : "wa", #checked.
		  		"eu" : "we", #checked.
		  		"iu" : "wu", #checked.
		  		"ou" : "wo", #checked.
		  		" ea" : " EA",  
		  		"ea" : "eA", 
		  		"eo" : "eO", 
		  		"ae" : "aE", 
		  		"oe" : "oE", 
		  		"ua" : "uA", 
		  		"ue" : "uE", 
		  		"oa" : "oA", 
		  		"uo" : "uO", 
		  		"ia": "iA", 
		  		"ie" : "iE", 
		  		"io" : "iO", 
		  		"iu" : "iU",
		  		"a " : "A ", #end of word fix
		  		"e " : "E ", #end of word fix
		  		"i ": "I ", #end of word fix
		  		"o " : "O ", #end of word fix
		  		"u ": "U ", #end of word fix
		  		#"y" : "Y ", #Y as consonant, use \Tanna
		  		"s " : "ç ", 
		  		"ks" : "x",
				"the " :"|",
				"of " : ">",
				" of the ": "[",
				"wh" : "]",
				"\n " : "\n",
		  		}

# " á" : " Á", " é" : " É", " í" : " Í", " ó" :  " Ó", " ú" : " Ú"
tengwar_equivalence = {"t" : "\Ttinco ", #checked
		       "p" : "\Tparma ",  #checked.
			   "*" : "\Tcalma ", #maps to ch
			   "c" : "\Tquesse", #checked.
			   "d" : "\Tando ", #checked.
			   "b" : "\Tumbar ", #checked.
			   "j" : "\Tanga ",  #checked.
			   "g" : "\Tungwe ",  #checked.
			   "q" : "\Tcalma\TTtilde",
			   "1" : "\Tthuule ",  #checked.
			   "f" : "\Tformen ",  #checked.
			   "+" : "\Taha ", #change to sh. correct mapping above. #checked.
			   "2" : "\Thwesta ", #ch as k in echo see above
			   "3" : "\Tanto ", #th as this
			   "4" : "\Tparma \TTnasalizer" ,
			   "v" : "\Tampa ", 
			   "5" : "\Tanca ", #empty, special use case such as g in mirage, si in illusion
			   "6" : "\Tunque ", #gh as ghost, mapped correctly.
			   "n" : "\Tnuumen ", 
			   "m" : "\Tmalta ", 
			   "ñ" : "\Tnoldo ", #empty
			   "Ñ" : "\Tnwalme ", #ng as ring, correct above.
			   "r" : "\Toore ", #end of word or preceding consonant
			   "w" : "\Tvala ", 
			  "Y" : "\TTbreve ", # Y as vowel, currently only at end of words.
			  #"w" : "\Tvilya ",  #empty
			   "R" : "\Troomen ", #r before vowel
			  #"7" : "\Tarda ", #empty
			   "l" : "\Tlambe ", 
			   "8" : "\Talda ", 
			   "s" : "\Tsilme ", #checked
			   #"S" : "\Tsilmenuquerna ", #delete I think, english doesn't use it.
			   "z" : "\Tesse ", #checked
			   #"Z" : "\Tessenuquerna ", #delete I think, english doesn't use it.
			   "h" : "\Thyarmen ", 
			   "@" : "\Tyanta ", #y
			   "=" : "\Textendedparma",
			   #"w" : "\Tuure ", 
			   "#" : "\Thalla ", #not sure what \Thalla even is.
			   " " : " \Ts ", 
			   "a" : "\TTthreedots ", #checked.
			   "e" : "\TTacute ", #checked.
			   "i" : "\TTdot ", #checked.
			   "o" : "\TTrightcurl ", #checked.
			   "u" : "\TTleftcurl ", #checked.
			   "y" : "\Tanna ", #y as consonant
			   "A" : "\TTthreedots \Ttelco ", #checked.
			   "E" : "\TTacute \Ttelco ", #checked.
			   "I" : "\TTdot \Ttelco ", #checked.
			   "O" : "\TTrightcurl \Ttelco ", #checked.
			   "U" : "\TTleftcurl \Ttelco ", #checked.
			   #"á" : "\Taara \TTthreedots ", #not in english.
			   #"é" : "\Taara \TTacute ", #not in english.
			   #"í": "\Taara \TTdot ", #not in english.
			   #"ó" : "\Taara \TTrightcurl ", #not in english.
			   #"ú" : "\Taara \TTleftcurl ", #not in english.
			   "T" : "\Ttinco \TTdoubler ", #checked.
			   "P" : "\Tparma \TTdoubler ", #checked.
			   "C" : "\Tcalma \TTdoubler ", #checked.
			   "F" : "\Tfoormen \TTdoubler ", #checked.
			   "N" : "\Tnuumen \TTdoubler ", #checked.
			   "M" : "\Tmalta \TTdoubler ", #checked.
			   "L" : "\Tlambe \TTdoubler ", #checked.
			   "ç" : "\Trighthook ", 
			   "x" : "\Tcalma \Tlefthook ", 
			   "\n" : "\n\n", 
			   "!" : "\Texclamation", 
			   "." : "\Tcolon", 
			   "?" : "\Tquestion", 
			   "(" : "\Tparenthesis", 
			   ")" : "\Tparenthesis", 
			   "," : "\Tcentereddot", 
			   "-" : " ", 
			   ";" : "\Tcentereddot", 
			   "|" : "\Textendedando",
			   ">" : "\Textendedumbar",
			   "[" : "\Textendedumbar \Tdoubler",
			   "]" : "\Thwestasindarinwa",
			   "'" : " "
			   }

vowels = ["a", "e", "i", "o", "u"]

accented_vowels = vowels +  ["á", "é", "í", "ó", "ú", "ë", "ä", "ö"]


def replacer(text):
	''' (str) -> str
	Takes special characters (doubled consonants, consonants like nt or th, nuquerna cases)
	and substitutes for the single characters in letters_change
	'''
	cons_keys = list(letters_change.keys())

	text = " " + text.lower()

	for i in range(0, len(cons_keys)):
		text = text.replace(cons_keys[i], letters_change[cons_keys[i]])


	for i in range(0, len(vowels)):
		esse = "z" + vowels[i]
		esse_nuquerna = "Z" + vowels[i]
		text = text.replace(esse, esse_nuquerna)

	for i in range(0, len(accented_vowels)):
		romen = "r" + accented_vowels[i]
		romen_change = "R" + accented_vowels[i]
		text = text.replace(romen, romen_change)

	return text[1:]

def transcriber(text):
	a = ""
	for i in range(len(text)):
		a = a + tengwar_equivalence[text[i]]
		print(a)
	return a
	
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
			scribe = scribe + tengwar_roman_to_tex(line)
		
	return scribe

def save(text):
	file_names = input("Enter the output file name: ")

	with open(file_names, "w", encoding='utf-8') as output_file:
		output_file.write(text)

def main():
	text = load_and_transcribe()

	save(text)

if __name__ == "__main__":
	main()