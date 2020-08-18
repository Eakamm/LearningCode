// import {sum} from "./js/aa.js"
// 
// console.log(sum(20, 20))

// 写依赖
import css from "./css/aa.css"

// import Image1 from "./img/1.jpg"
import Image2 from "./img/2.jpg"

import Vue from "vue"

// 导入vue组件
import aa from "./vue/aa.vue"



// const App = {
// 	template: `
// 		<div>
// 			<h2>{{message}}</h2>
// 			<button>test</button>
// 		</div>
// 	`,
// 	data(){
// 		return {
// 			message: "hello"
// 		}
// 	}
// }

new Vue({
	el: "#app",
	template: "<aa/>",
	components:{
		aa
	}
})