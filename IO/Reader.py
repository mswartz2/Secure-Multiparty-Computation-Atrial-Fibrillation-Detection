import pandas as pd
import numpy as np
import wfdb
import os

import Data.Datasets.CardiologyChallenge.training as cardiology_challenge_raw_data_training
import Data.Datasets.CardiologyChallenge.validation as cardiology_challenge_raw_data_validation
from Data import SignalDataset


def extract_cardiology_challenge_dataset(mix_training_and_vaidation_datasets=True):
    sample_rate = 300

    training_labels_csv = "Data/Datasets/CardioogyChallenge/training/REFERENCE-v3.csv"
    validation_labels_csv = (
        "Data/Datasets/CardioogyChallenge/validation/REFERENCE-v3.csv"
    )
    Y_training_df = pd.read_csv(training_labels_csv, header=None)
    Y_validation_df = pd.read_csv(validation_labels_csv, header=None)

    training_labels, training_patient_ids = get_labels_and_patient_ids(Y_training_df)
    validation_labels, validation_patient_ids = get_labels_and_patient_ids(
        Y_validation_df
    )

    training_raw_data, validation_raw_data = get_raw_data()

    training_signal_data_set = SignalDataset(
        training_raw_data, training_labels, training_patient_ids
    )
    validation_signal_data_set = SignalDataset(
        validation_raw_data, validation_labels, validation_patient_ids
    )
    both_signal_data_set = SignalDataset(
        training_raw_data + validation_raw_data,
        training_labels + validation_labels,
        training_patient_ids + validation_patient_ids,
    )

    if not mix_training_and_vaidation_datasets:
        return both_signal_data_set
    else:
        return training_signal_data_set, validation_signal_data_set


def get_labels_and_patient_ids(metadata_df):
    labels = np.zeros(len(metadata_df), dtype=int)
    patient_ids = np.empty(len(metadata_df), dtype="U25")

    # patient is the ecg_id - 1
    for patient in range(len(metadata_df)):
        patient_ids[0] = metadata_df[0][patient]  # Id

        if "A" == metadata_df[1][patient]:
            # this patient has AF
            labels[patient] = 1
            afCount += 1
        elif "N" == metadata_df[1][patient]:
            # this record is normal
            labels[patient] = 0
            normCount += 1
        elif "~" == metadata_df[1][patient]:
            # this record is noisy
            labels[patient] = 2
            normCount += 1
        else:
            # this patient isn't norm or AF or noisy
            labels[patient] = -1

    # create empty numpy arr to hold only norm and AF records
    clean_labels = []
    clean_patient_ids = []

    # fill numpy arr
    i = 0
    for i in range(len(metadata_df)):
        if labels[i] in [0, 1]:  # AF or Norm
            clean_labels.append(labels[i])
            clean_patient_ids.append(patient_ids[i])

    return clean_labels, clean_patient_ids


def get_files_list(parent_module):
    files_list = [
        f
        for f in os.listdir(parent_module)
        if os.path.isfile(os.path.join(parent_module, f)) and not f.endswith(".csv")
    ]
    return files_list


def get_raw_data():
    training_files_list = get_files_list(cardiology_challenge_raw_data_training)
    validation_files_list = get_files_list(cardiology_challenge_raw_data_validation)

    training_raw_data = extract_raw_data_from_WFDB_files(
        cardiology_challenge_raw_data_training, training_files_list
    )
    validation_raw_data = extract_raw_data_from_WFDB_files(
        cardiology_challenge_raw_data_validation, validation_files_list
    )

    return training_raw_data, validation_raw_data


def extract_raw_data_from_WFDB_files(dir_path, files_list):
    raw_signals_list = []
    for i in range(len(files_list)):
        current_record = dir_path + files_list[i]
        sig, fields = wfdb.rdsamp(current_record)

        # make signal file 1D
        flattened_signal = sig.flatten()

        raw_signals_list.append(flattened_signal)

    return raw_signals_list
