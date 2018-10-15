import React, { Component } from 'react';

class Footer extends Component {
    constructor(props) {
        super(props);

        this.state = {
            isVoice: false
        };
        this.likeClick = this.likeClick.bind(this);
    }

    likeClick() {
        this.setState({
            isVoice: !this.state.isVoice
        })
    }

    render() {
        return (
            <div className="expanded button-group warning tiny">
                <button type="button" className="button">
                    Автор: { this.props.author }
                </button>
                <button className={this.state.isVoice ? 'button voice-yes' : 'button'} onClick={this.likeClick}>
                    Нравится <i className={this.state.isVoice ? "fas fa-heart fa-lg":'far fa-heart fa-lg'}></i> 2
                </button>
            </div>
        )
    }
}

export default Footer