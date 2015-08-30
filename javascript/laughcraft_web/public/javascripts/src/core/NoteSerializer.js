LAUGH.NoteBuilder = function (noteData) {
    this.noteData = noteData;
}
LAUGH.NoteBuilder.prototype = {
    constructor: LAUGH.NoteBuilder,

    serialize: function () {
        return this.parseJson(this.scoreData);
    },

    getScore: function () {
        var json = this.serialize();
        for (var i=0; i < json.length; ++i) {
        }
    },

    parseJson: function () {
        return;
    }

}

