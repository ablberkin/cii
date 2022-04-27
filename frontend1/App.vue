<script>
	export default {
		onLaunch: function() {
			console.log('App Launch')
		},
		onShow: function() {
			console.log('App Show')
		},
		onHide: function() {
			console.log('App Hide')
		}
	}
</script>

<style lang="scss">
	/* 注意要写在第一行，同时给style标签加入lang="scss"属性 */
	// @import "@/uni_modules/vk-uview-ui/index.scss";
	// @import "./uni_modules/vk-uview-ui/index.scss";
	@import "@/uni_modules/uview-ui/index.scss";
	/*每个页面公共css */
		/* hello uniapp所用样式 */
		@import './common/uni.css';
		@import "@/static/iconfont.css";
		@import '@/uni_modules/vk-uview-ui/theme.scss';
		// @import "uview-ui/index.scss";
		

</style>
