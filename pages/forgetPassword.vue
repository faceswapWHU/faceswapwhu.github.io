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
    <UCard class=" w-full bg-white/75 dark:bg-white/5 backdrop-blur ">
        <div class="min-h-screen flex items-center justify-center bg-gray-50 ">
            <div class="max-w-md w-full space-y-8 border border-gray-300 p-6">
                <div class="flex items-center justify-between">
                    <div class="text-sm">
                        <a href="/login" class="font-medium text-indigo-600 hover:text-indigo-500">
                            返回登录
                        </a>
                    </div>
                </div>
                <div></div>
                <div>
                    <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
                        忘记密码
                    </h2>
                </div>
                <div class="mt-8 space-y-6">
                    <div class="rounded-md shadow-sm -space-y-px">
                        <div>
                            <label for="email" class="sr-only">邮箱</label>
                            <input id="email" name="email" type="text" v-model="email" autocomplete="email" required
                                class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300
                                 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500
                                  focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="邮箱" />
                        </div>
                        <div>
                            <!-- 这里要写一句话，是“如果有邮箱的话可以直接发送验证码登录，如果没有绑定邮箱则要联系管理员” -->
                        </div>
                        <div class="flex w-full">
                            <label for="code" class="sr-only">验证码</label>
                            <input id="code" name="code" type="text" v-model="code" autocomplete="current-password"
                                class="appearance-none rounded-none w-3/5 relative block px-3 py-2 border border-gray-300 
                                placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 
                                focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="验证码" />
                            <button class="group relative w-2/5 flex justify-center py-2 px-4 border border-transparent 
                                text-sm font-medium rounded-md text-white
                                focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                                :class="{
                                  'bg-indigo-600 hover:bg-indigo-700': !isCountingDown,
                                  'bg-indigo-300 cursor-not-allowed': isCountingDown
                                }"
                                @click="sendCode" :disabled="isCountingDown">
                                <div v-if="isCountingDown"> {{ countdown }} 秒</div>
                                <div v-else>发送验证码</div>
                            </button>
                        </div>  

                    </div>

                    <div class="mt-6 flex justify-between">
                        <button type="button" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm 
                            font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 
                            focus:ring-offset-2 focus:ring-indigo-500" @click="onReSet">
                            确定
                        </button>

                    </div>
                </div>
            </div>
        </div>
    </UCard>
</template>