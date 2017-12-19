$(document).ready(function() {
  console.log("Hello!");

  var results1 = $('#profile1 .score');
  var results2 = $('#profile2 .score');
  var watson_results = $('.watson-results');

  for (i=0; i < results1.length; i++) {
    results1[i].outerText.replace('%', '');
    console.log(parseFloat(results1[i].outerText));
    if (parseFloat(results1[i].outerText) <= 50) {
      $('#profile1 .result-' + i).css('border','2px solid red');
    } else {
      $('#profile1 .result-' + i).css('border','2px solid green');
    };
  };

  for (i=0; i < results2.length; i++) {
    results2[i].outerText.replace('%', '');
    console.log(parseFloat(results2[i].outerText));
    if (parseFloat(results2[i].outerText) <= 50) {
      $('#profile2 .result2-' + i).css('border','2px solid red');
    } else {
      $('#profile2 .result2-' + i).css('border','2px solid green');
    };
  };
  //
  // for (i=0; i < watson_results.length; i++) {
  //   watson_results[i].outerText.replace('%', '');
  //   console.log(parseFloat(watson_results[i].outerText));
  //   if (parseFloat(watson_results[i].outerText) > 50) {
  //     p = $('.card-header-results')[i].className;
  //     p = document.getElementsByClassName($('.card-header-results')[i].className);
  //     $(p).css('background-color', 'red');
  //   } else {
  //     p = $('.card-header-results')[i].className;
  //     p = document.getElementsByClassName($('.card-header-results')[i].className);
  //     $(p).css('background-color', 'green');
  //   };
  // };

  function donateStream() {

    var doners = [
      "bitcoin",
      "ethereum",
    ];

    function seriously() {

          var txt = [
            '<p>Help us make the internet a safe environment for everybody. Send  <img id="btc" src="//anthonyplummer.elementfx.com/wp-content/uploads/2017/10/btc-logo-1.png"> to: <a href="#"><span>1EXth6hM97rZAawuGo1CN9Qqc6CmYqgYSG</span></a></p>',
            '<p>No <img id="btc" src="//anthonyplummer.elementfx.com/wp-content/uploads/2017/10/btc-logo-1.png">? Send <img id="ethereum" src="//anthonyplummer.elementfx.com/wp-content/uploads/2017/10/ethereum-1.png"> to : <span>0x21A9a2Bb60442f943D501b6445Cfd126EF782172</span></p>',
          ];

          function change() {
            setInterval("$('.btcDonate').css('opacity', '1')", 1000);
            $('.btcDonate').html(txt[1]);
          }

          txt1 = $('.btcDonate').html();
          if (txt1.match(txt[0])) {
            setInterval("$('.btcDonate').css('opacity', '0')", 1000);
            setInterval(change, 7000);
          } else {
            $('.btcDonate').html(txt[0]);
          };

          $('.btcDonate').css('opacity', '1');

    };

    setTimeout(seriously, 0);
    $('.btcDonate').css('opacity', '0');
    $('footer').css('opacity','0');
    setTimeout(seriously, 7775);

  };

  function fadeInBTC() {
    $('.btcDonate').css('opacity', '1');
    donateStream();
  };

  setTimeout(fadeInBTC, 4773);

});
