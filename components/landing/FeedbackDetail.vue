<!-- components/FeedbackDetail.vue -->

<script setup lang="ts">
import { useFeedbackStore } from '~/composables/feedback'

const feedbackStore = useFeedbackStore()

const activeFeedback = computed(() => feedbackStore.activeFeedback)
</script>

<template>
  <div v-if="activeFeedback">
    <h1 class="text-2xl font-bold bg-gray-200 p-4 w-60">{{ activeFeedback.title }}</h1>
    <p class="border p-4 w-3/4">{{ activeFeedback.content }}</p>
    <!-- 这里可以添加更多反馈详情相关的UI -->
  </div>
</template>
