import sys

def loading_data(file_name):
	flag = False
	tokens, sentences = [], []
	with open(file_name, "r", encoding="utf8") as file:
		for line in file:
			if line != "\n":
				line = line.strip()
				
				if check_limit_datasets(line):
					flag = True

				if flag:
					line = only_value(line)
					tokens.append(line)

				if flag == False:
					line = remove_value(line)
					tokens.append(line)
			else:
				sentences.append(tokens)
				tokens = []

	return sentences

def check_limit_datasets(line):
	start_harem = False

	token = line.split(" ")[0]

	if token == "StartSecondHAREM":
		print("Found: 'StartSecondHAREM'")
		start_harem = True

	return start_harem

def only_value(line):
	token_tag = line.split(" ")
	token = token_tag[0]
	tag = token_tag[-1]

	if tag != "B-VAL" and tag != "I-VAL":
		tag = "O"

	return token+" "+tag

def remove_value(line):
	token_tag = line.split(" ")
	token = token_tag[0]
	tag = token_tag[-1]
	
	if tag == "B-VAL" or tag == "I-VAL":
		tag = "O"

	return token+" "+tag

def check_tokens(sentences_key, sentences_participant):
	flag = True
	for i in range(len(sentences_key)):
		for j in range(len(sentences_key[i])):
			token_key = sentences_key[i][j].split(" ")[0]
			token_participant = sentences_participant[i][j].split(" ")[0]
			if token_key != token_participant:
				print("Key: ", sentences_key[i][j], "Participant: ", sentences_participant[i][j])
				flag = False
				break
	if flag:
		print("Ok Tokens!")

def alignment(sentences_key, sentences_participant):
	sentences, tokens = [], []
	for i in range(len(sentences_key)):
		for j in range(len(sentences_key[i])):
			token_tag_participant = sentences_participant[i][j]
			token_tag_key = sentences_key[i][j]
			splited = token_tag_key.split(" ")
			tag_key = splited[-1]
			triple = token_tag_participant+" "+tag_key
			tokens.append(triple)
		sentences.append(tokens)
		tokens = []
	return sentences

def output_conll(output_file_name, conll):
	new_file = open(output_file_name, "w+", encoding="utf8")
	for sentence in conll:
		for line in sentence:
			new_file.write(line+"\n")
		new_file.write("\n")

def conlleval(output_file_name):
	import os

	os.system("perl conlleval.pl <"+str(output_file_name))

def main():
	input_file = sys.argv[1]
	key_file = sys.argv[2]
	output_file = sys.argv[3]

	sentences_key, sentences_participant = [], []
	sentences_participant = loading_data(input_file) 
	print("Sentences Participant: ", len(sentences_participant))
	sentences_key = loading_data(key_file)
	print("Sentences Key: ", len(sentences_key))
	check_tokens(sentences_key, sentences_participant)
	conll = alignment(sentences_key, sentences_participant)
	print("Sentences in CoNLL: ", len(conll))
	output_conll(output_file, conll)
	conlleval(output_file)

if __name__ == '__main__':
	main()
