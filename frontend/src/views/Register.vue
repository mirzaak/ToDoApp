<template>
    <div>
      <form action="post">
        <input type="text" name="username" placeholder="Your Username" v-model="username">
        <a>{{usernameCheck}}</a>
        <input type="password" name="password" placeholder="Your Password" v-model="password" @keyup.enter="submit">
        <a>{{passwordCheck}}</a>
      </form>
      <button v-on:click.prevent="submit()">Register</button>
      <p>Already have an account?</p><router-link to="/login"><p id="login">Login!</p></router-link>
    </div>
</template>


<script setup>
import { useRouter} from 'vue-router'
import { ref } from 'vue'

const router = useRouter()
const username = ref('')
const password = ref('')

const usernameCheck = ref('')
const passwordCheck = ref('')

const submit = () => {
    fetch('http://127.0.0.1:8000/api/users/register/',{
      method: 'POST',
      headers:{
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({username: username.value,email:'', password: password.value})
      
    })
    .then((response)=> response.json())
    .then((data)=> {
      if(data.username){
        usernameCheck.value = data.username[0]
      }
      if(data.password){
        passwordCheck.value = data.password[0]
      }
      if(data.hasOwnProperty('user')){
       router.push('/login')
      }
    })
  }
</script>

<style scoped>
div{
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
    align-items: center;
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
    margin-bottom: 20px;
}
::placeholder{
    color: #0077B6;
}
button:hover{
    background: #03045E;
}
p{
  color: #CAF0F8;
  margin: 2px;
}
#login{
  color: #03045E;
}
a{
  text-decoration: none;
  font-size: 1em;
  height: 10px;
  color: white;
  margin-bottom: 5px;
}
#login:hover{
  color: #CAF0F8;
  cursor: pointer;
}

</style>