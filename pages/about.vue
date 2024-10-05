<script setup>
definePageMeta({
  layout: "landing",
});

const TeamImg1 = "/whuP1.jpg";
const TeamImg2 = "/whuP2.jpg";
const TeamImg3 = "/whuP3.jpg";

const team = [
  {
    name: "武大樱顶",
    title: "美轮美奂",
    avatar: {
      src: TeamImg1,
      width: 480,
      height: 560,
    },
  },
  {
    name: "武大牌坊",
    title: "学在武大",
    avatar: {
      src: TeamImg2,
      width: 580,
      height: 580,
    },
  },
  {
    name: "日出而作",
    title: "优雅清晨",
    avatar: {
      src: TeamImg3,
      width: 580,
      height: 580,
    },
  },
];
</script>

<template>
  <LandingContainer>
    <LandingSectionhead>
      <template v-slot:title>关于我们</template>
      <template v-slot:desc>我们是一个小小的团队</template>
    </LandingSectionhead>

    <div class="flex flex-col gap-3 mx-auto max-w-4xl mt-16">
      <h2 class="font-bold text-3xl text-gray-800">
        用FaceSwap装点世界。
      </h2>
      <p class="text-lg leading-relaxed text-slate-500">
        我们是珞珈山职业技术学校的学生，虽然有时候会让别人觉得笨笨的，
        但是我我们很努力地学习为的就是告诉别人，好的大专不比大学差！
      </p>
    </div>
    <div class="grid md:grid-cols-3 gap-10 mx-auto max-w-4xl mt-12">
      <div v-for="item of team" class="group">
        <div class="w-full aspect-square">
          <img
            :src="item.avatar.src"
            :width="item.avatar.width"
            :height="item.avatar.height"
            format="avif"
            alt="Team"
            class="w-full h-full object-cover rounded transition group-hover:-translate-y-1 group-hover:shadow-xl"
          />
        </div>

        <div class="mt-4 text-center">
          <h2 class="text-lg text-gray-800">{{ item.name }}</h2>
          <h3 class="text-sm text-slate-500">{{ item.title }}</h3>
        </div>
      </div>
    </div>
  </LandingContainer>
</template>
