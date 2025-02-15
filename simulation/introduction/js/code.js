$(document).ready(function () {

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

});

window.setInterval(function() {

  var current = new Date();
  var expiry = new Date("February 15, 2025 21:30:00")

  if (current.getTime() < expiry.getTime()) {
    $('.questions').hide();
    $('.holdon').show();

  } else if (current.getTime() > expiry.getTime()) {
    $('.questions').show();
    $('.holdon').hide();
  }

}, 0);