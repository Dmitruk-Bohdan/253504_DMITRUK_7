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

    def archive(self, file_path : str, zip_file_path : str):

        with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
            zip_file.write(file_path, arcname=file_path.split('/')[-1])
    
        with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
            return zip_file.getinfo(file_path.split('/')[-1])

    def save_stat_as_file(self, file_path = "text_handler)log.txt"):
        sentences_count = len(self.get_sentences_count(self.text))
        print("\nSentences count:\n", sentences_count)
        narrative_sentences, interrogative_sentences, imperative_sentences = self.get_sentences_count_by_kinds(self.text)
        print("\nNarrative sentences:\n", narrative_sentences)
        print("\nInterrogative sentences:\n", interrogative_sentences)
        print("\nImperative sentences:\n", imperative_sentences)
        avg_sentence_length = self.average_sentence_length(self.text)
        print("\nAverage sentence length:\n", avg_sentence_length)
        avg_word_length = self.average_word_length(self.text)
        print("\nAverage word length:\n", avg_word_length)
        emoticon_count = self.get_emoticon_count(self.text)
        print("\nEmoticon count:\n", emoticon_count)
        low_case_and_numbers_words = self.get_low_case_and_numbers_words(self.text)
        print("\nLow case and numbers words:\n", low_case_and_numbers_words)
        is_ip = self.is_ip(self.text)
        print("\nIs IP:\n", is_ip)
        words_less_than_6_count = self.get_words_less_than_6(self.text)
        print("\nWords less than 6 characters count:\n", words_less_than_6_count)
        shortest_w_word = self.get_shortest_w_word(self.text)
        print("\nShortest 'w' word:\n", shortest_w_word)
        words_by_length = self.print_words_by_length(self.text)

        with open(file_path, 'w') as file:
            file.write("Sentences count: {}\n".format(sentences_count))
            file.write("Narrative sentences: {}\n".format(narrative_sentences))
            file.write("Interrogative sentences: {}\n".format(interrogative_sentences))
            file.write("Imperative sentences: {}\n".format(imperative_sentences))
            file.write("Average sentence length: {}\n".format(avg_sentence_length))
            file.write("Average word length: {}\n".format(avg_word_length))
            file.write("Emoticon count: {}\n".format(emoticon_count))
            file.write("Low case and numbers words: {}\n".format(low_case_and_numbers_words))
            file.write("Is IP address: {}\n".format(is_ip))
            file.write("Words less than 6 characters count: {}\n".format(words_less_than_6_count))
            file.write("Shortest word ending with 'w': {}\n".format(shortest_w_word))
            file.write("Words by length: {}\n".format(words_by_length))

    def get_sentences_count(self, string : str):
        return re.findall(r"([^.!?]+[.!?])", string)
    
    def get_sentences_count_by_kinds(self, string : str):
        narrative_sentences = re.findall(r"([^.!?]+\.)", string)
        interrogative_sentences = re.findall(r"([^.!?]+\?)", string)
        imperative_sentences = re.findall(r"([^.!?]+\!)", string)
        return narrative_sentences, interrogative_sentences, imperative_sentences
    
    def average_sentence_length(self, string : str):
        sentences = re.split(r"([^.!?]+[.!?])", string)
        return (int)(reduce(lambda x, y : x + y, [len(re.sub(r"[^\w]", "", sentence)) for sentence in sentences]) / len(sentences))
    
    def average_word_length(aelf, string : str):
        words = re.findall(r"\b(\w+)\b", string)
        return (int)(reduce(lambda x, y : x + y, [len(word) for word in words]) / len(words))
    
    def get_emoticon_count(self, string : str):
        return len(re.findall(r"[;:]-*[\(\)\[\]]+", string))

    def get_low_case_and_numbers_words(self, string : str):
        return re.findall(r"(\b\w*[a-z0-9]\w*\b)", string)

    def is_ip(self, string : str):
        pattern = r'^(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$'
        return bool(re.match(pattern, string))
    
    def get_words_less_than_6(self, string : str):
        return len(re.findall(r"\b\w{1,5}\b", string))
    
    def get_shortest_w_word(self, string : str):
        w_words = sorted(re.findall(r"\b\w*w\b", string), key=lambda x: len(x))
        return w_words[0] if w_words else None
    
    def print_words_by_length(self, string : str):
        print (sorted(re.findall(r"\b\w+\b", string), key=lambda x: len(x)))

    def remove_punctuation_and_spaces(self, text):
        punctuation_and_spaces = string.punctuation + " "
        for char in punctuation_and_spaces:
            text = text.replace(char, "")
        return text

    @staticmethod
    def demonstrate():
        handler = TextHandler()

        handler.read_from_file("input.txt")
        print("Text content after reading from file:")
        print(handler.text)
        print()

        handler.save_to_file("output.txt")
        print("Text content saved to 'output.txt' file.")
        print()

        archive_info = handler.archive("output.txt", "archive.zip")
        print("File 'output.txt' archived as 'archive.zip'.")
        print("Archived file info:")
        print(archive_info)
        print()

        handler.save_stat_as_file("statistics.txt")
        print("Text statistics saved to 'statistics.txt' file.")
        print()

        print("127.125.0.0")
        is_ip = handler.is_ip("127.125.0.0")
        print(f"Is IP address: {is_ip}\n")

        print("127.888.0")
        is_ip = handler.is_ip("127.888.0")
        print(f"Is IP address: {is_ip}\n")
