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
      currentDate: new Date(),
      // Attributes are supplied as an array
      attributes: [
        {
          key: "today",
          dot: "red",
          dates: [
            new Date(2021, 4, 1), // Jan 1st
            new Date(2021, 4, 10), // Jan 10th
            new Date(2021, 4, 22), // Jan 22nd
          ],
        },
      ],
    };
  },

  methods: {
    getCurrentDate() {
      return this.currentDate;
    },
  },
};
</script>
