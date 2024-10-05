<template>
    <div @click="navigateToProfile">
        <img :src="avatarSrc" alt="Profile Avatar" class="avatar">
    </div>
</template>

<script setup>
import { defineExpose } from 'vue';

const props = defineProps({
    avatarSrc: {
        type: String,
        required: true
    },
    profileUrl: {
        type: String,
        required: true
    }
});

const navigateToProfile = () => {
    navigateTo('/person')
};

defineExpose({ navigateToProfile });
</script>

<style scoped>
.avatar {
    border-radius: 50%; 
    /* 圆形头像 */
    width: 45px;
    /* 头像大小 */
    height: 45px;
    border: 2px solid #ffffff;
}

.avatar:hover {
    border-color: #e0e0e0;
    /* 鼠标悬停时边框颜色变为蓝色 */
    /* 你可以在这里添加更多悬停时的样式 */
}
</style>