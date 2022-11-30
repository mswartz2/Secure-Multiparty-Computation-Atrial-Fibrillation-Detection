from os import chdir, getcwd
import sys

sys.path.append(getcwd())

from Utils import PickleFileUtils

# DESCRIPTION:
# INPUTS:
# RETURNS:
# NOTES:

# Read in raw data pickles
save_data_folder = getcwd() + "\\Data\\PickleFiles\\CardiologyChallenge\\"

complete_signal_data_set = PickleFileUtils.read_in_pickle_file(
    save_data_folder + "CompleteDataSet"
)
# original_training_data_set = PickleFileUtils.read_in_pickle_file(
#     save_data_folder + "OriginalTrainingDataSet"
# )
# original_validation_data_set = PickleFileUtils.read_in_pickle_file(
#     save_data_folder + "OriginalValidationDataSet"
# )


# Cut data in to 10 folds
folds = []

# Save 10 folds

# Train 10 models
# fold_n is the testing fold, exclude it from model training
for fold_n in folds:
    # train model

    # save model

    pass
