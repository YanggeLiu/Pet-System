<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="12" md="6">
        <v-img src="@/assets/logo.png"></v-img>
      </v-col>
    </v-row>
    <v-snackbar v-model="snackbar" timeout="1000">
      <div>未开放</div>
      <template v-slot:action="{ attrs }">
        <v-btn color="red" text v-bind="attrs" @click="snackbar = false"
          >close</v-btn
        >
      </template>
    </v-snackbar>
  </v-container>
</template>

<script>
export default {
  name: "Chat",
  data: () => ({
    snackbar: true,
  }),
};
</script>