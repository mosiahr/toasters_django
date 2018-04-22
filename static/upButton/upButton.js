$(document).ready(function($) {
  
  var btn = $('#upBtn');

  $(window).scroll(function() {
	if ($(this).scrollTop() > 300) {
        btn.fadeIn();
    } else {
        btn.fadeOut();
    }
  });

  btn.on('click', function(e) {
    e.preventDefault();
    $('html, body').animate({scrollTop:0}, '300');
  });

});


