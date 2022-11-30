# from Data import SignalDataset
from os import chdir, getcwd
import sys

sys.path.append(getcwd())

from IO import Reader
from Utils import PickleFileUtils
from Data.SignalDataset import SignalDataset

# DESCRIPTION:
# INPUTS:
# RETURNS:
# NOTES:

complete_signal_data_set = Reader.extract_cardiology_challenge_dataset(
    combine_training_and_vaidation_datasets=True
)

(
    original_training_signal_data_set,
    original_validation_signal_data_set,
) = Reader.extract_cardiology_challenge_dataset(
    combine_training_and_vaidation_datasets=False
)

# combined_sets = Reader.extract_cardiology_challenge_dataset(
#     combine_training_and_vaidation_datasets=False
# )

# original_training_data_set = combined_sets[0]
# original_validation_data_set = combined_sets[1]

# write data to pickle files
save_data_folder = getcwd() + "\\Data\\PickleFiles\\CardiologyChallenge\\"

PickleFileUtils.write_to_pickle_file(
    complete_signal_data_set, save_data_folder + "CompleteDataSet.pickle"
)
PickleFileUtils.write_to_pickle_file(
    original_training_signal_data_set,
    save_data_folder + "OriginalTrainingDataSet.pickle",
)
PickleFileUtils.write_to_pickle_file(
    original_validation_signal_data_set,
    save_data_folder + "OriginalValidationDataSet.pickle",
)
