<script setup lang="ts">
import { ref } from 'vue';
import { useApi } from '~/composables/useApi';
const { apiBaseUrl } = useApi();
import { useAuthStore } from '~/composables/auth';
const authStore = useAuthStore();
import type { ButtonInstance, ElDivider } from 'element-plus'

definePageMeta({
    layout: "landing",
});


interface Item {
    id: number;
    title: string;
    description: string;
}

const items = ref<Item[]>([
    {
        id: 1,
        title: 'Card Title 1',
        description: 'This is a description for card 1.',
    },
    {
        id: 2,
        title: 'Card Title 2',
        description: 'This is a description for card 2.',
    }, {
        id: 3,
        title: 'Card Title 3',
        description: 'This is a description for card 3.',
    },
    {
        id: 1,
        title: 'Card Title 1',
        description: 'This is a description for card 1.',
    },
    {
        id: 2,
        title: 'Card Title 2',
        description: 'This is a description for card 2.',
    }, {
        id: 3,
        title: 'Card Title 3',
        description: 'This is a description for card 3.',
    },
]);
</script>

<template>
    <LandingContainer>
        <LandingSectionhead>
            <template v-slot:title>查看结果</template>
            <template v-slot:desc>在这里可以查看/下载您已完成的换脸结果 </template>
        </LandingSectionhead>
        <div class="container mt-8">
            <div class="card-list">
                <div v-for="item in items" :key="item.id" class="card">
                    <!-- <img :src="item.image" :alt="item.title" class="card-image"> -->
                    <div class="card-content">
                        <h3>{{ item.title }}</h3>
                        <p>{{ item.description }}</p>
                    </div>
                </div>
            </div>
        </div>
        <el-divider />
    </LandingContainer>
</template>


<style scoped>
.container {
    height: 90%;
    /* Full height of the viewport */
}

.card-list {
    height: 20%;
    /* 1/5 of the viewport height */
    overflow-y: auto;
    /* Enable scrolling if the content overflows */
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;

}

.card {
    flex: 0 0 calc(50% - 10px);
    flex-direction: column;
    display: flex;
    margin-bottom: 16px;
    border: 1px solid #ccc;
    border-radius: 8px;
    overflow: hidden;
}

.card-image {
    width: 100px;
    /* Fixed width for the image */
    height: auto;
}

.card-content {
    padding: 16px;
}

.card-content h3 {
    margin: 0;
    font-size: 1.2rem;
}

.card-content p {
    margin: 8px 0 0 0;
}
</style>