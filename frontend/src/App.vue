<template>
    <main class="container pt-4">
      <div>
        <router-link :to="{ name: 'main-page' }">Main Page</router-link>
        | 
        <router-link :to="{ name: 'other-page' }">Other Page</router-link>
        |
        <router-link :to="{ name: 'login' }">Login</router-link>
        |
        <router-link :to="{ name: 'register' }">Register</router-link>
      </div>
      <RouterView class="flex-shrink-0" />
    </main>
  </template>
  
  <script lang="ts">
  import { defineComponent } from "vue";
  import { RouterView } from "vue-router";
  
  export default defineComponent({
      components: { RouterView },
  });
  </script>
  
  <style scoped>
   /* specific styling if needed */
  </style>
  