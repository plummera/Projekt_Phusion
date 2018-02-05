$(document).ready(function() {
  console.log("Hello!");

  var results1 = $('#profile1 .score');
  var results2 = $('#profile2 .score');
  var watson_results = $('.watson-results');

  for (i=0; i < results1.length; i++) {
    results1[i].outerText.replace('%', '');
    if (parseFloat(results1[i].outerText) <= 50) {
      $('#profile1 .result-' + i).css('border','2px solid red');
      $('#profile1 .result-' + i).remove();
    } else {
      $('#profile1 .result-' + i).css('border','2px solid green');
    };

    $(".result-" + i).hover(function(){
      $(this).css("background-color", "green");
      }, function(){
      $(this).css("background-color", "cadetblue");
    });
  };

  for (i=0; i < results2.length; i++) {
    results2[i].outerText.replace('%', '');
    if (parseFloat(results2[i].outerText) <= 50) {
      $('#profile2 .result2-' + i).css('border','2px solid red');
      $('#profile2 .result2-' + i).remove();
    } else {
      $('#profile2 .result2-' + i).css('border','2px solid green');
    };

    $(".result2-" + i).hover(function(){
      $(this).css("background-color", "green");
      $(this).css('border','2px dotted green');
      }, function(){
      $(this).css("background-color", "cadetblue");
    });
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
      "monero",
      "ripple",
    ];

    function seriously() {

          var txt1 = [
            '<div class="col-md-12">',
            '<p>Help us make the internet a safe environment for everybody. Send  <img id="btc" src="//anthonyplummer.elementfx.com/wp-content/uploads/2017/10/btc-logo-1.png"> to: <a href="#"><span>1EXth6hM97rZAawuGo1CN9Qqc6CmYqgYSG</span></a></p>',
            '</div>',
          ];

          var txt2 = [
            '<div class="col-md-12">',
            '<p>No <img id="btc" src="//anthonyplummer.elementfx.com/wp-content/uploads/2017/10/btc-logo-1.png">? Send <img id="ethereum" src="//anthonyplummer.elementfx.com/wp-content/uploads/2017/10/ethereum-1.png"> to : <span>0x21A9a2Bb60442f943D501b6445Cfd126EF782172</span></p>',
            '</div>',
          ];

          function change() {
            setInterval("$('.btcDonate').css('opacity', '1')", 1000);
            $('.btcDonate').html(txt1);
          }

          txt1 = $('.btcDonate').html();
          if (txt1.match(txt1)) {
            setInterval("$('.btcDonate').css('opacity', '0')", 1000);
            setInterval(change, 7000);
          } else {
            $('.btcDonate').html(txt2);
          };

          $('.btcDonate').css('opacity', '1');

    };

    $('.btcDonate').css('opacity', '0');
    $('footer').css('opacity','0');
    setInterval(seriously, 7775);

  };

  function fadeInBTC() {
    $('.btcDonate').css('opacity', '1');
    donateStream();
  };

  setTimeout(fadeInBTC, 4773);

  if ($(document).width() < 600) {
    $('html').removeClass('video');
  }

  $(document).load(function () {
    $('html').removeAttr('loop');
  });

});
