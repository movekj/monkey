<template>
  <div>
    <el-card>
      <div slot="header" class="clearfix">
        <span>作业列表</span>
        <el-button 
          style="float: right; padding: 3px 0" 
          type="text" 
          @click="addJob"
        >添加作业</el-button>
      </div>
      <el-table
        :data="jobList"
        style="width: 100%">
        <el-table-column
          prop="name"
          label="名称">
        </el-table-column>
        <el-table-column
          prop="typ"
          label="类型">
        </el-table-column>
        <el-table-column
          prop="create_time"
          label="创建时间">
        </el-table-column>
        <el-table-column
          prop="status"
          label="状态">
        </el-table-column>
        <el-table-column
          label="操作">
          <template slot-scope="scope">
            <el-button @click="showJobDetail(scope.row)" type="text">查看</el-button>
            <el-button @click="editJob(scope.row)" type="text">编辑</el-button>
            <el-button type="text">历史</el-button>
            <el-button type="text">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
    <jobDialog 
      @listJobs="listJobs" 
      v-if="jobAddVisible"
      v-bind:operate_typ='operate_typ'
      v-bind:job_id='job_id'
      v-bind:visible.sync="jobAddVisible"></jobDialog>
  </div>
</template>
<script>
import JobDialog from './JobDialog'

export default {
  name: 'Job',
  data() {
    return {
      jobList: [],
      operate_typ: '',
      jobAddVisible: false,
      job_id: ''
    }
  },
  mounted(){

    this.listJobs()
  },
  methods: {
    listJobs(){
      this.axios.get('/api/v1/task/job/').then(resp => {
        this.jobList = resp.data.data
      })
    },
    addJob(){
      this.operate_typ = 'add'
      this.jobAddVisible = true
    },
    editJob(row){
      this.operate_typ = 'edit'
      this.job_id = row.id
      this.jobAddVisible  = true
    },
    showJobDetail(row){
      this.operate_typ = 'show'
      this.job_id = row.id
      this.jobAddVisible = true
    }
  },
  components: {
    JobDialog
  }
}
</script>

<style>

</style>