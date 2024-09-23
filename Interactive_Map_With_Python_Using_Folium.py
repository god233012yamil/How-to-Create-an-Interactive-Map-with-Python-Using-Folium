import folium
import webbrowser

# Create a map centered at New York City
m = folium.Map(location=[40.7128, -74.0060], zoom_start=10)

# Add OpenStreetMap layer (Default Street View)
folium.TileLayer('OpenStreetMap', name='OpenStreetMap').add_to(m)

# Add CartoDB Positron (Light Street View)
folium.TileLayer(
    tiles='https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
    attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
    name='CartoDB Positron'
).add_to(m)

# Add Terrain layer (using OpenTopoMap as an alternative)
folium.TileLayer(
    tiles='https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
    attr='Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)',
    name='Terrain (OpenTopoMap)'
).add_to(m)

# Add Satellite layer
folium.TileLayer(
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    attr='Esri',
    name='Satellite'
).add_to(m)

# Add Hybrid layer (Satellite with labels)
folium.TileLayer(
    tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
    attr='Google',
    name='Google Hybrid'
).add_to(m)

# Add layer control to switch between layers
folium.LayerControl().add_to(m)

# Save the map
m.save("map_with_working_layers.html")

# Automatically open the map in the default web browser
webbrowser.open("map_with_working_layers.html")