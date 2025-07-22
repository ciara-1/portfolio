# TODO: Define the Patient class below
class Patient:
    def __init__(self, patient_ID, total_visits, physicians, diagnosis):
        """
        Initializes a new Patient object.
        
        :param Patient_ID: A string, the unique identifier for the patient
        :param Total_Visits: An integer, the total number of visits for the patient
        :param Physicians: A list of strings, the unique physician IDs the patient has seen
        :param Diagnosis: A list of strings, the diagnoses codes for the patient
        """
        # TODO: Initialize the attributes
        self.patient_ID = patient_ID
        self.total_visits = total_visits
        self.physicians = list(set(physicians)) # Remove duplicate physician IDs
        self.diagnosis = diagnosis # List of diagnosis codes
        
    def most_frequent_diagnosis(self):
        """
        Calculates the most frequent diagnosis for the patient.

        :return: A string, the most frequent diagnosis code
        """
        # TODO: Implement the function to calculate the most frequent diagnosis
        
        # Check is the diagnosis list is empty
        if not self.diagnosis:
            return None  # No diagnoses available
        
        # Dictionary to store the frequency of each diagnosis
        frequency_dict = {}
        for diagnosis in self.diagnosis:
            if diagnosis in frequency_dict:
                frequency_dict[diagnosis] += 1
            else:
                frequency_dict[diagnosis] = 1
    
        # Calculate and return the most frequent diagnosis
        max_frequency = 0
        most_frequent = None
        for diagnosis, frequency in frequency_dict.items():
            if frequency > max_frequency:
                max_frequency = frequency
                most_frequent = diagnosis

        return most_frequent


# TODO: Instantiate the Patient class with the sample data below
# and call the most_frequent_diagnosis method, then print the result

patient_sample = {
    'Patient_ID': '00016F745862898F',
    'Total_Visits': 2,
    'Physicians': ['2963419753', '5737807753'],
    'Diagnosis': ['V5832', 'V5861', '2724', '3182', 'V5869', '42731', '9594', 'E9174', '4019', '2724', 'V5869']
}

# Create an instance of the Patient class
patient = Patient(
        patient_ID=patient_sample['Patient_ID'],
        total_visits=patient_sample['Total_Visits'],
        physicians=patient_sample['Physicians'],
        diagnosis=patient_sample['Diagnosis']
    )
# Call the most_frequent_diagnosis method
most_frequent = patient.most_frequent_diagnosis()

# Print the result
print(f"The most frequent diagnosis for patient {patient.patient_ID} is: {most_frequent}")