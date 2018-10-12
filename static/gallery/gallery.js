import React, { Component } from 'react';
import { render } from 'react-dom';
import Gallery from 'react-photo-gallery';
// import Gallery from 'react-grid-gallery';
import Lightbox from 'react-images';

// import { SpringGrid,  measureItems } from 'react-stonecutter';
// import { CSSGrid, layout } from 'react-stonecutter';

import './gallery.css';
import ButtonLike from './ButtonLike';
import Footer from './Footer';


// const Grid = measureItems(SpringGrid, { measureImages: true });
// const Card = ({ title, image }) => (
//   <div className="Card">
//     <h3>{title}</h3>
//     <img src={image} alt={title} />
//   </div>
// );


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

        // items.forEach(function (item) {
        //     if (item.album === 24) {
        //         photos.push({
        //             src: item.image,
        //             caption: (
        //                 <div style={{backgroundColor: "white", height: "100px"}}>
        //                     <ButtonLike />
        //                     Hello
        //                 </div>
        //             ),
        //
        //             thumbnail: item.image_thumbnail,
        //             thumbnailWidth: item.image_thumbnail_size[0],
        //             thumbnailHeight: item.image_thumbnail_size[1],
        //             thumbnailCaption:  <ButtonLike />
        //         })
        //     }
        // });

        // items.forEach(function (item) {
        //     if (item.album === 24) {
        //         photos.push({
        //             src: item.image,
        //             thumbnail: item.image_thumbnail,
        //             thumbnailWidth: item.image_thumbnail_size[0],
        //             thumbnailHeight: item.image_thumbnail_size[1],
        //         })
        //     }
        // });

        console.log(items);


        items.forEach(function (item) {
            if (item.album.id === 24) {
                photos.push({
                    src: item.image_thumbnail,
                    srcSet: item.image,
                    width: item.image_thumbnail_size[0],
                    height: item.image_thumbnail_size[1],
                    author: item.author.full_name,
                    caption: <Footer author={item.author.full_name}/>
                })
            }
        });



        console.log(photos);
        console.log(photos.map(img => {
            return {src: img.srcset}
        }));

        let styleLoaded = {marginTop: '100px', color: 'red', fontSize: '24px'};
        if (!isLoaded) {
            return <div className='text-center' style={styleLoaded}>Loading...</div>
        }
        else {
            return (
                <div>
                    <Gallery photos={photos}
                        direction={"column"}
                        columns={4}
                        onClick={this.openLightbox}
                    />
                    <Lightbox images={photos}
                        onClose={this.closeLightbox}
                        onClickPrev={this.gotoPrevious}
                        onClickNext={this.gotoNext}
                        currentImage={this.state.currentImage}
                        isOpen={this.state.lightboxIsOpen}
                        // showImageCount={false}
                    />
                </div>
            )
        }
    }
}
render(<App />, document.getElementById('app'));
