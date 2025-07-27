import { createRouter, createWebHistory } from "vue-router";

const TheHome = () => import("./pages/TheHome.vue");
const TheLogin = () => import("@/pages/TheLogin.vue");
const TheLogout = () => import("@/pages/TheLogout.vue");
const TheRegistration = () => import("./pages/TheRegistration.vue");
const TheAds = () => import("./pages/TheAds.vue");
const TheDemo = () => import("./pages/TheDemo.vue");
const NotFound = () => import("./pages/NotFound.vue");

const routes = [
  {
    // path: "/VueToDoApp/",
    path: "/",
    name: "Home",
    component: TheHome,
  },
  {
    // path: "/VueToDoApp/login",
    path: "/login",
    name: "Authorization",
    component: TheLogin,
  },
  {
    // path: "/VueToDoApp/login",
    path: "/logout",
    name: "Logout",
    component: TheLogout,
  },
  {
    // path: "/VueToDoApp/register",
    path: "/register",
    name: "Registration",
    component: TheRegistration,
  },
  {
    path: "/demo",
    name: "Demo",
    component: TheDemo,
  },
  {
    path: "/ads.txt"
  },
  { path: "/:notFound(.*)", component: NotFound },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
