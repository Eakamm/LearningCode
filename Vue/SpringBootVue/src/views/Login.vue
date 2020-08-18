<template>
	<div id="login">
		<el-card>
			<el-row>
				<el-col>登录</el-col>
				<el-col>
					账号：
					<el-input
					  placeholder="请输入内容"
					  v-model="account"
					  clearable>
					</el-input>
				</el-col>
				<el-col>
					密码
					<el-input
					  placeholder="请输入内容"
					  v-model="password"
					  show-password>
					</el-input>
				</el-col>
			</el-row>
		</el-card>
	</div>
</template>

<script>

	

</script>

<style>
</style>
