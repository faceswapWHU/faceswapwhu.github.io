<!-- components/FeedbackList.vue -->

<script setup lang="ts">
import { useFeedbackStore } from '~/composables/feedback'

const feedbackStore = useFeedbackStore()

// 假设fetchFeedbacks是异步的
await feedbackStore.fetchFeedbacks()
</script>

<template>
    <div>
        <div>反馈信息列表</div>
        <div v-for="feedback in feedbackStore.feedbacks" :key="feedback.id"
            @click="feedbackStore.setActiveFeedback(feedback)"
            class="ml-8 bg-gray-100 border-b py-2 px-4 cursor-pointer transition-colors duration-300"
            >
            {{ feedback.title }}
        </div>
    </div>
</template>
