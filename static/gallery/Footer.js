import React, { Component } from 'react';

class Footer extends Component {
    // constructor(props) {
    //     super(props)
    //
    //     this.state = {
    //         author: null
    //     }
    //
    // }
    render() {
        return (
            <div>
                <button type="button" className="hollow success button tiny float-left"
                    style={{
                    // color: "white",
                    // background: "lightgrey",
                    // textAlign: "center",
                    //     margin: "0",
                    //     marginTop: "1px"
                    }}>
                    Нравится <i className="far fa-heart fa-lg"></i> 2
                </button>
                <button type="button" className="hollow success button tiny float-left">
                    Автор: { this.props.author }
                </button>
                {/*<div className="text-center">*/}
                    {/*<h4><i className="far fa-heart fa-lg"></i></h4>*/}
                {/*</div>*/}
            </div>
        )
    }
}

export default Footer