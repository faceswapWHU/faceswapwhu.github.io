<script setup lang="ts">
defineProps(["plan"]);
import { ref } from 'vue'
import { ElMessage, ElMessageBox, ElLoading } from 'element-plus'
import { useApi } from '~/composables/useApi';
const { apiBaseUrl } = useApi();

import { useAuthStore } from '~/composables/auth';
const authStore = useAuthStore();

const openFullScreen2 = () => {
  const loading = ElLoading.service({
    lock: true,
    text: 'Loading',
    background: 'rgba(0, 0, 0, 0.7)',
  })
  setTimeout(() => {
    loading.close()
  }, 2000)
}

const open = (cnt: number) => {
  if (cnt == 0) return;
  ElMessageBox.confirm('确认要选择这个方案吗？', '充值', {
    // if you want to disable its autofocus
    // autofocus: false,
    confirmButtonText: '确认',
    cancelButtonText: '取消',
    type: 'info',
    beforeClose: async (action, instance, done) => {
      if (action === 'confirm') {
        instance.confirmButtonLoading = true;
        const jwt = authStore.user;
        try {
          const response = await fetch(apiBaseUrl.value + 'times/payment', {
            method: 'POST',
            headers: {
              'Authorization': `Bearer ${jwt}`,
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ times: cnt }),
          });
          const result = await response.json();
          if (response.ok) {
            authStore.updateTimes(cnt);
            ElMessage({
              duration: 1000,
              message: '充值成功',
              type: 'success',
            })
          } else {
            ElMessage.error('充值失败');
            throw new Error(result.msg);
          }
        } catch (error) {
          console.error('Login error:', error);
        }
        setTimeout(() => {
          done();
          instance.confirmButtonLoading = false;
        }, 2000);
      } else {
        done();
      }
    }
  })
    .then(() => {
      //向后端发送请求
      // ElMessage({
      //   type: 'success',
      //   message: '完成充值',
      // })
    })
    .catch(() => {
      ElMessage({
        type: 'info',
        message: '取消充值',
      })
    })
}

</script>

<template>
  <div>
    <div
      class="flex flex-col w-full order-first lg:order-none border-2 border-[#D8DEE9] border-opacity-50 py-5 px-6 rounded-md">
      <div class="text-center">
        <h4 class="text-lg font-medium text-gray-400">{{ plan.name }}</h4>
        <p class="mt-3 text-4xl font-bold text-black md:text-4xl">
          {{
            plan.price && typeof plan.price === "object"
              ? plan.price.monthly
              : plan.price
          }}
        </p>
      </div>
      <ul class="grid mt-8 text-left gap-y-4">
        <li v-for="item of plan.features" class="flex items-start gap-3 text-gray-800">
          <LandingTick className="w-6 h-6" />
          <span>{{ item }}</span>
        </li>
      </ul>
      <div class="flex mt-8">
        <LandingLink :href="plan.button.link || '#'" block :styleName="plan.popular ? 'primary' : 'outline'"
          @click="open(plan.counts)">
          {{ plan.button.text || "Get Started" }}
        </LandingLink>
      </div>
    </div>
  </div>
</template>
