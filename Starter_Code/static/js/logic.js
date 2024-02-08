// grab the data
let url = `https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson`;

 // make request
 d3.json(url).then(function (data) {
  console.log(data);

  makeMap(data);
});

// credit to prof booth for code
function makeMap(data) {
  // Step 1: Define your BASE Layers

  // Define variables for our tile layers.
  let street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  })

  let topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
  attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
  });

  // Step 2: Create the OVERLAY (DATA) Layers
  let markers = [];
  let circles = [];

  // Loop through the data.
  for (let i = 0; i < data.features.length; i++){

    // Set the data location property to a variable.
    let row = data.features[i];

    // Check for the location property.
    if (row.geometry) {
      let latitude = row.geometry.coordinates[1];
      let longitude = row.geometry.coordinates[0];
      let location = [latitude, longitude];
      let depth = row.geometry.coordinates[2];

      // Add a new marker to the cluster group, and bind a popup.
      let popup_text = `<h1>${row.properties.title}</h1><br><h1>Depth: ${depth} km</h1><hr><a href = "${row.properties.url}" target="_blank">Link</a>`;
      let magnitude = row.properties.mag;
      let marker = L.marker(location).bindPopup(popup_text);


      // for the marker layer
      markers.push(marker);

      //create a new circle 
      let color;
      if (depth < 10) {
        color = "#63B76C";
      } else if (depth < 30) {
        color = "#FFFF99"; 
      } else if (depth < 50) {
        color = "#FBE7B2"; 
      } else if (depth < 70) {
        color = "#FED85D"; 
      } else if (depth < 90) {
        color = "#EA822C";
        } else {
            color = "EA2C2C";
        } 

        //radius
        let radius = 10000 * (magnitude**2);

        //create a new circle
        let circle = L.circle(location, {
            color:color,
            fillColor: color,
            fillOpacity: 0.75,
            radius: radius
        }).bindPopup(popup_text);

      circles.push(circle);

    }
  }

  let markerLayer = L.layerGroup(markers);
  let circleLayer = L.layerGroup(circles);


  // Step 3: Create the MAP object

  // Create a map object, and set the default layers.
  let myMap = L.map("map", {
    center: [32.7767, -96.7970],
    zoom: 3.5,
    layers: [street, circleLayer]
  });

  // credit to XPERT assistant 
  // Step 4: Add the Layer Controls (Legend goes here too)
  function createLegend() {
    // Create an array of labels for the legend
    let labels = ["<10 km", "10-30 km", "30-50 km", "50-70 km", "70-90 km", ">90 km"];
  
    // Create a div element for the legend
    let legend = L.control({ position: "bottomright" });
  
    // Define the content of the legend
    legend.onAdd = function() {
      let div = L.DomUtil.create("div", "legend");
  
      // Loop through the labels and create a colored square for each
      for (let i = 0; i < labels.length; i++) {
        div.innerHTML +=
          '<i style="background:' + getColor(i) + '"></i> ' + labels[i] + '<br>';
      }
  
      return div;
    };
  
    // Add the legend to the map
    legend.addTo(myMap);
  }
  // Only one base layer can be shown at a time.
  let baseMaps = {
    Street: street,
    Topography: topo
  };

  // Overlays that can be toggled on or off
  let overlayMaps = {
    Markers: markerLayer,
    Circles: circleLayer
  };

  // Pass our map layers into our layer control.
  // Add the layer control to the map.
  L.control.layers(baseMaps, overlayMaps).addTo(myMap);

  // Create the legend
createLegend();

function getColor(depth) {
  switch (depth) {
    case 0:
      return "#63B76C";
    case 1:
      return "#FFFF99";
    case 2:
      return "#FBE7B2";
    case 3:
      return "#FED85D";
    case 4:
      return "#EA822C";
    case 5:
      return "#EA2C2C";
    default:
      return "#000000";
  }
}

}


