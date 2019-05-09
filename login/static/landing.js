$(document).ready(

  function(){

    $('#next').click(
      function(){
        if($('.pt-page-current').next().attr('class').indexOf('pt-page')<0 ){}
        else{
        var n = $('.pt-page-current');
        $('.pt-page-current').removeClass('pt-page-current');
        n.next('.pt-page').addClass('pt-page-current');
      }
}
    );
    $('#next').click(function(){
      var s = $(location).attr('href');
      ip = s.replace(s.substring(s.indexOf('8000')+4,s.length),'');

      window.location.replace('post/signin');

    });
  

    $('#previous').click(
      function(){
        if($('.pt-page-current').prev().attr('class').indexOf('pt-page')<0){

        }
        else{
        var n = $('.pt-page-current');
        $('.pt-page-current').removeClass('pt-page-current');
        n.prev('.pt-page').addClass('pt-page-current');
      }
      }
    );

  }


);
