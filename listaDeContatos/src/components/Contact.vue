<script>
export default {
  name: 'Contact',
  props: {
    contact: {
      type: Object,
      required: true
    }
  }
}
</script>

<template>
  <div class="contact">
    <img :src="contact.photo || 'https://via.placeholder.com/50'" :alt="contact.name" />
    <div class="info">
      <p class="name">{{ contact.name }}</p>
      <p class="email">{{ contact.email }}</p>
    </div>
  </div>
</template>

<style scoped>
.contact {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
  padding: 10px;
}

img {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-right: 15px;
  object-fit: cover;
}

.info {
  display: flex;
  flex-direction: column;
}

.name {
  font-weight: bold;
  font-size: 18px;
  color: #333333;
  margin: 0;
}

.gmail {
  color: #777777;
  font-size: 16px;
  margin: 0;
}
</style>
