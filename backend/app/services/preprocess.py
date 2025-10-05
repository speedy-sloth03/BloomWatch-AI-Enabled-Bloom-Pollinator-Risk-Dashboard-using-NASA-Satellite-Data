import numpy as np
from scipy.signal import savgol_filter

def smooth_ndvi_series(ndvi_series, window=3, poly=2):
    """
    Smooth NDVI series using Savitzky–Golay filter.
    """
    ndvi_vals = np.array([v['ndvi'] for v in ndvi_series])
    if len(ndvi_vals) < window:
        return ndvi_vals
    smoothed = savgol_filter(ndvi_vals, window_length=window, polyorder=poly)
    return smoothed.tolist()

def find_bloom_onset(smoothed_ndvi, threshold=0.1, ndvi_threshold=0.5, min_periods=2):
    """
    Detect bloom onset: first index where derivative > threshold AND NDVI > ndvi_threshold for n periods.
    """
    deriv = np.diff(smoothed_ndvi)
    for i in range(min_periods, len(deriv)):
        if all(deriv[j] > threshold and smoothed_ndvi[j] > ndvi_threshold for j in range(i-min_periods, i)):
            return i
    return None