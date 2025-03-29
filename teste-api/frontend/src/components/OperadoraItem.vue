<template>
    <li class="operadora-item">
      <h2>{{ operadora.Razao_Social }}</h2>
      <p><strong>CNPJ:</strong> {{ operadora.CNPJ }}</p>
      <p><strong>Representante:</strong> {{ operadora.Representante }}</p>
      <p><strong>Telefone:</strong> {{ operadora.Telefone }}</p>
      <p><strong>Email:</strong> <a :href="'mailto:' + operadora.Endereco_eletronico">{{ operadora.Endereco_eletronico }}</a></p>
      <p><strong>Modalidade:</strong> {{ operadora.Modalidade }}</p>
      <p><strong>Endereço:</strong> {{ operadora.Logradouro }}, {{ operadora.Numero }} - {{ operadora.Complemento }}</p>
      <p><strong>Cidade:</strong> {{ operadora.Cidade }} - <strong>UF:</strong> {{ operadora.UF }}</p>
      <p><strong>Bairro:</strong> {{ operadora.Bairro }} <strong>CEP:</strong> {{ operadora.CEP }}</p>
      <p><strong>Data de Registro ANS:</strong> {{ operadora.Data_Registro_ANS }}</p>
    </li>
  </template>
  
  <script>
  export default {
    name: 'OperadoraItem',
    props: {
      operadora: Object
    }
  };
  </script>
  
  <style scoped>
  .operadora-item {
    margin: 10px 0;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  
  h2 {
    font-size: 1.2em;
    margin-bottom: 10px;
  }
  </style>
  