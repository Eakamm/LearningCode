const path = require("path");
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const webpack = require("webpack")

module.exports = {
	// 入口
	entry: "./src/main.js",
	// 出口
	output: {
		// 路径为绝对路径
		path: path.resolve(__dirname, 'dist'),
		filename: "bundle.js",
	},
	module: {
		rules: [
			{
				test: /\.css$/,
				use: [ 'style-loader', 'css-loader' ]
			},
			{
				test: /\.(png|jpg|gif)$/,
					use: [
						{
							loader: 'url-loader',
							options: {
								limit: 8192,
								name: "img/[name].[hash:8].[ext]",
								// publicPath: "dist/"
							}
						}
					]
			},
			{
				test: /\.vue$/,
				loader: 'vue-loader'
			},
			{
				test: /\.js$/,
				exclude: /(node_modules|bower_components)/,
				use: {
					loader: 'babel-loader',
					options: {
						presets: ['es2015']
					}
				}
			}
		]
	},
	resolve: {
		alias: {
			'vue$': 'vue/dist/vue.esm.js' // 用 webpack 1 时需用 'vue/dist/vue.common.js'
		}
	},
	plugins: [
		// 请确保引入这个插件来施展魔法
		new VueLoaderPlugin(),
		// 
		new HtmlWebpackPlugin({
			template: "index.html"
		}),
		//热模块替换，它允许在运行时更新各种模块，而无需进行完全刷新
		new webpack.HotModuleReplacementPlugin({
		  // Options...
		})
	],
	// webpack_dev_server配置
	devServer: {
		open: true,
		port: 8081,
		contentBase: "./list",
		hot: true
	}
};