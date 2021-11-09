<template>
  <div>
    <el-card>
      <div slot="header" class="clearfix">
        <span>卡片名称</span>
        <el-button 
          style="float: right; padding: 3px 0" 
          type="text" 
          @click="jobAddVisible=true"
        >添加作业</el-button>
      </div>
      <el-table
        :data="tableData"
        style="width: 100%">
        <el-table-column
          prop="date"
          label="日期"
          width="180">
        </el-table-column>
        <el-table-column
          prop="name"
          label="姓名"
          width="180">
        </el-table-column>
        <el-table-column
          prop="address"
          label="地址">
        </el-table-column>
      </el-table>
    </el-card>
    <jobAddDialog v-bind:visible.sync="jobAddVisible"></jobAddDialog>
  </div>
</template>
<script>
import jobAddDialog from './jobAddDialog'

export default {
  name: 'Job',
  data() {
    return {
      jobAddVisible: false,
      tableData: [{
        date: '2016-05-02',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1517 弄'
      }, {
        date: '2016-05-01',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1519 弄'
      }, {
        date: '2016-05-03',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }]
    }
  },
  components: {
    jobAddDialog
  }

}
</script>

<style>

</style>