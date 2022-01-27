import streamlit as st
from streamlit_folium import folium_static
import geopandas as gpd
import folium
from folium import plugins
from PIL import Image

st.set_page_config(page_title='Tana Web GIS', layout = 'wide', page_icon=":shark:")

# loading the png image
img = Image.open("./img/tana.png")

# removing menu and footer note
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden; }
    footer {visibility: hidden; }
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html = True)


st.image(img, width=700)
st.write("""
####         A map displaying projects under TWWDA coverage area

*To view in fullscreen, press the icon below the - zoom button*
""")

# point layers
ADB = gpd.read_file("./data/adb_new.geojson")
uhc = gpd.read_file("./data/uhc_new.geojson")
bq = gpd.read_file("./data/bq.geojson")
cc = gpd.read_file("./data/crosscounty.geojson")
drill = gpd.read_file("./data/drill_n_pumping.geojson")


 # loading polygon layers
forest = gpd.read_file("./data/Forest Cover.geojson")
mawasco = gpd.read_file("./data/Mawasco.geojson")
mathira = gpd.read_file("./data/Mathira.geojson")
mewass = gpd.read_file("./data/Mewass.geojson")
Imetha = gpd.read_file("./data/Imetha.geojson")
Kiriwasco = gpd.read_file("./data/Kiriwasco.geojson")
Kyeni = gpd.read_file("./data/Kyeniwasco.geojson")
MDE = gpd.read_file("./data/Multipurpose dams in Embu.geojson")
MM = gpd.read_file("./data/Murugi-Mugumango.geojson")
Muthambi = gpd.read_file("./data/Muthambi_4K.geojson")
Naruwasco = gpd.read_file("./data/Naruwasco.geojson")
Ndamunge = gpd.read_file("./data/Ndamunge.geojson")
NN = gpd.read_file("./data/Nginda Ngandori.geojson")
Nithi = gpd.read_file("./data/Nithiwasco.geojson")
Nyewasco = gpd.read_file("./data/Nyewasco.geojson")
Omwasco = gpd.read_file("./data/Omwasco.geojson")
RW = gpd.read_file("./data/Rukanga WSP.geojson")
TW = gpd.read_file("./data/Teawasco.geojson")
Kenya = gpd.read_file("./data/Counties.geojson")      

# the code 
# FINAL MAP WITH COMBINED POINT LAYERS

m = folium.Map(location=[-1.266, 37.999], min_zoom=5, zoom_start=6, control_scale=True)

# preliminaries
ht = '<strong style="color:red;">Name</strong>: {} <br><p> <strong>Scope</strong>: {} <br><p> <strong>Population to be Served</strong>: {} <br><p> <strong>Progress%</strong>: {}'
ht_2 = '<strong style="color:red;">Name</strong>: {} <br><p> <strong>Scope</strong>: {} <br><p> <strong>Population to be Served</strong>: {} <br><p> <strong>Drilled Depth</strong>: {} <br><p> <strong>Yield m3/h</strong>: {} <br><p> <strong>Progress%</strong>: {}'

# loading the cluster layers
# cluster for adb project
cluster_adb = plugins.MarkerCluster(name='Africa Development Bank Projects').add_to(m)
for _, r in ADB.iterrows():
    lat = r['LAT']
    lon = r['LONG']
    folium.Marker(location=[lat, lon],
                  tooltip='Click for ADB',
                  popup=folium.Popup(html = ht.format(r['NAME'], r['SCOPE'], r['POPULATION'], r['PROGRESS %']), max_width=300),
                  icon=folium.Icon(color='red', icon='glyphicon-tint', prefix='glyphicon')).add_to(cluster_adb)

# cluster for cc
cluster_cc = plugins.MarkerCluster(name='Cross County Projects').add_to(m)
for _, r in cc.iterrows():
    lat = r['LAT']
    lon = r['LONG']
    folium.Marker(location=[lat, lon],
                  tooltip='Click for CC',
                  popup=folium.Popup(html = ht.format(r['NAME'], r['SCOPE'], r['POPULATION'], r['PROGRESS %']), max_width=300),
                  icon=folium.Icon(color='gray', icon='glyphicon-tint', prefix='glyphicon')).add_to(cluster_cc)

# updated uhc
cluster_uhc_new = plugins.MarkerCluster(name='Universal Health Care Projects').add_to(m)
for _, r in uhc.iterrows():
    lat = r['LAT']
    lon = r['LONG']
    folium.Marker(location=[lat, lon],
                  tooltip='Click for UHC',
                  popup=folium.Popup(html = ht.format(r['NAME'], r['SCOPE'], r['POPULATION'], r['PROGRESS %']), max_width=300),
                  icon=folium.Icon(color='darkpurple', icon='glyphicon-tint', prefix='glyphicon')).add_to(cluster_uhc_new)

# try for borehole drilling
cluster_drill = plugins.MarkerCluster(name='Drilling and Test Pumping projects').add_to(m)
for _, r in drill.iterrows():
    lat = r['LAT']
    lon = r['LONG']
    folium.Marker(location=[lat, lon],
                  tooltip='Click for BH drilling',
                  popup=folium.Popup(html = ht_2.format(r['NAME'], r['SCOPE'], r['POPULATION'], r['DRILLED DEPTH(M)'], r['YIELD M3 /H'], r['PROGRESS %']), max_width=300),
                  icon=folium.Icon(color='orange', icon='glyphicon-tint', prefix='glyphicon')).add_to(cluster_drill)

# clustering bq
cluster_bq = plugins.MarkerCluster(name='Borehole Equiping Projects').add_to(m)
for _, r in bq.iterrows():
    lat = r['LAT']
    lon = r['LONG']
    folium.Marker(location=[lat, lon],
                  tooltip='Click for BQ',
                  popup=folium.Popup(html = ht.format(r['NAME'], r['SCOPE'], r['POPULATION'], r['PROGRESS %']), max_width=300),
                  icon=folium.Icon(color='blue', icon='glyphicon-tint', prefix='glyphicon')).add_to(cluster_bq)


# loading vector layer
style_1 = {'fillColor': '#00FF00', 'color': '#78AB46'}    
forest_cover = folium.GeoJson(forest, name='Forest Cover', style_function= lambda x: style_1, control=False).add_to(m)

style_2 = {'fillColor': '#FFA500', 'color': '#FF8C00'}
Mawasco = folium.GeoJson(mawasco, name='Mawasco WSC', style_function= lambda x: style_2, tooltip='click for Mawasco').add_to(m)

style_3 = {'fillColor': '#CD853F', 'color': '#CD853F'}
Mathira = folium.GeoJson(mathira, name='Mathira WSC', style_function= lambda x: style_3, tooltip='click for Mathira').add_to(m)

Mewass = folium.GeoJson(mewass, name='MEWASS', style_function= lambda x: style_3, tooltip='click for Mewass').add_to(m)

imetha = folium.GeoJson(Imetha, name='Imetha', style_function = lambda x: style_3, tooltip='click for Imetha').add_to(m)

kiriwasco = folium.GeoJson(Kiriwasco, name='Kiriwasco', style_function = lambda x: style_3, tooltip='click for Kiriwasco').add_to(m)

kyeni = folium.GeoJson(Kyeni, name='Kyeni', style_function = lambda x: style_3, tooltip='click for Kyeni').add_to(m)

mde = folium.GeoJson(MDE, name='Multipurpose Dams in Embu', style_function = lambda x: style_3, tooltip='click for MDE').add_to(m)

mm = folium.GeoJson(MM, name='Murugi-Mugumango', style_function = lambda x: style_3, tooltip='click for MM').add_to(m)

muthambi = folium.GeoJson(Muthambi, name='Muthambi', style_function = lambda x: style_3, tooltip='click for Muthambi').add_to(m)

naruwasco = folium.GeoJson(Naruwasco, name='Naruwasco', style_function = lambda x: style_3, tooltip='click for Naruwasco').add_to(m)

ndamunge = folium.GeoJson(Ndamunge, name='Ndamunge', style_function = lambda x: style_3, tooltip='click for Ndamunge').add_to(m)

nn = folium.GeoJson(NN, name='Nginda Ngandori', style_function = lambda x: style_3, tooltip='click for NN').add_to(m)

nithi = folium.GeoJson(Nithi, name='Nithi', style_function = lambda x: style_3, tooltip='click for Nithi').add_to(m)

nyewasco = folium.GeoJson(Nyewasco, name='Nyewasco', style_function = lambda x: style_3, tooltip='click for Nyewasco').add_to(m)

omwasco = folium.GeoJson(Omwasco, name='Omwasco', style_function = lambda x: style_3, tooltip='click for Omwasco').add_to(m)

rw = folium.GeoJson(RW, name='Rukanga', style_function = lambda x: style_3, tooltip='click for Rukanga').add_to(m)

tw = folium.GeoJson(TW, name='Teawasco', style_function = lambda x: style_3, tooltip='click for Teawasco').add_to(m)

style_19 = {'fillColor': '#FFFFFF', 'color': '#696969'}
kenya = folium.GeoJson(Kenya, name='Counties',
                       style_function = lambda x: {
                           'color': 'black',
                           'weight': 1,
                           "opacity": 1,
                           'fillOpacity': 0,
                           'interactive': False
                       },
                       control=True).add_to(m)


# adding basemap layers
folium.raster_layers.TileLayer('Open Street Map').add_to(m)
folium.raster_layers.TileLayer('Stamen Terrain').add_to(m)
folium.raster_layers.TileLayer('Stamen Toner').add_to(m)
folium.raster_layers.TileLayer('Stamen Watercolor').add_to(m)
folium.raster_layers.TileLayer('Cartodb Positron').add_to(m)
folium.raster_layers.TileLayer('Cartodb Dark_Matter').add_to(m)


# adding functionalities to the map
# mini map, scrol zoom, drawing tools, measure tools, tile layers, 
# plugin for mini map
#mini_map = plugins.MiniMap(tile_layer='cartodb positron', 
#                           position='bottomright')

# adding the mini map to the main map
#m.add_child(mini_map)

# add full screen toggle button
plugins.Fullscreen(position='topleft').add_to(m)


# adding the drawing tools
draw = plugins.Draw(export=True)

m.add_child(draw)

#########################
## adding the measure tools
measure_control = plugins.MeasureControl(position='topleft',
                                        active_color='red',
                                        completed_color='green',
                                        primary_area_unit='meters')


m.add_child(measure_control)


# add lat and long tool to the map
m.add_child(folium.LatLngPopup())



folium.LayerControl().add_to(m)

# final display
folium_static(m, width=1200, height=600)
