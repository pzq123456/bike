let List = [[121.47620086950215,31.260364670274015],
[121.54623871129903,31.260364670274015],
[121.54623871129903,31.33077321098865],
[121.47620086950215,31.33077321098865],
[121.47620086950215,31.260364670274015]]

let Colorado = RVGeo.toLineString(List.map((p) => new RVGeo.Point([p[0],p[1]]))); // 科罗拉多州边界（粗略）
let area = RVGeo.EPSG3857.area(Colorado.coordinates);
console.log(area);
console.log(sqm2sqkm(area));

function sqm2sqkm(sqm) {
    return sqm / 1000000;
}
