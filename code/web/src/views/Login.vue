<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card class="elevation-12">
          <v-toolbar color="primary" dark falt>
            <v-toolbar-title>Login</v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-form>
              <v-text-field
                v-model="account"
                label="account"
                prepend-icon="mdi-account"
                type="text"
                clearable
                :disabled="loading"
              ></v-text-field>

              <v-text-field
                v-model="password"
                label="password"
                prepend-icon="mdi-lock"
                type="password"
                clearable
                :disabled="loading"
              ></v-text-field>
            </v-form>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="primary" @click="post_login" :loading="loading"
                >Login</v-btn
              >
            </v-card-actions>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-snackbar v-model="snackbar" @input="error_find">
      {{ error }}
      <template #action="{ attrs }">
        <v-btn color="red" text v-bind="attrs" @click="error_find">close</v-btn>
      </template>
    </v-snackbar>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  inject: ["reload"],
  data: () => ({
    account: "",
    password: "",
    loading: false,
    snackbar: false,
    error: "",
  }),
  name: "Login",
  methods: {
    post_login() {
      this.loading = true;
      console.log(this.account, this.password);
      axios
        .post(
          "//post.newsea.xyz/login",
          {
            account: this.account,
            password: this.password,
          },
          {
            timeout: 10000,
          }
        )
        .then((response) => {
          console.log(response);
          if (
            (response.status == 200) &
            (response.data["info"] == "success!")
          ) {
            this.$store.commit("SET_USER", response.data["user"]);
            this.$cookies.set("token", "123", "60s");
            if (this.$cookies.isKey("token")) {
              this.reload();
            }
          } else if (
            (response.status == 200) &
            (response.data == "pwd is wrong")
          ) {
            this.error = response.data;
            this.snackbar = true;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    error_find() {
      this.loading = false;
      this.snackbar = false;
    },
  },
};
</script>