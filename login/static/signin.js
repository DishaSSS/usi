$(document).ready(

function(){
  if(check=="True"){
    $('#check').show();
  }
  else{
    $('#check').hide();
  }
  $('input[name="register"]').click(
    function(){
      var s = $(location).attr('href');
      ip = s.replace(s.substring(s.indexOf('8000')+4,s.length),'');
    window.location["href"] = ip+"/post/";
  }
  );
}

);
