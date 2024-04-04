import pickle
from typing import Dict
import csv
import random

class GTOHandler:
    """
    The GTO_handler class is designed to handle and manipulate data of examinees participating in a physical fitness test.
    It provides methods for saving and loading data to/from CSV and pickle files, as well as retrieving statistics and sorting the data.

    Attributes:
        examinees (Dict[str, tuple[float, float]]): A dictionary containing examinee names as keys and their running time and jump distance as values.
        running_standart (float): The standard running time that examinees need to meet or exceed.
        jump_standart (float): The standard jump distance that examinees need to meet or exceed.
    """

    def __init__(self, examinees: Dict[str, tuple[float, float]], running_standart = 15.0, jump_standart = 165.0):
        """
        Initializes a new instance of the GTO_handler class.

        Args:
            examinees (Dict[str, tuple[float, float]]): A dictionary containing examinee names as keys and their running time and jump distance as values.
            running_standart (float, optional): The standard running time that examinees need to meet or exceed. Defaults to 15.0.
            jump_standart (float, optional): The standard jump distance that examinees need to meet or exceed. Defaults to 165.0.
        """
        self.examinees = examinees
        self.running_standart = running_standart
        self.jump_standart = jump_standart

    def save_to_csv(self):
        """
        Saves the examinee data to a CSV file.
        The file name is generated based on the first and last keys of the examinees dictionary.
        The CSV file will have columns for Name, Running Time, and Jump Distance.
        """
        keys_list = list(self.examinees.keys())
        with open(f'{keys_list[0]}-{keys_list[-1]}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Running Time', 'Jump Distance'])
            for name, (running_time, jump_distance) in self.examinees.items():
                writer.writerow([name, running_time, jump_distance])

    def boot_from_csv(self, file_path : str):
        """
        Loads examinee data from a CSV file and updates the examinees attribute.

        Args:
            file_path (str): The path to the CSV file.
        """
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                name = row[0]
                running_time = float(row[1])
                jump_distance = float(row[2])
                self.examinees[name] = (running_time, jump_distance)

    def save_to_pickle(self):
        """
        Saves the instance of the class to a pickle file.
        The file name is generated based on the first and last keys of the examinees dictionary.
        """
        keys_list = list(self.examinees.keys())
        with open(f'{keys_list[0]}-{keys_list[-1]}.pickle', 'wb') as file:
            pickle.dump(self, file)

    def boot_from_pickle(self, file_path : str):
        """
        Loads an instance of the class from a pickle file.

        Args:
            file_path (str): The path to the pickle file.

        Returns:
            GTO_handler: The loaded instance of the class.
        """
        with open(file_path, 'rb') as file:
            return pickle.load(file)

    def get_stats_by_name(self, name : str):
        """
        Retrieves the statistics for a specific examinee by name.

        Args:
            name (str): The name of the examinee.

        Returns:
            tuple[float, float] or None: The running time and jump distance of the examinee, or None if the name is not found.
        """
        return self.examinees.get(name)

    def get_failures(self):
        """
        Retrieves a list of examinees who failed to meet the running or jump standards.

        Returns:
            list[tuple[str, tuple[float, float]]]: A list of tuples containing the name and statistics of the failed examinees.
        """
        examinees_list = self.get_as_list()
        return [item for item in examinees_list 
                if item[1][0] > self.running_standart or item[1][1] < self.jump_standart]

    def get_passed(self):
        """
        Retrieves a list of examinees who passed the running and jump standards.

        Returns:
            list[tuple[str, tuple[float, float]]]: A list of tuples containing the name and statistics of the passed examinees.
        """
        examinees_list = self.get_as_list()
        return [item for item in examinees_list 
                if item[1][0] <= self.running_standart and item[1][1] >= self.jump_standart]

    def get_bests(self):
        """
        Retrieves the top three examinees with the highest jump distances.

        Returns:
            list[tuple[str, tuple[float, float]]]: A list of tuples containing the name and statistics of the top three examinees.
        """
        return self.get_as_list(1)[:3]

    def get_as_list(self, sort_parameter = 0):
        """
        Converts the examinees dictionary into a list and sorts it based on the given sort parameter.

        Args:
            sort_parameter (int, optional): The parameter used for sorting the list. Defaults to 0.
                                           0 - Sort by key (name)
                                           1 - Sort by jump distance (ascending)
                                           2 - Sort by jump distance (descending)

        Returns:
            list[tuple[str, tuple[float, float]]]: A list of tuples containing the name and statistics of the examinees.
        """
        if sort_parameter == 1:
            return sorted(self.examinees.items(), key=lambda x: x[1][1])
        elif sort_parameter == 2:
            return sorted(self.examinees.items(), key=lambda x: x[1][1], reverse=True)
        else: 
            return [(key, self.examinees[key]) for key in sorted(self.examinees)]
        
    def demonstrate():
        """
            Function that demonstrates the usage of the GTO_handler module.

            Prints examples of using the GTO_handler class and its methods.
            Takes no parameters.
        """
        examinees = {}
        names = [
        "Emma", "Liam", "Olivia", "Noah", "Ava", "Isabella", "Sophia", "Mia", "Charlotte", "Amelia",
        "Harper", "Evelyn", "Abigail", "Emily", "Elizabeth", "Mila", "Ella", "Avery", "Sofia", "Camila"]

        for i in range(20):
            rand_run = round(random.uniform(12.0, 18.0), 2)
            rand_jump = round(random.uniform(100.0, 200.0), 2)
            examinees[names[i]] = (rand_run, rand_jump)

        handler = GTOHandler(examinees)    

        handler.save_to_csv()

        handler.boot_from_csv('Emma-Camila.csv')

        handler.save_to_pickle()

        loaded_handler = handler.boot_from_pickle('Emma-Camila.pickle')

        print("\nGet statistics by name")
        stats = loaded_handler.get_stats_by_name('Noah')
        print(stats)

        print("\nGet a list of losers")
        failures = loaded_handler.get_failures()
        print(failures)

        print("\nGet a list of successful participants")
        passed = loaded_handler.get_passed()
        print(passed)

        print("\nGet a list of the top 3 results")
        bests = loaded_handler.get_bests()
        print(bests)

        print("\nGet a list of data in the form of a list")
        data_list = loaded_handler.get_as_list()
        print(data_list)

