<template>
  <div id="app">
    <vc-calendar is-expanded :attributes="attributes" />
  </div>
</template>

<script>
export default {
  name: "App",

  data() {
    return {
      departmentID: 0,
      currentDate: new Date(),
      // Attributes are supplied as an array
      attributes: [
        {
          key: "today",
          dot: "red",
          dates: [
            new Date(2021, 4, 1),
            new Date(2021, 4, 10),
            new Date(2021, 4, 22),
          ],
          popover: {
            label: "this is an example popoverrrr",
          },
        },
        {
          key: "not today",
          dot: "green",
          dates: [new Date(2021, 4, 22)],
          popover: {
            label: "<3 <3",
          },
        },
      ],
    };
  },

  methods: {
    getCurrentDate() {
      return this.currentDate;
    },

    getData() {},
  },

  mounted() {
    this.getData();
  },
};
</script>
