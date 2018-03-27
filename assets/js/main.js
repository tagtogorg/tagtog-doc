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

  var isChrome = /Chrome/.test(navigator.userAgent) && /Google Inc/.test(navigator.vendor);
  var isSafari = /Safari/.test(navigator.userAgent);
  if (window.location.hash && (isChrome||isSafari)) {
    setTimeout(function () {
      var hash = window.location.hash;
      window.location.hash = "";
      window.location.hash = hash;
    }, 300);
  }
});