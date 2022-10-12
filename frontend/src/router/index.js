import { createRouter, createWebHistory } from 'vue-router'
import Register from '../views/Register.vue'
import Login from '../views/Login.vue'
import Tasks from '../views/Tasks.vue'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/tasks',
    name: 'Tasks',
    component: Tasks
  },
  {
    path: '/',
    name: 'Home',
    component: Home
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// router.beforeEach(async (to, from) => {
//   if (
//     // make sure the user is authenticated
//     localStorage.getItem('access') !== undefined &&
//     // ❗️ Avoid an infinite redirect
//     to.name !== 'Login'
//     &&
//     to.name == 'Tasks'
    
//   ) {
//     // redirect the user to the login page
//     return { name: 'Login' }
//   }
// })

export default router
