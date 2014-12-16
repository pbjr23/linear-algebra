/*!
 * Start Bootstrap - Agnecy Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 */

// jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});

// Highlight the top nav as scrolling occurs
$('body').scrollspy({
    target: '.navbar-fixed-top'
})

// Closes the Responsive Menu on Menu Item Click
$('.navbar-collapse ul li a').click(function() {
    $('.navbar-toggle:visible').click();
});

$(document).ready(function(){
  $('#contact-submit').click(function(evt) {
    evt.preventDefault();
    var name = $('#name').val();
    var email = $('#email').val();
    var comments = $('#message').val();
    if ((name !== "") && (email!=="") && (comments!=="")) {
    $.ajax({
      url: "https://docs.google.com/forms/d/1XXQWJu-skbOjjehRrDPJ8dAOyGxQv5lImpTi7_kaKHQ/formResponse",
        type: "POST",
        dataType: "xml",
        data: {
          'entry.1445318317' : name,
          'entry.938466652' : email,
          'entry.1687927010' : comments,
          'draftResponse': [,,"-441002587461861719"],
          'pageHistory': 0,
          'fbzx' : -441002587461861719
        },
        statusCode: {
          0: function() {
            $('#contactForm').prepend('<p>Thanks for your feedback - we will get back to you soon!</p>');
            $('#contactForm input, #contactForm textarea').val("");
          },
          200: function(){
            $('#contactForm').prepend('<p>Thanks for your feedback - we will get back to you soon!</p>');
            $('#contactForm input, #contactForm textarea').val("");
          }
       }
    });
    } else {
      $('#contactForm').prepend('<p>Form not complete - please try again.</p>');
    }
  });
});
