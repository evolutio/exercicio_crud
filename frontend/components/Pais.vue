<template>
  <v-layout justify-center align-center>
    <v-data-table
      :headers="headers"
      :items="pais"
      hide-actions
      class="elevation-1"
    >
      <template slot="items" slot-scope="props">
        <td>
          <router-link :to="{ name: 'paiedit-id', params: { id: props.item.id }}">
            {{ props.item.name }}
          </router-link>
        </td>
        <td class="text-xs-right">{{ props.item.countfilhos }}</td>
        <td class="text-xs-right">{{ props.item.maisvelho }}</td>
      </template>
    </v-data-table>
    <v-btn :to="{name: 'paiedit-id'}">Novo</v-btn>
  </v-layout>
</template>

<script>

import Pais from '~/components/Pais.vue'
import AppApi from '~apijs'

export default {
  data () {
    return {
      pais: [],
      headers: [
        { text: 'Nome', value: 'name' },
        { text: 'Quantos filhos', value: 'countfilhos' },
        { text: 'O filho mais velho...', value: 'maisvelho' },
      ]
    }
  },
  created() {
    AppApi.list_pais().then(response => {
      this.pais = response.data
    })
  }
}
</script>

<style>
</style>
