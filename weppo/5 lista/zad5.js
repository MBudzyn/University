var http = require('https');
http.get('https://www.google.com', function(resp) {
 var buf = '';
 resp.on('data', function(data) {
 buf += data.toString();
 });

 resp.on('end', function() {
 console.log( buf );
 });
});