import sys, os
import csv, json, re
from collections import Counter
from statistics import mean, variance

PREPOSITIONS = {
    "to", "before", "under", "with", "against", "from", "since", "in", "between",
    "towards", "until", "for", "by", "according", "without", "under", "on", "after"
}

# ------------------------------------------------------
# Function to calculate metrics of a line of text
# ------------------------------------------------------
def calculate_line_metrics(line):
    words = re.findall(r'\b\w+\b', line.lower())
    lengths = [len(word) 
               for word in words
               ]

    return {
        "number_of_terms": len(words),
        "number_of_signs": len(re.findall(r'[^\w\s]', line)), # Regex for any character that is not a letter or space
        "number_of_prepositions": sum(1 
                                      for word in words 
                                          if word in PREPOSITIONS
                                      ),

        "average_vowels": sum(char in "aeiouáéíóú" 
                              for word in words 
                                  for char in word) / len(words) if words else 0,
        
        "max_length": max(lengths, default=0),
        "min_length": min(lengths, default=0),
        
        "total_length": len(line),
        "length_without_spaces": len(line.replace(" ", ""))
    }

# -------------------------------------------------------
# Function to calculate summary of all lines of text
# -------------------------------------------------------
def calculate_summary(lines, line_metrics):
    total_words = []
    total_prepositions = Counter()

    for line in lines:
        line_words = re.findall(r'\b\w+\b', line.lower()) # Regex to recognize words (r'\b\w+\b')
        total_words.extend(line_words)
        total_prepositions.update(word 
                                  for word in line_words 
                                      if word in PREPOSITIONS
                                  )

    frequent_words = Counter(total_words)
    most_frequent_preposition = total_prepositions.most_common(1)
    lengths = [len(line.strip()) 
               for line in lines
               ]

    return {
        "total_number_of_lines": len(lines),
        "average_terms": mean(metrics["number_of_terms"] 
                              for metrics in line_metrics
                              ),
        "average_prepositions": mean(metrics["number_of_prepositions"] 
                                     for metrics in line_metrics
                                     ),
        "average_signs": mean(metrics["number_of_signs"] 
                              for metrics in line_metrics
                              ),
        "average_characters": mean(lengths),

        "character_variance": variance(lengths) if len(lengths) > 1 else 0,

        "most_frequent_word": frequent_words.most_common(1)[0][0],
        "most_frequent_preposition": most_frequent_preposition[0][0] if most_frequent_preposition else None
    }

# ---------------------------------
# Function to read the TXT file
# ---------------------------------
def read_text_file(file_path):
    if not os.path.exists(file_path):
        print(f"ERROR, FILE DOES NOT EXIST: {file_path}!")
        return []
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

# --------------------------------
# Function to write to the CSV
# --------------------------------
def write_csv_file(csv_path, line_metrics):
    fields = [
        "number_of_terms", "number_of_signs", "number_of_prepositions", "average_vowels", 
        "max_length", "min_length", "total_length", "length_without_spaces"
    ]
    with open(csv_path, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(line_metrics)

# ---------------------------------
# Function to write to the JSON
# ---------------------------------
def write_json_file(json_path, summary):
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(summary, json_file, ensure_ascii=False, indent=4)

# -----------------------------------------
# Function to process all files
# -----------------------------------------
def process_files(text_path, csv_path, json_path):
    lines = read_text_file(text_path)
    if not lines:
        return

    line_metrics = [calculate_line_metrics(line.strip()) 
                    for line in lines
                    ]

    write_csv_file(csv_path, line_metrics)

    summary = calculate_summary(lines, line_metrics)
    summary["csv_file_name"] = csv_path

    write_json_file(json_path, summary)


def main():
    if len(sys.argv) != 2:
        print("COMMAND: python gotPython.py got.txt")
        return
    
    text_path = sys.argv[1]
    output_folder = "output"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    csv_path = os.path.join(output_folder, "got.csv")
    json_path = os.path.join(output_folder, "got.json")
    process_files(text_path, csv_path, json_path)

if __name__ == "__main__":
    main()