$(document).ready(


function(){
  var s = $(location).attr('href');
  ip = s.replace(s.substring(s.indexOf('8000')+4,s.length),'');
  $('#id_password_conf').keyup(
    function(){
      if($('#id_password').val()!="" && ($('#id_password').val()!=$('#id_password_conf').val()))
        $('#matchpass').text("Passwords don't match");
      else {
        $('#matchpass').text('');

      }
    }

  );
  $('#id_password').keyup(
    function(){
      if($('#id_password_conf').val()!="" && ($('#id_password').val()!=$('#id_password_conf').val()))
        $('#matchpass').text("Passwords don't match");
      else {
        $('#matchpass').text('');

      }
    }

  );
  $('#id_username').keyup(
    function(event){
      $.ajax({
        url : ip+'/post/checkusername/',
        type: 'POST',
        dataType: 'json',
        data: {'username': $('#id_username').val()},
        success: function(data, textStatus, xhr){
            if(data['match'] == true){
              $('#matchusername').text('username already exists.');
            }
            else{
              $('#matchusername').text('Can keep this username.')
            }
            if($('#id_username').val()=="")
            $('#matchusername').text('');


        }
}
  );

    }

  );

    $('.regid').keyup(function(){
      var str = $(this).val();
      $('input[name="mood_reg"]').val(str);
    });
var mood_verify=false , erp_verify=false;
$('#verifyerp').click(
  function(){

    var person = {
        'regid' : $('.regid').val(),
        'passw' : $('.passw').val(),
    }
$.ajax({
    url : ip+'/post/api/verifyerp',
    type: 'POST',
    dataType: 'json',
    data: person,
    success : function(data, textStatus, xhr){

        if(data['STATUS']==true){
          erp_verify=true;
          $('#verifyerp').attr('disabled','true')
          if(mood_verify==true)
            $('input')[10].disabled=false;
          alert('Confirmed');
        }
        else{
          erp_verify=false;
          alert('Wrong details. Please check again');
        }
    }

  });


}
);


$('#verifymood').click(
  function(){

    var person1 = {
        'mood_reg' : $('.moodreg').val(),
        'mood_passw' : $('.moodpassw').val(),
    }
$.ajax({
    url : ip+'/post/api/verifymood',
    type: 'POST',
    dataType: 'json',
    data: person1,
    success : function(data, textStatus, xhr){

        if(data['STATUS']==true){
          mood_verify=true;
          $('#verifymood').attr('disabled','true')

          if(erp_verify==true)
            $('input')[10].disabled=false;
          alert('Confirmed');
        }
        else{
          mood_verify=false;
          alert('Wrong details. Please check again');
        }
    }

  });


}
);




}
);
