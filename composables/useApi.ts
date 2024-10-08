// composables/useApi.ts
import {ref} from 'vue';
export const useApi = () => {
  const apiBaseUrl = ref("http://localhost:8080/");

  return {
    apiBaseUrl
  }
}