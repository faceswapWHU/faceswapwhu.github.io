<script setup lang="ts">
definePageMeta({
})

useSeoMeta({
    title: 'Login'
})


const email = ref("")
const code = ref("")
import { useAuthStore } from '~/composables/auth';
import { useApi } from '~/composables/useApi';
const { apiBaseUrl } = useApi();

const authStore = useAuthStore();

// 倒计时秒数
const countdown = ref(60);

// 是否正在倒计时
const isCountingDown = ref(false);

// 启动倒计时
const startCountdown = () => {
  isCountingDown.value = true;
  countdown.value = 60; // 重置倒计时秒数
  const timer = setInterval(() => {
    if (countdown.value > 0) {
      countdown.value--;
    } else {
      clearInterval(timer);
      isCountingDown.value = false;
    }
  }, 1000);
};

async function onReSet(data: any) {
    if (code.value == "") {
        ElMessage({
            message: '请输入验证码！',
            type: 'warning',
        })
        return;
    }
    try {
        const response = await fetch(apiBaseUrl.value + 'auth/reset_password', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email: email.value, code: code.value }),
        });
        const result = await response.json();
        if (response.ok) {
            //   store.setToken(result.access_token);
            ElMessage({
                showClose: true,
                duration: 0,
                message: '您的密码已被重置为123456,请您马上登录修改密码',
                type: 'warning',
            })
            navigateTo('/login')
        } else {
            ElMessage({
                message: '验证码错误！',
                type: 'error',
            })
        }
    } catch (error) {
        console.error('Login error:', error);
    }
}

function validateEmail(email: string) {
    const regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    return regex.test(email);
}

async function sendCode() {
    if (!validateEmail(email.value)) {
        ElMessage.error('请输入正确的邮箱！')
        return;
    }
    console.log(email.value)
    try {
        const response = await fetch(apiBaseUrl.value + 'auth/send_reset_code', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email: email.value }),
        });
        const result = await response.json();
        if (!response.ok) {
            ElMessage.error('该邮箱与任何账号绑定！')
        }
        else {
            ElMessage({
                message: '已发送验证码！',
                type: 'success',
            })
            startCountdown();
        }
    } catch (error) {

    }
}
</script>

<template>
    <div class="bgc">
      <div class="sbgc">
    <div class="loginBox">
      <div class="title">Retrieve Password</div>
      <form>
        <div class="item">
          <input type="text" v-model="username" required />
          <label for="email">Email</label>
        </div>
        <div class="item">
          <input type="password" v-model="password" required style="width:55%;"/>
          <label for="code">验证码</label>
          <div style="display:block; width:35%;">
          <button class="btn2" @click="sendCode" :disabled="isCountingDown">
            <div v-if="isCountingDown"> {{ countdown }} 秒</div>
            <div v-else>发送</div>
          </button>
        </div>
        </div>
        <div>
        </div>
        <div style="display:flex; justify-content:center;">
        <button class="btn" @click="onReSet">确认
        
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
      height: auto;
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
    margin-bottom: 40px;
    font-family: fantasy;
    font-size:30px;
  }
  
  .item {
    height: 45px;
    margin-bottom: 30px;
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }
  
  .item input {
    width: 100%;
    height: 100%;
    color: #070636;
    padding-top: 20px;
    box-sizing: border-box;
    border-bottom: 1px solid #070636;
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
  
  .btn2{
    border-radius: 5px;
    color: #ffffff;
    width:100%;
    height:100%;
    background: #0b1624;
  }

  .btn2:hover{
    border-radius: 5px;
    color: #ffffff;
  
    background: #0b1624;
    box-shadow: 0 0 10px 0 #070636,
                0 0 10px 0 #070636,
                0 0 10px 0 #070636,
                0 0 10px 0 #070636;
  
    transition: all 0.5s linear;
  }

  .btn {
    padding: 10px 20px;
    margin-top: 20px;
    color: #0b1624;
    overflow: hidden;
    text-transform: uppercase;
    letter-spacing: 2px;
    display: flex;
    justify-content: center;
    flex-direction: column;
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