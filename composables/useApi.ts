// composables/useApi.ts
import {ref} from 'vue';
export const useApi = () => {
  const apiBaseUrl = ref("http://127.0.0.1:5000/");

  return {
    apiBaseUrl
  }
}