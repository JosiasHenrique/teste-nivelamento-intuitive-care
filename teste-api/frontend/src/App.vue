<template>
  <div id="app">
    <div class="content">
      <SearchInput @buscar="buscarOperadoras" />
    <ul>
      <li v-if="operadoras.length === 0">Nenhuma operadora encontrada.</li>
      <OperadoraItem 
        v-for="operadora in operadoras" 
        :key="operadora.CNPJ" 
        :operadora="operadora" 
      />
    </ul>
    </div>
    <footer>
    <p>Desenvolvido por Josias Henrique</p>
  </footer>
  </div>
</template>

<script>
import axios from 'axios';
import SearchInput from './components/SearchInput.vue';
import OperadoraItem from './components/OperadoraItem.vue';

export default {
  name: 'App',
  components: {
    SearchInput,
    OperadoraItem
  },
  data() {
    return {
      operadoras: [],
    };
  },
  methods: {
    buscarOperadoras(termoBusca) {
      if (termoBusca.trim() === '') {
        this.operadoras = [];
        return;
      }
      axios.get(`http://127.0.0.1:5000/buscar?termo=${termoBusca}`)
        .then(response => {
          this.operadoras = response.data;
        })
        .catch(error => {
          console.error('Erro ao buscar as operadoras:', error);
        });
    },
  },
};
</script>

<style scoped>
@import './assets/styles/global.css';
</style>
