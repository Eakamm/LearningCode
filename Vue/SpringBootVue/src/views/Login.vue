<template>
  <div id="login">
    <el-form ref="form" label-width="80px" class="login-form">
      <el-form-item>
        <h3 class="title">注册</h3>
      </el-form-item>
      <el-form-item label="账号">
        <el-input v-model="account"></el-input>
      </el-form-item>

      <el-form-item label="密码">
        <el-input v-model="password"></el-input>
      </el-form-item>

      <el-form-item label="验证码">
        <el-input v-model="captcha"></el-input>
        <div>
          <img :src="codeUrl" @click="getCaptcha"/>
        </div>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="onSubmit">立即注册</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      password: "",
      account: "",
      captcha:'',
      codeUrl:'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'
    };
  },
  created(){
    this.getCaptcha()
  },
  methods: {
    onSubmit() {
      axios({
        method: "POST",
        url: "http://localhost:8080/user/api/register",
        data: {
          password: this.password,
          username: this.account
        }
      }).then(response => {
        this.$message(response);
        console.log(response);
      });
    },
    getCaptcha(){
      axios({
        method: 'GET',
        url: 'http://localhost:8080/captchaImage',
      }).then(response => {
        // this.$message(response);
        // console.log(response);
        this.codeUrl = "data:image/gif;base64," + response.data.img
        console.log(this.codeUrl);
      });
    }
  }
};
</script>

<style>
.login {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  background-size: cover;
}

.title {
  margin: 0px auto 30px auto;
  text-align: center;
  color: #707070;
}

.login-form {
  border-radius: 6px;
  background: #ffffff;
  width: 400px;
  padding: 25px 25px 5px 25px;
}
</style>
