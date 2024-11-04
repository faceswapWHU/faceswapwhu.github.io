// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  css: ["~/assets/css/main.css"],

  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  vite: {
    server: {
      // proxy: {
      //   '/api': {
      //     target: 'https://jsonplaceholder.typicode.com/',
      //     changeOrigin: true, // 后端配置 Cors 时设置
      //     rewrite: path => path.replace(/^\/api/, ''), // 后端接口无 api前缀时设置
      //   },
      // },
      proxy: {
        '/api': {
          target: 'http://127.0.0.1:5000', // 本地环境
          changeOrigin: true, // 后端配置 Cors 时设置
          rewrite: path => path.replace(/^\/api/, ''), // 后端接口无 api前缀时设置
        },
      },
    },
  },
  modules: ["nuxt-icon","@nuxt/ui","@element-plus/nuxt","@pinia/nuxt"],
  compatibilityDate: "2024-07-10",
});