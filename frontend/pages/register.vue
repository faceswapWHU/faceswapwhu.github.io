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
                    注册
                </h2>
            </div>
            <form class="mt-8 space-y-6" @submit.prevent="onReg">
                <div class="rounded-md shadow-sm -space-y-px">
                    <div>
                        <!-- <el-tooltip :content="passwordError" placement="right" v-show="uE"> -->
                        <label for="username" class="sr-only">用户名</label>
                        <input id="username" name="username" type="text" v-model="username" autocomplete="username"
                            required pattern="[a-zA-Z0-9]+"
                            class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                            placeholder="用户名" />
                    </div>
                </div>
                <div class="rounded-md shadow-sm -space-y-px">
                    <div>
                        <!-- <el-tooltip :content="passwordError" placement="right" v-show="uP"> -->

                        <label for="password" class="sr-only">密码</label>
                        <input id="password" name="password" type="password" v-model="password"
                            autocomplete="current-password" required
                            class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                            placeholder="密码" />
                    </div>
                    <div>
                        <label for="password" class="sr-only">重复密码</label>
                        <input id="repassword" name="repassword" type="password" v-model="repassword"
                            autocomplete="current-password" required
                            class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                            placeholder="重复密码" />
                    </div>
                </div>



                <div class="mt-6 flex justify-between">
                    <button type="submit"
                        class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                        注册
                    </button>

                </div>
            </form>
        </div>
    </div>
</template>