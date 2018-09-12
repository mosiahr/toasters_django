$(document).ready(function(){

    var headerImgUrl = $("#myVar").val();
    // console.log(headerImgUrl);
    $('.intro').css('background-image', 'url(' + headerImgUrl + ')');

    // SELECT 2
    $('.form-select2').select2({
        // adaptContainerCssClass: false,
        // adaptDropdownCssClass: false,
        // allowClear: true,
        // containerCss: true,
        // dataAdapter: false,
        // debug: true,
        // dropdownAutoWidth: true,
        theme: "foundation",
        // theme: "classic",
        // selectOnClose: true,
        allowClear: true,
        // placeholder: 'This is my placeholder',
        // minimumResultsForSearch: Infinity,  //непоказ. строку поиска
    });

    $('.form-select2-type').select2({
        allowClear: true,
        theme: "foundation",
        placeholder: 'Выбирете категорию',
        minimumResultsForSearch: Infinity,  //непоказ. строку поиска
    });

    $('.form-select2-city').select2({
        allowClear: true,
        theme: "foundation",
        placeholder: 'Выбирете город',
        language: {
            noResults: function (params) {
              return "Результатов не найдено";
            }
        }
    });

    $('.form-select2-price').select2({
        allowClear: true,
        theme: "foundation",
        placeholder: 'Выбирете стоимость',
        minimumResultsForSearch: Infinity,  //непоказ. строку поиска
    });

    $('.form-select2-addPhoto').select2({
        allowClear: true,
        theme: "foundation",
        placeholder: 'Выберите альбом',
        minimumResultsForSearch: Infinity,  //непоказ. строку поиска
    });

    // $('#form-filter').on('select2:open', function (e) {
    //     $('html, body').css({
    //         overflow: 'hidden',
    //         // height: '100%',
    //     });
    // });

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
            var name = data[key]['name'];
            if (name.length>25){
                name = name.slice(0, 25) + '...';
            }
            var d = {
                id: data[key]['id'],
                name: name,
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


    // INPUT FILE

    $(".inputfile").on('change', function (event) {
        var fileName = $(this).val().split('\\').pop();
        // console.log(event.target.value.split( '\\' ).pop())
        var label = $(this).prev();
        if (fileName)
            label.find('span').html(fileName);

    });

});