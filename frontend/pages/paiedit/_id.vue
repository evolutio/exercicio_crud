<template>
  <v-layout justify-center align-center>
    <PaiEdit :id="$route.params.id"></PaiEdit>
  </v-layout>
</template>

<script>

import PaiEdit from '~/components/PaiEdit.vue'

export default {
  data () {
    return {}
  },
  mounted () {
    // window.PaiEdit = this // debug temporario
  },
  components: {
    PaiEdit
  }
}
</script>

<style>
</style>
