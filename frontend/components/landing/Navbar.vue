<script setup lang="ts">
import Avatar from '~/components/landing/Avatar.vue';
import { SwitchButton } from '@element-plus/icons-vue';

import { useAuthStore } from '~/composables/auth';
const authStore = useAuthStore();

const logmenuitems = [
  {
    title: "换脸",
    path: "/swap",
  },
  {
    title: "充值",
    path: "/pricing",
  },
  {
    title: "关于",
    path: "/about",
  },
  {
    title: "反馈",
    path: "/contact",
  },
];
const notlogmenuitems = [
  {
    title: "换脸",
    path: "/login",
  },
  {
    title: "充值",
    path: "/login",
  },
  {
    title: "关于",
    path: "/login",
  },
  {
    title: "反馈",
    path: "/login",
  },
];

const open = ref(false);
const router = useRouter();


import { useApi } from '~/composables/useApi';
const { apiBaseUrl } = useApi();

const getUserInfo = async () => {
  const jwt = authStore.user;
  try {
    const response = await fetch(apiBaseUrl.value + 'auth/get_userinfo', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${jwt}`,
      },
    });
    const result = await response.json();
    if (response.ok) {

      authStore.username = result.username;
      authStore.signature = result.signature;
      if (result.email!=null){
        authStore.email = result.email;
      }    
      authStore.times = result.times;
      const base64ImageString = result.avatar;
      let dataUrl = 'data:image/png;base64,' + base64ImageString;
      const imageDataUrl = ref(dataUrl);
      authStore.avatar = dataUrl;
    }
  } catch (error) {
  }
}

onMounted(() => {
  authStore.restoreState();
  if (authStore.isAuthenticated)
    getUserInfo();
});

onUpdated(() => {
  authStore.restoreState();
  if (authStore.isAuthenticated)
    getUserInfo();
})

function goToProfile() {
  navigateTo('/person')
}
function logout() {
  authStore.logout();
  navigateTo('/');
}

const colorValue = '#c8c8c8';
</script>

<template>
  <LandingContainer>
    <header class="flex flex-col lg:flex-row justify-between items-center my-5">
      <div class="flex w-full lg:w-auto items-center justify-between">
        <a href="/" class="text-lg"><span class="font-bold text-slate-800">Face</span><span
            class="text-slate-500">swap</span>
        </a>
        <div class="block lg:hidden">
          <button @click="open = !open" class="text-gray-800">
            <svg fill="currentColor" class="w-4 h-4" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <title>Menu</title>
              <path v-show="open" fill-rule="evenodd" clip-rule="evenodd"
                d="M18.278 16.864a1 1 0 01-1.414 1.414l-4.829-4.828-4.828 4.828a1 1 0 01-1.414-1.414l4.828-4.829-4.828-4.828a1 1 0 011.414-1.414l4.829 4.828 4.828-4.828a1 1 0 111.414 1.414l-4.828 4.829 4.828 4.828z">
              </path>
              <path v-show="!open" fill-rule="evenodd"
                d="M4 5h16a1 1 0 010 2H4a1 1 0 110-2zm0 6h16a1 1 0 010 2H4a1 1 0 010-2zm0 6h16a1 1 0 010 2H4a1 1 0 010-2z">
              </path>
            </svg>
          </button>
        </div>
      </div>
      <nav class="w-full lg:w-auto mt-2 lg:flex lg:mt-0" :class="{ block: open, hidden: !open }">
        <ul class="flex flex-col lg:flex-row lg:gap-3">
          <li v-if="authStore.isAuthenticated" v-for="item of logmenuitems">
            <a :href="item.path" class="flex lg:px-3 py-2 text-gray-600 hover:text-gray-900">
              {{ item.title }}
            </a>
          </li>
          <li v-else v-for="item of notlogmenuitems">
            <a :href="item.path" class="flex lg:px-3 py-2 text-gray-600 hover:text-gray-900">
              {{ item.title }}
            </a>
          </li>
        </ul>
      </nav>
      <div>
        <template v-if="authStore.isAuthenticated">
          <!-- 登录后的状态 -->
          <div class="flex w-32 gap-4 items-center">
            <Avatar :avatarSrc="authStore.avatar" class="hover:scale-125" profileUrl="/person" />
            <button @click="logout"><el-icon :color="colorValue" class="rounded-full" style="font-size: 24px;">
                <SwitchButton />
              </el-icon></button>
          </div>
        </template>
        <template v-else class="w-32">
          <div class="hidden lg:flex items-center gap-4">
            <a href="/login">登录</a>
            <LandingLink href="/register" size="md">注册</LandingLink>
          </div>
        </template>

      </div>
    </header>
  </LandingContainer>
</template>
