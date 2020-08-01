import folium
import pandas

#how to improve program 0
#add population per country in the existing feature group (fgp) 
#

 
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
 
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    if 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

 
map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name = "Volcanoes")
 
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius= 20, popup=str(el)+"m", fill_color=color_producer(el), color='black', fill_opactiy=0.9))
 
fgp = folium.FeatureGroup(name = "Population")
 
fgp.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] <= 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'})) #world coordinates for polygon/color by population size


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())


map.save("Map_html_popup_simple.html")