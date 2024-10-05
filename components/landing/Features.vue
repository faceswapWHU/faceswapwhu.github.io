<script setup>
const features = [
  {
    title: "简单易用",
    description:
      "FaceSwap使用非常简单，只需要上传您的照片或者视频，按照指引的流程即可一键换脸。",
    icon: "bx:bxs-briefcase",
  },
  {
    title: "效果显著",
    description:
      "换脸的效果非常显著，我们选用的是最新的换脸模型，而且保证会定期更新模型和参数，保证换脸的效果。",
    icon: "bx:bxs-window-alt",
  },
  {
    title: "隐私保障",
    description:
      "我们保证不会泄露任何您上传的图片或者视频，竭尽全力保障用户的隐私安全。 ",
    icon: "bx:bxs-data",
  },
  {
    title: "速度快",
    description:
      "我们提升了换脸的速度，在有限的运算资源下，让您无需等待长时间即可看到效果。",
    icon: "bx:bxs-bot",
  },
  {
    title: "价格合理",
    description:
      "我们提供多种不同的套餐，您可以根据自己的情况选择，每一种都是合理的价格！",
    icon: "bx:bxs-file-find",
  },
  {
    title: "支持视频换脸",
    description:
      "不仅仅支持图片换脸，我们还支持视频换脸，不断提高我们的技术水平。",
    icon: "bx:bxs-user",
  },
];
</script>

<template>
  <div class="mt-16 md:mt-0">
    <h2 class="text-4xl lg:text-5xl font-bold lg:tracking-tight">
      轻松换脸，无限创意，尽在FaceSwap
    </h2>
    <p class="text-lg mt-4 text-slate-600">
        Acquiring enlightening and innovation from the FaceSwap project,
        you can feel free to use our project to have fun! 
    </p>
  </div>

  <div class="grid sm:grid-cols-2 md:grid-cols-3 mt-16 gap-16">
    <div v-for="item of features" class="flex gap-4 items-start">
      <div class="mt-1 bg-black rounded-full p-2 w-8 h-8 shrink-0">
        <Icon class="text-white" :name="item.icon" />
      </div>
      <div>
        <h3 class="font-semibold text-lg">{{ item.title }}</h3>
        <p class="text-slate-500 mt-2 leading-relaxed">
          {{ item.description }}
        </p>
      </div>
    </div>
  </div>
</template>
