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

    def archive(file_path : str, zip_file_path : str):

        with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
            zip_file.write(file_path, arcname=file_path.split('/')[-1])
    
        with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
            return zip_file.getinfo(file_path.split('/')[-1])

    def save_stat_as_file(self, file_path = "text_handler)log.txt"):
        sentences_count = len(self.get_sentences_count(self.text))
        narrative_sentences, interrogative_sentences, imperative_sentences = self.get_sentences_count_by_kinds(self.text)
        avg_sentence_length = self.average_sentence_length(self.text)
        avg_word_length = self.average_word_length(self.text)
        emoticon_count = self.get_emoticon_count(self.text)
        low_case_and_numbers_words = self.get_low_case_and_numbers_words(self.text)
        is_ip = self.is_ip(self.text)
        words_less_than_6_count = self.get_words_less_than_n(self.text, 6)
        shortest_w_word = self.get_shortest_w_word(self.text)
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

    def get_low_case_and_numbers_words(string : str):
        return re.findall(r"(\b\w*[[a-z][0-9]]\w*\b)", string)

    def is_ip(string : str):
        return re.match(r"\d{3}.\d{3}.\d{3}.\d{3}", string)
    
    def get_words_less_than_n(string : str, n : int):
        return len(re.findall(r"\b\w{1,5}\b"))
    
    def get_shortest_w_word(string : str):
        return sorted(re.findall(r"\b\w*w\b", string), lambda x: len(x))[0]
    
    def print_words_by_length(string : str):
        print(re.findall(r"\b\w+\b", string), lambda x: len(x))

    def remove_punctuation_and_spaces(text):
        punctuation_and_spaces = string.punctuation + " "
        for char in punctuation_and_spaces:
            text = text.replace(char, "")
        return text

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

        
        sentences_count = handler.get_sentences_count(handler.text)
        print("Sentences count:")
        for sentence in sentences_count:
            print(sentence)
        print()

        
        narrative_sentences, interrogative_sentences, imperative_sentences = handler.get_sentences_count_by_kinds(handler.text)
        print("Narrative sentences:")
        for sentence in narrative_sentences:
            print(sentence)
        print("Interrogative sentences:")
        for sentence in interrogative_sentences:
            print(sentence)
        print("Imperative sentences:")
        for sentence in imperative_sentences:
            print(sentence)
        print()

        
        avg_sentence_length = handler.average_sentence_length(handler.text)
        print("Average sentence length:", avg_sentence_length)
        print()


        avg_word_length = handler.average_word_length(handler.text)
        print("Average word length:", avg_word_length)
        print()


        emoticon_count = handler.get_emoticon_count(handler.text)
        print("Emoticon count:", emoticon_count)
        print()


        low_case_and_numbers_words = handler.get_low_case_and_numbers_words(handler.text)
        print("Low case and numbers words:")
        for word in low_case_and_numbers_words:
            print(word)
        print()


        is_ip = handler.is_ip(handler.text)
        print("Is IP address:", is_ip)
        print()


        words_less_than_6_count = handler.get_words_less_than_n(handler.text, 6)
        print("Words less than 6 characters count:", words_less_than_6_count)
        print()


        shortest_w_word = handler.get_shortest_w_word(handler.text)
        print("Shortest word ending with 'w':", shortest_w_word)
        print()


        words_by_length = handler.print_words_by_length(handler.text)
        print("Words by length:")
        for length, words in words_by_length.items():
            print(length, "characters:")
            for word in words:
                print(word)
        print()
