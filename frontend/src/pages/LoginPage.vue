  <template>
    <div class="login-container">
      <h2>Login Page</h2>
      <form @submit.prevent="loginUser">
        <input v-model="username" type="text" placeholder="Username" />
        <input v-model="password" type="password" placeholder="Password" />
        <input type="submit" value="Login">
      </form>
      <p v-if="error" class="error">{{ error }}</p>
      <p class="register-link">
      Don't have an account? <router-link to="/register">Register here</router-link>
    </p>
    </div>
  </template>
  
  <script>
  export default {
    name: 'LoginPage',
    data() {
      return {
        username: '',
        password: '',
        error: null
      };
    },
    methods: {
      getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
          const cookies = document.cookie.split(';');
          for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
            }
          }
        }
        return cookieValue;
      },
      async loginUser() {
        const csrfToken = this.getCookie('csrftoken');
        try {
          const response = await fetch('http://localhost:8000/api/login', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({
              username: this.username,
              password: this.password
            })
          });
  
          if (!response.ok) {
            throw new Error('Login failed');
          }

          if (response.ok) {
            this.$router.push('/main-page');
          }

 
  
        } catch (error) {
          this.error = error.message;
        }
      }
    }
  };
  </script>
  
  <style scoped>
      .login-container {
    text-align: center;
    margin-top: 0;
    font-size: 24px;
    padding: 20px;
    background-color: white;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }

  input[type="text"],
  input[type="password"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
  }

  input[type="submit"] {
    background-color: #4CAF50; /* Green background */
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-top: 10px;
  }

  input[type="submit"]:hover {
    background-color: #45a049; /* Darker green */
  }

  .error {
    color: red;
  }

  .register-link {
    margin-top: 20px;
  }

  .register-link a {
    color: #007bff;
    text-decoration: none;
  }

  .register-link a:hover {
    text-decoration: underline;
  }
  </style>
  
  