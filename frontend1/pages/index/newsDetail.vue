<template>
	<view>
		<uni-list>
			<!-- <template v-slot:right> -->
				<uni-fav :checked="checkList[1]" :star="false" class="favBtn" @click="favClick(1)" />
				<uni-fav :checked="checkList[5]"  :circle="true" @click="favClick(5)" />
			<!-- </template> -->
		</uni-list>
			
		<view class='title'>{{newsDetail.title}}</view>
		<view>作者：{{username}}</view>
		<view>修改时间：{{getTime()}}</view>
		<view class='content' v-html="newsDetail.body"></view>

		
	</view>
</template>



<script>
	export default{
		name:'newsDetail',
		data(){
			return{
				newsDetail:'',
				checkList: [false, false, false, false, false, false],
				username:'unknown',
			}
		},
		methods:{
			// 测试mp属性所用函数
			// test: function() {
			// 			console.log(this.$mp.query.id);
			// 		},
					
			getAll(){
				// 在家进行测试所用ip地址
				// const baseUrl = 'http://192.168.1.27:8000/newsindex/'
				const baseUrl = 'http://127.0.0.1:8000/newsindex/'
				uni.request({
					// 微信小程序需要mp属性
					url : baseUrl + this.$mp.query.id,
					// url:'http://127.0.0.1:8000/newsindex/' + this.$route.query.id,
					data: {
						newsDetail:'',
						url:'',
						id:'',
						title:'',
						introduction:'',
						
					},
					method:'GET',
					success:(res)=>{
						this.newsDetail = res.data;
						// vm : this.$route
						console.log(this.newsDetail.author)
						// 获取作者信息
						uni.request({
							url : this.newsDetail.author,
							// url:'http://127.0.0.1:8000/newsindex/' + this.$route.query.id,
							data: {
								username:'unknown',
							},
							method:'GET',
							success:(res)=>{
								// vm : this.$route
								this.username = res.data.username
								console.log('用户名',this.username)
								
								}
						})
					},
				})
			},
			getTime(){
				// 获取文章更新时间
				// 用v-if解决提前渲染的问题
				return this.newsDetail.updated.slice(0,10)+' '+this.newsDetail.updated.slice(11,16)
			},
			favClick(index) {
				this.checkList[index] = !this.checkList[index]
				console.log(this.checkList[index]);
				this.$forceUpdate()
			}

			
		},
		

		
		mounted(){
		  this.getAll();
		}
		
	}
</script>

<style lang="scss">
	.title{
		font-size: 36upx;
		color: #303133;
		margin-bottom: 16upx;
		text-align: center;
	}
	page{
		height: 100%;
	}
	
	.content{
		font-size: 28upx;
		color: #333;
		padding-top:20upx;
	}
	
	
</style>
