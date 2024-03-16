<template>
  <h1>Logged out</h1>
  
</template>

<script setup>
import { ref } from "vue";
import { useAuthStore } from "@/store/authStore.js";
import PostIt from "@/components/layout/PostIt.vue";
import { storeToRefs } from "pinia";
import { event } from "vue-gtag";

import router from "@/router.js";

const authStore = useAuthStore();

router.push({path: "Home"});

</script>

<style scoped>
* {
  font-family: "Kalam", cursive;
}

.post-it {
  font-size: 15px;
  width: 200px;
  position: relative;
  left: 50%;
  transform: translateX(-50%);
  padding-top: 50px;
  padding-bottom: 50px;
}

.user-img {
  width: 25px;
  height: 25px;
}

.password-img {
  width: 20px;
  height: 20px;
  margin-left: 3px;
}

.show-password-img {
  width: 25px;
  height: 25px;
  margin-right: 3px;
}

#error-message {
  color: red;
  font-weight: bold;
  margin-top: 10px;
}

#icon {
  margin-right: 10px;
}

.fa-icons {
  font-size: 18px;
  margin-left: 5px;
}

.icon-div {
  display: flex;
  flex-direction: row;
  border: 1px solid #374669;
  border-radius: 5px;
  background: #fff;
  align-items: center;
  overflow: hidden;
  margin-top: 2px;
  margin-bottom: 5px;
}

.icon-div input {
  outline: none;
  border: none;
  background: none;
  font-size: 1em;
  padding: 0.5em;
  color: inherit;
  flex: auto 1 1;
  width: 100%;
  background: none;
  background-color: transparent;
}

.button-74 {
  background-color: #fbeee0;
  border: 2px solid #422800;
  border-radius: 25px;
  box-shadow: #422800 4px 4px 0 0;
  color: #422800;
  cursor: pointer;
  display: inline-block;
  font-weight: 600;
  font-size: 18px;
  padding: 0 18px;
  line-height: 40px;
  text-align: center;
  text-decoration: none;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  margin-top: 10px;
  margin-bottom: 0px;
}

.button-74:hover {
  background-color: #fff;
}

.button-74:active {
  box-shadow: #422800 2px 2px 0 0;
  transform: translate(2px, 2px);
}

@media (min-width: 768px) {
  .button-74 {
    min-width: 120px;
    padding: 0 25px;
  }
}
</style>
