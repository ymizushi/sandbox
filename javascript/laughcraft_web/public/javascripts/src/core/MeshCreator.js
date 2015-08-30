LAUGH.MeshCreator = function (meshInfo) {
  this.meshInfo = meshInfo;
}

LAUGH.MeshCreator.prototype = {
  constructor: LAUGH.MeshCreator,

  create: function () {
    return new Mesh();
  }
}
