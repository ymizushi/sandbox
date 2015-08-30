describe("Pianoroll test", function() {
  it("constructor", function() {
    expect(LAUGH.Pianoroll.KEYMAP['C1']).toBe(1);
    expect(new LAUGH.Pianoroll() instanceof LAUGH.Pianoroll).toBe(true);
  });
});
