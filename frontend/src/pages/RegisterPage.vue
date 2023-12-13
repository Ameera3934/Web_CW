<template>
    <div class="register-container">
      <h2>Register Page</h2>
      <form @submit.prevent="registerUser">
        <div class="form-group">
          <label for="username">Username</label>
          <input type="text" id="username" v-model="username">
        </div>
        <div class="form-group">
          <label for="password1">Password</label>
          <input type="password" id="password1" v-model="password1">
        </div>
        <div class="form-group">
          <label for="password2">Confirm Password</label>
          <input type="password" id="password2" v-model="password2">
        </div>
        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" id="email" v-model="email">
        </div>
        <!-- Additional fields like dob and profile_image can be added here -->
        <input type="submit" value="Register">
      </form>
      <p v-if="error" class="error">{{ error }}</p>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    data() {
      return {
        username: '',
        password1: '',
        password2: '',
        email: '',
        // Add additional fields like dob and profile_image
        error: null
      };
    },
    methods: {
      async registerUser() {
        // Implement the registration logic here
        // This typically involves making an API call to your backend
      }
    }
  });
  </script>
  
  <style scoped>
    .register-container {
      max-width: 600px;
      margin: 0 auto;
      padding: 20px;
      background-color: #ffffff;
      border-radius: 5px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
  
    h2 {
      text-align: center;
      font-size: 24px;
      margin-top: 20px;
    }
  
    .form-group {
      margin-bottom: 10px;
    }
  
    label {
      display: block;
    }
  
    input[type="text"],
    input[type="password"],
    input[type="email"],
    input[type="submit"] {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 5px;
      font-size: 16px;
    }
  
    input[type="submit"] {
      background-color: #4CAF50;
      color: #fff;
      cursor: pointer;
    }
  
    input[type="submit"]:hover {
      background-color: #45a049;
    }
  
    .error {
      color: red;
    }
  </style>
  