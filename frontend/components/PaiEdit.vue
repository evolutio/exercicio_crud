<template>
  <v-layout justify-center align-center>
    <template v-if="!loading">
      <v-form>
        <v-text-field v-model="pai.name" label="Nome"></v-text-field>
        <v-text-field v-model="pai.countfilhos" type="number" label="Quantos filhos"></v-text-field>
        <v-text-field v-model="pai.maisvelho" label="O filho mais velho..."></v-text-field>
      </v-form>
      <v-btn @click="salvar()" :loading="saving">Salvar</v-btn>
      <v-btn v-if="pai.id" @click="remove()" :loading="removing">Remover</v-btn>
    </template>
  </v-layout>
</template>

<script>

import Pais from '~/components/Pais.vue'
import AppApi from '~apijs'

export default {
  props: ['id'],
  data () {
    return {
      pai: {
        name: '',
        countfilhos: 0,
        maisvelho: ''
      },
      loading: false,
      saving: false,
      removing: false
    }
  },
  created () {
    if(this.id){
      this.loading = true
      AppApi.get_pai(this.id).then(response => {
        this.pai = response.data;
        this.loading = false
      })
    }
  },
  methods: {
    salvar (){
      this.saving = true
      AppApi.save_pai(this.pai).then(response => {
        this.saving = false
        this.$router.push({name: 'pais'})
      })
    },
    remove () {
      this.removing = true
      AppApi.remove_pai(this.pai.id).then(response => {
        this.removing = false
        this.$router.push({name: 'pais'})
      })
    }
  }
}
</script>

<style>
</style>
