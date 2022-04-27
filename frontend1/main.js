import App from './App'

// #ifndef VUE3
import Vue from 'vue'
// import uView from './uni_modules/vk-uview-ui'
import uView from '@/uni_modules/uview-ui'
// import GoEasy from './lib/goeasy-2.2.4.min.js';
// import { createSSRApp } from 'vue'

// export function createApp() {
//   const app  = createSSRApp(App)
  // return { app }
  // 使用 uView UI
  // app.use(uView)


// }
Vue.use(uView)
Vue.config.productionTip = false
// const goEasy = GoEasy.getInstance({
// 	host:"hangzhou.goeasy.io",//应用所在的区域地址: 【hangzhou.goeasy.io |singapore.goeasy.io】
// 	appkey:"BC-2fa32f417d7b4275b002c7108f25a1d7",// common key
// 	// true表示支持通知栏提醒，false则表示不需要通知栏提醒
// 	allowNotification:true, //仅有效于app，小程序和H5将会被自动忽略
// 	modules: ['pubsub'],
// });
// Vue.prototype.goEasy = goEasy;
// App.mpType = 'app'

// #endif

// #ifdef VUE3
import { createSSRApp } from 'vue'
export function createApp() {
  const app = createSSRApp(App)
  return {
    app
  }
}
// #endif

// goEasy.onClickNotification((notificaionMessage) => {
// 	console.log("User clicked the notification:", notificaionMessage);
// });



// goEasy.connect({
// 	onSuccess: function(){
// 		console.log("GoEasy connect successfully.")
// 	},
// 	onFailed: function(error){
// 		console.log("Failed to connect GoEasy, code:"+error.code+ ",error:"+error.content);
// 		uni.showModal({
// 			title: error.code.toString(),
// 			content: error.content,
// 			showCancel: false,
// 			duration: 6000
// 		})
// 	},
// 	onProgress: function(attempts){
// 		console.log("GoEasy is connecting", attempts);
// 	}
// });


Vue.config.productionTip = false
App.mpType = 'app'
const app = new Vue({
	...App
})

//格式化时间
Date.prototype.formatDate = function (fmt) {
	var o = {
		"M+": this.getMonth() + 1,
		"d+": this.getDate(),
		"h+": this.getHours(),
		"m+": this.getMinutes(),
		"s+": this.getSeconds(),
		"q+": Math.floor((this.getMonth() + 3) / 3),
		"S": this.getMilliseconds()
	};
	if (/(y+)/.test(fmt))
		fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
	for (var k in o)
		if(o.hasOwnProperty(k)){
			if (new RegExp("(" + k + ")").test(fmt))
				fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
		}
	return fmt;
};
app.$mount()