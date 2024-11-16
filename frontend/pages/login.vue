<script setup lang="ts">
// definePageMeta({
//     layout: 'auth'
// })

import { ref } from 'vue';
useSeoMeta({
  title: 'Login'
})

const username = ref("")
const password = ref("")


import { useApi } from '~/composables/useApi';
const { apiBaseUrl } = useApi();

import { useAuthStore } from '~/composables/auth';
const authStore = useAuthStore();


const login_in = async (credentials: any) => {
  // 这里应该是你的登录逻辑，比如调用API
  // 假设登录成功，我们调用store的login方法
  authStore.login(credentials);
};

const login = async () => {
  try {
    const response = await fetch(apiBaseUrl.value + 'auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username: username.value, password: password.value }),
    });
    const result = await response.json();
    console.log(result);
    if (response.ok) {
      //   store.setToken(result.access_token);
      ElMessage({
        duration: 1000,
        message: '登录成功！',
        type: 'success',
      })
      login_in(result.access_token)
      navigateTo('/')
    } else {
      throw new Error(result.msg);
    }
  } catch (error) {
    console.error('Login error:', error);
    ElMessage.error('用户不存在或者密码错误！');
  }
};

</script>

<template>
  <div class="bgc">
    <div class="sbgc">
  <div class="loginBox">
    <div class="title">Login</div>
    <form @submit.prevent="login">
      <div class="item">
        <input type="text" v-model="username" required />
        <label for="">用户名</label>
      </div>
      <div class="item">
        <input type="password" v-model="password" required />
        <label for="">密码</label>
      </div>
      <div>
      </div>
      <div style="display:flex; justify-content:center;">
      <button class="btn" type="submit">登陆
      
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
    </form>
  </div>
  <div class="links">
    <div>
     <a href="/" class="link">返回主页</a>
    </div>
    <div>
     <a href="/forgetPassword" class="link">忘记密码？</a>
    </div>
    <div>
     <a href="/register" class="link">注册</a>
    </div>
  </div>
</div>
</div>
</template>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

a {
  text-decoration: none;
}

input,
button {
  background: transparent;
  border: 0;
  outline: none;
}

.bgc {
  height: 100vh;
  background-color: #edecec;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 16px;
  color: #03e9f4;
  flex-direction: column;
}
.sbgc{
    height: 80%;
    width: 60%;
    background-color: #ffffff;
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 10px;
    box-shadow: 0px 1px 5px 0px rgba(0, 0, 0, 0.5);
}

.links{
  margin-top: 50px;
  margin-bottom: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 60px;
}
.link{
  color: #070636;
  padding: 5px;
}
.link:hover {
  border-radius: 5px;
  color: #ffffff;

  background: #0b1624;
  box-shadow: 0 0 5px 0 #070636,
              0 0 5px 0 #070636,
              0 0 5px 0 #070636,
              0 0 5px 0 #070636;

  transition: all 0.5s linear;
}

.loginBox {
  width: 400px;
  height: 399px;
  background-color: #ffffff;
  border-radius: 10px;
  box-shadow: 0 15px 25px 0 rgba(0, 0, 0, .6);
  padding: 40px;
  box-sizing: border-box;
  margin-top: 70px;
}

.title {
  text-align: center;
  color: #0b1624;
  margin-bottom: 35px;
  font-family: fantasy;
  font-size:30px;
}

.item {
  height: 45px;
  border-bottom: 1px solid #070636;
  margin-bottom: 30px;
  position: relative;
}

.item input {
  width: 100%;
  height: 100%;
  color: #070636;
  padding-top: 20px;
  box-sizing: border-box;
}

.item input:focus + label,
.item input:valid + label {
  top: 0px;
  font-size: 12px; /* 修改为适合的字体大小 */
}

.item label {
  position: absolute;
  left: 0;
  top: 12px;
  transition: all 0.5s linear;
  color: #0b1624;
}

.btn {
  padding: 10px 20px;
  margin-top: 15px;
  color: #0b1624;
  position: relative;
  overflow: hidden;
  text-transform: uppercase;
  letter-spacing: 2px;
}

.btn:hover {
  border-radius: 5px;
  color: #fff;
  background: #070636;
  box-shadow: 0 0 5px 0 #070636,
              0 0 25px 0 #070636,
              0 0 25px 0 #070636,
              0 0 25px 0 #070636;
  transition: all 0.7s linear;
}

.btn > span {
  position: absolute;
}

.btn > span:nth-child(1) {
  width: 100%;
  height: 2px;
  background: linear-gradient(left, transparent, #03e9f4);
  left: -100%;
  top: 0px;
  animation: line1 1s linear infinite;
}

@keyframes line1 {
  50%, 100% {
    left: 100%;
  }
}

.btn > span:nth-child(2) {
  width: 2px;
  height: 100%;
  background: linear-gradient(top, transparent, #03e9f4);
  right: 0px;
  top: -100%;
  animation: line2 1s 0.25s linear infinite;
}

@keyframes line2 {
  50%, 100% {
    top: 100%;
  }
}

.btn > span:nth-child(3) {
  width: 100%;
  height: 2px;
  background: linear-gradient(left, #03e9f4, transparent);
  left: 100%;
  bottom: 0px;
  animation: line3 1s 0.75s linear infinite;
}

@keyframes line3 {
  50%, 100% {
    left: -100%;
  }
}

.btn > span:nth-child(4) {
  width: 2px;
  height: 100%;
  background: linear-gradient(top, transparent, #03e9f4);
  left: 0px;
  top: 100%;
  animation: line4 1s 1s linear infinite;
}

@keyframes line4 {
  50%, 100% {
    top: -100%;
  }
}

</style>