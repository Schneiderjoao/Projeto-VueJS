<script>
import axios from 'axios';
import Contact from './Contact.vue';

export default {
  name: 'App',
  components: { Contact },
  data() {
    return {
      contacts: [],
      contact: { name: '', email: '', photo: '' },  // para criação
      contactOld: null,                             // para atualização, se precisar
    };
  },
  mounted() {
    this.getContacts();
  },
  methods: {
    async getContacts() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/contacts');
        this.contacts = response.data.contacts; // Atualiza a lista de contatos
      } catch (error) {
        console.error('Failed to fetch contacts:', error);
      }
    },

    async createContact() {
      try {
        const response = await axios.post('http://127.0.0.1:5000/contacts', this.contact);
        this.contacts.push(response.data); // Adiciona o novo contato à lista (ajuste conforme seu backend)
        this.contact = { name: '', email: '', photo: '' }; // Limpa o formulário
      } catch (error) {
        console.error('Erro ao adicionar contato:', error);
      }
    },

    async updateContact() {
      if (!this.contactOld) {
        console.warn('Nenhum contato selecionado para atualizar');
        return;
      }

      if (confirm(`Deseja atualizar os dados de ${this.contactOld.name}?`)) {
        try {
          const response = await axios.put(`http://127.0.0.1:5000/contacts/${this.contactOld.email}`, this.contact);
          if (response.status === 200) {
            console.log(`Contato ${this.contact.name} atualizado com sucesso.`);
            // Atualiza lista local: substitui o contato antigo pelo atualizado
            const index = this.contacts.findIndex(c => c.email === this.contactOld.email);
            if (index !== -1) {
              this.contacts.splice(index, 1, response.data);
            }
          }
        } catch (error) {
          console.error('Erro ao atualizar contato:', error);
        }
      }
    },

    async updateContactName(contact, newName) {
      try {
        const response = await axios.patch(`http://127.0.0.1:5000/contacts/${contact.email}`, { name: newName });
        console.log(`Nome atualizado para: ${response.data.name}`);
        // Atualiza localmente também
        contact.name = response.data.name;
      } catch (error) {
        console.error('Erro ao atualizar o nome do contato:', error);
      }
    },

    async removeContact(contact) {
      if (confirm(`Apagar o contato: ${contact.email}?`)) {
        try {
          await axios.delete(`http://127.0.0.1:5000/contacts/${contact.email}`);
          this.contacts.splice(this.contacts.indexOf(contact), 1); // Remove localmente
        } catch (error) {
          console.error('Erro ao remover o contato:', error);
        }
      }
    }
  }
};
</script>

<template>
  <div id="app">
    <h1>Contatos</h1>
    <ul>
      <li v-for="contact in contacts" :key="contact.email">
        <Contact :contact="contact" />
        <button @click="removeContact(contact)">Excluir</button>
      </li>
    </ul>
  </div>
</template>

<style scoped>
#app {
  font-family: 'Roboto', Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  padding: 20px;
}

ul {
  padding: 0px;
}

li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 15px;
  margin: 10px;
  border: 1px solid #dddddd;
  border-radius: 8px;
  background: #ffffff;
  box-shadow: 1px 4px 6px rgba(0, 0, 0, 0.1);
}

li:hover {
  background-color: #eaf7ff;
  transform: scale(1.05);
  box-shadow: 1px 8px 12px rgba(0, 0, 0, 0.15);
}

button {
  background-color: #f44336;
  color: #ffffff;
  border: none;
  padding: 12px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

button:hover {
  background-color: #ca2c29;
}

button:active {
  background-color: #ff5100;
  transform: scale(0.98);
}

button:focus {
  outline: none;
}
</style>