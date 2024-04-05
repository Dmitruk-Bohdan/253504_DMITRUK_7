from functools import reduce
import string
import zipfile 
import re

class TextHandler:
    def __init__(self):
        self.text = str()

    def read_from_file(self, file_path : str):
        with open(file_path, 'r') as file:
            self.text = file.read()

    def save_to_file(self, file_path : str):
        with open(file_path, 'w') as file:
            file.write(self.text)

    def archive(file_path, zip_file_path):

        with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
            zip_file.write(file_path, arcname=file_path.split('/')[-1])
    
        with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
            return zip_file.getinfo(file_path.split('/')[-1])


    def get_stat_as_file():
        pass

    def get_sentences_count(string : str):
        return re.findall(r"([^.!?]+[.!?])", string)
    
    def get_sentrnces_count_by_kinds(string : str):
        narrative_sentences = re.findall(r"([^.!?]+\.)", string)
        interrogative_sentences = re.findall(r"([^.!?]+\?)", string)
        imperative_sentences = re.findall(r"([^.!?]+\!)", string)
        return narrative_sentences, interrogative_sentences, imperative_sentences
    
    def average_sentence_length(string : str):
        sentences = re.split(r"([^.!?]+[.!?])", string)
        return (int)(reduce(lambda x, y : x + y, [len(re.sub(r"[^\w]", "", sentence)) for sentence in sentences]) / len(sentences))
    
    def average_word_length(string : str):
        words = re.findall(r"(\w+)", string)
        return (int)(reduce(lambda x, y : x + y, [len(word) for word in [words]]) / len(words))
    
    def get_emoticon_count(string : str):
        return len([re.findall(r"[;:]-*[()[]]+")])

    def get_low_case_and_numbers_words():
        words = re.findall(r"(\w+)", string)
        return re.findall(r"(?:^|\s)(\w*[[a-z][0-9]]\w*)(?:$|\s|[!?.,(...)])")

    def is_ip():
        pass

    def remove_punctuation_and_spaces(text):
        punctuation_and_spaces = string.punctuation + " "
        for char in punctuation_and_spaces:
            text = text.replace(char, "")
        return text

