<template>
<el-container style="height: 100%">
  <el-header>
    <span class="logo">
      monkey作业管理平台
    </span>
  </el-header>
  <el-container style="height: 100%">
    <el-aside width="200px" style="height: 100%" >
      <el-menu
        class="el-menu-vertical-demo"
        background-color="#fafafa"
        router
        style="height: 100%"
        default-active='/task'>
        <el-menu-item index="/job">
          <i class="el-icon-menu"></i>
          <span slot="title">作业管理</span>
        </el-menu-item>
        <el-submenu index="sub-0" style="margin-left: 5px">
          <template slot="title">
            <font-awesome-icon :icon="['fas', 'tasks']" style="font-size: 16px; font-weight: 500;; color: #909399" />
            <span style="margin-left: 10px">任务</span>
          </template>
          <el-menu-item index="/task">
            <span slot="title">任务列表</span>
          </el-menu-item>
          <el-menu-item index="/task/template">
            <span slot="title">任务模版</span>
          </el-menu-item>
        </el-submenu>
      </el-menu>
    </el-aside>
    <el-main style="height: 100%">
      <router-view></router-view>
    </el-main>
  </el-container>
</el-container>
</template>

<script>
export default {
  name: 'Layout',
}
</script>

<style scoped>
  .logo {

    display: inline-block;
    margin-top: 16px;
    font-size: 18px;
    font-weight: 600;

  }
  .el-header {

    background-color: #292961;
    color: #d1d1f0;

  }
  
  .el-aside {

    background-color: #fafafa;
    color: #717171;
    height: 100%;

  }

  .el-container {
    height: 100%;
  }
  
  .el-main {
    background-color: #ffffff;
    color: #333;

  }
  
</style>
