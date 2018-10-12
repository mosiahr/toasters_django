import React, { Component } from 'react';

class ButtonLike extends Component {
    render() {
        return (
            <button type="button" className="hollow success button tiny expanded float-center"
                style={{
                // color: "white",
                // background: "lightgrey",
                // textAlign: "center",
                    margin: "0",
                    marginTop: "1px"
                }}>
                Нравится <i className="far fa-heart fa-lg"></i> 2
            </button>
        )
    }
}

export default ButtonLike



