<template>
    <div class="register-container">
      <h2>Register Page</h2>
      <form @submit.prevent="registerUser">
        <!-- Username creation -->
        <div class="form-group">
          <label for="username">Username</label>
          <input type="text" id="username" v-model="username">
        </div>
        <!-- Password creation and confirmation -->
        <div class="form-group">
          <label for="password1">Password</label>
          <input type="password" id="password1" v-model="password1">
        </div>
        <div class="form-group">
          <label for="password2">Confirm Password</label>
          <input type="password" id="password2" v-model="password2">
        </div>
        <!-- Email -->
        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" id="email" v-model="email">
        </div>
        <!-- DOB -->
        <div class="form-group">
            <label for="dob">Date of Birth</label>
            <input type="date" id="dob" v-model="dob">
        </div>

        <!-- Profile Image -->
       <div class="form-group">
        <label for="profileImage">Profile Image</label>
        <input type="file" id="profileImage" @change="onFileChange">
       </div>
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
        dob: '',
        profileImage: null,
        error: null
      };
    },
    methods: {
        onFileChange(event) {
            this.profileImage = event.target.files[0];
        },
      async registerUser() {
        const formData = new FormData();
        formData.append('username', this.username);
        formData.append('password1', this.password1);
        formData.append('password2', this.password2);
        formData.append('email', this.email);
        formData.append('dob', this.dob);

        if (this.profileImage) {
          formData.append('profile_image', this.profileImage);
        }

        const response = await fetch('http://127.0.0.1:8000/register', {
          method: 'POST',
          body: formData
        });

        if (response.ok) {
          // Redirect to login page after successful registration
          this.$router.push('/login');
        } else {
          const responseData = await response.json();
          this.error = responseData.error || 'Registration failed';
        }

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
  