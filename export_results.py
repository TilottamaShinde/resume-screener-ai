import csv

def export_to_csv(results, output_file = 'screening_results.csv'):
   """
    Exports screening results to a CSV file.

    Parameters:
        results (list of dict): Each dict contains 'filename', 'score', 'keywords'
        output_file (str): The name of the output CSV file
    """
