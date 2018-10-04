const path = require('path');

const MiniCssExtractPlugin = require("mini-css-extract-plugin");  //
// const devMode = process.env.NODE_ENV !== 'production'

module.exports = {
    mode: 'development',
    context: path.resolve(__dirname, 'static'),
    entry: {
        main: './src/main.js',
        gallery: './gallery/gallery.js',
        app: './src/scss/app.scss'
    },
    output: {
        path: path.resolve(__dirname, 'static/dist'),
        filename: '[name].js',
        publicPath: "./static/dist"
    },
    resolve: {
        extensions: ['*', '.js', '.jsx'],
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
                test: /\.css$/,
                use: [ 'style-loader', 'css-loader' ]
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
            // filename: "style.bundle.css",
            chunkFilename: "[name].css"
        })
    ],
};