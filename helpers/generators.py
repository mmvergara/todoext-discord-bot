import time


def generate_section_id():
    section_id = ""
    random_chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    current_time = int(time.time() * 1000)  # Convert seconds to milliseconds
    for i in range(8):
        section_id += random_chars[current_time // (36**i) % 36]
    return section_id


# Example usage
result = generate_section_id()
print(result)
