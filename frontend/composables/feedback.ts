// stores/feedback.ts

import { defineStore } from 'pinia'

// 定义 Feedback 类型
interface Feedback {
    id: number;
    title: string;
    content: string;
    // 可以根据需要添加更多属性
  }

export const useFeedbackStore = defineStore('feedback', {
  state: () => ({
    feedbacks: [] as Feedback[],
    activeFeedback: null as Feedback | null
  }),
  actions: {
    async fetchFeedbacks() {
      // 这里是获取反馈信息的逻辑
    //   try {
    //     const response = await fetch('/api/feedbacks');
    //     if (!response.ok) {
    //       throw new Error('Failed to fetch feedbacks');
    //     }
    //     const data = await response.json();
    //     this.feedbacks = data; // 假设返回的数据格式就是 Feedback[] 类型
    //   } catch (error) {
    //     console.error('Error fetching feedbacks:', error);
    //     // 这里可以处理错误，例如显示通知用户
    //   }
          // 模拟从后端获取数据
          const mockFeedbacks: Feedback[] = [
            { id: 1, title: '反馈标题1', content: '这是第一条反馈内容' },
            { id: 2, title: '反馈标题2', content: '这是第二条反馈内容' },
            { id: 3, title: '反馈标题3', content: '这是第三条反馈内容' },
            // 可以继续添加更多模拟反馈数据
          ];
          // 延迟一段时间以模拟网络请求的异步行为
          await new Promise(resolve => setTimeout(resolve, 1000));
          this.feedbacks = mockFeedbacks;
    },
    setActiveFeedback(feedback: Feedback) {
      this.activeFeedback = feedback
    }
  }
})
