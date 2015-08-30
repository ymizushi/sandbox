LAUGH.api.Json = function (url, method, data) {
    this.url = url;
    this.method = method;
    this.data = data;
}
LAUGH.api.Json.prototype = {
  constructor: LAUGH.api.Json,
  fetch: function () {
    var sample = {
      "synth" : [
        {
          "synthDef": {}
        }
      ],
      "score" : [
        {
          "stepNum": 1,
          "synthNum": 1,
          "meshId": 1,
          "key": "G1",
        },
        {
          "stepNum": 2,
          "synthNum": 1,
          "meshId": 1,
          "key": "E1",
          "synthDef":{ }
        },
        {
          "stepNum": 3,
          "synthNum": 1,
          "meshId": 1,
          "key": "D1",
          "synthDef":{ }
        }
      ]
    }
  }
}
