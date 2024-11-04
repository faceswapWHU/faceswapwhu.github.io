<script setup lang="ts">
definePageMeta({
  layout: "landing",
});


</script>

<template>
  <LandingContainer>
    <LandingSectionhead>
      <template v-slot:title>反馈</template>
      <template v-slot:desc>我们衷心等待您的建议</template>
    </LandingSectionhead>

    <div class="grid md:grid-cols-2 gap-10 mx-auto max-w-4xl mt-16">
      <div>
        <h2 class="font-medium text-2xl text-gray-800">
          联系FaceSwap的创建者
        </h2>
        <p class="text-lg leading-relaxed text-slate-500 mt-3">
          你有什么想告诉我们的吗？我在这里随时恭候，您可以选择联系下方的地址，也可以填写右边的表单，我们会及时回复。
        </p>
        <div class="mt-5">
          <div class="flex items-center mt-2 space-x-2 text-gray-600">
            <Icon class="text-gray-400 w-4 h-4" name="uil:map-marker" />
            <span>湖北，武汉，珞珈山职业技术学校</span>
          </div>
          <div class="flex items-center mt-2 space-x-2 text-gray-600">
            <Icon class="text-gray-400 w-4 h-4" name="uil:envelope" /><a
              href="mailto:jakobaichmayr@gmail.com"
              >1321533477@qq.com</a
            >
          </div>
        </div>
      </div>
      <div>
        <LandingContactform />
      </div>
    </div>
  </LandingContainer>
</template>
