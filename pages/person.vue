<script setup lang="ts">
import { User } from '@element-plus/icons-vue';
import { ref } from 'vue';
import { ArrowDown, ArrowUp } from '@element-plus/icons-vue';

import { useApi } from '~/composables/useApi';
const { apiBaseUrl } = useApi();

import { useAuthStore } from '~/composables/auth';
const authStore = useAuthStore();

const modifyEmail = ref(false);
const modifyPass = ref(false);

const goToCharge = () => {
    navigateTo("/pricing")
}

const validateEmail = async (email:string) => {
    // 正则表达式验证邮箱格式
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailRegex.test(email)) {
        ElMessage.error('邮箱格式不正确');
        return false;
    }
};

const newEmail = ref("");
const modEmail = async () => {
    const isValid = await validateEmail(newEmail.value);
    if (!isValid) {
        return;
    }
    const jwt = authStore.user;
    try {
        const response = await fetch(apiBaseUrl.value + 'user/setEmail', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${jwt}`,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email: newEmail.value }),
        });
        const result = await response.json();
        if (response.ok) {
            authStore.updateEmail(newEmail.value);
            ElMessage({
                duration: 1000,
                message: '邮箱已修改',
                type: 'success',
            })
        } else {
            ElMessage.error('邮箱已绑定其他账户');
            throw new Error(result.msg);
        }
    } catch (error) {
        console.error('Login error:', error);
    }
};

const newPass=ref("");
const modPass = async () => {
    if(newPass.value==null) return;
    const jwt = authStore.user;
    try {
        const response = await fetch(apiBaseUrl.value + 'user/setPassword', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${jwt}`,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ password: newPass.value }),
        });
        const result = await response.json();
        if (response.ok) {
            ElMessage({
                duration: 1000,
                message: '密码已修改',
                type: 'success',
            })
            newPass.value = "";
        } else {
            ElMessage.error('密码修改失败');
            throw new Error(result.msg);
        }
    } catch (error) {
        console.error('Login error:', error);
    }
}

// 设置页面元数据
definePageMeta({
    layout: "landing",
});

const fileInputRef = ref<HTMLInputElement | null>(null);
const openFilePicker = () => {
    if (fileInputRef.value) {
        fileInputRef.value.click();
    }
};
//上传新头像
const uploadAvatar = async (event: Event) => {
    const target = event.target as HTMLInputElement;
    if (target.files && target.files[0]) {
        const file = target.files[0];
        const reader = new FileReader();
        reader.onloadend = async () => {
            const base64String = reader.result as string;
            authStore.updateAvatar(base64String);
            const jwt = authStore.user;
            try {
                const response = await fetch(apiBaseUrl.value + 'user/setAvatar', {
                    method: 'POST',
                    headers: {
                        'Authorization': `Bearer ${jwt}`,
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ avatar: authStore.avatar }),
                });
                const result = await response.json();
                if (response.ok) {
                    //   store.setToken(result.access_token);
                    ElMessage({
                        duration: 1000,
                        message: '头像已修改',
                        type: 'success',
                    })
                } else {
                    ElMessage.error('出现异常');
                    throw new Error(result.msg);
                }
            } catch (error) {
                console.error('Login error:', error);
            }
        };
        reader.readAsDataURL(file);
    }
};

onMounted(() => {
    authStore.restoreState();
    // console.log("挂载前：",authStore.signature);
});
onUpdated(()=>{
    authStore.restoreState();
})
</script>

<template>
    <LandingContainer>
        <LandingSectionhead>
            <template v-slot:title>个人中心</template>
            <template v-slot:desc>查看和修改你的个人信息。</template>
        </LandingSectionhead>
        <div class="flex gap-10 mx-auto max-w-6xl  mt-16 w-full min-h-96">
            <!-- 左侧：头像和用户名，签名等信息 -->
            <div class="flex flex-col w-1/4 items-center border-2 border-[#D8DEE9] rounded-lg">
                <div class="flex flex-col items-center my-2">
                    <div class="w-32 h-32 rounded-full border-2 cursor-pointer">
                        <input type="file" ref="fileInputRef" class="rounded-full hidden" @change="uploadAvatar" />
                        <img class="rounded-full hover:scale-110" :src="authStore.avatar" alt="用户头像"
                            @click="openFilePicker" />
                    </div>
                    <div class="text-xl font-bold mt-2">
                        {{ authStore.username }}
                    </div>
                </div>
                <!-- 签名 -->
                <LandingEditableText class="h-8 mb-20" />
                <div>
                </div>
            </div>

            <!-- 右侧：邮箱信息和剩余使用次数，按钮组 -->
            <div class="flex flex-col w-3/4 items-left border-2 border-[#D8DEE9] rounded-lg">
                <!-- 邮箱信息和剩余使用次数 -->
                <div class="mt-5 ml-5">
                    <div class="flex items-center gap-10 mb-2">
                        <p class="text-lg">邮箱: {{ authStore.email }}</p>
                        <button class="border-2 rounded-xl hover:bg-cyan-100 hover:shadow-lg"
                            @click="modifyEmail = !modifyEmail">更换邮箱
                            <el-icon v-if="modifyEmail">
                                <ArrowUp />
                            </el-icon>
                            <el-icon v-else>
                                <ArrowDown />
                            </el-icon></button>
                    </div>
                    <div v-if="modifyEmail">
                        <input class="border-2 w-60 h-12 rounded-2xl p-2 mr-4" v-model="newEmail"
                            placeholder="请输入新的邮箱"></input>
                        <button class="border-2 rounded-xl" @click="modEmail">确定</button>
                    </div>

                    <div class="flex items-center gap-10 mt-5">
                        <p class="text-lg">剩余使用次数: {{ authStore.times }}</p>
                        <button class="border-2 rounded-xl hover:bg-cyan-100 hover:shadow-lg"
                            @click="goToCharge">去充值</button>
                    </div>
                    <ElDivider></ElDivider>
                    <div class="flex items-center gap-10 mb-2">
                        <p class="text-lg">密码:●●●●●●●●</p>
                        <button class="border-2 rounded-xl hover:bg-cyan-100 hover:shadow-lg"
                            @click="modifyPass = !modifyPass">修改密码
                            <el-icon v-if="modifyPass">
                                <ArrowUp />
                            </el-icon>
                            <el-icon v-else>
                                <ArrowDown />
                            </el-icon>
                        </button>

                    </div>
                    <div v-if="modifyPass">
                        <input v-model="newPass" class="border-2 w-60 h-12 rounded-2xl p-2 mr-4" placeholder="请输入新的密码"></input>
                        <button class="border-2 rounded-xl" @click="modPass">确定</button>
                    </div>

                </div>
            </div>
        </div>
    </LandingContainer>
</template>

<style scoped>
.user-profile {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
}

.username {
    margin-top: 10px;
    font-size: 20px;
}

.signature {
    margin-top: 5px;
    font-style: italic;
}

.email-usage {
    margin-top: 10px;
}

.buttons {
    display: flex;
    justify-content: space-between;
    width: 200px;
    margin-top: 20px;
}

button {
    padding: 10px 20px;
    cursor: pointer;
}
</style>