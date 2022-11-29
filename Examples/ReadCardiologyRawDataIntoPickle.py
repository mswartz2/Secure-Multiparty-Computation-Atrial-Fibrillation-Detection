# from Data import SignalDataset
from os import chdir, getcwd
import sys

sys.path.append(getcwd())

from IO import Reader
from Utils import PickleFileUtils
from Data import SignalDataset

# DESCRIPTION:
# INPUTS:
# RETURNS:
# NOTES:

both_signal_data_set = Reader.extract_cardiology_challenge_dataset(
    mix_training_and_vaidation_datasets=True
)
training_data_set, validations_data_set = Reader.extract_cardiology_challenge_dataset(
    mix_training_and_vaidation_datasets=False
)

# write data to pickle files
