<script setup>
const check = ref(false);

onMounted(() => {
  const form = document.getElementById("form");
  const result = document.getElementById("result");

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    form.classList.add("was-validated");
    if (!form.checkValidity()) {
      form.querySelectorAll(":invalid")[0].focus();
      return;
    }
    check.value = true;
    if (check.value)
      submitIssue();
  });
});

import { useApi } from '~/composables/useApi';
const { apiBaseUrl } = useApi();

import { useAuthStore } from '~/composables/auth';
const authStore = useAuthStore();

const newEmail = ref("");
const newBody = ref("");
const newCallname = ref("");
const submitIssue = async () => {
    if (!check.value) return;
    check.value = false;
    const jwt = authStore.user;
    try {
        const response = await fetch(apiBaseUrl.value + 'issues/new', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${jwt}`,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email:newEmail.value,body:newBody.value, callname:newCallname.value }),
        });
        const result = response.json();
        if (response.ok) {
            ElMessage({
                duration: 1000,
                message: '反馈已提交',
                type: 'success',
            })
            newBody.value="";
            newCallname.value="";
            newEmail.value="";
        } else {
            ElMessage.error('反馈失败o(╥﹏╥)o');
            throw new Error(result.msg);
        }
    } catch (error) {
        console.error('Login error:', error);
    }
    // check.value = false;
};

</script>

<template>
  <form
    id="form"
    class="needs-validation"
    novalidate
  >
    <input
      type="checkbox"
      class="hidden"
      style="display: none"
      name="botcheck"
    />
    <div class="mb-5">
      <input
        type="text"
        placeholder="称谓"
        v-model="newCallname"
        required
        class="w-full px-4 py-3 border-2 placeholder:text-gray-800 rounded-md outline-none
         focus:ring-4 border-gray-300 focus:border-gray-600 ring-gray-100"
        name="name"
      />
      <div class="empty-feedback invalid-feedback text-red-400 text-sm mt-1">
        请提供您的称呼
      </div>
    </div>
    <div class="mb-5">
      <label for="email_address" class="sr-only">邮箱地址</label
      ><input
        id="email_address"
        type="email"
        v-model="newEmail"
        placeholder="邮箱地址"
        name="email"
        required
        class="w-full px-4 py-3 border-2 placeholder:text-gray-800 rounded-md outline-none
         focus:ring-4 border-gray-300 focus:border-gray-600 ring-gray-100"
      />
      <div class="empty-feedback text-red-400 text-sm mt-1">
        请提供您的邮箱地址。
      </div>
      <div class="invalid-feedback text-red-400 text-sm mt-1">
        请提供有效的邮箱地址。
      </div>
    </div>
    <div class="mb-3">
      <textarea
        name="message"
        v-model="newBody"
        required
        placeholder="您的反馈信息"
        class="w-full px-4 py-3 border-2 placeholder:text-gray-800 rounded-md outline-none
         h-36 focus:ring-4 border-gray-300 focus:border-gray-600 ring-gray-100"
      ></textarea>
      <div class="empty-feedback invalid-feedback text-red-400 text-sm mt-1">
        输入您的反馈信息
      </div>
    </div>
    <LandingButton type="submit" size="lg" block >提交反馈</LandingButton>
    <div id="result" class="mt-3 text-center"></div>
  </form>
</template>

<style>
.invalid-feedback,
.empty-feedback {
  display: none;
}

.was-validated :placeholder-shown:invalid ~ .empty-feedback {
  display: block;
}

.was-validated :not(:placeholder-shown):invalid ~ .invalid-feedback {
  display: block;
}

.is-invalid,
.was-validated :invalid {
  border-color: #dc3545;
}
</style>
