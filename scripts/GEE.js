var image;  // image has been imported as a global variable (one band kernel density image)

// m16
// var Min = -43789.04174797;
// var Max = 47493.6070857597;

var Min = -41864.609002553465;
var Max = 41270.14581821809;

Map.addLayer(image, {min: Min, max: Max, palette: ['blue', 'yellow', 'red']}, 'Kernel Density');

// ***Panel*** \\
// set position of panel
var legend = ui.Panel({
  layout: ui.Panel.Layout.flow('vertical'),
  style: {
    position: 'bottom-left',
    padding: '30x 30px',
    color: '000000'
  }
});
 
// Create legend title
var legendTitle = ui.Label({
  value: 'Legend',
  style: {
    fontWeight: 'bold',
    fontSize: '18px',
    margin: '0 0 0 0',
    padding: '0'
    }
});

 // Add the title to the panel
legend.add(legendTitle); 

// create the legend image
var lon = ee.Image.pixelLonLat().select('latitude');
var gradient = lon.multiply((viz.max-viz.min)/100.0).add(viz.min);
var legendImage = gradient.visualize(viz);


// create text on top of legend
var panel = ui.Panel({
    widgets: [
      ui.Label(viz['max'])
    ],
  });

legend.add(panel);
  
// create thumbnail from the image
var thumbnail = ui.Thumbnail({
  image: legendImage,
    params: {bbox:'0,0,10,100', dimensions:'20x200'},  
    style: {padding: '1px', position: 'bottom-center'},
  });

// add the thumbnail to the legend
legend.add(thumbnail);

// create text on top of legend
var panel = ui.Panel({
    widgets: [
      ui.Label(viz['min'])
    ],
   });

legend.add(panel);

Map.add(legend);
