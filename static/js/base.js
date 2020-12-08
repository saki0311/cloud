$(document).ready(function() {
    $("#open_btn").on("click", function(e) {
        e.preventDefault();
        $("#e_modal").addClass("active");
  
        $("#close_btn").on("click", function() {
            $("#e_modal").removeClass("active");
            return false;
        });
    });
  });