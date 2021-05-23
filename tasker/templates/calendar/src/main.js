import Vue from "vue";
import App from "./App.vue";

import VueCustomElement from "vue-custom-element";

import VCalendar from "v-calendar";
import Calendar from "v-calendar/lib/components/calendar.umd";
import DatePicker from "v-calendar/lib/components/date-picker.umd";

Vue.config.productionTip = false;

Vue.use(VueCustomElement);
Vue.use(VCalendar, {
  componentPrefix: "vc", // Use <vc-calendar /> instead of <v-calendar />
});
Vue.component("calendar", Calendar);
Vue.component("date-picker", DatePicker);
Vue.customElement("vue-widget", App);
