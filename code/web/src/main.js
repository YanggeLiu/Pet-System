import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import axios from 'axios';
import VueCookies from 'vue-cookies';
import Vuex from 'vuex';
import './registerServiceWorker'

Vue.config.productionTip = false
Vue.use(VueCookies)
Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    user: ''
  },
  mutations: {
    SET_USER: (state, send) => {
      state.user = send
    }
  }
})

new Vue({
  vuetify,
  router,
  axios,
  store: store,
  render: h => h(App)
}).$mount('#app')
