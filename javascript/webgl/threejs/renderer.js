// Our Javascript will go here.
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );
camera.position.z = 5;

var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

// var geometry = new THREE.CubeGeometry(1,1,1);
// var material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
// var cube = new THREE.Mesh( geometry, material );
// scene.add( cube );

var Point = function (x, y ,z) {
    this.x = x;
    this.y = y;
    this.z = z;
}

var Size = function (width, height, depth) {
    this.width = width;
    this.height = height;
    this.depth = depth;
}

var Box = function (point, size) {
    var geometry = new THREE.CubeGeometry(point.x, point.y, point.z)
    var material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
    this.cube     = new THREE.Mesh(geometry, material);
}

var boxes = [];
var geometry;
var material;
var cube;

for (var j=0; j<5; j++) {
    for (var i=0; i < 5; i++) {
        geometry = new THREE.CubeGeometry(1,1,1);
        material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
        cube = new THREE.Mesh(geometry, material);
        cube.position.x = i*2
        cube.position.y = j*2
        boxes.push(cube);
        scene.add( cube );
    }
}

function render() {
    requestAnimationFrame(render);
    renderer.render(scene, camera);
    for (var index in boxes) {
        boxes[index].rotation.x += 0.05;
        boxes[index].rotation.y += 0.05;
    }
}
render();
