<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="12" md="6">
        <v-list>
          <v-list-item>
            <v-list-item-content>
              <div>暗黑模式</div>
            </v-list-item-content>
            <v-list-item-action>
              <v-switch></v-switch>
            </v-list-item-action>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <div>夜视模式</div>
            </v-list-item-content>
            <v-list-item-action>
              <v-switch
                v-model="v_status"
                :loading="v_switch"
                :disabled="v_disable"
                @change="vision_mode"
              ></v-switch>
            </v-list-item-action>
          </v-list-item>
          <v-list-item class="text-center">
            <v-list-item-content>
              <v-btn
                class="text-center"
                color="red"
                :loading="reboot_loading"
                @click="reboot"
                >重启设备</v-btn
              >
            </v-list-item-content>
          </v-list-item>
          <v-list-item class="text-center">
            <v-list-item-content
              ><v-btn class="text-center" color="red"
                >退出登录</v-btn
              ></v-list-item-content
            >
          </v-list-item>
        </v-list>
      </v-col>
    </v-row>
    <v-snackbar v-model="reboot_snackbar" @click="close_reboot">
      {{ reboot_response }}
      <template #action="{ attrs }">
        <v-btn color="red" text v-bind="attrs" @click="close_reboot"
          >close</v-btn
        >
      </template>
    </v-snackbar>
  </v-container>
</template>


<script>
import axios from "axios";
export default {
  name: "Setting",
  data: () => ({
    reboot_loading: false,
    reboot_snackbar: false,
    reboot_response: "",
    relink_data: 0,
    v_status: false,
    v_switch: false,
    v_disable: true,
  }),
  created() {
    this.check_mode();
  },
  methods: {
    sleep(time) {
      return new Promise((resolve) => {
        setTimeout(resolve, time);
      });
    },
    reboot() {
      this.reboot_loading = true;
      axios.get("//newsea.xyz/reboot").catch((error) => {
        console.error(error);
      });
      this.sleep(10000).then(() => {
        this.relink();
      });
    },
    relink() {
      axios.get("//post.newsea.xyz/relink").then((response) => {
        if ((response.status == 200) & (response.data == "relink")) {
          this.reboot_response = "success";
          this.reboot_snackbar = true;
          clearTimeout(this.relink_data);
          this.sleep(5000).then(() => {
            this.close_reboot();
          });
        }
      });
      this.relink_data = setTimeout(() => {
        this.relink();
      }, 40000);
    },
    close_reboot() {
      this.reboot_loading = false;
      this.reboot_snackbar = false;
    },
    vision_mode() {
      this.v_switch = true;
      let status = "1";
      if (this.v_status == true) {
        status = "0";
      }
      axios
        .post(
          "//post.newsea.xyz/v_mode",
          {
            status: status,
          },
          {
            timeout: 10000,
          }
        )
        .then((response) => {
          console.log(response);
          if ((response.status == 200) & (response.data == "changed")) {
            this.v_switch = false;
          }
        });
    },
    check_mode() {
      axios.get("//post.newsea.xyz/check_status").then((response) => {
        if ((response.status == 200) & (response.data["info"] == "success")) {
          var status = response.data["status"];
          if (status == "0") {
            this.v_status = true;
          }
          this.v_disable = false;
        }
      });
    },
  },
};
</script>

<style>
</style>