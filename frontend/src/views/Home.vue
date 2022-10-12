<template>
 <main>
    <router-link to="/login">Login</router-link>
    <router-link to="/register">Register</router-link>
 </main>
</template>

<script>
</script>

<style scoped>
main{
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
a{
    color: white;
    text-decoration: none;
    font-size: 2em;
    font-weight: bold;
    margin: 10px;
}
a:hover{
    color: gray;
}
</style>