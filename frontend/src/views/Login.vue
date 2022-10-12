<template>
    <div class="content">
      <form action="post">
        <input type="text" name="username" placeholder="Username" v-model="username">
        <input type="password" name="password" placeholder="Password" v-model="password" @keyup.enter="submit">
      </form>
      <button v-on:click.prevent="submit()">Login</button>
      <p>Don't have an account?</p><router-link to="/register"><p id="register">Register !</p></router-link>
    </div>
  </template>

  <script setup>
import { useRouter } from 'vue-router'
  import {ref} from 'vue'
  const username = ref('')
  const password = ref('')
  const contentContainer = ref()
  const router = useRouter()

  const submit = () => {
    fetch('http://127.0.0.1:8000/api/token/', {
      method: 'POST',
      headers:{
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({username: username.value,email:'', password: password.value})
      
    })
    .then((response)=>
     response.json())
  
    .then(authData=> {
      handleAuthData(authData)
    })
  }
  function handleAuthData(authData, callback) {
    localStorage.setItem('access', authData.access)
    localStorage.setItem('refresh', authData.refresh)
    if(callback) {
      callback()
    }
      if(authData.access!='' || authData.access != undefined){
        router.push('/tasks')
      }
  }
  </script>
<style scoped>
.content{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin: auto;
    margin-top: 150px;
    background: #0077B6;
    width: 700px;
    height: 300px;
    border-radius: 40px;
    padding: 100px;
}
form{
    display: flex;
    flex-direction: column;
}
input{
    margin: 10px;
    width: 400px;
    height: 20px;
    padding: 20px;
    border-radius: 40px;
    border: none;
    font-weight: bold;
    color: #0077B6;
}
button{
    margin-top: 10px;
    width: 150px;
    height: 40px;
    border-radius: 40px;
    border: none;
    cursor: pointer;
    font-weight: bold;
    color: #0077B6;
    background: #CAF0F8;
    margin-bottom: 10px;
}
::placeholder{
    color: #0077B6;
}
input::-moz-focus-inner{
    border: none;
}
button:hover{
    background: #03045E;
}
p{
  color: #CAF0F8;
  margin: 2px;
}
#register{
  color: #03045E;
}
#register:hover{
  color: #CAF0F8;
  cursor: pointer;
}
a{
  text-decoration: none;
  font-size: 1em;
  height: 10px;
  color: white;
  margin-bottom: 5px;
}
</style>