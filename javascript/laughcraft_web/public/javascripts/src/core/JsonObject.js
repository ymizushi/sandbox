var LAUGH;
(function (LAUGH) {
  var JsonRequestor = function () {
    var JsonRequestor = function (data) {
      this.data = data;
    };

    JsonRequestor.prototype.fetch = function (urlString) {
      var score;
      $.ajax(
        { async: false,
          type: "GET",
          url: urlString,
          success: function (json) {
            score = json
          }
        }
      );
      return score;
    };
    return JsonRequestor;
  }();
  LAUGH.JsonRequestor = JsonRequestor;
})(LAUGH || (LAUGH = {}));
