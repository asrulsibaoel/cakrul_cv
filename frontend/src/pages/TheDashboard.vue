<template>
  <the-header></the-header>
  <main>
    <h1>Welcome to the to-do list app</h1>
    <h2>Simple, yet powerful task management application</h2>
    <div class="linksbox">
      <post-it id="demo-link">
        <div class="inner-demo-link">
          <p>
            <strong> Try Demo Playground. No registration required! </strong>
          </p>
          <button @click="
            router.push({ name: 'Demo' });
          demoAnalytics();
          " class="button-74">
            Demo
          </button>
        </div>
      </post-it>
    </div>
    <div class="swip">
      <swiper :slidesPerView="1" :spaceBetween="30" :loop="true" :lazy="true" :centeredSlides="true" :pagination="{
        clickable: true,
      }" :autoplay="{
  delay: 5000,
  // disableOnInteraction: false,
}" :navigation="true" :modules="modules">
        <swiper-slide><img :src="slide1URL" alt="slide 1" class="slide-1 swiper-lazy" rel="preload" /></swiper-slide>
        <swiper-slide><img :src="slide2URL" alt="slide 2" class="slide-2 swiper-lazy" rel="preload" /></swiper-slide>
        <swiper-slide><img :src="slide3URL" alt="slide 3" class="slide-3 swiper-lazy" rel="preload" /></swiper-slide>
      </swiper>
    </div>
  </main>
  <the-footer class="footer"></the-footer>
</template>

<script setup>
import { ref } from "vue";
import { Swiper, SwiperSlide } from "swiper/vue";
import PostIt from "@/components/layout/PostIt.vue";
import { event } from "vue-gtag";

import SwiperCore, {
  Navigation,
  Pagination,
  Scrollbar,
  A11y,
  Autoplay,
  Lazy,
} from "swiper";

import "swiper/css";
import "swiper/css/navigation";
import "swiper/css/pagination";
import "swiper/css/autoplay";
import "swiper/css/lazy";

import { useRouter } from "vue-router";

SwiperCore.use([Navigation, Pagination, Scrollbar, A11y, Autoplay, Lazy]);
const modules = ref([Navigation, Pagination, Scrollbar, A11y, Autoplay, Lazy]);
const router = useRouter();

const slide1URL = new URL("@/assets/tasks_slide_1.webp", import.meta.url).href;
const slide2URL = new URL("@/assets/tasks_slide_2.webp", import.meta.url).href;
const slide3URL = new URL("@/assets/tasks_slide_3.webp", import.meta.url).href;


const demoAnalytics = async () => {
  event("demo-button-clicked", {
    event_category: "analytics",
    event_label: "Demo",
    value: 1,
  });
}
</script>

<style scoped>
* {
  font-family: "Kalam", cursive;
}

.slide-1 {
  width: 90%;
  height: 50%;
}

.slide-2 {
  width: 70%;
  height: 70%;
}

.slide-3 {
  width: 50%;
  height: 50%;
  margin-bottom: 15px;
}

.linksbox {
  display: flex;
  justify-content: center;
  margin-bottom: 5px;
}

#demo-link {
  display: flex;
  width: 60%;
  justify-content: center;
  align-items: center;
  padding: 0px;
  min-height: 5em;
  background: #bbe1f5;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
}

#demo-link:after {
  content: "";
  border-color: #bbe1f5;
  border-bottom-left-radius: 15px;
  bottom: -1em;
  left: 0;
  right: 1em;
  border-width: 0.5em;
}

#demo-link:before {
  border-color: #53b2e5 transparent;
  bottom: -1em;
  border-width: 1em 1em 0 0;
}

.inner-demo-link {
  display: flex;
  flex-direction: column;
  align-items: center;
}

main {
  display: flex;
  flex-direction: column;
  min-height: 90vh;
}

.footer {
  margin-top: auto;
}

.button-74 {
  background-color: #2179b8;
  border: 2px solid transparent;
  border-radius: 25px;
  cursor: pointer;
  font-weight: 300;
  font-size: 16px;
  padding: 3px 18px;
  line-height: 20px;
  text-align: center;
  text-decoration: none;
  color: #bbe1f5;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  flex: 0;
  width: 120px;
  margin-bottom: 10px;
}

.button-74:hover {
  background-color: #18458e;
}
</style>

<style>
.swiper-button-next,
.swiper-button-prev {
  color: lightsalmon;
  height: 0px;
  width: 15px;
}

.swiper-pagination-bullet {
  margin-right: 5px !important;
}
</style>
