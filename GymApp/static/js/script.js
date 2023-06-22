$(document).ready(function() {
    $(".dropdown-toggle").click(function(e) {
      e.preventDefault();
      $(this).siblings(".dropdown-menu").toggle();
    });
  });
  