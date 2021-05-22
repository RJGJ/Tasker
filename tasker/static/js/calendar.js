$("#calendar-toggler").click(() => {
  const calContainer = $("#calendar-container");

  var attr = calContainer.attr("visible");

  if (typeof attr !== undefined && attr !== false && attr !== "") {
    // reverse chevron icon
    $("#calendar-toggler").html('calendar <i class="fas fa-chevron-up"></i>');

    calContainer.attr("visible", "");
    calContainer.css("display", "inherit");
  } else {
    // reverse chevron icon
    $("#calendar-toggler").html('calendar <i class="fas fa-chevron-down"></i>');

    calContainer.removeAttr("visible");
    calContainer.css("display", "none");
  }
});
