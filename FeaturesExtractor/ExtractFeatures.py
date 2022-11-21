# based on example code from Sebastian Goodfellow
import numpy as np
import pandas as pd
import scipy as sp
from statistics import stdev, variance


def extract_waveform_stats():
    # can add to later to improve accuracy
    stats = []

    return stats


def extract_template_stats():
    # can add to later to improve accuracy
    stats = []

    return stats


def extract_hrv_stats(rpeaks, sample_rate):
    stats = []

    # RRI
    rri = np.diff(rpeaks) * 1 / sample_rate
    rri_ts = rpeaks[0:-1] / sample_rate + rri / 2

    # RRI Velocity
    diff_rri = np.diff(rri)
    diff_rri_ts = rri_ts[0:-1] + diff_rri / 2

    # RRI Acceleration
    diff2_rri = np.diff(diff_rri)
    diff2_rri_ts = diff_rri_ts[0:-1] + diff2_rri / 2

    # compute heart rate
    heart_rate_ts = rri_ts
    heart_rate = 60.0 / rri

    # Calculate basic statistics
    if len(heart_rate) > 0:
        heart_rate_min = np.min(heart_rate)
        heart_rate_max = np.max(heart_rate)
        heart_rate_mean = np.mean(heart_rate)
        heart_rate_median = np.median(heart_rate)
        heart_rate_std = np.std(heart_rate, ddof=1)
        heart_rate_skew = sp.stats.skew(heart_rate)
        heart_rate_kurtosis = sp.stats.kurtosis(heart_rate)
    else:
        # TODO: Add removing from the datset here
        heart_rate_min = np.nan
        heart_rate_max = np.nan
        heart_rate_mean = np.nan
        heart_rate_median = np.nan
        heart_rate_std = np.nan
        heart_rate_skew = np.nan
        heart_rate_kurtosis = np.nan

    stats.extend(
        [
            heart_rate_min,
            heart_rate_max,
            heart_rate_mean,
            heart_rate_median,
            heart_rate_std,
            heart_rate_skew,
            heart_rate_kurtosis,
        ]
    )

    return stats


def extract_features(
    sample_rate,
    ts,
    signal_filtered,
    rpeaks,
    templates_ts,
    templates,
    template_before,
    template_after,
):

    features = extract_hrv_stats(rpeaks, sample_rate)

    return features
