const path = require('path');

module.exports = {
    mode: 'development',
    entry: './static/src/main.js',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, './static/dist')
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
                use: [
                    "babel-loader"
                ]
            },
            {
                test: /\.scss$/,
                use: [
                    "style-loader", // creates style nodes from JS strings
                    "css-loader", // translates CSS into CommonJS
                    "sass-loader" // compiles Sass to CSS, using Node Sass by default
                ]
            }
        ]
    },
    watch: true
};