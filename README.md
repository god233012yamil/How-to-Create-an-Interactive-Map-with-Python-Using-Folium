# Interactive Map with Custom Layers using Folium

This project demonstrates how to create an interactive map with multiple customizable layers using the Python library `folium`. The map allows users to switch between different map views such as street view, terrain, satellite, and hybrid, all using a simple control interface.

With Folium, you can create visually engaging maps with minimal code, providing an intuitive interface for users to interact with geographical data. Whether you’re building a simple map or a full-featured mapping application, Folium simplifies the process by leveraging the JavaScript-based Leaflet library in Python.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Map Layers Included](#map-layers-included)
- [How It Works](#how-it-works)
- [License](#license)

## Project Overview

This project builds an interactive map centered on New York City, utilizing the Python `folium` library to create different map layers. The map includes layers such as OpenStreetMap, CartoDB Positron, OpenTopoMap (Terrain), Esri Satellite, and Google Hybrid (Satellite + Labels).

You can view the generated map in a browser and toggle between the layers with ease. This project serves as an example for anyone interested in learning how to create interactive maps with Python.

![image](https://github.com/user-attachments/assets/316213d5-2b6f-421f-a1d4-9765cfd0e342)

## Technologies Used

- **Python 3.7+**
- **Folium** (A Python wrapper for Leaflet.js)
- **Web Browser** (For displaying the generated map)

## Features

- Interactive map centered on New York City.
- Multiple map layers: OpenStreetMap, CartoDB Positron, Terrain, Satellite, and Google Hybrid.
- Layer control widget for easy switching between map layers.
- Automatically opens the generated map in the browser.
  
## Installation

### Prerequisites
Before running the project, ensure you have Python installed on your system. You can download Python [here](https://www.python.org/downloads/).

### Step-by-Step Installation

1. **Clone the repository**:
   
   git clone https://github.com/yourusername/folium-interactive-map.git

2. **Navigate to the project directory**:

   cd folium-interactive-map

3. **Install dependencies**:

   Install the required folium module using pip:
   pip install folium

## Usage

To create the interactive map, simply run the provided Python script:
python Folium_Customizing_Map_Layers.py

This will generate an HTML file (map_with_working_layers.html) that contains the interactive map. The map will automatically open in your default web browser.

## Map Layers Included

The project includes the following map layers, which can be toggled via the control interface:

1. **OpenStreetMap** (Default street view layer)
2. **CartoDB Positron** (A light, minimalistic street view layer)
3. **Terrain (OpenTopoMap)** (Topographical map for viewing terrain features)
4. **Satellite** (Esri's high-resolution satellite imagery)
5. **Google Hybrid** (Satellite imagery with street labels)

## How It Works

The core functionality is built using the folium library. The interactive map is centered on a specific geographic location (New York City) with multiple layers added for users to switch between:

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE License - see the LICENSE file for details.

You can just modify the content to suit your GitHub repository's structure, such as adjusting the installation section based on your package manager or dependencies.

