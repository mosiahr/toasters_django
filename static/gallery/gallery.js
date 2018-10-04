import React, { Component } from 'react';
import { render } from 'react-dom';
// import Gallery from 'react-photo-gallery';
import Gallery from 'react-grid-gallery';
// import Lightbox from 'react-images';
import './gallery.css';


class App extends Component {
    constructor() {
        super();
        this.state = {
            currentImage: 0,

            items: [],
            isLoaded: false,
        };
        this.closeLightbox = this.closeLightbox.bind(this);
        this.openLightbox = this.openLightbox.bind(this);
        this.gotoNext = this.gotoNext.bind(this);
        this.gotoPrevious = this.gotoPrevious.bind(this);
    }

    componentDidMount() {
        fetch('/api/v1/gallery/photo-list/')
            .then(res => res.json())
            .then(json => {
                this.setState({
                    items: json,
                    isLoaded: true,
                })
            });
    }

    openLightbox(event, obj) {
        this.setState({
            currentImage: obj.index,
            lightboxIsOpen: true,
        });
    }
    closeLightbox() {
        this.setState({
            currentImage: 0,
            lightboxIsOpen: false,
        });
    }
    gotoPrevious() {
        this.setState({
            currentImage: this.state.currentImage - 1,
        });
    }
    gotoNext() {
        this.setState({
            currentImage: this.state.currentImage + 1,
        });
    }
    render() {

        let {isLoaded, items} = this.state;
        const photos = [];

        items.forEach(function (item) {
            if (item.album === 24) {
                photos.push({
                    src: item.image,
                    thumbnail: item.image_thumbnail,
                    thumbnailWidth: item.image_thumbnail_size[0],
                    thumbnailHeight: item.image_thumbnail_size[1],
                    thumbnailCaption:  (
                        <button type="button" className="hollow success button tiny expanded float-center"
                            style={{
                            // color: "white",
                            // background: "lightgrey",
                            // textAlign: "center",
                                margin: "0",
                                marginTop: "1px"
                            }}>
                            Нравится <i class="far fa-heart fa-lg"></i> 2
                        </button>
                    )
                });
            }
        });

        console.log(photos);

        let styleLoaded = {marginTop: '100px', color: 'red', fontSize: '24px'};
        if (!isLoaded) {
            return <div className='text-center' style={styleLoaded}>Loading...</div>
        }
        else {
            return (
                <div className="div-gallery">

                    <Gallery
                        images={photos}
                        showLightboxThumbnails={true}
                        backdropClosesModal={true}
                        // enableLightbox={false}
                        enableImageSelection={false}
                    />

                </div>
            )
        }
    }
}
render(<App />, document.getElementById('app'));
