import Vue from "vue";
import vuetify from "@/plugins/vuetify";
import About from "@/views/About.vue"


new Vue({
    vuetify,
    render: h => h(About)
}).$mount('#app')