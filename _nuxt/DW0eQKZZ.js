import{_ as M}from"./Cvpy_CI0.js";import{u as $}from"./Cw83A_A0.js";import{E as l}from"./QBwLtVxC.js";import{g as O,m as c,p as R,o as n,c as k,t as C,q as B,v as D,M as Z,_ as z,N as F,e as b,w as v,b as _,d as S,a as t,i as d,k as N,K as q}from"./hp5d10Ce.js";import{u as L}from"./DywMN9It.js";import{E as K,a as P,b as V}from"./RkIcayXh.js";import{E as G}from"./Bhw61WhV.js";import{_ as H}from"./t-qc3aWD.js";const Q=O({__name:"EditableText",setup(U){const{apiBaseUrl:y}=$(),o=L(),i=c(!1),a=c("这个人很懒，什么都没有留下"),w=c(null);R(()=>{o.signature!==null?a.value=o.signature:o.updateSignature(a.value)});function T(){i.value=!0,Z(()=>{w.value&&w.value.focus()})}async function p(){i.value=!1,o.updateSignature(a);const E=o.user;try{const s=await fetch(y.value+"user/setSig",{method:"POST",headers:{"Content-Type":"application/json",Authorization:`Bearer ${E}`},body:JSON.stringify({signature:o.signature})}),x=await s.json();if(s.ok)l({duration:1e3,message:"修改签名成功！",type:"success"});else throw l.error("修改失败"),new Error(x.msg)}catch(s){console.error("error:",s)}}return(E,s)=>(n(),k("div",null,[i.value?B((n(),k("textarea",{key:1,"onUpdate:modelValue":s[0]||(s[0]=x=>a.value=x),onBlur:p,ref_key:"inputRef",ref:w,rows:"5",class:"editable-textarea"},null,544)),[[D,a.value]]):(n(),k("div",{key:0,onClick:T,class:"editable-text"},C(a.value),1))]))}}),W=z(Q,[["__scopeId","data-v-40ffb4c8"]]),X={class:"flex gap-10 mx-auto max-w-6xl mt-16 w-full min-h-96"},Y={class:"flex flex-col w-1/4 items-center border-2 border-[#D8DEE9] rounded-lg"},ee={class:"flex flex-col items-center my-2"},te={class:"w-32 h-32 rounded-full border-2 cursor-pointer"},oe=["src"],se={class:"text-xl font-bold mt-2"},ae={class:"flex flex-col w-3/4 items-left border-2 border-[#D8DEE9] rounded-lg"},re={class:"mt-5 ml-5"},ne={class:"flex items-center gap-10 mb-2"},le={class:"text-lg"},ie={key:0},ue={class:"flex items-center gap-10 mt-5"},de={class:"text-lg"},ce={class:"flex items-center gap-10 mb-2"},pe={key:1},me=O({__name:"person",setup(U){const{apiBaseUrl:y}=$(),o=L(),i=c(!1),a=c(!1),w=()=>{q("/pricing")},T=async m=>{if(!/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/.test(m))return l.error("邮箱格式不正确"),!1},p=c(""),E=async()=>{if(console.log("invoke the mod email func"),!await T(p.value))return;const e=o.user;try{const r=await fetch(y.value+"user/setEmail",{method:"POST",headers:{Authorization:`Bearer ${e}`,"Content-Type":"application/json"},body:JSON.stringify({email:p.value})}),u=await r.json();if(console.log(u),r.ok)o.updateEmail(p.value),l({duration:1e3,message:"邮箱已修改",type:"success"});else throw l.error("邮箱已绑定其他账户"),new Error(u.msg)}catch(r){console.error("Login error:",r)}},s=c(""),x=async()=>{if(s.value==null)return;const m=o.user;try{const e=await fetch(y.value+"user/setPassword",{method:"POST",headers:{Authorization:`Bearer ${m}`,"Content-Type":"application/json"},body:JSON.stringify({password:s.value})}),r=await e.json();if(e.ok)l({duration:1e3,message:"密码已修改",type:"success"}),s.value="";else throw l.error("密码修改失败"),new Error(r.msg)}catch(e){console.error("Login error:",e)}},A=c(null),I=()=>{A.value&&A.value.click()},J=async m=>{const e=m.target;if(e.files&&e.files[0]){const r=e.files[0],u=new FileReader;u.onloadend=async()=>{const g=u.result;o.updateAvatar(g);const j=o.user;try{const h=await fetch(y.value+"user/setAvatar",{method:"POST",headers:{Authorization:`Bearer ${j}`,"Content-Type":"application/json"},body:JSON.stringify({avatar:o.avatar})}),f=await h.json();if(h.ok)l({duration:1e3,message:"头像已修改",type:"success"});else throw l.error("出现异常"),new Error(f.msg)}catch(h){console.error("Login error:",h)}},u.readAsDataURL(r)}};return R(()=>{o.restoreState()}),F(()=>{o.restoreState()}),(m,e)=>{const r=M,u=W,g=K,j=G,h=H;return n(),b(h,null,{default:v(()=>[_(r,null,{title:v(()=>e[4]||(e[4]=[S("个人中心")])),desc:v(()=>e[5]||(e[5]=[S("查看和修改你的个人信息。")])),_:1}),t("div",X,[t("div",Y,[t("div",ee,[t("div",te,[t("input",{type:"file",ref_key:"fileInputRef",ref:A,class:"rounded-full hidden",onChange:J},null,544),t("img",{class:"rounded-full hover:scale-110",src:d(o).avatar,alt:"用户头像",onClick:I},null,8,oe)]),t("div",se,C(d(o).username),1)]),_(u,{class:"h-8 mb-20"}),e[6]||(e[6]=t("div",null,null,-1))]),t("div",ae,[t("div",re,[t("div",ne,[t("p",le,"邮箱: "+C(d(o).email),1),t("button",{class:"border-2 rounded-xl hover:bg-cyan-100 hover:shadow-lg",onClick:e[0]||(e[0]=f=>i.value=!i.value)},[e[7]||(e[7]=S("更换邮箱 ")),i.value?(n(),b(g,{key:0},{default:v(()=>[_(d(P))]),_:1})):(n(),b(g,{key:1},{default:v(()=>[_(d(V))]),_:1}))])]),i.value?(n(),k("div",ie,[B(t("input",{class:"border-2 w-60 h-12 rounded-2xl p-2 mr-4","onUpdate:modelValue":e[1]||(e[1]=f=>p.value=f),placeholder:"请输入新的邮箱"},null,512),[[D,p.value]]),t("button",{class:"border-2 rounded-xl",onClick:E},"确定")])):N("",!0),t("div",ue,[t("p",de,"剩余使用次数: "+C(d(o).times),1),t("button",{class:"border-2 rounded-xl hover:bg-cyan-100 hover:shadow-lg",onClick:w},"去充值")]),_(j),t("div",ce,[e[9]||(e[9]=t("p",{class:"text-lg"},"密码:●●●●●●●●",-1)),t("button",{class:"border-2 rounded-xl hover:bg-cyan-100 hover:shadow-lg",onClick:e[2]||(e[2]=f=>a.value=!a.value)},[e[8]||(e[8]=S("修改密码 ")),a.value?(n(),b(g,{key:0},{default:v(()=>[_(d(P))]),_:1})):(n(),b(g,{key:1},{default:v(()=>[_(d(V))]),_:1}))])]),a.value?(n(),k("div",pe,[B(t("input",{"onUpdate:modelValue":e[3]||(e[3]=f=>s.value=f),class:"border-2 w-60 h-12 rounded-2xl p-2 mr-4",placeholder:"请输入新的密码"},null,512),[[D,s.value]]),t("button",{class:"border-2 rounded-xl",onClick:x},"确定")])):N("",!0)])])])]),_:1})}}}),be=z(me,[["__scopeId","data-v-e2ca3579"]]);export{be as default};
