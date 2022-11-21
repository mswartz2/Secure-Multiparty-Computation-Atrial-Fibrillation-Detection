# based on example code from Sebastian Goodfellow
import numpy as np
from biosppy.signals import ecg
from biosppy.signals.tools import filter_signal


def extract_templates(signal, sample_rate, rpeaks, before, after):

    # convert delimiters to samples
    before = int(before * sample_rate)
    after = int(after * sample_rate)

    # Sort R-Peaks in ascending order
    rpeaks = np.sort(rpeaks)

    # Get number of sample points in waveform
    length = len(signal)

    # Create empty list for templates
    templates = []

    # Create empty list for new rpeaks that match templates dimension
    rpeaks_new = np.empty(0, dtype=int)

    # Loop through R-Peaks
    for rpeak in rpeaks:

        # Before R-Peak
        a = rpeak - before
        if a < 0:
            continue

        # After R-Peak
        b = rpeak + after
        if b > length:
            break

        # Append template list
        templates.append(signal[a:b])

        # Append new rpeaks list
        rpeaks_new = np.append(rpeaks_new, rpeak)

    # Convert list to numpy array
    templates = np.array(templates).T

    return templates, rpeaks_new


def apply_filter(signal, sample_rate, filter_bandwidth):

    # Calculate filter order
    order = int(0.3 * sample_rate)

    # Filter signal
    signal, _, _ = filter_signal(
        signal=signal,
        ftype="FIR",
        band="bandpass",
        order=order,
        frequency=filter_bandwidth,
        sampling_rate=sample_rate,
    )

    return signal


def pre_process_signal(
    signal_raw,
    sample_rate,
    filter_bandwidth,
    normalize=True,
    polarity_check=True,
    template_before=0.2,
    template_after=0.4,
):

    # Filter signal
    signal_filtered = apply_filter(signal_raw, sample_rate, filter_bandwidth)

    # Get BioSPPy ECG object
    ecg_object = ecg.ecg(signal=signal_raw, sampling_rate=sample_rate, show=False)

    # Get BioSPPy output
    ts = ecg_object["ts"]  # Signal time array
    rpeaks = ecg_object["rpeaks"]  # rpeak indices

    # Get templates and template time array
    templates, rpeaks = extract_templates(
        signal_filtered, sample_rate, rpeaks, template_before, template_after
    )
    templates_ts = np.linspace(
        -template_before, template_after, templates.shape[1], endpoint=False
    )

    # Polarity check
    if polarity_check:

        # Get extremes of median templates
        templates_min = np.min(np.median(templates, axis=1))
        templates_max = np.max(np.median(templates, axis=1))

        if np.abs(templates_min) > np.abs(templates_max):

            # Flip polarity
            signal_raw *= -1
            signal_filtered *= -1
            templates *= -1

    # Normalize waveform
    if normalize:

        # Get median templates max
        templates_max = np.max(np.median(templates, axis=1))

        # Normalize ECG signals
        signal_raw /= templates_max
        signal_filtered /= templates_max
        templates /= templates_max

    return ts, signal_raw, signal_filtered, rpeaks, templates_ts, templates
