<template>
  <v-app id="app">
    <v-app-bar app> </v-app-bar>

    <v-main>
      <router-view v-if="token"></router-view>
      <Login v-if="!token" />
    </v-main>
    <v-bottom-navigation color="primary" mandatory v-if="token">
      <v-btn @click="to_Home">
        <v-icon>mdi-account-outline</v-icon>
      </v-btn>

      <v-btn @click="to_Cloud">
        <v-icon>mdi-cloud</v-icon>
      </v-btn>

      <v-btn @click="to_Cam">
        <v-icon>mdi-webcam</v-icon>
      </v-btn>

      <v-btn @click="to_Chat">
        <v-icon>mdi-message-text</v-icon>
      </v-btn>

      <v-btn @click="to_Setting">
        <v-icon>mdi-cog-outline</v-icon>
      </v-btn>
    </v-bottom-navigation>
  </v-app>
</template>

<script>
import router from "./router";
import Login from "@/views/Login.vue";

export default {
  components: { Login },
  name: "App",
  beforeDestroy() {
    this.$vuetify.theme.dark = true;
  },

  data: () => ({
    token: false,
  }),
  provide() {
    return {
      reload: this.reload,
    };
  },

  methods: {
    to_Home: function () {
      router.push("/");
    },
    to_Cloud: () => {
      router.push("./cloud");
    },
    to_Cam: function () {
      router.push("./cam");
    },
    to_Chat: function () {
      router.push("./chat");
    },
    to_Setting: function () {
      router.push("./setting");
    },
    reload() {
      this.$nextTick(() => {
        this.token = true;
      });
    },
  },
};
</script>
