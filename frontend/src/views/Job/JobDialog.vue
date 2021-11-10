<template>
  <div>
    <el-dialog
      :title="titleMp[operate_typ]"
      :visible.sync="dialogVisible"
      width="80%">
      <el-row>
        <el-col :span="4">
          <el-form 
            :model="form" 
            :rules="rules" 
            ref="jobForm" 
            label-width="100px" 
            label-position="top">
            <el-form-item label="名称：" prop="name">
              <el-input 
                v-model="form.name"
                :disabled="operate_typ === 'show'"
              ></el-input>
            </el-form-item>
            <el-form-item label="类型：" prop="typ">
              <el-radio-group v-model="form.typ" :disabled="operate_typ === 'show'">
                <el-radio label="shell">Shell</el-radio>
                <el-radio label="python">Python</el-radio>
                <el-radio label="playbook">Playbook</el-radio>
              </el-radio-group>
            </el-form-item>     
          </el-form>
        </el-col>
        <el-col :span="20" style="padding-left: 10px">
          <Editor
            v-if="visible"
            v-bind:code.sync="form.content"
            v-bind:lang='form.typ'
            v-bind:readOnly="operate_typ === 'show'"
            @getCode="getCode"
            ></Editor>
        </el-col>
      </el-row>
      
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="submit">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
  import Editor from '../../components/Editor.vue'
  export default {
    name: 'JobDialog',
    props: ['visible', 'operate_typ', 'job_id'],
    data() {
      return {
        titleMp: {
          add: '创建作业',
          edit: '编辑作业', 
          show: '查看作业'
        },
        form: {
        },
        rules: {
          name: [
            { required: true, message: '请输入作业名称', trigger: 'blur' }
          ],
          content: [
            { required: true, message: '请输入作业内容', trigger: 'blur' }
          ],
          typ: [
            { required: true, message: '请选择作业类型', trigger: 'blur' }
          ],
        }
      }
    }, 
    computed: {
      dialogVisible: {
        get(){
          return this.visible
        },
        set(val){
          this.$emit('update:visible', val)
        }
      },
    },
    mounted(){
      if ((this.operate_typ == 'show' || this.operate_typ == 'edit' )&& this.job_id){
        this.axios.get('/api/v1/task/job/?id=' + this.job_id).then(resp => {
          let job = resp.data.data[0]
          this.form = {
            name: job.name,
            content: job.content,
            typ: job.typ,
            id: job.id,
          }
          if (this.operate_typ == 'show') {
            this.form.create_time = job.create_time
          } 
        })
      } else if (this.operate_typ == 'add') {
          this.form = {
            content: '',
            name: '',
            typ: ''
          } 
      }
    },
    methods: {
      getCode(code){
        this.form.content = code
      },
      submit(){
          this.$refs["jobForm"].validate((valid) => {
          if (valid) {
            if (this.operate_typ == 'add'){
              this.axios.post('/api/v1/task/job/', this.form).then(() => {
                this.$emit('update:visible', false)
                this.$emit('listJobs')
              })
            } else if (this.operate_typ == 'edit') {
              this.axios.put('/api/v1/task/job/', this.form).then(() => {
                this.$emit('update:visible', false)
                this.$emit('listJobs')
              })
            }
          } else {
            console.log('');
            return false;
          }
        });
      }

    },
    components: {
      Editor
    },
  }
</script>

<style>

</style>