import numpy as np
from sklearn.cluster import DBSCAN

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Haversine distance in km.
    """
    R = 6371
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    return R * c

def cluster_blooms(points, epsilon_km=10, min_pts=3):
    """
    Cluster bloom points using DBSCAN with Haversine metric.
    points: [{'lat': float, 'lon': float, ...}]
    Returns cluster labels.
    """
    coords = np.array([[p['lat'], p['lon']] for p in points])
    # Convert lat/lon to radians for Haversine
    kms_per_radian = 6371
    db = DBSCAN(eps=epsilon_km/kms_per_radian, min_samples=min_pts, metric='haversine')
    labels = db.fit_predict(np.radians(coords))
    return labels.tolist()