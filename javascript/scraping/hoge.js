var page = require('webpage').create();
var url = 'http://imsingle.tv/search/turnout/q/2229/t/1/';

page.onConsoleMessage = function (msg) {
  console.log("console>" + msg);
}

page.open(url, function(status) {
  page.includeJs('http://code.jquery.com/jquery-1.9.1.min.js', function() {
     page.evaluate(function() {
       var piyo = jQuery.ajax({
              url: 'http://imsingle.tv/search/turnout/q/2229/t/1/',
              cache : false,
              data: {
                  ajax: '1',
                  nh: '1'
              },
              success: function( data ) {
                console.log("fuga");
              },
              error: function( data ) {
                console.log("piyo");
              }
            });
            console.log(piyo['responseText']);
      });
    phantom.exit();
  });
});
