<template>
    <div id="bottomImg" class="bottomImg" :style="{ height: imgHeigth, width: imgWidth, backgroundImage: 'url(' + props.bottomImg + ')' }">
      <span class="imgLabel">{{ props.bottomLabel }}</span>
      <div v-if="props.upperImg" class="upperImg" :style="{ backgroundImage: 'url(' + props.upperImg + ')', width: 100 - upperImgWidth + '%' }">
        <span class="imgLabel">{{ props.upperLabel }}</span>
      </div>
      <div v-else class="upperUndefined" :style="{ width: 100 - upperImgWidth + '%' }">
        <span class="undefinedSpan">暂无结果</span>
      </div>
      <span class="spanHandle" :style="{ left: 'calc(' + upperImgWidth + '% - 24px)' }"></span>
      <input class="inputRange" type="range" v-model="upperImgWidth" min="0" max="100" />
    </div>
  </template>
  
  <script lang="ts" setup>
  import { ref, watch, onMounted } from "vue";
  
  const imgHeigth = ref("320px"); // 固定高度
  const imgWidth = ref("220px"); // 固定宽度
  const upperImgWidth = ref(20);
  
  const props = defineProps({
    bottomImg: {
      type: String,
      default: "",
    },
    upperImg: {
      type: String,
      default: "",
    },

  });
  
  // 跟踪底层图片的变化，因为底层图片是基础
  watch(
    () => props.bottomImg,
    () => {
      upperImgWidth.value = 20;
    }
  );
  
  // 首次加载时初始化
  onMounted(() => {
    upperImgWidth.value = 20;
  });
  </script>
  
  <style>
  .bottomImg {
    position: relative;
    overflow: hidden;
    width: 300px; /* 固定宽度 */
    height: 300px; /* 固定高度 */
    background-size: cover; /* 保持图片比例并填充 */
    background-position: center; /* 图片居中 */
  }
  
  .upperImg {
    position: absolute;
    top: 0;
    right: 0;
    height: 100%;
    z-index: 1;
    background-size: cover; /* 保持图片比例并填充 */
    background-position: right top;
    border-left: 2px solid rgb(255, 255, 255, 0.5);
  }
  
  .imgLabel {
    font-size: 20px;
    color: aliceblue;
    text-shadow: 1px 1px #533d4a, 2px 2px #533d4a;
    position: absolute;
    bottom: 10px;
    left: 10px;
  }
  
  .upperUndefined {
    position: absolute;
    top: 0;
    right: 0;
    height: 100%;
    z-index: 1;
    font-size: 60px;
    background-color: rgb(255, 255, 255, 0.8);
    background-position: right top;
    border-left: 2px solid rgb(255, 255, 255, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #999;
    overflow: hidden;
  }
  
  .undefinedSpan {
    display: flex;
    width: 100%;
    height: 100%;
    align-items: center;
    justify-content: center;
    color: #999;
    overflow: hidden;
  }
  
  .inputRange {
    position: absolute;
    height: 100%;
    z-index: 3;
    left: -4px;
    touch-action: auto;
    width: calc(100% + 4px);
    opacity: 0;
  }
  
  .spanHandle {
    position: absolute;
    z-index: 2;
    height: 48px;
    width: 48px;
    border: 1px solid #000;
    border-radius: 50%;
    top: calc(50% - 24px); /* 垂直居中 */
    background-color: rgb(255, 255, 255, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .spanHandle:before,
  .spanHandle:after {
    border-left: 2px solid;
    border-top: 2px solid;
    content: "";
    height: 10px;
    position: absolute;
    top: 50%;
    transform-origin: 0 0;
    width: 10px;
  }
  
  .spanHandle:before {
    left: 5px;
    transform: rotate(-45deg);
  }
  
  .spanHandle:after {
    right: -5px;
    transform: rotate(135deg);
  }
  </style>