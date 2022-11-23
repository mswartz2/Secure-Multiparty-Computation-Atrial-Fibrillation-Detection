from dataclasses import dataclass


@dataclass
class SignalDataset:
    raw_data: list
    labels: list
    patient_ids: list

    def __init__(self, raw_data, labels, patient_ids):
        self.raw_data = raw_data
        self.labels = labels
        self.patient_ids = patient_ids

    def get_raw_data(self):
        return self.raw_data

    def get_labels(self):
        return self.labels

    def get_patient_ids(self):
        return self.patient_ids
