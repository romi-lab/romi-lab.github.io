window.setInterval(function() {

  var current = new Date();
  var expiry = new Date("March 7, 2024 14:59:00")

  if (current.getTime() < expiry.getTime()) {
    $('.questions').hide();
    $('.holdon').show();

  } else if (current.getTime() > expiry.getTime()) {
    $('.questions').show();
    $('.holdon').hide();
  }

}, 0);
