import { createApp } from "vue";
import App from "./App.vue";

import "./assets/main.css";

import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import {
  faMagnifyingGlass,
  faBars,
  faCartShopping,
  faLocationDot,
} from "@fortawesome/free-solid-svg-icons";
import { faUser } from "@fortawesome/free-regular-svg-icons";

import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

library.add(faUser, faBars, faMagnifyingGlass, faCartShopping, faLocationDot);

createApp(App).component("font-awesome-icon", FontAwesomeIcon).mount("#app");
