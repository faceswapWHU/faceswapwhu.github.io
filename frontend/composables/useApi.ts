// composables/useApi.ts
import {ref} from 'vue';
export const useApi = () => {
  const apiBaseUrl = ref("http://1.94.178.239:80/");

  return {
    apiBaseUrl
  }
}