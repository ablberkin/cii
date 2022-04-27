<!-- <template>
	<view class="wrap">
		<view class="top"></view>
		<view class="content">
			<view class="title">欢迎注册</view>
			<input class="u-border-bottom" v-model="name" placeholder="请输入昵称" />
			<input class="u-border-bottom" v-model="email" placeholder="请输入邮箱" />
			<input class="u-border-bottom" type="password" v-model="password" placeholder="请输入密码" />
			<input class="u-border-bottom" type="password" v-model="password_confirmation" placeholder="请再次输入密码" />
			<button @tap="submit" :style="[inputStyle]" class="getCaptcha">注册</button>
			<view class="alternative">
				<view class="password">密码设置规则</view>
				<view class="issue">帮助</view>
			</view>
		</view>
	</view>
</template>
 
<script>
	export default {
		data() {
			return {
				name: '',
				email: '',
				password: '',
				password_confirmation: ''
			}
		},
		computed: {
			inputStyle() {
				let style = {};
				if (this.$u.test.email(this.email) && this.password && this.name && this.password_confirmation) {
					//当都输入之后，按钮才会变色可点击
					style.color = "#fff";
					style.backgroundColor = this.$u.color['warning'];
				}
				return style;
			}
		},
		methods: {
			// ========================进行注册
			async submit() {
				// 1. 表单验证（邮箱格式、两次密码是否一致……）   我已经注册了一个7640907599@qq.com
				if (this.password !== this.password_confirmation) {
					this.$u.toast('两次密码不一致')
					return;                
				}
				// 2. 准备提交参数
				const params = {
					name: this.name,
					email: this.email,
					password: this.password,
					password_confirmation: this.password_confirmation
				}
				// 3. 传到后端去注册
				const res = await this.$u.api.authRegister(params)
				// 4. 注册完之后跳转到登录页面
				this.$u.route({
					type:"redirectTo",           //这个是uniapp原生的
					url:'pages/mine/login'     
				})
			}
		}
	}
</script>
 
<style lang="scss" scoped>
	.u-border-bottom {
		margin-bottom: 40rpx !important; //还要写个！important提高优先级。不太懂
	}
 
	.wrap {
		font-size: 28rpx;
 
		.content {
			width: 600rpx;
			margin: 80rpx auto 0;
 
			.title {
				text-align: left;
				font-size: 60rpx;
				font-weight: 500;
				margin-bottom: 100rpx;
			}
 
			input {
				text-align: left;
				margin-bottom: 10rpx;
				padding-bottom: 6rpx;
			}
 
			.tips {
				color: $u-type-info;
				margin-bottom: 60rpx;
				margin-top: 8rpx;
			}
 
			.getCaptcha {
				background-color: rgb(253, 243, 208);
				color: $u-tips-color;
				border: none;
				font-size: 30rpx;
				padding: 12rpx 0;
 
				&::after {
					border: none;
				}
			}
 
			.alternative {
				color: $u-tips-color;
				display: flex;
				justify-content: space-between;
				margin-top: 30rpx;
			}
		}
 
		.buttom {
			.loginType {
				display: flex;
				padding: 350rpx 150rpx 150rpx 150rpx;
				justify-content: space-between;
 
				.item {
					display: flex;
					flex-direction: column;
					align-items: center;
					color: $u-content-color;
					font-size: 28rpx;
				}
			}
 
			.hint {
				padding: 20rpx 40rpx;
				font-size: 20rpx;
				color: $u-tips-color;
 
				.link {
					color: $u-type-warning;
				}
			}
		}
	}
</style> -->


<!-- <template>
	<view class="wrap">
		<u-toast ref="uToast"></u-toast>
		<u-verification-code :seconds="seconds" @end="end" @start="start" ref="uCode" 
		@change="codeChange"></u-verification-code>
		<u-button @tap="getCode">{{tips}}</u-button>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				tips: '',
				// refCode: null,
				seconds: 10,
			}
		},
		onReady() {
			// 注意这里不能将一个组件赋值给data的一个变量，否则在微信小程序会
			// 造成循环引用而报错，如果你想这样做，请在非data中定义refCode变量
			// this.refCode = this.$refs.uCode;
		},
		methods: {
			codeChange(text) {
				this.tips = text;
			},
			getCode() {
				if(this.$refs.uCode.canGetCode) {
					// 模拟向后端请求验证码
					uni.showLoading({
						title: '正在获取验证码'
					})
					setTimeout(() => {
						uni.hideLoading();
						// 这里此提示会被this.start()方法中的提示覆盖
						this.$u.toast('验证码已发送');
						// 通知验证码组件内部开始倒计时
						this.$refs.uCode.start();
					}, 2000);
				} else {
					this.$u.toast('倒计时结束后再发送');
				}
			},
			end() {
				this.$u.toast('倒计时结束');
			},
			start() {
				this.$u.toast('倒计时开始');
			}
		}
	}
</script>

<style lang="scss" scoped>
	.wrap {
		padding: 24rpx;
	}
</style> -->




<!-- 云数据库上传 -->
<!-- <template>
	<view class="">
		<button class="btn" type="default" @click="upload">上传图片</button>
		<button class="btn" type="default" @click="browseImage">查看云图片</button>
	</view>
</template>

<script>
	export default {
		data() {
			return {}
		},
		methods: {
			upload() {
				uni.chooseImage({
					count: 1,
					success(res) {
						console.log(res);
						if (res.tempFilePaths.length > 0) {
							uni.showLoading({
								title: '上传中...'
							})
							
							let filePath = res.tempFilePaths[0]					
							// callback方式 ，进行上传操作
							uniCloud.uploadFile({
								filePath: filePath,  //要上传的文件对象
								cloudPath: Date.now() + '.jpg',  //保存在云端的文件名，这里以时间戳命名
								success(res) {
									//console.log(res.fileID)
									let imageUrl = res.fileID  //云端返回的图片地址
									uniCloud.callFunction({  //调用云端函数，把图片地址写入表
										name: 'addImage',  //云函数名称
										data: {				//提交给云端的数据
											imageUrl: imageUrl,									
											createTime: Date.now()
										},
										success: (res) => {	
											//console.log('数据插入成功')
											console.log(res)
										},
										fail: (err) => {
											console.log(err)
										},
										complete: () => {
											
										}				
									})
								},
								fail(err) {
									console.log(err)
								},
								complete() {
									uni.hideLoading()
								}
							});		
						}
					}
				});
			},
			
			// browseImage() {				
			// 	uni.navigateTo({  //跳转到指定页面
			// 		url: "../browseImage/browseImage",
			// 	});
			// }
		}
	}
</script>

<style>
	.btn{
		margin: 10px;
		background-color: #4CD964;
	}
</style> -->

<template>
	<view class="free-panel-title">
		<view class="free-WaterfallFlow">
		  <block>
			<view class="flex-wrap" v-for="(item,index) in imgList" :key="index" v-if="index % 2 != 0">
				<image mode="widthFix" :src="item.imageUrl" :data-src="item.imageUrl" @click="clickimg" ></image>
				<view>评论</view>
				<view> {{item.createTime}} </view>
			</view>
		  </block>
		  <block>
			<view class="flex-wrap" v-for="(item,index) in imgList" :key="'2-'+index" v-if="index % 2 == 0">
				<image mode="widthFix" :src="item.imageUrl" :data-src="item.imageUrl" @click="clickimg" ></image>
				<view>评论</view>
				<view> {{item.createTime}} </view>
			</view>
		  </block>
		</view>
		<!--返回顶部-->
		<view class="top" :style="{'display':(flag===true? 'block':'none')}">
			<!-- <image class="topc" @click="top" src="../../static/top.png" ></image> -->
		</view>
	</view>
</template>

<script>

	export default {
		data() {
			return {				
				imgList: [],				
				flag: false
			}
		},
		
		onLoad() {
			uni.showLoading({
				title: '查询中...'
			})
			uniCloud.callFunction({  //调用云函数
				name:'selectImages',  //云函数名称
				success: res => {
					//console.log(res)
					this.imgList = res.result.data  //云端返回的数据
					this.imgList.forEach( item => {  //循环调用函数happenTimeFun，将时间戳转为年月日
					    item.createTime = this.happenTimeFun(item.createTime)  
					})
				},
				fail(e) {
					console.log(e)
				},
				complete: () => {
					uni.hideLoading()
				}	
			})
		},
		
		methods: {	
			happenTimeFun(num){  //时间戳数据处理
				let date = new Date(num);  //时间戳为10位需*1000，时间戳为13位的话不需乘1000				
				let y = date.getFullYear();
				let MM = date.getMonth() + 1;
				MM = MM < 10 ? ('0' + MM) : MM;//月补0
				let d = date.getDate();
				d = d < 10 ? ('0' + d) : d;//天补0
				let h = date.getHours();
				h = h < 10 ? ('0' + h) : h;//小时补0
				let m = date.getMinutes();
				m = m < 10 ? ('0' + m) : m;//分钟补0
				let s = date.getSeconds();
				s = s < 10 ? ('0' + s) : s;//秒补0
				return y + '-' + MM + '-' + d; //年月日
				//return y + '-' + MM + '-' + d + ' ' + h + ':' + m+ ':' + s; //年月日时分秒
			}, 
			
			// 图片预览
			clickimg(event) {
				var imgurl = event.currentTarget.dataset.src
				var currentUrl = event.currentTarget.dataset.src   //获取点击图片的地址, **对应<template>里面的 :data-src="item.src"					
				uni.previewImage({       
					urls: [imgurl],    //这里是单图 . 需要预览的全部图片地址,这个数组是必须的,要用[] 					
					current: currentUrl, //当前显示图片的地址					
				})  
			},
			
			//回到顶部
			top() { 
				uni.pageScrollTo({
					scrollTop: 0,
					duration: 300
				});
			},
			onPageScroll(e) { //根据距离顶部距离是否显示回到顶部按钮
				if(e.scrollTop>600){ //当距离大于600时显示回到顶部按钮
					this.flag=true
				}else{ //当距离小于600时隐藏回到顶部按钮
					this.flag=false
				}
			}

		}
	}
</script>

<style>
	.free-WaterfallFlow{
		width:96%;
		column-count:2; /* 分隔的列数 */
	}
	.free-WaterfallFlow .flex-wrap{
		display: inline-block;
		width:98%;
		margin-left:3%;
		margin-bottom:3%;		
		padding:2%;
		padding-top:5%;	
		border:0px solid #cc22b0; /* 边框 */
		box-shadow: 0 2px 2px rgba(34, 25, 25, 0.4); /* 框阴影 */
		text-align: center; /* 框内元素居中对齐 */
	}
	.flex-wrap image{
		width:95%;
		margin:0 auto;
	}
	.flex-wrap view:nth-child(2){
		font-size:15px;
		padding:2% 0;
		color:#717171;
	}
	.flex-wrap view:nth-child(3){
		font-size:13px;
		padding:2% 0;
		color:#aaa;
		text-align: right;
	}
	
	/* 回到顶部 */
	.top {
		position: relative;
		display: none; /* 先将元素隐藏 */
	} 
	.topc {
		height: 30px; 
		width: 30px;
		position: fixed;
		right: 5px;
		top: 80%;
	}
</style>
