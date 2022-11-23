# from Data import SignalDataset
from IO import Reader
from Utils import PickleFileUtils

both_signal_data_set = Reader.extract_cardiology_challenge_dataset(
    mix_training_and_vaidation_datasets=True
)
training_data_set, validations_data_set = Reader.extract_cardiology_challenge_dataset(
    mix_training_and_vaidation_datasets=False
)

# write data to pickle files
