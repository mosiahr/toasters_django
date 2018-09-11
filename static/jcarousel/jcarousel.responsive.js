(function($) {
    $(function() {
        var jcarousel = $('.jcarousel');

        var numItems = $('#lightgallery li').length;
        // console.log(numItems);

        $('.jcarousel-wrapper').show();

        // if (numItems >= 5) {
        //     $('.jcarousel-control-prev, .jcarousel-control-next').show();
        // }
        // if (numItems / )
        // $('.jcarousel-control-prev, .jcarousel-control-next').show();
        // console.log(jcarousel.innerWidth());


        jcarousel
            .on('jcarousel:reload jcarousel:create', function () {
                var carousel = $(this),
                    width = carousel.innerWidth();

                if (width >= 1000) {
                     width = width / 6;
                } else if (width >= 800) {
                    width = width / 5;
                } else if (width >= 600) {
                    width = width / 4;
                } else if (width >= 450) {
                    width = width / 3;
                } else if (width >= 300) {
                    width = width / 2;
                } else if (width >= 250) {
                    width = width / 1;
                }

                carousel.jcarousel('items').css('width', Math.ceil(width) + 'px');
            })
            .jcarousel({
                wrap: 'circular',
            });

        $('.jcarousel-control-prev')
            .jcarouselControl({
                target: '-=1'
            });


        $('.jcarousel-control-next')
            .jcarouselControl({
                target: '+=1'
            });

        // console.log(jcarousel.width());
        // if (jcarousel.width() >= 600) {
        //
        //     $('.jcarousel-pagination')
        //         .on('jcarouselpagination:active', 'a', function() {
        //             $(this).addClass('active');
        //         })
        //         .on('jcarouselpagination:inactive', 'a', function() {
        //             $(this).removeClass('active');
        //         })
        //         .on('click', function(e) {
        //             e.preventDefault();
        //         })
        //         .jcarouselPagination({
        //             perPage: 1,
        //             item: function(page) {
        //                 return '<a href="#' + page + '">' + page + '</a>';
        //             }
        //         });
        // }
    });
})(jQuery);
