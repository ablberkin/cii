<template>
	<view>
		<view>
			<view class="content">
				<navigator url="./newsindex" hover-class="navigator-hover">
				                    <xt-colorful-card header="学院讯息":borderRadius="30" color-from="#ABDCFF" color-to="#0396FF" class="mb-2"></xt-colorful-card>
				</navigator>
				<navigator url="./academic/academicIndex" hover-class="navigator-hover">
					<xt-colorful-card header="学术信息":borderRadius="30" color-from="#FEB692" color-to="#EA5455" class="mb-2"></xt-colorful-card>
				</navigator>
				<navigator url="./lifeInformationIndex" hover-class="navigator-hover">
					<xt-colorful-card header="生活信息":borderRadius="30" color-from="#90F7EC" color-to="#32CCBC" class="mb-2"></xt-colorful-card>
				</navigator>
				<navigator url="./newsindex" hover-class="navigator-hover">
					<xt-colorful-card header="党政资讯":borderRadius="30" color-from="#FF2222" color-to="#FF0000" class="mb-2"></xt-colorful-card>
				</navigator>
			</view>
			<!-- <uni-grid :column="2">
			    <uni-grid-item>
					<navigator url="../college/college" hover-class="navigator-hover">
						<image src="../../static/image/index/school.png" class="school" ></image>
					</navigator>
			    </uni-grid-item>
			    <uni-grid-item>
					<navigator url="../college/college" hover-class="navigator-hover">
						<image src="../../static/image/index/aca.png" class="school" ></image>
					</navigator>
			    </uni-grid-item>
			    <uni-grid-item>
					<navigator url="../college/college" hover-class="navigator-hover">
						<image src="../../static/image/index/leben.png" class="school" ></image>
					</navigator>
			    </uni-grid-item>
				<uni-grid-item>
					<navigator url="../college/college" hover-class="navigator-hover">
						<image src="../../static/image/index/party.png" class="school" ></image>
					</navigator>
				</uni-grid-item>
			</uni-grid> -->
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		onLoad() {

		},
		methods: {

		}
	}
</script>

<style>
	.school{
		display: flex;
		width: 750rpx;
		height: 100rpx;
	}
	.text1{
		font-size: 50rpx;
	}
</style>
