<template>
    <div class="relative w-1/5" style="height: 320px">
      <img v-if="imageSrc" :src="imageSrc" alt="图片" class="absolute inset-0 w-full h-full object-cover" />
      <div v-else class="absolute inset-0 flex items-center justify-center bg-gray-100 text-gray-600 border border-dashed border-gray-300">
        等待您的结果
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  interface Props {
    imageSrc?: string;
  }
  
  const props = defineProps<Props>();
  </script>
  
  <style scoped>
  /* 你可以在这里添加额外的样式，但通常 Tailwind CSS 已经足够 */
  </style>
  