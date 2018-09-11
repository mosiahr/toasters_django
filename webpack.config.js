const path = require('path');

const MiniCssExtractPlugin = require("mini-css-extract-plugin");  //
// const devMode = process.env.NODE_ENV !== 'production'

module.exports = {
    mode: 'development',
    // entry: ['./static/src/main.js', './static/src/scss/app.scss'],
    // entry: './static/src/main.js',
    // entry: {
    //     main: ['./static/src/main.js', './static/src/scss/app.scss'],
    // },
    entry: [
        './static/src/main.js',
        './static/src/scss/app.scss'
    ],
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, './static/dist'),
        publicPath: "./static/dist"
    },
    resolve: {
        alias: {
            'vue$': 'vue/dist/vue.esm.js' // 'vue/dist/vue.common.js' for webpack 1
        }
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: [
                    "babel-loader"
                ]
            },
            {
                test: /\.vue$/,
                use: [
                    "vue-loader"
                ]
            },
            {
                test: /\.scss$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    // { loader: 'sass-loader', options: { sourceMap: true } },
                    // "style-loader", // creates style nodes from JS strings
                    "css-loader", // translates CSS into CommonJS
                    "sass-loader" // compiles Sass to CSS, using Node Sass by default
                ]
            }
        ]
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: "style.bundle.css",
            // chunkFilename: "[name].css"
        })
    ],
};