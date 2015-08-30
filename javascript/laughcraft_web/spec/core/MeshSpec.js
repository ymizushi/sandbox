describe("Mesh test", function() {
  it("constructor", function() {
    geometry = new LAUGH.Geometry();
    material = new LAUGH.Material();
    var mesh = new LAUGH.Mesh(geometry, material);
    expect(mesh.geometry instanceof LAUGH.Geometry).toBe(true);
    expect(mesh.material instanceof LAUGH.Material).toBe(true);
  });
});

