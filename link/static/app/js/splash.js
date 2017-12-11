$(document).ready(function() {
  console.log("Hello!");

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
