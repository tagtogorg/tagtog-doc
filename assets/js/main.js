$(document).ready(function() {
  $(".tabs-menu a").click(function(event) {
      event.preventDefault();
      $(this).parent().addClass("current");
      $(this).parent().siblings().removeClass("current");
      var tab = $(this).attr("href");
      $(tab).siblings(".tab-content").css("display", "none");
      $(tab).fadeIn();
  });
  var anchors = new AnchorJS();
  anchors.add();

});