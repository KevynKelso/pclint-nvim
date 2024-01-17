# python/static_analysis.py

import csv
from pynvim import attach

def parse_csv(file_path):
    results = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            results.append({'file': row[0], 'line': int(row[1]), 'message': row[2]})
    return results

def load_analysis(current_file):
    nvim = attach('socket', path='/tmp/nvim')
    analysis_results = parse_csv('test.csv')

    for result in analysis_results:
        if result['file'] == current_file:
            # Display as virtual text (ghost text)
            nvim.api.buf_set_virtual_text(0, -1, result['line'] - 1, [[result['message'], 'Error']], {})
