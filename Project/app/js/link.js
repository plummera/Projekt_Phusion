function updateScroll(){
    var element = document.getElementById("portal");
    element.scrollTop = element.scrollHeight;
}

function navBarRelat(){
  var element = document.getElementById("dontClick");
}

function greenLightIfSuccessful() {
  var element = $("#hit");
  element.fadeIn(2);
  element.fadeOut(4);
  element.fadeIn(16);
  element.fadeOut(32);
  element.fadeIn(64);
  element.fadeOut(128);
  element.fadeIn(256);
  element.fadeOut(512);
  element.fadeIn(1024);
  element.fadeOut(2048);
}

function redLightIfUnsuccessful() {
  var element = $("#miss");
  element.fadeIn(2);
  element.fadeOut(2);
  element.fadeIn(4);
  element.fadeOut(4);
  element.fadeIn(16);
  element.fadeOut(16);
  element.fadeIn(32);
  element.fadeOut(32);
  element.fadeIn(64);
  element.fadeOut(64);
}

function lightIndicator() {
  if ($("#portal li")[0].outerText == "Connected!") {
    $("#hit").removeClass("hidden");
    setInterval(greenLightIfSuccessful, 500);
  } else {
    $("#miss").removeClass("hidden");
    setInterval(redLightIfUnsuccessful, 500);
  }
}

setInterval(updateScroll, 500);
setInterval(lightIndicator, 500);
