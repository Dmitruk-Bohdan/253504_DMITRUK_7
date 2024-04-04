import zipfile 

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

    def get_low_case_and_numbers_words():
        pass

    def is_ip():
        pass

    

