
<template>
	<view class="content">
		
		<u-notify ref="uNotify"></u-notify>
		
		<view class="login_from">
			
			<view class="login_from_input">
				<view class="login_from_name">姓名</view>
				<view class="login_from_fun"><input type="text" placeholder="请输入姓名"  v-model="name"></view>
			</view>
			
			<view class="login_from_input">
				<view class="login_from_name">昵称</view>
				<view class="login_from_fun"><input type="text" placeholder="请输入用户名"  v-model="user_name"></view>
			</view>

			<view class="login_from_input">
				<view class="login_from_name">密码</view>
				<view class="login_from_fun"><input type="digit" password="true" placeholder="请输入登录密码" v-model="password"></view>
			</view>
			
			<view class="login_from_input">
				<view class="login_from_name"  >身份</view>
				<view class="login_from_fun">
					<picker @change="bindPickerChange1" :value="identityIndex" :range="identityArray" range-key="name" >
						<view class="uni-input" v-model="identity">{{identityArray[identityIndex].name}}</view>
					</picker>
				</view>
			</view>
			
			<view class="login_from_input">
				<view class="login_from_name">性别</view>
				<view class="login_from_fun">
					<picker @change="bindPickerChange2" :value="genderIndex" :range="genderArray" range-key="name">
						<view class="uni-input"  v-model="gender">{{genderArray[genderIndex].name}}</view>
					</picker>
				</view>
			</view>
			
			<view class="login_from_input">
				<view class="login_from_name">邮箱</view>
				<view class="login_from_fun"><input type="text" placeholder="请输入ecnu邮箱" v-model="email"></view>
			</view>
			
			<view class="login_from_input">
				<view class="login_from_name">验证码</view>
				<view class="login_from_fun"><input type="text" placeholder="请输入验证码" v-model="verifyCode"></view>
				<!-- <button class="u-reset-button"  style="color: #0066CC;" @click="validate">验证码</button> -->
				<!-- <button v-else class="u-reset-button"  style="color: #0066CC;" @click="validate">{{verifyTip+'秒'}}</button> -->
				<button type="primary" @tap="validate($event), numberst($event)" :disabled="countdown < 60 && countdown >= 1">
				{{countdown < 60 && countdown >= 1?`${countdown}秒重获`:'获取验证码'}}</button>
			</view>
			
			<view class="login_from_dl">
				<button @click="register">注册</button>
			</view>
			
			<view class="logo_xieyi">
				<checkbox @click="moutcl" value="cb" />
				<!-- <label @click="moutcl" :class="gouxSta?'cuIcon-squarecheckfill':'cuIcon-square'"></label> -->
				<view class="logo_text">请勾选并阅读<text>《注册协议》</text>及<text>《隐私协议》</text></view>
				<!-- <u-alert :title="title" type = "warning" :description = "description"></u-alert> -->
				<!-- <u-alert-tips :show="show" type="error" @close="show = false" :title="title" :close-able="true"></u-alert-tips> -->

			</view>
			
		</view>
		
	</view>
</template>
<script>
 export default {
   data(){
     return {
		identityArray: [{name:'student'},{name: 'teacher'}, {name:'tourist'}],
		identityIndex: 0,
		genderArray: [{name:'male'},{name: 'female'}],
		genderIndex: 0,
		gouxSta:false,
		rand : Math.round(Math.random()*10000)+1000,
		countdown:60,
		title:'uView的目标是成为uni-app生态最优秀的UI框架',
		description:'uView是uni-app生态专用的UI框架',
		// 初始化，减少报错
		name:'',
		user_name: '',
		password: '',
		identity:'student',
		gender:'male',
		email: '',
		verifyCode: '',
		get_value: '',
		// user_name: '666',
		 
	}
	   },
    onLoad(){
     },
    methods: {
		bindPickerChange1: function(e) {
			console.log('picker发送选择改变，携带值为：' + e.detail.value)
			console.log(this.rand)
			this.identityIndex = e.detail.value
			this.identity = this.identityArray[this.identityIndex].name
			console.log(this.identity)
		},
		
		bindPickerChange2: function(e) {
			console.log('picker发送选择改变，携带值为：' + e.detail.value)
			this.genderIndex = e.detail.value
			this.gender = this.genderArray[this.genderIndex].name
			console.log(this.gender)
		},
		
		moutcl(){
			
			if( this.gouxSta == false){
				
				this.gouxSta = true
				
			}else{
				
				this.gouxSta = false
				
			}
			
		},
		validate(){
			var today = new Date()
			uni.request({
				url:'http://127.0.0.1:8000/sendEmail/',
				data: {
					// 编辑器
					value: this.rand,
					email_address: this.email,
				},
				method:'post',
				success:(res)=>{
					console.log(today)
					console.log('验证码请求成功')
				},
			})
			
			uni.request({
				url:'http://127.0.0.1:8000/emailValidate/',
				data: {
					// 编辑器
					value: this.rand,
					email_address: this.email,
					time: today
				},
				method:'post',
				success:(res)=>{
					console.log('验证码成功进入数据库')
				},
			})
		},
		
		register(){
			uni.request({
				url: 'http://127.0.0.1:8000/sendEmail/emailvalidSearch?email_address='+this.email,
				data: {
							// get_value: '',
					// 编辑器 
				},
				method:'get',
				success:(res)=>{
					this.get_value = res.data[0].value
					// console.log(res.data[0].value)
					console.log(this.get_value)
					console.log('上传信息',this.gender,this.identity)
					console.log('验证码成功获取')
					if (this.verifyCode == this.get_value){
						uni.request({
							url:'http://127.0.0.1:8000/users/',
							data: {
								// 编辑器 
								base_url:'http://127.0.0.1:8000/users/',
								name:this.name, 
								username: this.user_name,
								password: this.password,
								gender: this.gender,
								identity: this.identity,
								email: this.email,
								// verifyCode: this.verifyCode,
							},
							method:'post',
							success:(res)=>{
								console.log(this.gender)
								console.log('注册成功')
								uni.switchTab({
									url:'./mine'
								});
							},
						})
					}
					else{
						this.$refs.uNotify.show({
							show: false,
							message: '验证码错误',
							type: 'error',
							color: '#ffffff',
							bgColor: '',
							fontSize: 14,
							duration: 3000,
							safeAreaInsetTop: false
							// ...params
						})
					}
				},
			})
			// uni.request({
			// 	url:'http://127.0.0.1:8000/users/',
			// 	data: {
			// 		// 编辑器 
			// 		base_url:'http://127.0.0.1:8000/users/',
			// 		name:this.name, 
			// 		username: this.user_name,
			// 		password: this.password,
			// 		gender: this.gender,
			// 		identity: this.identity,
			// 		email: this.email,
			// 		verifyCode: this.verifyCode,
			// 	},
			// 	method:'post',
			// 	success:(res)=>{
			// 		console.log(this.gender)
			// 		console.log('注册成功')
			// 		uni.switchTab({
			// 			url:'./mine'
			// 		});
			// 	},
			// })
			
			// if( this.gouxSta == false){
				
			// 	uni.showToast({
			// 		"title":"请阅读并勾选用户协议",
			// 		"icon":'none'
			// 	})				
				
			// }else{
				
			// 	uni.showToast({
			// 		"title":"账号不存在",
			// 		"icon":'none'
			// 	})
				
			// }		
			
		},
		// 倒计时功能
numberst(e){
			//其他代码....
			this.countDown();
		},
		// 倒计时
		countDown(){
			let self = this;
			self.countdown = 60;
			self.countdown -= 1;
			if(self.clear){
				clearInterval(self.clear)
			}
			self.clear = null;
			self.clear = setInterval(_ => {
				if(self.countdown > 0){
					self.countdown -= 1;
				}else{
					clearInterval(self.clear)
				}
			},1000)
		},
		
		
		
		
     },
	 mounted(){

	 },

 }
</script>
<style>
	
	page{ background: #fff;font-family: arial,verdana,helvetica,'PingFang SC','HanHei SC',STHeitiSC-Light,Microsoft Yahei,sans-serif; }
	
	.login_img{ width: 100%; height: auto; margin-top: 90upx; }
	.login_img image{ width: 200upx; height: 200upx; display: block; margin: 0px auto; border-radius: 50%; }
	
	.login_from{ width: 100%; height: auto; box-sizing: border-box; padding: 40upx 8%; margin-top: 80upx; }
	
	.login_from_input{ width: 100%; height:auto; display: flex; flex-direction: row; justify-content: space-between; align-items: center; border-bottom: 1px #eee solid; padding: 50upx 0px; margin: 0px auto;  } 
	
	.login_from_name{ width: 20%; }
	.login_from_fun{ width: 100%; display: flex; flex-direction: row; justify-content: flex-end;  }
	.login_from_fun input{ width: 100%; text-align: left; font-size: 14px;  }
	
	
	.login_from_dl{ width: 100%; height: 50px; line-height: 50px; margin-top: 150upx;   }
	.login_from_dl button{ width: 100%; height: 50px; line-height: 50px; background: #007AFF; color: #fff; border-radius: 0px; }
	
	.logo_xieyi{ width: 100%; height: 40px; line-height: 40px; display: flex; flex-direction: row; margin-top: 30upx; align-items: center; color: #444; font-size: 14px; justify-content: center; }
	.logo_xieyi label{ font-size: 18px; margin-right: 1%; }
	
	.cuIcon-squarecheckfill{ color: #007AFF; }
	.logo_text text{ color: #007AFF; }
	
	
</style>

