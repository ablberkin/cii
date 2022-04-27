<template>
	<view>
		<!-- 学院选择器 -->
		<scroll-view ref="tabbar1" id="tab-bar" class="tab-bar" :scroll="false" :scroll-x="true" :show-scrollbar="false"
		  :scroll-into-view="scrollInto">
		  <view style="flex-direction: column;">
		    <view style="flex-direction: row;">
		      <view class="uni-tab-item" v-for="(tab,index) in tabList" :key="tab.id" :id="tab.id" :ref="'tabitem'+index"
		        :data-id="index" :data-current="index" @click="ontabtap">
		        <text class="uni-tab-item-title" :class="tabIndex==index ? 'uni-tab-item-title-active' : ''">{{tab.name}}</text>
		      </view>
		    </view>
		    <view class="scroll-view-indicator">
		      <view ref="underline" class="scroll-view-underline" :class="isTap ? 'scroll-view-animation':''" :style="{left: indicatorLineLeft + 'px', width: indicatorLineWidth + 'px'}"></view>
		    </view>
		  </view>
		</scroll-view>
		
		<!-- 轮播图 -->
		<view class="uni-margin-wrap">
			<swiper class="swiper"  :autoplay='true' :interval="3000" :duration="1000">
				<swiper-item>
					<view class="swiper-item uni-bg-red">A</view>
				</swiper-item>
				<swiper-item>
					<view class="swiper-item uni-bg-green">B</view>
				</swiper-item>
				<swiper-item>
					<view class="swiper-item uni-bg-blue">C</view>
				</swiper-item>
			</swiper>
		</view>
		
		<!-- 新闻页面 -->
		<view>
			<div v-for='(item,index) in newsList' :key='newsList.id'>
				<!-- <navigator :url="'/pages/index/newsDetail?id='+ item.id"  hover-class="navigator-hover"> -->
				<navigator :url="'/pages/index/newsDetail?id='+ item.id"  hover-class="navigator-hover">
					<uni-card :title='item.title'>
						<text>{{item.introduction}}</text>
					</uni-card>
				</navigator>
			</div>
		</view>
		
		<!-- 编辑器按钮 -->
		<view>
			<navigator url="../editor/schoolNewsEditor">
				<uni-fab
						:pattern="pattern"
						:horizontal="horizontal"
						:vertical="vertical"
						:direction="direction"
				></uni-fab>
			</navigator>
		</view>
	</view>
</template>

<script>
	export default{
		name:'newsindex',
		data(){
			return{
				newsList:null,
				url:'',
				id:'',
				title:'',
				introduction:'',
				tabList: [{
				  id: "tab01",
				  name: '经管书院',
				  newsid: 0
				}, {
				  id: "tab02",
				  name: '孟院',
				  newsid: 23
				}, {
				  id: "tab03",
				  name: '内容',
				  newsid: 223
				}, {
				  id: "tab04",
				  name: '消费',
				  newsid: 221
				}, {
				  id: "tab05",
				  name: '娱乐',
				  newsid: 225
				}, {
				  id: "tab06",
				  name: '区块链',
				  newsid: 208
				}],
				tabIndex: 0,
				cacheTab: [],
				scrollInto: "",
				navigateFlag: false,
				indicatorLineLeft: 0,
				indicatorLineWidth: 0,
				isTap: false,
				// 编辑器样式设置
				horizontal: 'right',
				vertical: 'bottom',
				direction: 'horizontal',
				pattern: {
						color: '#7A7E83',
						backgroundColor: '#fff',
						selectedColor: '#007AFF',
					}
				}
			},
		methods:{
			// 读取后台数据
			getAll(){
				uni.request({
					url:'http://127.0.0.1:8000/newsindex/',
					data: {
						newsList:'',
						url:'',
						id:'',
						title:'',
						introduction:'',
					},
					method:'GET',
					success:(res)=>{
						this.newsList = res.data;
						// console.log(this.newsList[0].id)
					},
				})
			},
			
		},
		
		// 挂载时加载信息
		mounted(){
		  this.getAll();
		}
	}
</script>

<style>
	.tab-bar {
	  /* #ifdef APP-PLUS */
	  width: 750rpx;
	  /* #endif */
	  height: 42px;
	  flex-direction: row;
	  /* #ifndef APP-PLUS */
	  white-space: nowrap;
	  /* #endif */
	}
	
	/* #ifndef APP-NVUE */
	.tab-bar ::-webkit-scrollbar {
	  display: none;
	  width: 0 !important;
	  height: 0 !important;
	  -webkit-appearance: none;
	  background: transparent;
	}
	
	/* #endif */
	
	.tab-bar-line {
	  height: 1px;
	  background-color: #cccccc;
	}
	
	.uni-tab-item {
	  /* #ifndef APP-PLUS */
	  display: inline-block;
	  /* #endif */
	  flex-wrap: nowrap;
	  padding-left: 20px;
	  padding-right: 20px;
	}
	
	.uni-tab-item-title {
	  color: #555;
	  font-size: 15px;
	  height: 40px;
	  line-height: 40px;
	  flex-wrap: nowrap;
	  /* #ifndef APP-PLUS */
	  white-space: nowrap;
	  /* #endif */
	}
	
	.uni-tab-item-title-active {
	  color: #007AFF;
	}
	
</style>