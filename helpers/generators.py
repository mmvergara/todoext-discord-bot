import time
from datetime import datetime


def generate_section_id():
    section_id = ""
    random_chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    current_time = int(time.time() * 1000)  # Convert seconds to milliseconds
    for i in range(8):
        section_id += random_chars[current_time // (36**i) % 36]
    return section_id


def generate_task_id():
    return generate_section_id() + str(int(datetime.now().timestamp()))
