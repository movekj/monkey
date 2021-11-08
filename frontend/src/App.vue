<template>
  <div id="app" style="height: 100%">
    <router-view></router-view>
  </div>
</template>

<script>

import Vue from 'vue';
import ElementUI from 'element-ui';
import router from './router' 


import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI);


export default {
  name: 'App',
  router,
  components: {
  }
}
</script>

<style>
html, body {
  margin: 0;
  padding: 0;
  height: 100%;
}
#app {
  height: 100%;
}

</style>
