import streamlit as st
import pickle
import folium
from streamlit_folium import st_folium
import polyline

from utils.geocoder import get_coordinates
from utils.route_fetcher import get_routes

# Load ML model
model = pickle.load(open("models/model.pkl", "rb"))

st.title("🚦 Smart AI Route Planner")

# Inputs
start = st.text_input("Enter start location")
dest = st.text_input("Enter destination")

# Button sets state
if st.button("Find Routes"):
    st.session_state["run"] = True

# MAIN LOGIC OUTSIDE BUTTON ✅
if "run" in st.session_state:

    if start == "" or dest == "":
        st.warning("Please enter both locations")
        st.stop()

    # Convert to coordinates
    start_coords = get_coordinates(start)
    dest_coords = get_coordinates(dest)

    if start_coords is None or dest_coords is None:
        st.error("Location not found. Try a more specific place.")
        st.stop()

    # Fetch routes
    routes = get_routes(start_coords, dest_coords)

    if len(routes) == 0:
        st.error("Unable to fetch routes. Please try again.")
        st.stop()

    results = []

    for route in routes:

        distance = route["summary"]["distance"] / 1000
        duration = route["summary"]["duration"] / 60

        predicted_time = model.predict([[distance, duration]])[0]

        geometry = route["geometry"]

        results.append({
            "distance": distance,
            "time": predicted_time,
            "geometry": geometry
        })

    # Sort routes
    results = sorted(results, key=lambda x: x["time"])

    # Display results
    st.subheader("📊 Route Comparison")

    for i, r in enumerate(results):
        st.write(f"### Route {i+1}")
        st.write(f"Distance: {round(r['distance'], 2)} km")
        st.write(f"Estimated Time: {round(r['time'], 2)} minutes")
        st.write("---")

    st.success("Best route is highlighted in green on the map")

    # Create map
    map = folium.Map(location=start_coords, zoom_start=12)

    colors = ["green", "blue", "red"]

    for i, route in enumerate(results):

        coords = polyline.decode(route["geometry"])

        folium.PolyLine(
            locations=coords,
            color=colors[i],
            weight=5,
            opacity=0.8,
            tooltip=f"Route {i+1}: {round(route['time'],2)} min"
        ).add_to(map)

    # Markers
    folium.Marker(start_coords, tooltip="Start").add_to(map)
    folium.Marker(dest_coords, tooltip="Destination").add_to(map)

    # Show map
    st.subheader("🗺 Route Map")
    st_folium(map, width=700, height=500)