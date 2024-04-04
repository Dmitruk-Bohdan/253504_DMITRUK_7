import csv
import pickle

class GTOData:
    def __init__(self, data):
        self.data = data

    def save_to_csv(self, file_path):
        with open(file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Result100m', 'ResultLongJump'])
            writer.writeheader()
            writer.writerows(self.data)

    def save_to_pickle(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self.data, file)

    def read_from_csv(file_path):
        with open(file_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
            print(row)