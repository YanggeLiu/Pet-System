<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="12" md="6">
        <v-card elevation="10">
          <v-img
            class="white--text align-end"
            height="200px"
            src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
          >
            <v-sheet
              class="ma-auto"
              elevation="60"
              color="cyan"
              rounded="circle"
              max-width="110"
              max-height="110"
            >
              <v-avatar size="110">
                <v-img
                  src="https://gobrandgo.com/wp-content/uploads/2013/10/surprised-cat-eric-hacke.jpg"
                >
                </v-img>
              </v-avatar>
            </v-sheet>
            <div class="my-5 text-h6 text-center font-weight-medium">
              {{ time }}, {{ user }}
            </div>
          </v-img>
          <v-card-text class="text-center">
            <template>
              <vue-weather
                api-key="db4b8eccddf770833d85294f7f89d5b7"
                units="uk"
                language="zh"
              />
            </template>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
.a {
  bottom: -60px;
  position: relative;
  z-index: 100;
}
</style>

<script>
// @ is an alias to /src
import VueWeather from "vue-weather-widget";

export default {
  name: "Home",
  created() {
    this.get_user();
    this.get_time();
  },
  data: () => ({
    user: "",
    time: "",
  }),
  methods: {
    get_user() {
      this.user = this.$store.state.user;
    },
    get_time() {
      var hours = new Date().getHours();
      if ((6 <= hours) & (hours < 12)) {
        this.time = "Morning";
      } else if ((12 <= hours) & (hours < 19)) {
        this.time = "Afternoon";
      } else {
        this.time = "Evening";
      }
    },
  },
  components: {
    VueWeather,
  },
};
</script>
