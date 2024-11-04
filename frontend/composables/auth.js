// stores/auth.ts
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isAuthenticated: false,
    user: null,
    username: "user",
    signature: "这个人很懒，什么都没有留下",
    email: "未绑定邮箱",
    times: 10,
    avatar:"avatar.png"
  }),
  actions: {
    login(user) {
      this.isAuthenticated = true;
      this.user = user;
      localStorage.setItem('auth', JSON.stringify({ isAuthenticated: this.isAuthenticated, user:this.user }));
    },
    logout() {
      this.isAuthenticated = false;
      this.user = null;
      localStorage.removeItem('auth');
      localStorage.removeItem('authAva');
      localStorage.removeItem('authSign');
      localStorage.removeItem('authTimes');
      localStorage.removeItem('authEmail');
    },  
    updateAvatar(avatarBase64) {
      this.avatar = avatarBase64;
      this.saveAuthData();
      this.restoreState();
    },
    updateSignature(newSign){
      this.signature = newSign;
      this.saveSignData()
      this.restoreState()
    },
    updateEmail(newEmail){
      this.email = newEmail;
      this.saveEmailData()
      this.restoreState()
    },
    updateTimes(newTimes){
      this.times += newTimes;
      this.saveTimesData();
      this.restoreState();
    },
    saveTimesData(){
      const authTimes = JSON.stringify({
        times: this.times
      });
      localStorage.setItem('authTimes', authTimes);
    },
    saveEmailData(){
      const authEmail = JSON.stringify({
        email: this.email
      });
      localStorage.setItem('authEmail', authEmail);
    },
    saveSignData() {
      const authSign = JSON.stringify({
        signature: this.signature
      });
      localStorage.setItem('authSign', authSign);
    },
    saveAuthData() {
      const authAva = JSON.stringify({
        avatar: this.avatar
      });
      localStorage.setItem('authAva', authAva);
    },
    restoreState() {
      const authData = localStorage.getItem('auth');    
      const authAva = localStorage.getItem('authAva');
      const authSign = localStorage.getItem('authSign');
      const authEmail = localStorage.getItem('authEmail');
      const authTimes = localStorage.getItem('authTimes');
      if (authData) {
        const parsedData = JSON.parse(authData);
        this.isAuthenticated = parsedData.isAuthenticated;
        this.user = parsedData.user;
      }
      if (authAva){
        const pD= JSON.parse(authAva)
        this.avatar = pD.avatar;
      }
      if(authSign){
        const pS = JSON.parse(authSign)
        this.signature = pS.signature;
      }
      if(authEmail){
        const pE = JSON.parse(authEmail)
        this.email = pE.email;
      }
      if(authTimes){
        const pT = JSON.parse(authTimes)
        this.times = pT.times;
      }
    }
  }
});
