<script setup>
import Contacts from './components/Contacts.vue';
</script>

<template>
  <div id="app">
    <h1>📒 Lista de Contatos</h1>
    <Contacts />
  </div>
</template>

<style scoped>
#app {
  margin: 20px auto;
  padding: 20px;
  max-width: 800px;
  text-align: center;
  background: #f9f9f9;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h1 {
  margin-bottom: 20px;
  font-family: 'Roboto', Arial, sans-serif;
  font-size: 28px;
  color: #2c3e50;
}
</style>