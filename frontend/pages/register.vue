<script setup lang="ts">
definePageMeta({
})

useSeoMeta({
    title: 'Register'
})



import { useApi } from '~/composables/useApi';
const { apiBaseUrl } = useApi();


const username = ref("")
const password = ref("")
const repassword = ref("")

async function onReg(data: any) {
    checkUsername();
    if (uE.value) return;
    checkPass();
    if (uP.value) return;

    console.log(JSON.stringify({
        username: username.value,
        password: password.value
    }))
    if (repassword.value != password.value) {
        ElMessage({
            showClose: true,
            message: '请输入相同的密码',
            type: 'warning',
        })
        return
    }
    try {
        const regresponse = await fetch(apiBaseUrl.value + 'auth/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
                //?
            },
            body: JSON.stringify({
                username: username.value,
                password: password.value
            })
        });

        if (regresponse.ok) {
            // 注册成功，可以进行重定向等操作
            ElMessage({
                showClose: true,
                message: '注册成功！',
                type: 'success',
            })
            navigateTo('/login')
        } else {
            ElMessage({
                showClose: true,
                message: '该用户已存在！',
                type: 'warning',
            })
        }
    } catch (error) {
        console.error('Error:', error);

    }
}

//实时判断用户名是否合法
const usernameError = ref('');
const uE = ref(false);
const passwordError = ref('');
const uP = ref(false);
// 定义用户名合法性规则
const isValidUsernameNumber = (username: string): boolean => {
    return username.length >= 2 && username.length <= 30;
};

const isValidPassNumber = (username: string): boolean => {
    return username.length >= 6 && username.length <= 20;
};

const isValid = (username: string): boolean => {
    const regex = /^[A-Za-z0-9]+$/;
    return regex.test(username);
};

// 实时检查用户名是否合法
const checkUsername = () => {
    if (isValidUsernameNumber(username.value)) {
        usernameError.value = '';
        uE.value = false;
    } else {
        usernameError.value = '用户名必须大于等于4个字符且小于等于10个字符';
        uE.value = true;
        ElMessage({
            showClose: true,
            message: usernameError.value,
            type: 'warning',
        })
        return;
    }
    if (isValid(username.value)) {
        usernameError.value = '';
        uE.value = false;
    } else {
        usernameError.value = '用户名只能包含(a-z,A-Z,0-9)';
        uE.value = true;
        ElMessage({
            showClose: true,
            message: usernameError.value,
            type: 'warning',
        })
        return;
    }
};

const checkPass = () => {
    if (isValidPassNumber(password.value)) {
        passwordError.value = '';
        uP.value = false;
    } else {
        passwordError.value = '密码必须大于等于6个字符且小于等于10个字符';
        uP.value = true;
        ElMessage({
            showClose: true,
            message: passwordError.value,
            type: 'warning',
        })
        return;
    }
    if (isValid(password.value)) {
        passwordError.value = '';
        uP.value = false;
    } else {
        passwordError.value = '密码只能包含(a-z,A-Z,0-9)';
        uP.value = true;
        ElMessage({
            showClose: true,
            message: passwordError.value,
            type: 'warning',
        })
        return;
    }
};

</script>

<template>
    <div class="bgc">
        <div class="sbgc">
        <div class="loginBox">
          <div class="title">Register</div>
          <form @submit.prevent="onReg">
            <div class="item">
              <input type="text" v-model="username" pattern="[a-zA-Z0-9]+" required />
              <label for="">Username</label>
            </div>
            <!-- <div class="item">
                <input type="text" v-model="email" required />
                <label for="">Email</label>
            </div> -->
            <div style="height: 25px;">

            </div>
            <div class="item">
              <input type="password" v-model="password" required />
              <label for="">Password</label>
            </div>
            <div class="item">
                <input type="password" v-model="repassword" required />
                <label for="">Confirm</label>
            </div>
            <div style="display: flex; justify-content:center;">
            <button class="btn" type="submit">Sign Up
            
              <span></span>
              <span></span>
              <span></span>
            </button>
            </div>
          </form>
        </div>
        <div class="links">
          <div>
           <a href="/" class="link">home</a>
          </div>
          <div>
           <a href="/login" class="link">sign in</a>
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
  margin-bottom: 80px;
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
  margin-bottom: 15px;
  font-family: fantasy;
  font-size:30px;
}

.item {
  height: 45px;
  border-bottom: 1px solid #070636;
  margin-bottom: 0px;
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
  margin-top: 30px;
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