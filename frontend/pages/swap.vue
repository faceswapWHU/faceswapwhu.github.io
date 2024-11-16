<script setup lang="ts">
import { ref } from 'vue';
import type { ButtonInstance, ElDivider } from 'element-plus'
import { Right, Plus } from '@element-plus/icons-vue'
import { useApi } from '~/composables/useApi';
const { apiBaseUrl } = useApi();
import { useAuthStore } from '~/composables/auth';

import TwoImgCompare from "@/components/landing/integrate.vue";
const bottomImg = ref(new URL("@/assets/img/eg_old.jpg", import.meta.url).href); // 底图
const upperImg = ref(new URL("@/assets/img/eg_new.jpg", import.meta.url).href); // 上层图

const authStore = useAuthStore();

const Ref1 = ref<HTMLElement>()
const Ref2 = ref<HTMLElement>()
const Ref3 = ref<ButtonInstance>()
const open = ref(false)
const Ref4 = ref<HTMLElement>()
const Ref5 = ref<HTMLElement>()
const Ref6 = ref<ButtonInstance>()
const Ref7 = ref<ButtonInstance>()
const open1 = ref(false);
const upVideo = ref(true);

const image1 = ref("");
const image2 = ref("");
const resultImage = ref("");

const isFaceSwapped = ref(true); // 新增的状态变量

const images = ref([
    { src: 'p1.png', alt: 'Image 1' },
    { src: 'p2.png', alt: 'Image 2' },
    { src: 'p3.png', alt: 'Image 3' },
    { src: 'p4.png', alt: 'Image 4' },
]);

definePageMeta({
    layout: "landing",
});

function setImageBase64(imageSrc: any) {
    // 使用 require 来引入静态资源
    const image = new Image();
    image.src = imageSrc;
    image.onload = () => {
        const canvas = document.createElement('canvas');
        canvas.width = image.width;
        canvas.height = image.height;
        const ctx = canvas.getContext('2d')!;
        ctx.drawImage(image, 0, 0);
        image2.value = canvas.toDataURL('image/png');
    };
}
function setImage3Base64(imageSrc: any) {
    // 使用 require 来引入静态资源
    const image = new Image();
    image.src = imageSrc;
    image.onload = () => {
        const canvas = document.createElement('canvas');
        canvas.width = image.width;
        canvas.height = image.height;
        const ctx = canvas.getContext('2d')!;
        ctx.drawImage(image, 0, 0);
        image3.value = canvas.toDataURL('image/png');
    };
}
function onImageUpload(event: any, imageNumber: any) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (e) => {
        if (imageNumber === 1) {
            image1.value = e.target!.result! as string;
        } else {
            image2.value = e.target!.result! as string;
        }
    };
    reader.readAsDataURL(file);
}

function selectImage(imageNumber: Number) {
    const fileInput = imageNumber == 1 ?
        document.querySelector<HTMLElement>('.image-upload-block:nth-child(1) .upload-button')
        : document.querySelector<HTMLElement>('.image-upload-block:nth-child(3) .upload-button');
    if (fileInput) {
        fileInput.click();
    }
}

function onImageUpload2(event: any) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (e) => {
        image3.value = e.target!.result! as string;
    };
    reader.readAsDataURL(file);
}

function selectImage2() {
    const fileInput = document.querySelector<HTMLElement>('.video-upload:nth-child(3) .upload-button')
    if (fileInput) {
        fileInput.click();
    }
}

async function startFaceSwap() {
    const requestData = {
        src: image2.value,
        tar: image1.value
    };

    ElMessage({
        message: '开始换脸！',
        type: 'success',
    })

    const jwt = authStore.user;
    try {
        const response = await fetch(apiBaseUrl.value + 'face/gen_img', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${jwt}`,
            },
            body: JSON.stringify(requestData)
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        if (!data.image) {
            ElMessage({
                message: '源图片未识别到人脸！',
                type: 'warning',
            })
        } else {
            resultImage.value = data.image;
            // isFaceSwapped.value = false; // 换脸成功后设置为 true
        }
    } catch (error) {
        console.error('Failed to start face swap:', error);
    }
}

function shareResult() {
    // 这里添加分享逻辑
}

function downloadResult() {
    const link = document.createElement('a');
    link.href = resultImage.value;
    if (link.href != "") {
        link.download = 'face-swapped-image.png';
        link.click();
        link.remove();
    } else {
        console.log("没有图片！")
    }

}

function downloadResultVideo() {
    const jwt = authStore.user;
    const url = apiBaseUrl.value + 'face/download_video'; // Flask 后端的下载路由  

    fetch(url, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${jwt}`, // 确保你的 Flask 后端期望这样的 JWT 格式  
            'Content-Type': 'application/json' // 通常对于 GET 请求这不是必需的，但根据后端配置可能有所不同  
        },
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            // 读取响应体为 Blob  
            return response.blob();
        })
        .then(blob => {
            // 创建一个指向 blob 的 URL  
            const url = window.URL.createObjectURL(blob);
            // 创建一个 a 标签来触发下载  
            const a = document.createElement('a');
            a.href = url;
            // 你可以根据需要设置文件名  
            a.download = 'video.mp4'; // 或者从响应头中获取文件名  
            // 触发下载  
            document.body.appendChild(a);
            a.click();
            // 清理  
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);
        })
        .catch(error => {
            console.error('Error downloading video:', error);
        });
}

const image3 = ref<string>('');
const swapWhat = ref(false);//false时为图片换脸
const hero1 = ref("上传图片然后点击转换吧!")
const hero2 = ref("上传视频然后点击转换吧!")

const selectedFile = ref(null);

function selectVideo() {
    upVideo.value = true;
    console.log("点击了")
    const fileInput = document.querySelector<HTMLElement>('.video-upload:nth-child(1) .upload-button')
    console.log(fileInput);
    if (fileInput) {
        fileInput.click();
    }
}

function handleFileChange(event: any) {
    console.log("上传了？")
    selectedFile.value = event.target.files[0];
}

async function uploadVideo() {
    upVideo.value = false;
    if (!selectedFile.value) {
        ElMessage({
            message: '请先选择选择一个视频',
            type: 'warning',
        })
        return;
    }
    const formData = new FormData();
    formData.append('video', selectedFile.value);
    const jwt = authStore.user;
    console.log(jwt)
    try {
        const response = await fetch(apiBaseUrl.value + 'face/upload_video', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${jwt}`,
            },
            body: formData,
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error('Error uploading file:', error);
    }
}

function goToResult() {
    navigateTo("/result");
}

async function uploadImage3() {
    console.log("开始上传图片3");
    const requestData = {
        tar: image3.value
    };

    ElMessage({
        message: '开始换脸！',
        type: 'success',
    })

    const jwt = authStore.user;
    try {
        const response = await fetch(apiBaseUrl.value + 'face/gen_video', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${jwt}`,
            },
            body: JSON.stringify(requestData)
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        // resultImage.value = data.image;
        if (!data.video){
            ElMessage({
                message: '源图片未识别到人脸！',
                type: 'warning',
            })
        }else{
            upVideo.value = true;
        }
        
    } catch (error) {
        console.error('Failed to upload Image3', error);
    }
}
</script>
<template>
    <LandingContainer>
        <div class='bgc'>
        <LandingSectionhead>
            <template v-slot:title>尝试换脸</template>
            <template v-slot:desc>{{ swapWhat ? hero2 : hero1 }} </template>
        </LandingSectionhead>
        <div class="content-center w-full" style="text-align: center;">
            <el-switch v-model="swapWhat" class="ml-2"
                style="--el-switch-on-color: #000000; --el-switch-off-color: #babab1; " width="80px" size="large" />
        </div>

        <div v-if="swapWhat">

            <div class="button-container">
                <el-button @click="open1 = true" class="start-button">
                    怎么开始？
                </el-button>
            </div>
            
            <el-tour v-model="open1">
                <el-tour-step title="选择视频" description="点击此处选择或更改视频" placement="left" :target="Ref4" />
                <el-tour-step title="上传视频" description="点击按钮上传视频！" placement="top" :target="Ref7?.$el" />
                <el-tour-step title="上传图片" description="点击此处上传或更改图片" placement="right" :target="Ref5" />
                <el-tour-step title="开始转换" description="点击按钮开始转换！" placement="top" :target="Ref6?.$el" />
            </el-tour>

            <!-- 这里是上传视频 -->
            <div class="flex gap-20 items-center mt-8 ml-12">
                <div class="video-upload flex flex-col items-center w-1/5 hover:scale-110" ref="Ref4">
                    <div class="image-preview" :class="{ 'empty-preview': !selectedFile }" @click="selectVideo()">
                        <img v-if="selectedFile" class="object-contain p-4" src="/right1.png" alt="Image 1" />
                    </div>
                    <input type="file" @change="handleFileChange" accept="video/mp4" class="upload-button" />
                    <text class="my-2">视频</text>
                </div>
                <el-icon style="font-size: 50px;">
                    <Plus />
                </el-icon>
                <!-- 视频上传展示块 2 -->
                <div class="video-upload flex flex-col items-center w-1/5 hover:scale-110" ref="Ref5">
                    <div class="image-preview" :class="{ 'empty-preview': !image3 }" @click="selectImage2()">
                        <img v-if="image3" :src="image3" alt="Image 3" />
                    </div>
                    <input type="file" @change="onImageUpload2($event)" accept="image/*" class="upload-button" />
                    <text class="my-2">换脸目标图片</text>
                </div>
                <!-- 开始转换按钮 -->
                <div class="button-container flex flex-col gap-2 items-left">
                    <div>
                        <el-tooltip class="box-item" effect="dark" :content="selectedFile ? '点击上传！' : '请先添加视频'"
                            placement="top">
                            <el-button @click="uploadVideo" :disabled="!selectedFile"
                                class="start-button hover:scale-110" size="large" ref="Ref7">上传视频</el-button>
                        </el-tooltip>
                    </div>
                    <el-popover :width="300"
                        popper-style="box-shadow: rgb(14 18 22 / 35%) 0px 10px 38px -10px, rgb(14 18 22 / 20%) 0px 10px 20px -15px; padding: 20px;">
                        <template #reference>
                            <el-button class="start-button hover:scale-110" size="large">选择模板</el-button>
                        </template>
                        <template #default>
                            <div class="demo-rich-conent"
                                style="display: flex; flex-wrap: wrap; gap: 16px; justify-content: center;">
                                <img v-for="(image, index) in images" :key="index" :src="image.src" :alt="image.alt"
                                    class="popover-image"
                                    style="width: 100px; height: auto; margin-bottom: 8px; cursor: pointer;"
                                    @click=setImage3Base64(image.src) />
                            </div>
                        </template>
                    </el-popover>
                    <div>
                        <el-tooltip class="box-item" effect="dark"
                            :content="selectedFile && image3 ? '点击换脸！' : '请先上传视频和照片'" placement="bottom">
                            <el-button @click="uploadImage3" :disabled="!selectedFile || !image3 || upVideo"
                                class="start-button hover:scale-110" size="large" ref="Ref6">开始换脸</el-button>
                        </el-tooltip>
                    </div>
                </div>


                <div class="flex flex-col w-8">
                    <div class="action-buttons">
                        <button @click="shareResult" class="border-2 rounded-lg mb-4">分享</button>
                        <button @click="downloadResultVideo" class="border-2 rounded-lg">下载</button>
                    </div>
                </div>
            </div>
        </div>
        <div v-else>
            <div class="button-container">
                <el-button @click="open = true" class="start-button">
                    怎么开始？
                </el-button>
            </div>
            <el-tour v-model="open">
                <el-tour-step title="上传源图片" description="点击此处上传或更改源图片(源图片是需要被替换面部的图片)" placement="left"
                    :target="Ref1" />
                <el-tour-step title="上传目的图片" description="点击此处上传或更改目的图片（目的图片是提供面部的图片）" placement="right"
                    :target="Ref2" />
                <el-tour-step title="开始转换" description="点击按钮开始转换！" placement="top" :target="Ref3?.$el" />
            </el-tour>

            <!-- 图片上传展示块容器 -->
            <div class="flex gap-20 items-center mt-8 ml-12">
                <!-- 图片上传展示块 1 -->
                <div class="image-upload-block w-1/5 hover:scale-110" ref="Ref1">
                    <div class="image-preview" :class="{ 'empty-preview': !image1 }" @click="selectImage(1)">
                        <img v-if="image1" :src="image1" alt="Image 1" />
                    </div>
                    <input type="file" @change="onImageUpload($event, 1)" accept="image/*" class="upload-button" />
                </div>
                <el-icon style="font-size: 50px;">
                    <Plus />
                </el-icon>
                <!-- 图片上传展示块 2 -->
                <div class="image-upload-block w-1/5 hover:scale-110" ref="Ref2">
                    <div class="image-preview" :class="{ 'empty-preview': !image2 }" @click="selectImage(2)">
                        <img v-if="image2" :src="image2" alt="Image 2" />
                    </div>
                    <input type="file" @change="onImageUpload($event, 2)" accept="image/*" class="upload-button" />
                </div>
                <el-icon style="font-size: 50px;">
                    <Right />
                </el-icon>
                <!-- <landingImagePlaceHolder :imageSrc="resultImage" /> -->
                 <div v-if ="!image2 ">
                    <TwoImgCompare :bottom-img="bottomImg" bottom-label="原图" :upper-img="upperImg" upper-label="结果图"></TwoImgCompare>
                </div>
                <div v-else>
                    <TwoImgCompare :bottom-img="image2" bottom-label="原图" :upper-img="resultImage" upper-label="结果图"></TwoImgCompare>
                </div>
                <!-- <landingImagePlaceHolder v-else :imageSrc="resultImage" /> -->
                    <div class="flex flex-col w-8">
                    <div class="action-buttons">
                        <button @click="shareResult" class="border-2 rounded-lg mb-4">分享</button>
                        <button @click="downloadResult" class="border-2 rounded-lg">下载</button>
                    </div>
                </div>

            </div>

            <!-- 开始转换按钮 -->
            <div class="button-container">
                <el-tooltip class="box-item" effect="dark" :content="image1 && image2 ? '点击换脸！' : '请先上传两张照片'"
                    placement="bottom">
                    <el-button @click="startFaceSwap" :disabled="!image1 || !image2"
                        class="start-button hover:scale-110" size="large" ref="Ref3">开始换脸</el-button>
                </el-tooltip>

                <el-popover :width="300"
                    popper-style="box-shadow: rgb(14 18 22 / 35%) 0px 10px 38px -10px, rgb(14 18 22 / 20%) 0px 10px 20px -15px; padding: 20px;">
                    <template #reference>
                        <el-button class="start-button hover:scale-110" size="large">选择模板</el-button>
                    </template>
                    <template #default>
                        <div class="demo-rich-conent"
                            style="display: flex; flex-wrap: wrap; gap: 16px; justify-content: center;">
                            <img v-for="(image, index) in images" :key="index" :src="image.src" :alt="image.alt"
                                class="popover-image"
                                style="width: 100px; height: auto; margin-bottom: 8px; cursor: pointer;"
                                @click=setImageBase64(image.src) />
                        </div>
                    </template>
                </el-popover>

            </div>
        </div>
        </div>
    </LandingContainer>
</template>

<style>

.bgc{
    height: 100%;
    width: 100%;
    background-color: #ffffff;

    border-radius: 10px;
    box-shadow: 0px 1px 5px 0px rgba(0, 0, 0, 0.5);
    padding: 10px;
}

.gradient-button {
    padding: 10px 20px;
    font-size: 1.2rem;
    border: none;
    color: white;
    cursor: pointer;
    background-image: linear-gradient(to right, #ffff00, #0000ff);
    transition: background-image 0.3s ease-in-out;
}

.start-button {
    padding: 10px 20px;
    margin-top: 30px;
    color: #0b1624;
    position: relative;
    overflow: hidden;
    text-transform: uppercase;
    letter-spacing: 2px;
}
  .start-button:hover {
    border-radius: 5px;
    color: #fff;
    background: #070636;
    box-shadow: 0 0 5px 0 #070636,
                0 0 25px 0 #070636,
                0 0 25px 0 #070636,
                0 0 25px 0 #070636;
    transition: all 0.5s linear;
  }

  
.gradient-button:hover {
    background-image: linear-gradient(to right, #ffcc00, #0066ff);
    /* 鼠标悬停时渐变颜色变化 */
}

.image-upload-block {
    position: relative;
}

.video-upload {
    position: relative;
}

.image-preview {
    width: 100%;
    height: 320px;
    /* 固定高度 */
    background-color: #ffffff;
    /* 灰色底面 */
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    border: 1px solid #ccc;
    cursor: pointer;

        
    border-radius: 10px;
    box-shadow: 0px 1px 5px 0px rgba(0, 0, 0, 0.5);
}

.image-preview img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.empty-preview:before {
    content: '点击上传';
    color: #888;
    font-size: 1rem;
    text-align: center;
}

.upload-button {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 50px;
    opacity: 0;
    cursor: pointer;
}

.button-container {
    text-align: center;
    margin-top: 20px;
}

.start-button:disabled {
    background-image: linear-gradient(to right, #ccc 0%, #ddd 0%, #eee 21%, #f9f9f9 52%, #e9e9e9 78%, #d9d9d9 100%);
    /* 禁用时的渐变色背景 */
    color: #888;
    /* 禁用时按钮文字颜色 */
    cursor: not-allowed;
    /* 禁用时鼠标悬停不显示指针样式 */
}
</style>