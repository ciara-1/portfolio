import csv

def process_outpatient_data(filename):
    """
    Process the outpatient data to calculate the required statistics for each patient.
    
    Args:
    - filename (str): Path to the outpatient_sample.csv
    
    Returns:
    - result (list): List of dictionaries with patient data.
    """
    patient_data = {}
    
    # TODO: Read the CSV file
    # TODO: Process the data and populate the patient_data dictionary
    # TODO: Calculate the required statistics for each patient
    
    from collections import defaultdict, Counter

    # Create a dictionary to store outpaitent data for each patient
    patient_data = defaultdict(lambda: {
        'visits': 0,
        'physicians': set(),
        'diagnoses': [],
        'diagnosis_count': Counter()
    })

    # Read the CSV file
    with open(filename, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            patient_id = row['Patient_ID']

            # Count total visits
            patient_data[patient_id]['visits'] += 1

            # Set of unique physicians seen
            physicians = {row['Primary_Physician'], row['Operating_Physician'], row['Other_Physician']}
            # Remove empty values
            physicians = {physician for physician in physicians if physician}
            patient_data[patient_id]['physicians'].update(physicians)

            # Set of unique diagnoses associated with the patient
            for i in range(1, 11): #ICD9_DGNS_CD_1 to ICD9_DGNS_CD_10
                diagnosis = row[f'ICD9_DGNS_CD_{i}']
                if diagnosis:
                    patient_data[patient_id]['diagnoses'].append(diagnosis)
                    patient_data[patient_id]['diagnosis_count'][diagnosis] += 1

    result = []
    # TODO: Convert the processed patient_data into the desired output format (list of dictionaries)
    
     # Convert the processed patient_data into a list of dictionaries containing patient data
    result = []
    for patient_id, data in patient_data.items():
        # Track most frequent diagnosis for each patient
        if data['diagnoses']:
            most_freq_diagnosis = data['diagnosis_count'].most_common(1)[0][0]
        else:
            most_freq_diagnosis = '' # No diagnosis available
 
        result.append({
            'Patient_ID': patient_id,
            'Total_Visits': data['visits'],
            'Total_Physicians': len(data['physicians']),
            'Total_Diagnosis': len(set(data['diagnoses'])),
            'Most_Freq_Diagnosis': most_freq_diagnosis
        })

    return result

def write_summary_to_csv(data, filename):
    """
    Write the processed patient data to a csv file.
    
    Args:
    - data (list): List of dictionaries with patient data.
    - filename (str): Path to the output csv.
    """
    fieldnames = ["Patient_ID", "Total_Visits", "Total_Physicians", "Total_Diagnosis", "Most_Freq_Diagnosis"]
    
    # TODO: Write the processed patient data to a new CSV file

    # Write the processed patient data to a new CSV file
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            writer.writerow(row)

def main():
    input_file = "outpatient_sample.csv"
    output_file = "2105542_hw4.csv"  # Replace '<username>' with your UTHealth username.
    
    processed_data = process_outpatient_data(input_file)
    write_summary_to_csv(processed_data, output_file)

if __name__ == "__main__":
    main()