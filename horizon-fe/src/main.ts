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

// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

library.add(faUser, faBars, faMagnifyingGlass, faCartShopping, faLocationDot);

const vuetify = createVuetify({
  components,
  directives,
});

const app = createApp(App);
app.component("font-awesome-icon", FontAwesomeIcon);
app.use(vuetify);
app.mount("#app");
