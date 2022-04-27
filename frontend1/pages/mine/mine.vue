<script src="../../lib/imservice.js"></script>
<template>
	
    <div class="mine">
        <div class="top">
			<uni-card :title='currentUser && currentUser.name'>
				<text>{{currentUser && currentUser.identity}}</text>
			</uni-card>
            <!-- <image :src="currentUser && currentUser.avatar"></image> -->
        </div>
		<navigator url="./login" hover-class="navigator-hover" class="login">
			<button class="login-btn">登录</button>
		</navigator>
		<navigator url="./register" hover-class="navigator-hover" >
			<view class="register">注册</view>
		</navigator>
    </div>
</template>

<script>

    export default {
        data () {
            return {
                currentUser : null,
            }
        },
        onShow () {
			this.init()
        },
        methods : {
			init () {
				//本应该在onshow里面做，uniapp新版本有bug，switchTab不会触发onShow
				this.currentUser = uni.getStorageSync('currentUser');
			},
			
            // logout () {
            //     this.goEasy.disconnect({
            //         onSuccess: function(){
            //             console.log('断连成功')
            //             uni.removeStorageSync('currentUser');
            //             getApp().globalData.imService = null;
            //             uni.navigateTo({
            //                 url : './login'
            //             })
            //         },
            //         onFailed: function(error){
            //             uni.showToast({
            //                 title:'断连失败'
            //             })
            //         }
            //     });
            // }
        }
    }
</script>

<style  lang="scss">
    .mine{
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    .top{
        height: 200rpx;
        background: #F3F4F7;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .top image{
        width:156rpx;
        height: 156rpx;
        border-radius: 156rpx;
    }
    .top .name{
        line-height: 80rpx;
    }
    .bottom{
        text-align: center;
        line-height: 200rpx;
    }
	.logout{
		width: 266rpx;
		height: 76rpx;
		line-height: 76rpx;
		margin: 0 auto;
		background-color: #618DFF;
		border-radius: 10rpx;
		color: #FFFFFF;
		font-size: 32rpx;
		
	}
	
	.login{
		padding-top: 100rpx;
		width:100%;
		height: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	
	.login-btn{
		width: 680rpx;
		height: 100rpx;
		line-height: 100rpx;
		font-size:36rpx ;
		text-align: center;
		color: #ffffff;
		background: #618DFF;
		outline: none;
		border: 0;
	}
	
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
				// color: $u-type-info;
				margin-bottom: 60rpx;
				margin-top: 8rpx;
			}
	 
			.getCaptcha {
				background-color: rgb(253, 243, 208);
				// color: $u-tips-color;
				border: none;
				font-size: 30rpx;
				padding: 12rpx 0;
	 
				&::after {
					border: none;
				}
			}
	 
			.alternative {
				// color: $u-tips-color;
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
					// color: $u-content-color;
					font-size: 28rpx;
				}
			}
	 
			.hint {
				padding: 20rpx 40rpx;
				font-size: 20rpx;
				// color: $u-tips-color;
	 
				.link {
					// color: $u-type-warning;
				}
			}
		}
	}
	/* 注册 */
	.register {
		/* text-align:center; */
		color:#82848A;
		display: flex;
		justify-content:center;
		margin-top: 30rpx;
		align-items: center;
		/* margin:0 auto; */
	}
</style>