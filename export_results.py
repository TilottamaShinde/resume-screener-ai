import csv

def export_to_csv(results, output_file = 'screening_results.csv'):
   """
    Exports screening results to a CSV file.

    Parameters:
        results (list of dict): Each dict contains 'filename', 'score', 'keywords'
        output_file (str): The name of the output CSV file
    """

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Resume Name', 'Match Score (%)', 'Top Matching Keywords'])
        writer.writeheader()

        for result in results:
            writer.writerow({
                'Resume Name': result['filename'],
                'Match Score (%)': round(result['score'] * 100, 2),
                'Top Matching Keywords': ', '.join(result['matched_keywords'])
            })

    print(f"✅ Results exported to {output_file}")
