import re

text = "Hello! @ World123"
filtered_text = re.sub(r'[^a-zA-Z]', '', text)
print(filtered_text)