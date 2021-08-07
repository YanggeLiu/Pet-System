<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="12" md="6">
        <v-card>
          <v-img
            src="//post.newsea.xyz/go_cam"
            lazy-src="https://picsum.photos/id/11/100/60"
            class="blue-grey lighten-4"
          >
            <template v-slot:placeholder>
              <v-row class="fill-height ma-0" align="center" justify="center">
                <v-progress-circular
                  indeterminate
                  color="grey"
                ></v-progress-circular>
              </v-row>
            </template>
          </v-img>
        </v-card>
        <!--<v-row align="center" justify="center">
          <v-col cols="6" md="4" sm="14">
            <v-card class="ma-2" max-width="200">
              <v-toolbar flat dense>
                <v-toolbar-title>
                  <span class="subheading">COL</span>
                </v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <v-row class="mb-4" justify="space-between">
                  <v-col class="text-center">
                    <span
                      class="display-3 font-weight-light"
                      v-text="col"
                    ></span>
                    <span class="subheading font-weight-light mr-1">°</span>
                  </v-col>
                </v-row>
                <v-slider
                  v-model="col"
                  color="indigo"
                  track-color="grey"
                  always-dirty
                  min="40"
                  max="60"
                  @input="post_col(col)"
                >
                  <template v-slot:prepend>
                    <v-icon color="indigo" @click="col_decrement">
                      mdi-minus
                    </v-icon>
                  </template>

                  <template v-slot:append>
                    <v-icon color="indigo" @click="col_increment"
                      >mdi-plus</v-icon
                    >
                  </template>
                </v-slider>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="6" md="4" sm="4">
            <v-card class="ma-2" max-width="200">
              <v-toolbar flat dense>
                <v-toolbar-title>
                  <span class="subheading">ROW</span>
                </v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <v-row class="mb-4" justify="space-between">
                  <v-col class="text-center">
                    <span
                      class="display-3 font-weight-light"
                      v-text="row"
                    ></span>
                    <span class="subheading font-weight-light mr-1">°</span>
                  </v-col>
                </v-row>
                <v-slider
                  v-model="row"
                  color="indigo"
                  track-color="grey"
                  always-dirty
                  min="50"
                  max="166"
                  @input="post_row(row)"
                >
                  <template v-slot:prepend>
                    <v-icon color="indigo" @click="row_decrement">
                      mdi-minus
                    </v-icon>
                  </template>

                  <template v-slot:append>
                    <v-icon color="indigo" @click="row_increment"
                      >mdi-plus</v-icon
                    >
                  </template>
                </v-slider>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>-->
      </v-col>
    </v-row>
    <v-row align="center" justify="center">
      <v-col class="text-center" cols="12" sm="12" md="6">
        <v-card rounded>
          <v-card-text>
            <v-row align="center" justify="center">
              <v-col
                class="text-center"
                cols="6"
                md="3"
                sm="3"
                v-for="position of all_angles"
                :key="position"
                ><v-btn
                  rounded
                  @click="move_angle(position)"
                  :loading="angle_load"
                  >{{ position }}</v-btn
                ></v-col
              >
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-speed-dial absolute bottom right v-model="fab">
      <template v-slot:activator>
        <v-btn fab v-model="fab">
          <v-icon v-if="fab"> mdi-close </v-icon>
          <v-icon v-else> mdi-cog-outline </v-icon>
        </v-btn>
      </template>
      <v-btn fab @click="sheet_plus = !sheet_plus"
        ><v-icon>mdi-plus</v-icon></v-btn
      >
      <v-btn fab @click="sheet_delete = !sheet_delete"
        ><v-icon color="red">mdi-delete</v-icon></v-btn
      >
    </v-speed-dial>
    <v-bottom-sheet v-model="sheet_plus">
      <v-sheet>
        <v-container>
          <v-row align="center" justify="center">
            <v-col class="text-center" cols="4" md="4">
              <v-text-field
                v-model="position_name"
                label="name"
                rounded
                outlined
                :disabled="loading_plus"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row align="center" justify="center">
            <v-col class="text-center" cols="6" md="2" sm="3">
              <v-card class="mx-2" max-width="200">
                <v-toolbar flat dense>
                  <v-toolbar-title>
                    <span class="subheading">COL</span>
                  </v-toolbar-title>
                </v-toolbar>
                <v-card-text>
                  <v-row class="mb-4" justify="space-between">
                    <v-col class="text-center">
                      <span
                        class="display-3 font-weight-light"
                        v-text="col"
                      ></span>
                      <span class="subheading font-weight-light mr-1">°</span>
                    </v-col>
                  </v-row>
                  <v-slider
                    v-model="col"
                    track-color="grey"
                    always-dirty
                    min="40"
                    max="60"
                    @input="post_col(col)"
                  >
                    <template v-slot:prepend>
                      <v-icon @click="col_decrement"> mdi-minus </v-icon>
                    </template>

                    <template v-slot:append>
                      <v-icon @click="col_increment">mdi-plus</v-icon>
                    </template>
                  </v-slider>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col class="text-center" cols="6" md="2" sm="3">
              <v-card class="mx-2" max-width="200">
                <v-toolbar flat dense>
                  <v-toolbar-title>
                    <span class="subheading">ROW</span>
                  </v-toolbar-title>
                </v-toolbar>
                <v-card-text>
                  <v-row class="mb-4" justify="space-between">
                    <v-col class="text-center">
                      <span
                        class="display-3 font-weight-light"
                        v-text="row"
                      ></span>
                      <span class="subheading font-weight-light mr-1">°</span>
                    </v-col>
                  </v-row>
                  <v-slider
                    v-model="row"
                    track-color="grey"
                    always-dirty
                    min="50"
                    max="166"
                    @input="post_row(row)"
                  >
                    <template v-slot:prepend>
                      <v-icon @click="row_decrement"> mdi-minus </v-icon>
                    </template>

                    <template v-slot:append>
                      <v-icon @click="row_increment">mdi-plus</v-icon>
                    </template>
                  </v-slider>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
          <v-row align="center" justify="center">
            <v-col class="text-center">
              <v-btn rounded @click="create_angle" :loading="loading_plus"
                >create</v-btn
              >
            </v-col>
          </v-row>
        </v-container>
      </v-sheet>
    </v-bottom-sheet>
    <v-bottom-sheet v-model="sheet_delete">
      <v-sheet>
        <v-container>
          <v-row align="center" justify="center">
            <v-col class="text-center">
              <v-list-item v-for="position of all_angles" :key="position">
                <v-list-item-content>
                  <div>{{ position }}</div>
                </v-list-item-content>
                <v-list-item-action>
                  <v-btn
                    color="red"
                    icon
                    @click="remove_angle(position)"
                    :loading="loading_delete"
                    ><v-icon>mdi-delete</v-icon></v-btn
                  >
                </v-list-item-action>
              </v-list-item>
            </v-col>
          </v-row>
        </v-container>
      </v-sheet>
    </v-bottom-sheet>
    <v-snackbar v-model="snackbar_plus" @input="close_plus">
      {{ success_plus }}
      <template #action="{ attrs }">
        <v-btn color="red" text v-bind="attrs" @click="close_plus">close</v-btn>
      </template>
    </v-snackbar>
    <v-snackbar v-model="snackbar_delete" @input="close_delete"
      >{{ success_delete }}
      <template #action="{ attrs }">
        <v-btn color="red" text v-bind="attrs" @click="close_delete"
          >close</v-btn
        >
      </template>
    </v-snackbar>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  name: "Cam",
  data: () => ({
    fab: false,
    sheet_plus: false,
    sheet_delete: false,
    loading_plus: false,
    loading_delete: false,
    snackbar_plus: false,
    snackbar_delete: false,
    success_plus: "",
    success_delete: "",
    position_name: "",
    all_angles: [],
    angle_load: false,
    col: 40,
    row: 50,
  }),
  created() {
    this.get_angle();
  },
  methods: {
    col_decrement() {
      this.col--;
    },
    col_increment() {
      this.col++;
    },
    row_decrement() {
      this.row--;
    },
    row_increment() {
      this.row++;
    },
    post_col(col) {
      console.log("this is " + col);
      axios({
        method: "post",
        url: "//post.newsea.xyz/col",
        data: {
          col: col,
        },
      })
        .then((response) => {
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    post_row(row) {
      console.log("this is " + row);
      axios({
        method: "post",
        url: "//post.newsea.xyz/row",
        data: {
          row: row,
        },
      })
        .then((response) => {
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    create_angle() {
      this.loading_plus = true;
      console.log(this.position_name, this.col, this.row);
      axios({
        method: "post",
        url: "//post.newsea.xyz/create_angle",
        data: {
          position_name: this.position_name,
          col: this.col,
          row: this.row,
        },
      })
        .then((response) => {
          if ((response.status == 200) & (response.data == "creata success!")) {
            this.get_angle();
            console.log(response);
            this.success_plus = response.data;
            this.snackbar_plus = true;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    close_plus() {
      this.loading_plus = false;
      this.sheet_plus = false;
      this.snackbar_plus = false;
    },
    close_delete() {
      this.loading_delete = false;
      this.sheet_delete = false;
      this.snackbar_delete = false;
    },
    get_angle() {
      this.$nextTick(() => {
        axios
          .get("//post.newsea.xyz/get_angle")
          .then((response) => {
            console.log(response);
            this.all_angles = response.data.all_angle;
            console.log(response.data.all_angle);
          })
          .catch((error) => {
            console.log(error);
          });
      });
    },
    move_angle(position) {
      console.log(position);
      this.angle_load = true;
      axios
        .post("//post.newsea.xyz/move_angle", {
          angle_name: position,
        })
        .then((response) => {
          if ((response.status == 200) & (response.data == "moved")) {
            this.angle_load = false;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    remove_angle(position) {
      this.loading_delete = true;
      axios
        .post("//post.newsea.xyz/remove_angle", {
          remove: position,
        })
        .then((response) => {
          if ((response.status == 200) & (response.data == "removed")) {
            this.get_angle();
            this.success_delete = response.data;
            this.snackbar_delete = true;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>