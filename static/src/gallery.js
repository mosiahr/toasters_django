// import _ from 'lodash';
// Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";

import Vue from 'vue';
import VueResource from 'vue-resource';
// import VuePreload from 'vue-preload/vue-preload'

// Vue.use(VuePreload);
Vue.use(VueResource);

var tit = "{{ title }}";
console.log(tit);

// Component header-gallery
Vue.component('header-gallery', {
    delimiters: ['${','}'],

    template: "<h2>Hello ${ title }</h2>",
    data: function () {
        return {
            title: "{{ title }}",
        }
    }
});

new Vue({
    delimiters: ['${','}'],
    el: '#app',
    data: {
        active: false,
        photos: [],
        loading: true,
        title: 'Welcome to My Gallery'
    },
    mounted: function() {
        this.getPhotos();
    },
    methods: {
        getPhotos: function () {
            // var baseURL = "{% url 'api_gallery:photo_list' %}";       //  '/api/v1/gallery/photo-list/'
            var baseURL = "/api/v1/gallery/photo-list/";       //  '/api/v1/gallery/photo-list/'
            this.loading = true;

            this.$http.get(baseURL)
                .then((response) => {
                    var photos = response.data;
                    for (var obj in photos){
                        photos[obj] = {
                            imgThumbnail: photos[obj]['image_thumbnail'],
                            // imgThumbnail: photos[obj]['image'].split('.').join('.thumbnail.'),
                            // imgSmall: photos[obj]['image'].split('.').join('.small.'),
                        }
                    }
                    this.photos = photos;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        showImg: function() {
            console.log("show");
        },
        mouseOver: function () {
            console.log("mouse");
            // event.target.style.bordercolor="red";
            // event.target.style.transform = "scale(1.1)";
        }

    },

});



