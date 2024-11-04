<template>
  <main class="grid lg:grid-cols-2 place-items-center pt-16 pb-8 md:pt-8">
    <div class="p-24 md:order-1 hidden md:block">
      <img class="rounded-full transition-transform transform hover:scale-125" src="~/assets/img/hero.jpg"
        alt="Starship starts the engine" loading="eager" format="avif" width="512" height="512" />
    </div>

    <div>
      <h1 class="text-5xl lg:text-6xl xl:text-7xl font-bold lg:tracking-tight">
        基于e4s模型的换脸体验站
      </h1>
      <p class="text-lg mt-4 text-slate-600 max-w-xl">
        faceswap是一个简单易用的换脸网站，我们提供图片和视频换脸两种服务，
        您可以在这里尽情体验换脸的乐趣。你可以点击下方的按钮立刻开始体验，
        也可以查看我们的gitee仓库以了解更多相关信息。
      </p>
      <div class="mt-6 flex flex-col sm:flex-row gap-3">
        <LandingLink v-if="authStore.isAuthenticated" href="/swap" target="_blank" rel="noopener">开始体验</LandingLink>
        <LandingLink v-else href="/login" target="_blank" rel="noopener">开始体验</LandingLink>
        <LandingLink size="lg" styleName="outline" rel="noopener"
          href="https://gitee.com/kinnont/face-magic/tree/master/" target="_blank">访问仓库</LandingLink>
      </div>
    </div>
  </main>
</template>

<script setup lang="ts">

import { useAuthStore } from '~/composables/auth';

const authStore = useAuthStore();
const path = authStore.isAuthenticated ? "/swap" : "/login"
</script>