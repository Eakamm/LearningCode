<template>
  <div id="app">
    <!-- 登录 -->
    <Login/>

    <!--  -->
    <!-- <TabBar/> -->

    <!-- Vuex -->
    <!-- <Vuex/> -->
	<!-- <a href="../public/index.html">jjjj</a> -->
  </div>
</template>

<script>
import Login from './views/Login'
import TabBar from './views/components/TabBar/TabBar'
import Vuex from './views/Vuex/Vuex'

export default {
  name: 'app',
  components: {
    // TabBar
    Login,
    Vuex
  }
}
</script>

<style>

</style>
