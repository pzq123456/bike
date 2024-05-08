import geopandas as gpd
from preprocess import load_track
from cluster import convert_list_to_linestring


track = load_track('H:\\bike\\data\\track16_sim.pickle')
track = [i for i in track if len(i) > 2]
track = convert_list_to_linestring(track)

# save track as geojson
track.to_file('track.geojson', driver='GeoJSON')

