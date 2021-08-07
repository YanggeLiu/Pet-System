<template>
  <v-app id="about">
    <v-app-bar app></v-app-bar>
    <v-main>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="12" md="6">
            <v-img src="@/assets/logo.png"></v-img>
            <div class="text-h3 text-center">Powered by <pre></pre>VUE FLASK</div>
          </v-col>
        </v-row>
        <v-snackbar v-model="snackbar" timeout="10000">
          <div>请检查设备网络后刷新</div>
          <template v-slot:action="{ attrs }">
            <v-btn color="red" text v-bind="attrs" @click="snackbar = false"
              >close</v-btn
            >
          </template>
        </v-snackbar>
        <v-footer absolute class="font-weight-medium">
          <v-col class="text-center" cols="12"
            >Copyright © {{ new Date().getFullYear() }} YanggeLiu.
            <pre>All Rights Reserved.</pre></v-col
          >
        </v-footer>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "about",
  beforeDestroy() {
    this.$vuetify.theme.dark = true;
  },
  data: () => ({
    snackbar: true,
  }),
};
</script>