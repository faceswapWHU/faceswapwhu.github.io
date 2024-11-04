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
    const response = await fetch(apiBaseUrl.value + 'api/auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ usernameOrEmail: username.value, password: password.value }),
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
  <div class="min-h-screen flex items-center justify-center bg-gray-50">
    <div class="max-w-md w-full space-y-8 border border-gray-300 p-4">
      <div class="flex items-center justify-between">
          <div class="text-sm">
            <a href="/" class="font-medium text-indigo-600 hover:text-indigo-500">
              返回主页
            </a>
          </div>
        </div>
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          登录
        </h2>
      </div>
      <form class="mt-8 space-y-6" @submit.prevent="login">
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="username" class="sr-only">用户名</label>
            <input id="username" name="username" type="text" v-model="username" autocomplete="username" required
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="用户名" />
          </div>
          <div>
            <label for="password" class="sr-only">密码</label>
            <input id="password" name="password" type="password" v-model="password" autocomplete="current-password"
              required
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="密码" />
          </div>
        </div>

        <div class="flex items-center justify-between">
          <div class="text-sm">
            <a href="/forgetPassword" class="font-medium text-indigo-600 hover:text-indigo-500">
              忘记密码？
            </a>
          </div>
        </div>

        <div class="mt-6 flex justify-between">
          <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent
             text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 
             focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            以二
          </button>
          <LandingLink href="/register" size="md" class="group relative w-full flex justify-center py-2 px-4 border border-transparent 
            text-sm font-medium rounded-md text-white bg-gray-600 hover:bg-gray-700 focus:outline-none 
            focus:ring-2 focus:ring-offset-2 focus:ring-gray-500">
            注册</LandingLink>
        </div>
      </form>
    </div>
  </div>
</template>