import pickle
import os


def write_to_pickle_file(data, filename):
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))

    pickle_file = open(filename, "wb")
    pickle.dump(data, pickle_file)
    pickle_file.close()


def read_in_pickle_file(filename):
    with open(filename, "rb") as myfile:
        data = pickle.load(myfile)

    return data


def getDiagnosisText(diagnosis):
    diagnosisText = ""

    if diagnosis == 0:
        diagnosisText = "NORM"
    elif diagnosis == 1:
        diagnosisText = "AF"
    elif diagnosis == 2:
        diagnosisText = "NOISY"
    else:
        diagnosisText = "OTHER"

    return diagnosisText


def plotOneSingleLeadECGSignal(
    data, signalName, diagnosis, sampleRate, saveRec, saveDir=""
):
    """saveRec is a boolean field, if True, put where to save the file in saveDir"""

    diagnosisText = getDiagnosisText(diagnosis)
    plotTitle = f"ECG Signal - Patient {signalName} - {diagnosisText} - Sample Rate: {sampleRate} Hz"


def getIdsToVisualize(labelsMetaDataArr, numRecs):
    """Returns numRecs # of signals for nosiy, af, and norm records
    The returned values are just a list of the IDs (not other metadata)"""
    normIds = []
    afIds = []
    noisyIds = []
    i = 0
    while len(normIds) < numRecs or len(afIds) < numRecs or len(noisyIds) < numRecs:
        currentRecType = labelsMetaDataArr[i][1]
        if currentRecType == 0 and len(normIds) < numRecs:
            normIds.append(labelsMetaDataArr[i][0])  # append the signal filepath
        elif currentRecType == 1 and len(afIds) < numRecs:
            afIds.append(labelsMetaDataArr[i][0])  # append the signal filepath
        elif currentRecType == 2 and len(noisyIds) < numRecs:
            noisyIds.append(labelsMetaDataArr[i][0])  # append the signal filepath

        i += 1
        if i == len(labelsMetaDataArr):
            break
    return normIds, afIds, noisyIds
