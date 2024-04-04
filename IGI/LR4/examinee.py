from datetime import time

class Examinee:
    def __init__(self, name : str, jump_result : float, running_time : time):
        self.name = name
        self.jump_result = jump_result
        self.running_time = running_time
    