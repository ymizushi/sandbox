LAUGH.CubeMesh = function (size, position, color) {
  var geometry = new THREE.BoxGeometry(size.x, size.y, size.z);
  this.position = position;
  this.material = new THREE.MeshLambertMaterial({color:color, shading:THREE.FlatShading, overdraw:0.5});
}

LAUGH.CubeMesh.prototype = {
  constructor: LAUGH.CubeMesh,

  create: function () {
    var mesh = new THREE.Mesh(this.geometry, this.material);
    mesh.position = this.position
  }
}

