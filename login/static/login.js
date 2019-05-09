$(document).ready(function() {
  var s = $(location).attr("href");
  ip = s.replace(s.substring(s.indexOf("8000") + 4, s.length), "");

  str =
    '<div class="loader" hidden> <div class="cssload-container">	<div class="cssload-shaft1"></div>	<div class="cssload-shaft2"></div>	<div class="cssload-shaft3"></div>	<div class="cssload-shaft4"></div>	<div class="cssload-shaft5"></div>	<div class="cssload-shaft6"></div>	<div class="cssload-shaft7"></div>	<div class="cssload-shaft8"></div><div class="cssload-shaft9"></div><div class="cssload-shaft10"></div></div></div><div id="addText"></div>';
  var person = {
    regid: regid,
    passw: passw
  };
  $.ajax({
    url: ip + "/post/api/attend/",
    type: "POST",
    dataType: "json",
    data: person,
    success: function(data, textStatus, xhr) {
      $("title").text("HI " + data["name"] + "!");
      $("h2.greet").text("HI " + data["name"] + "!");

      $(
        "<table><tr><th>ID</th> <th>Course Code</th> <th>Subject</th> <th>Course Credits</th> <th>Attendance</th> <th>Attendance(%)</th> </th>"
      ).appendTo("#container");
      for (i = 0, len = data["lis"].length; i < len; i++) {
        $(
          "<tr><td>" +
            data["lis"][i]["id"] +
            "</td><td>" +
            data["lis"][i]["code"] +
            "</td><td>" +
            data["lis"][i]["subject"] +
            "</td><td>" +
            data["lis"][i]["credit"] +
            "</td><td>" +
            data["lis"][i]["total"] +
            "</td><td>" +
            data["lis"][i]["percent"] +
            "</td></tr>"
        ).appendTo("table");
      }

      $("</table>").appendTo("#container");
    },
    beforeSend: function() {
      $("#attend").show();
    },
    complete: function() {
      $("#attend").hide();
    }
  });
  var person2 = {
    mood_reg: mood_reg,
    mood_passw: mood_passw
  };
  $.ajax({
    url: ip + "/post/api/moodle/",
    type: "POST",
    dataType: "json",
    data: person2,
    success: function(data, textStatus, xhr) {
      $("h3")
        .eq(0)
        .html('Events to be completed<i class="material-icons">event</i>');

      if (data["events"] == "NO") {
        $("h3")[0].after("<p>No events anytime soon.</p>");
      } else {
        var rt = "";
        rt += "<ul>";
        for (i = 0, len = data["temp"].length; i < len; i++) {
          rt +=
            "<li><a value='" +
            data["temp1"][i] +
            "' class='todo'>" +
            data["temp"][i] +
            str +
            " </a> <div id='addText'></div></li>";
        }
        rt += "</ul>";

        $("#event").html(rt);
      }
      $("h3")
        .eq(1)
        .html(
          'Events in this month<i class="material-icons">calendar_today</i>'
        );

      if (data["isimp"] == "NO") {
        $("h3")[1].after("<p>No events anytime soon.</p>");
      } else {
        var rt1 = "";
        rt1 += "<ul class='month'><ul>";
        for (i = 0, len = data["text"].length; i < len; i++) {
          if (data["date"][i] == data["date"][i - 1] && i != 0) {
            rt1 +=
              "<li><a value='" +
              data["links"][i] +
              "' class='todo'>" +
              data["text"][i] +
              "</a></li>";
          } else {
            rt1 +=
              "<p>" +
              data["date"][i] +
              "</p><ul><li><a value='" +
              data["links"][i] +
              "' class='todo'>" +
              data["text"][i] +
              "</a></li>";
          }
          rt1 += "</ul>";
        }

        rt1 += "</ul></ul>";

        $("#month").html(rt1);
      }
    },
    beforeSend: function() {
      $("#mood-load").show();
    },
    complete: function() {
      $("#mood-load").hide();
    }
  });

  $("#event").on("click", "a", function(event) {
    console.log("success:  " + ip);
    console.log();
    $(event.target)
      .find("table")
      .remove();
    console.log($(event.target).find("table"));
    var person = {
      hr: $(event.target).attr("value"),
      mood_reg: mood_reg,
      mood_passw: mood_passw
    };
    $.ajax({
      url: ip + "/post/api/assign/",
      type: "POST",
      dataType: "json",
      data: person,
      success: function(data, textStatus, xhr) {
        console.log("success:  " + ip);
        $(event.target).append("<table>");
        for (i = 0, len = data["leftSide"].length; i < len; i++) {
          $(event.target)
            .children("table")
            .append(
              "<tr><td>" +
                data["leftSide"][i] +
                "</td><td>" +
                data["rightSide"][i] +
                "</td></tr>"
            );
        }
        $(event.target).append("</table>");
      },
      beforeSend: function() {
        $(event.target)
          .children(".loader")
          .show();
      },
      complete: function() {
        $(event.target)
          .children(".loader")
          .hide();
      }
    });
  });

  $("#event").mouseenter(function(event) {
    $(event.target).css({ "text-decoration": "underline wavy blue" });
  });
  $("#event").mouseout(function(event) {
    $(event.target).css({ "text-decoration": "none" });
  });

  function erp() {}
});
