<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useAuthStore } from '~/composables/auth';
import { useApi } from '~/composables/useApi';
const { apiBaseUrl } = useApi();
const authStore = useAuthStore();

const isEditing = ref(false);
const text = ref("这个人很懒，什么都没有留下");
const inputRef = ref<HTMLTextAreaElement | null>(null);

onMounted(() => {
  if (authStore.signature !== null) {
    text.value = authStore.signature;
  } else {
    authStore.updateSignature(text.value);
  }
});

function startEditing() {
  isEditing.value = true;
  // 在下一个tick中聚焦到输入框
  nextTick(() => {
    if (inputRef.value) {
      inputRef.value.focus();
    }
  });
}

async function stopEditing() {
  isEditing.value = false;
  authStore.updateSignature(text);
  const jwt = authStore.user;
  try {
    const response = await fetch(apiBaseUrl.value + 'user/setSig', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${jwt}`,
      },
      body: JSON.stringify({ signature: authStore.signature }),
    });
    const result = await response.json();
    if (response.ok) {
      //   store.setToken(result.access_token);
      ElMessage({
        duration: 1000,
        message: '修改签名成功！',
        type: 'success',
      });
    } else {
      ElMessage.error('修改失败');
      throw new Error(result.msg);
    }
  } catch (error) {
    console.error('error:', error);
  }
}
</script>

<template>
  <div>
    <!-- 显示文本，当点击时变为输入框 -->
    <div v-if="!isEditing" @click="startEditing" class="editable-text">
      {{ text }}
    </div>
    <!-- 输入框，用于编辑文本 -->
    <textarea v-else v-model="text" @blur="stopEditing" ref="inputRef" rows="5" class="editable-textarea" />
  </div>
</template>

<style scoped>
.editable-text,
.editable-textarea {
  width: 100%;
  /* 设置宽度为100% */
  box-sizing: border-box;
  /* 确保padding和border包含在宽度内 */
  padding: 8px;
  cursor: text;
}

.editable-text {
  border: 1px solid transparent;
}

.editable-text:hover {
  border-color: #ccc;
}

.editable-textarea {
  border: 1px solid #ccc;
  /* 设置边框样式 */
  min-height: 50px;
  /* 设置最小高度，根据需要调整 */
}
</style>