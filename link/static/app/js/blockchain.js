$(document).ready(function() {

  for (thing in $('.cryptoplayer h3')) {
    if ($('.cryptoplayer h3')[thing].outerHTML == "<h3>Market Cap: N/A</h3>") {
      ($('.cryptoplayer')[thing]).addClass('hidden');
    };
  };

  function protoss(request) {
    window.location = 'https://'+window.location.hostname+':8443'
  };

});
