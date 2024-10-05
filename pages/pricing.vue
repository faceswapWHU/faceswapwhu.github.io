<script setup lang="ts">
definePageMeta({
  layout: "landing",
});

const pricing = [
  {
    name: "按次数购买",
    price: "¥5",
    counts:100,
    popular: false,
    features: [
      "按量计费",
      "100次换脸次数",
      "包含视频换脸",
      "永久不过期",
      "包含视频换脸",
      "处理反馈通知",
    ],
    button: {
      text: "选购套餐",
      // link: "/swap",
    },
  },
  {
    name: "按次数购买",
    price: {
      monthly: "¥100",
      annual: "¥888",
      discount: "33%",
      original: "¥150",
    },
    counts:2888,
    popular: true,
    features: [
      "更优惠的方案",
      "2888次换脸次数",
      "包含视频换脸",
      "优先处理反馈",
      "更自由尝试换脸",
      "提供社区帮助",
    ],
    button: {
      text: "选购套餐",
      // link: "/swap",
    },
  },
  {
    name: "公司团购",
    price: "共同协商",
    popular: false,
    counts:0,
    features: [
      "计费更灵活",
      "次数可控",
      "包含视频换脸",
      "即时处理反馈",
      "提供换脸指导",
      "售后服务",
    ],
    button: {
      text: "联系我们",
      link: "/contact",
    },
  },
];

</script>

<template>
  <LandingContainer>
    <LandingSectionhead>
      <template v-slot:title>充值次数</template>
      <template v-slot:desc>自由选择适合您的套餐。</template>
    </LandingSectionhead>

    <div class="grid md:grid-cols-3 gap-10 mx-auto max-w-screen-lg mt-12">
      <LandingPricing v-for="item of pricing" :plan="item" />
    </div>
  </LandingContainer>
</template>
