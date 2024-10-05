<script setup lang="ts">
definePageMeta({
    layout: "landing",
});
</script>

<template>
    <div class="flex gap-5">
        <div class="border p-4 ml-12">
            <landingFeedbackList />
        </div>
        <div class="flex-grow">
            <landingFeedbackDetail />
        </div>
    </div>
</template>
