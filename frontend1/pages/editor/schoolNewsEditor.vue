<template>
	<view class="container">
		<view class="uni-list">
			<view class="uni-list-cell">
				<view class="uni-list-cell-left">
					学院
				</view>
				<view class="uni-list-cell-db">
					<picker @change="bindPickerChange" :value="index" :range="array" range-key="name">
						<view class="uni-input">{{array[index].name}}</view>
					</picker>
				</view>
			</view>
			<view class="uni-list-cell">
				<view class="uni-list-cell-left">
					标题
				</view>
				<view class="uni-list-cell-db">
					<uni-easyinput focus v-model="title" placeholder="请输入内容"></uni-easyinput>
				</view>
			</view>
			<view class="uni-list-cell">
				<view class="uni-list-cell-left">
					简介
				</view>
				<view class="uni-list-cell-db">
					<uni-easyinput focus v-model="introduction" placeholder="请输入内容"></uni-easyinput>
				</view>
			</view>
		</view>
		<view class="page-body">
			<view class='wrapper'>
				<view class='toolbar' @tap="format" style="height: 120px;overflow-y: auto;">
					<view :class="formats.bold ? 'ql-active' : ''" class="iconfont icon-zitijiacu" data-name="bold"></view>
					<view :class="formats.italic ? 'ql-active' : ''" class="iconfont icon-zitixieti" data-name="italic"></view>
					<view :class="formats.underline ? 'ql-active' : ''" class="iconfont icon-zitixiahuaxian" data-name="underline"></view>
					<view :class="formats.strike ? 'ql-active' : ''" class="iconfont icon-zitishanchuxian" data-name="strike"></view>
					<view :class="formats.align === 'left' ? 'ql-active' : ''" class="iconfont icon-zuoduiqi" data-name="align"
					 data-value="left"></view>
					<view :class="formats.align === 'center' ? 'ql-active' : ''" class="iconfont icon-juzhongduiqi" data-name="align"
					 data-value="center"></view>
					<view :class="formats.align === 'right' ? 'ql-active' : ''" class="iconfont icon-youduiqi" data-name="align"
					 data-value="right"></view>
					<view :class="formats.align === 'justify' ? 'ql-active' : ''" class="iconfont icon-zuoyouduiqi" data-name="align"
					 data-value="justify"></view>
					<view :class="formats.lineHeight ? 'ql-active' : ''" class="iconfont icon-line-height" data-name="lineHeight"
					 data-value="2"></view>
					<view :class="formats.letterSpacing ? 'ql-active' : ''" class="iconfont icon-Character-Spacing" data-name="letterSpacing"
					 data-value="2em"></view>
					<view :class="formats.marginTop ? 'ql-active' : ''" class="iconfont icon-722bianjiqi_duanqianju" data-name="marginTop"
					 data-value="20px"></view>
					<view :class="formats.previewarginBottom ? 'ql-active' : ''" class="iconfont icon-723bianjiqi_duanhouju" data-name="marginBottom"
					 data-value="20px"></view>
					<view class="iconfont icon-clearedformat" @tap="removeFormat"></view>
					<view :class="formats.fontFamily ? 'ql-active' : ''" class="iconfont icon-font" data-name="fontFamily" data-value="Pacifico"></view>
					<view :class="formats.fontSize === '24px' ? 'ql-active' : ''" class="iconfont icon-fontsize" data-name="fontSize"
					 data-value="24px"></view>

					<view :class="formats.color === '#0000ff' ? 'ql-active' : ''" class="iconfont icon-text_color" data-name="color"
					 data-value="#0000ff"></view>
					<view :class="formats.backgroundColor === '#00ff00' ? 'ql-active' : ''" class="iconfont icon-fontbgcolor"
					 data-name="backgroundColor" data-value="#00ff00"></view>

					<view class="iconfont icon-date" @tap="insertDate"></view>
					<view class="iconfont icon--checklist" data-name="list" data-value="check"></view>
					<view :class="formats.list === 'ordered' ? 'ql-active' : ''" class="iconfont icon-youxupailie" data-name="list"
					 data-value="ordered"></view>
					<view :class="formats.list === 'bullet' ? 'ql-active' : ''" class="iconfont icon-wuxupailie" data-name="list"
					 data-value="bullet"></view>
					<view class="iconfont icon-undo" @tap="undo"></view>
					<view class="iconfont icon-redo" @tap="redo"></view>

					<view class="iconfont icon-outdent" data-name="indent" data-value="-1"></view>
					<view class="iconfont icon-indent" data-name="indent" data-value="+1"></view>
					<view class="iconfont icon-fengexian" @tap="insertDivider"></view>
					<view class="iconfont icon-charutupian" @tap="insertImage"></view>
					<view :class="formats.header === 1 ? 'ql-active' : ''" class="iconfont icon-format-header-1" data-name="header"
					 :data-value="1"></view>
					<view :class="formats.script === 'sub' ? 'ql-active' : ''" class="iconfont icon-zitixiabiao" data-name="script"
					 data-value="sub"></view>
					<view :class="formats.script === 'super' ? 'ql-active' : ''" class="iconfont icon-zitishangbiao" data-name="script"
					 data-value="super"></view>
					<view class="iconfont icon-shanchu" @tap="clear"></view>
					<view :class="formats.direction === 'rtl' ? 'ql-active' : ''" class="iconfont icon-direction-rtl" data-name="direction"
					 data-value="rtl"></view>

				</view>

				<view class="editor-wrapper">
					<editor id="editor" class="ql-container" placeholder="开始输入吧..." showImgSize showImgToolbar showImgResize
					 @statuschange="onStatusChange"  @ready="onEditorReady" v-model='content'>
					</editor>
				</view>
			</view>
		</view>
		

		<view class="icon-content" >
			<view class="icon-item" @click="saveBlog()">
				<uni-icons custom-prefix="iconfont" type="icon-baocun" size="30"></uni-icons>
				<text style="color:#5e6d82;">保存</text>
			</view>
		</view>


	</view>
</template>

<script>
	export default {
		data() {
			return {
				// 选择器 
				title: '',
				formats: {},
				array: [{name:'经管书院'},{name: '孟承宪书院'}, {name:'巴西'}, {name:'日本'}],
				index: 0,
				body:'',
				introduction: '',
				content: '',
				imageUrl: '',
			}
		},
		onShow () {
			this.init()
		},
		methods: {
			init () {
				//本应该在onshow里面做，uniapp新版本有bug，switchTab不会触发onShow
				this.currentUser = uni.getStorageSync('currentUser');
			},
			bindPickerChange: function(e) {
				console.log('picker发送选择改变，携带值为：' + e.detail.value)
				this.index = e.detail.value
			},
			
			// editor方法
			readOnlyChange() {
				this.readOnly = !this.readOnly
			},
			onEditorReady() {
				uni.createSelectorQuery().select('#editor').context((res) => {
					this.editorCtx = res.context
				}).exec()
			},
			undo() {
				this.editorCtx.undo()
			},
			redo() {
				this.editorCtx.redo()
			},
			format(e) {
				let {
					name,
					value
				} = e.target.dataset
				if (!name) return
				// console.log('format', name, value)
				this.editorCtx.format(name, value)

			},
			onStatusChange(e) {
				const formats = e.detail
				this.formats = formats
			},
			insertDivider() {
				this.editorCtx.insertDivider({
					success: function() {
						console.log('insert divider success')
					}
				})
			},
			clear() {
				this.editorCtx.clear({
					success: function(res) {
						console.log("clear success")
					}
				})
			},
			removeFormat() {
				this.editorCtx.removeFormat()
			},
			insertDate() {
				const date = new Date()
				const formatDate = `${date.getFullYear()}/${date.getMonth() + 1}/${date.getDate()}`
				this.editorCtx.insertText({
					text: formatDate
				})
			},
			insertImage() {
				uni.chooseImage({
					count: 1,
					success: (res) => {
						let that = this;
						let filePath = res.tempFilePaths[0]
						// callback方式 ，进行上传操作
						uniCloud.uploadFile({
							filePath: filePath,  //要上传的文件对象
							cloudPath: Date.now() + '.jpg',  //保存在云端的文件名，这里以时间戳命名
							// cloudPath: res.tempFilePaths[0].split('/',-1)[3] + '.jpg',  //保存在云端的文件名，这里以时间戳命名
							success(res) {
								//console.log(res.fileID)
								this.imageUrl = res.fileID  //云端返回的图片地址
								uniCloud.callFunction({  //调用云端函数，把图片地址写入表
									name: 'addImage',  //云函数名称
									data: {				//提交给云端的数据
										// imageUrl: this.imageUrl,
										imageUrl: this.imageUrl,
										createTime: Date.now()
									},
									success: (res) => {	
										that.editorCtx.insertImage({
											// src: res.tempFilePaths[0],
											src: this.imageUrl,
											alt: '图像',
											success: function() {
												console.log('编辑器插入', res.tempFilePaths[0].split('/',-1)[3])
												console.log('插入2:',res.tempFilePaths[0])
												}
												})
										//console.log('数据插入成功')
										console.log('成功回调函数地址',this.imageUrl)
										console.log('成功回调函数path',filePath)
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
						// this.editorCtx.insertImage({
						// 	src: res.tempFilePaths[0],
						// 	// src: this.imageUrl,
						// 	alt: '图像',
						// 	success: function() {
						// 		console.log('编辑器插入', res.tempFilePaths[0].split('/',-1)[3])
						// 		console.log('插入2:',res.tempFilePaths[0])
						// 		}
						// 		})
					},
					async complete(){
						console.log('结束', this.imageUrl)
						// this.editorCtx.insertImage({src:  this.imageUrl})
					}
				})
								
								// let filePath = res.tempFilePaths[0]
								// // callback方式 ，进行上传操作
								// uniCloud.uploadFile({
								// 	filePath: filePath,  //要上传的文件对象
								// 	cloudPath: Date.now() + '.jpg',  //保存在云端的文件名，这里以时间戳命名
								// 	success(res) {
								// 		//console.log(res.fileID)
								// 		let imageUrl = res.fileID  //云端返回的图片地址
								// 		uniCloud.callFunction({  //调用云端函数，把图片地址写入表
								// 			name: 'addImage',  //云函数名称
								// 			data: {				//提交给云端的数据
								// 				imageUrl: imageUrl,									
								// 				createTime: Date.now()
								// 			},
								// 			success: (res) => {	
								// 				//console.log('数据插入成功')
								// 				console.log(res)
								// 			},
								// 			fail: (err) => {
								// 				console.log(err)
								// 			},
								// 			complete: () => {
												
								// 			}				
								// 		})
								// 	},
								// 	fail(err) {
								// 		console.log(err)
								// 	},
								// 	complete() {
								// 		uni.hideLoading()
								// 	}
								// });		
								
								// uni.uploadFile({
								// 	url: 'http://127.0.0.1:8000/img/', //域名+上传文件的请求接口 (根据你实际的接口来)       
								// 	method:'POST',
								// 	filePath: res.tempFilePaths[0],
								// 	// filePath: res.tempFilePaths[0], // tempFilePath可以作为img标签的src属性显示图片 服务器图片的路径         
								// 	name: 'img', //上传到服务器的参数，自定义
								// 	// header: {
								// 	// 	"Content-Type": "multipart/form-data"
								// 	// },          
								// 	success(res) {
								// 		console.log('res:',res)
								// 		// var data = JSON.parse(res.data)
								// 		that.editorCtx.insertImage({
								// 			width: '100%', //设置宽度为100%防止宽度溢出手机屏幕
								// 			height: 'auto',
								// 			src: data.url, //服务端返回的url
								// 			alt: '图像',
								// 			success: function() {
								// 				console.log('666')
								// 			}
								// 		})
								// 		console.log('editorCtx',that.editorCtx)
								// 	}
								// })
						// 	}
						// })
				// 	}
				// })
					// function imgToBase64(data){
					// 	 plus.zip.compressImage({  
					// 		src: data.tempFilePaths[0],  
					// 		dst: "_doc/a.jpg",  
					// 		overwrite: true,  
					// 		width: '1920px',  
					// 		height:'1080px',  
					// 		format: 'jpg',  
					// 		quality: 100  
					// 	  },  
					// 	  function(e) {  
					// 		let reader = new plus.io.FileReader();  
					// 			reader.readAsDataURL(e.target);  
					// 			reader.onloadend = function (e) { 
					// 				//这是转成功的base64文件，需要正则去一下换行
					// 				let base64 = e.target.result.split(',')[1].replace(/[\r\n]/g,"") 
					// 				iOCR(base64)
					// 			};  
					// 	  },  
					// 	  function(err) {  
					// 		plus.nativeUI.alert('未知错误！',function() {  
					// 		});  
					// 	  }  
					// 	);  
					// }
			},
			
			saveBlog(){
				uni.request({
					url:'http://127.0.0.1:8000/newsindex/',
					data: {
						// 编辑器 
						base_url:'http://127.0.0.1:8000/newsindex/',
						author: "http://127.0.0.1:8000/users/"+this.currentUser.id+'/',
						category: "collegeNews",
						title: this.title,
						introduction: this.introduction,
						body: this.content.detail.html,
					},
					method:'post',
					success:(res)=>{
						this.body = res.data;
						// console.log(this.content.detail.text)
						uni.switchTab({
							url:'../index/index'
						});
					},
				})
			},
			
			// 文章增删查改
			// saveBlog(){
			//   //两种情况， 一种是新建博客，另一种是修改博客
			//   //通过url是否为空来判定
			//   if (this.url == ''){
			//     //新增
			//     axios.post(this.base_url, {title: this.title, body: this.body})
			// 	console.log('发送1')
			//       // .then(()=>{
			//       //   this.getAll();
			//       // })
			//   }else{
			//     //修改
			//     axios.put(this.url, {title: this.title, body: this.body})
			// 	console.log('发送2')
			//     // .then(()=>{
			//     //   this.getAll();
			//     // })
			  
			//   }
			// },
		},
		onLoad() {
			uni.loadFontFace({
				family: 'Pacifico',
				source: 'url("https://sungd.github.io/Pacifico.ttf")'
			})
		},
		// updated(){
		// 	console.log('摧毁')
		// 	this.editorCtx.insertImage({src:  this.imageUrl})
		// }

	}
</script>

<style lang="scss">
	@import "./editor-icon.css";

	.page-body {
		height: calc(100vh - var(--window-top) - var(--status-bar-height));
	}

	.wrapper {
		height: 100%;
	}

	.editor-wrapper {
		height: calc(100vh - var(--window-top) - var(--status-bar-height) - 140px);
		background: #fff;
	}

	.iconfont {
		display: inline-block;
		padding: 8px 8px;
		width: 24px;
		height: 24px;
		cursor: pointer;
		font-size: 20px;
	}

	.toolbar {
		box-sizing: border-box;
		border-bottom: 0;
		font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
	}


	.ql-container {
		box-sizing: border-box;
		padding: 12px 15px;
		width: 100%;
		min-height: 30vh;
		height: 100%;
		margin-top: 20px;
		font-size: 16px;
		line-height: 1.5;
	}

	.ql-active {
		color: #06c;
	}
	
	/* icon样式 */
	.icon-content {
		display: flex;
		flex-wrap: wrap;
		flex-direction: row;
		justify-content: center;

		.icon-item {
			/* #ifndef APP-NVUE */
			display: flex;
			box-sizing: border-box;
			width: calc(100% / 4);
			/* #endif */
			/* #ifdef APP-NVUE */
			width: 187rpx;
			/* #endif */
			align-items: center;
			padding: 10px;
			text-align: center;
			flex-direction: column;
		}
	}
	
</style>
