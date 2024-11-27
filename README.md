## Objective:
Develop a Python program to analyze the book "Game of Thrones" and extract linguistic metrics for the construction of a complex reasoning model.

```python	
python gotPython.py got.txt got.csv got.json
```

## Requirements:
1. Evaluate each line of the text file and generate metrics.
2. Store the metrics in two separate files:
    - A CSV file with detailed information per line.
    - A JSON file with general information based on the content of the CSV file.

### Details of the CSV file (Information per line):
- Number of terms (words in the line).
- Number of punctuation marks.
- Number of prepositions (using a specific list).
- Average number of vowels in the terms.
- Size of the longest term.
- Size of the shortest term.
- Total length of the line.
- Length of the line excluding spaces.

### Details of the JSON file (General information):
- Name of the CSV file.
- Total number of lines.
- Average number of terms per line.
- Average number of prepositions per line.
- Average number of punctuation marks per line.
- Average number of characters per line.
- Variance in the number of characters per line.
- Most frequent word in the entire file.
- Most frequent preposition in the entire file.

### **Constraints:**
- Develop the program in Python.
- Receive three input parameters:
  1. The text file to process.
  2. The name of the file with information per line (CSV).
  3. The name of the file with general information (JSON).
- Ensure the number of parameters is correct.
- Ensure the input file exists.
- Do not use libraries like pandas, numpy, or similar.
- Do not use sorting algorithms.
