<template>
  <!-- <header>
    <img src="@/assets/note.png" alt="" />
    <nav>
      <h1 class="app-name">
        <router-link :to="{ name: 'Home' }"> to-do app </router-link>
      </h1>
    </nav>
    <button v-if="!loggedIn" @click="router.push({ name: 'Registration' })" class="button-74">
      Register
    </button>
    <button v-if="!loggedIn" @click="router.push({ name: 'Authorization' })" class="button-74" id="login-button">
      Log In
    </button>
    <button v-else class="button-74" @click="authStore.logout()">Logout</button>
  </header> -->
  <header>
      <button class="btn btn-white btn-share ml-auto mr-3 ml-md-0 mr-md-auto"><img src="/src/assets/images/share.svg" alt="share" class="btn-img">
          SHARE</button>
      <nav class="collapsible-nav" id="collapsible-nav">
          <a href="/" class="nav-link active">HOME</a>
<!--            <a href="/resume" class="nav-link {% if is_resume == True %}active {% endif %}">RESUME</a>-->
<!--            <a href="/portfolio" class="nav-link {% if is_portfolio == True %}active {% endif %}">PORTFOLIO</a>-->
<!--            <a href="/blog" class="nav-link {% if is_blog == True %}active {% endif %}">BLOG</a>-->
          <a href="/contact" class="nav-link active">CONTACT</a>
      </nav>
      <button class="btn btn-menu-toggle btn-white rounded-circle" data-toggle="collapsible-nav"
          data-target="collapsible-nav"><img src="/src/assets/images/hamburger.svg" alt="hamburger"></button>
  </header>
</template>

<script setup>
import { useAuthStore } from "@/store/authStore.js";
import { computed } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const authStore = useAuthStore();
const loggedIn = computed(() => authStore.isAuthenticated);
</script>

<!-- <style scoped>
* {
  font-family: "Kalam", cursive;
}

header {
  grid-area: header;
  margin-top: 2px;
  background-color: bisque;
  /* making HEADER inside of the grid flexbox */
  display: flex;
  justify-content: center;
  align-items: center;
}

.greetings {
  margin-left: 30%;
  margin-top: 25px;
  align-items: center;
}

.greetings span {
  color: #127b14;
}

header nav {
  margin-left: 10px;
  display: flex;
  width: 100%;
}

header a {
  text-decoration: none;
  color: black;
}

.button-74 {
  background-color: #fbeee0;
  border: 2px solid #422800;
  border-radius: 25px;
  box-shadow: #422800 3px 3px 0 0;
  color: #422800;
  cursor: pointer;
  font-weight: 300;
  font-size: 16px;
  padding: 3px 18px;
  line-height: 20px;
  text-align: center;
  text-decoration: none;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  flex: 0;
  margin-right: 15px;
  flex-basis: 100px;
}

#login-button {
  flex-basis: 90px;
  flex-shrink: 0;
}

header img {
  width: 30px;
  margin-left: 10px;
}

.button-74:hover {
  background-color: #fff;
}

.button-74:active {
  box-shadow: #422800 2px 2px 0 0;
  transform: translate(2px, 2px);
}

@media only screen and (max-width: 460px) {
  .greetings {
    margin-left: 10px;
  }
}
</style> -->
