<template>
  <div id="app">
    <vc-calendar is-expanded :attributes="computedTasks" />
  </div>
</template>

<script>
import Cookies from "js-cookie";
import axios from "axios";

export default {
  name: "App",

  data() {
    return {
      currentDate: new Date(),
      tasks: [],
    };
  },

  computed: {
    computedTasks: function() {
      let computedVal = [];
      const colors = [
        "gray",
        "red",
        "orange",
        "yellow",
        "green",
        "teal",
        "blue",
        "indigo",
        "purple",
        "pink",
      ];
      console.log(this.tasks);
      for (var idx in this.tasks) {
        let task = this.tasks[idx];
        computedVal.push({
          key: task.pk,
          dot: colors[(colors.length * Math.random()) | 0],
          dates: {
            start: new Date(task.fields.created_on),
            end: new Date(task.fields.due_on),
          },
          popover: {
            label: `${task.fields.name}: ${task.fields.description}`,
          },
        });
      }
      return computedVal;
    },
  },

  methods: {
    getData() {
      const departmentId = Cookies.get("department_id");
      axios
        .get(`http://localhost:8000/api/get-tasks/${departmentId}/`)
        .then((response) => {
          const tasks = response.data;
          this.tasks = tasks;
        })
        .catch((err) => console.log(err));
    },
  },

  mounted() {
    this.getData();

    if (window.webpackHotUpdate) {
      console.log("In Dev Mode.");

      // set temporary cookie
      Cookies.set("department_id", 1, { expires: 1, path: "" });
    }
  },
};
</script>
