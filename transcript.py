import re

def remove_timestamps_and_paragraphs(text):
    # Remove timestamps
    text_without_timestamps = re.sub(r'\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}', '', text)

    # Remove paragraph breaks
    text_without_paragraphs = text_without_timestamps.replace('\n', ' ')

    # Remove double spaces
    text_without_double_spaces = re.sub(r'\s+', ' ', text_without_paragraphs)

    return text_without_double_spaces.strip()

# Prompt user for input
input_text = input("Text:\n")

result_text = remove_timestamps_and_paragraphs(input_text)

print(result_text)
