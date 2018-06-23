$(document).ready(function(){

    var headerImgUrl = $("#myVar").val();
    // console.log(headerImgUrl);
    $('.intro').css('background-image', 'url(' + headerImgUrl + ')');




    // SELECT 2
    $('.form-select2').select2();

    // FAVORITE
    var addFavorite = $('button#addFavorite');
    addFavorite.click(function(event) {
        event.preventDefault();

        if ($(this).find('i').hasClass('fas') !== true){
            $(this).find('i').addClass('fas fav');
            $(this).find('span:eq( 0 )').removeClass('hide');
            $(this).find('span:eq( 1 )').addClass('hide');
        }else{
            $(this).find('i').removeClass('fas fav');
            $(this).find('span:eq( 0 )').addClass('hide');
            $(this).find('span:eq( 1 )').removeClass('hide');
        }

        var thisUrl = $(this).attr("data-url");

        $.ajax({
                method: "GET",
                url: thisUrl,
                // data: formData
            })
            .done(function(data) {
                var count_fav = data['count_fav'];
                if (count_fav > 0){
                    $('#heart-menu>i').addClass('fas fav');
                    $('#count_fav').text(count_fav);
                }else{
                    $('#heart-menu>i').removeClass('fas fav');
                    $('#count_fav').text('');
                }
            })
            .fail(function(data) {
                console.log("error");
                console.log(data);
            })
    });

    // GET FAVORITES
    var btnHeart = $('#heart-menu');
    btnHeart.click(function(event) {
        event.preventDefault();
        var thisUrl = $(this).attr("data-url");
        console.log(thisUrl);
        $.ajax({
                method: "GET",
                url: thisUrl,
                // data: formData
            })
            .done(function(data) {
                $('#getFavorites').foundation('open');
                drawFavorites(data);
            })
            .fail(function(data) {
                console.log("error");
                console.log(data);
            })
    });

    function drawFavorites(data){
        $( "#companyFav" ).empty();
        $( "#companyFav" ).append('<div class="cell grid-x grid-margin-x grid-margin-y align-left">');

        for (var key in data){
            var d = {
                id: data[key]['id'],
                name: data[key]['name'],
                avatarThumbnail: data[key]['avatar'].replace('jpg', 'thumbnail.jpg')
            }

            var template = [
                '<div class="cell small-12 medium-6 large-3">',
                    '<div class="thumbnail">',

                        '<div style="height: 200px">',
                            '<a href="/company/{{ id }}">',
                                '<img class="float-center " src="{{ avatarThumbnail }}">',
                            '</a>',
                            // '<button class="close-button" data-close aria-label="Close modal" type="button">',
                            //     '<span aria-hidden="true">&times;</span>',
                            // '</button>',
                        '</div>',

                        '<h5 class="card-section text-center">',
                            '<a class="" href="/company/{{ id }}">{{ name }}</a>',
                        '</h5>',

                    '</div>',
                '</div>'
            ].join("\n");

            var html = Mustache.render(template, d);
            $( "#companyFav" ).append(html);
        }
        $( "#companyFav" ).append('</div>');


    }

    // $('.related-widget-wrapper').select2();
    // $('#id_type').select2({
    //     placeholder: 'Select an option',
    //     // dropdownAutoWidth: true,
    //     // disabled: true
    //     // theme: "classic"
    // });





    // $('.your-class').slick({
    //   centerMode: true,
    //   // centerPadding: '60px',
    //   slidesToShow: 3,
    //   responsive: [
    //     {
    //       breakpoint: 768,
    //       settings: {
    //         arrows: false,
    //         centerMode: true,
    //         // centerPadding: '40px',
    //         slidesToShow: 3
    //       }
    //     },
    //     {
    //       breakpoint: 480,
    //       settings: {
    //         arrows: false,
    //         centerMode: true,
    //         // centerPadding: '40px',
    //         slidesToShow: 1
    //       }
    //     }
    //   ]
    // });

    // $('.div-slick').slick({
    //     autoplay: true,
    //     // slidesToShow: 3,
    //     // slidesToScroll: 1
    // })



    // var options = {
    //                     $AutoPlay: 1,                                    //[Optional] Auto play or not, to enable slideshow, this option must be set to greater than 0. Default value is 0. 0: no auto play, 1: continuously, 2: stop at last slide, 4: stop on click, 8: stop on user navigation (by arrow/bullet/thumbnail/drag/arrow key navigation)
    //                     $Idle: 4000,                            //[Optional] Interval (in milliseconds) to go for next slide since the previous stopped if the slider is auto playing, default value is 3000
    //                     $SlideDuration: 500,                                //[Optional] Specifies default duration (swipe) for slide in milliseconds, default value is 500
    //                     $DragOrientation: 3,                                //[Optional] Orientation to drag slide, 0 no drag, 1 horizental, 2 vertical, 3 either, default value is 1 (Note that the $DragOrientation should be the same as $PlayOrientation when $Cols is greater than 1, or parking position is not 0)
    //                     $UISearchMode: 0,                                   //[Optional] The way (0 parellel, 1 recursive, default value is 1) to search UI components (slides container, loading screen, navigator container, arrow navigator container, thumbnail navigator container etc).
    //
    //                     $ThumbnailNavigatorOptions: {
    //                         $Class: $JssorThumbnailNavigator$,              //[Required] Class to create thumbnail navigator instance
    //                         $ChanceToShow: 2,                               //[Required] 0 Never, 1 Mouse Over, 2 Always
    //
    //                         $Loop: 1,                                       //[Optional] Enable loop(circular) of carousel or not, 0: stop, 1: loop, default value is 1
    //                         $SpacingX: 3,                                   //[Optional] Horizontal space between each thumbnail in pixel, default value is 0
    //                         $SpacingY: 3,                                   //[Optional] Vertical space between each thumbnail in pixel, default value is 0
    //
    //                         $ArrowNavigatorOptions: {
    //                             $Class: $JssorArrowNavigator$,              //[Requried] Class to create arrow navigator instance
    //                             $ChanceToShow: 2,                               //[Required] 0 Never, 1 Mouse Over, 2 Always
    //                             $Steps: 6                                       //[Optional] Steps to go for each navigation request, default value is 1
    //                         }
    //                     }
    //                 };
    //
    //                 var jssor_slider1 = new $JssorSlider$('slider1_container', options);
    //
    //                 /*#region responsive code begin*/
    //                 //you can remove responsive code if you don't want the slider scales while window resizing
    //                 function ScaleSlider() {
    //                     var parentWidth = jssor_slider1.$Elmt.parentNode.clientWidth;
    //                     if (parentWidth)
    //                         jssor_slider1.$ScaleWidth(Math.min(parentWidth, 720));
    //                     else
    //                         $Jssor$.$Delay(ScaleSlider, 30);
    //                 }
    //
    //                 ScaleSlider();
    //                 $(window).bind("load", ScaleSlider);
    //                 $(window).bind("resize", ScaleSlider);
    //                 $(window).bind("orientationchange", ScaleSlider);
                    /*#endregion responsive code end*/

});