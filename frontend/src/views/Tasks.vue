<template>
<main>
  <div id="navbar"><h2 id="logOut" @click="logOut">Log Out</h2><h1>Tasks</h1><h2 v-if="user">{{user.username}}</h2></div>
    <div id="content">
      <input type="text" placeholder="New Task" id="newTask" v-model="title" @keyup.enter="submit">
      <input type="text" placeholder="Description" id="newDesc" v-model="description" @keyup.enter="submit">
      <div id="task" v-for="item in contentContainer" :key="item">
        <div id="taskWrapper">
          <input type="checkbox" id="checkbox" @click="performUpdate(item.pk,item.done)" v-model="item.done">
          <a href="">{{item.title}}</a>
          <a href="">·</a>
          <p href="">{{item.description}}</p>
          <button id="taskButton" @click="performDelete(item.pk,item)">Delete</button>
        </div>
      </div>
    </div>
</main>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ref, shallowRef } from 'vue'

const router = useRouter()
const contentContainer = ref()
const title = shallowRef('')
const description = shallowRef('')
const done = shallowRef()
const doneTasks = ref([])
const user = ref()


const submit = () => {
  contentContainer.value.push(({title: title.value, description: description.value, done: done.value}))
    fetch('http://127.0.0.1:8000/api/tasks/', {
      method: 'POST',
      headers:{
        'Content-Type': 'application/json',
        "Authorization": `Bearer ${localStorage.getItem('access')}`
      },
      body: JSON.stringify({title: title.value, description: description.value, done: done.value})
      
    })
    .then((response)=>
     response.json())
  }

  const performDelete = (pk,item) => {
    fetch('http://127.0.0.1:8000/api/tasks/'+pk+'/destroy/', {
      method: 'DELETE',
      headers:{
        'Content-Type': 'application/json',
        "Authorization": `Bearer ${localStorage.getItem('access')}`
      }
    })
    .then((response)=>
     response.json())
      contentContainer.value.splice(contentContainer.value.indexOf(item),1)
  }

  const performUpdate = (pk, isDone) => {
    fetch('http://127.0.0.1:8000/api/tasks/'+pk+'/update/', {
      method: 'PUT',
      headers:{
        'Content-Type': 'application/json',
        "Authorization": `Bearer ${localStorage.getItem('access')}`
      },
      body: JSON.stringify({done: !isDone})
    })
    .then((response)=>
     response.json())
  }

  function getFetchOptions(method, body){
      return {
          method: method === null ? "GET" : method,
          headers: {
              "Content-Type": "application/json",
              "Authorization": `Bearer ${localStorage.getItem('access')}`
          },
          body: body ? body : null
      }
  }
  
  const getProductList = (method, body) => {
    fetch('http://127.0.0.1:8000/api/tasks/', {
      method: method === null ? "GET" : method,
          headers: {
              "Content-Type": "application/json",
              "Authorization": `Bearer ${localStorage.getItem('access')}`
          },
          body: body ? body : null
    })
    .then(response=>response.json())
    .then(data=> {
      contentContainer.value = data
      console.log(contentContainer.value)
      if(contentContainer.value.code === 'token_not_valid'){
  router.push('/login')

}
    })
  }

const logOut = () => {
  localStorage.clear()
  router.push('/login')
}

const getUserData = () => {
  fetch('http://127.0.0.1:8000/api/users/user/', {
      method: 'GET',
          headers: {
              "Content-Type": "application/json",
              "Authorization": `Bearer ${localStorage.getItem('access')}`
          }   
    })
    .then(response=>response.json())
    .then(data=> {
      user.value = data
    })
}

getProductList()
getUserData()
</script>

<style scoped>
#navbar{
  margin: auto;
  width: 95%;
  height: 20px;
  margin-top: 5px;
  border-radius: 20px;
  background: #0077B6;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
}
#navbar h1{
  margin: 0;
  position: absolute;
  left: 50%;
  font-weight: bold;
  font-size: 1.4em;
  color: #CAF0F8;
}
#navbar h2{
  margin: 0;
  margin-right: 20px;
  margin-left: 20px;
  font-weight: bold;
  font-size: 1em;
  color: white;
}
#content{
  width: 800px;
  margin: auto;
  display: flex;
  flex-direction: column;
}
#task{
  width: 800px;
  height: 20px;
  background: #00B4D8;
  margin: auto;
  margin: 10px;
  padding: 20px;
  border-radius: 20px;
  font-weight: bold;
  display: flex;
  align-items: center;
}
#newTask{
  width: 800px;
  height: 20px;
  background: white;
  margin: auto;
  margin: 10px;
  margin-bottom: 50px;
  padding: 20px;
  border-radius: 20px;
  border: none;
  color: #00B4D8;
  z-index: 2;
}
input:focus{
    outline: none;
}
::placeholder{
  color: #00B4D8;
}
#newTask:focus{
  outline: none;
}
#task a{
  color: #CAF0F8;
  text-decoration: none;
  margin-right: 5px;
}
#task p{
  color: #CAF0F8;
  font-weight: 400;
}
#taskWrapper{
  display: flex;
  align-items: center;
  width: 100%;
  height: 100%;
  position: relative;
}
#checkbox{
  margin-right: 10px;
  width: 25px;
  height: 25px;
  cursor: pointer;
}
#logOut{
  cursor: pointer;
}
#taskButton{
  right: 0;
  position: absolute;
  padding: 5px;
  width: 100px;
  border-radius: 10px;
  border: none;
  background: #CAF0F8;
  font-weight: bold;
  color: #00B4D8;
}
#taskButton:hover{
  background: #00B4D8;
  color: #CAF0F8;
  cursor: pointer;
}
#newDesc{
  width: 800px;
  height: 20px;
  background: white;
  margin: auto;
  margin: 10px;
  padding: 20px;
  border-radius: 20px;
  border: none;
  color: #00B4D8;
  position: absolute;
  z-index: 1;
}
#newTask:focus + #newDesc{
  margin-top: 60px;
  transition: 0.5s;
}
#newTask:hover + #newDesc{
  margin-top: 60px;
  transition: 0.5s;
}
#newDesc:hover{
  margin-top: 60px;
}
#newDesc:focus{
  margin-top: 60px;
}
</style>