<template>
  <div>
    <el-dialog
      title="创建作业"
      :visible.sync="dialogVisible"
   
      width="80%">
      <el-row>
        <el-col :span="4">
          <el-form 
            :model="form" 
            :rules="rules" 
            ref="createJobForm" 
            label-width="100px" 
            label-position="top">
            <el-form-item label="名称：" prop="form.name">
              <el-input v-model="form.name" ></el-input>
            </el-form-item>
            <el-form-item label="类型：" prop="form.typ">
              <el-radio-group v-model="form.typ">
                <el-radio label="shell">shell</el-radio>
                <el-radio label="python">python</el-radio>
                <el-radio label="playbook">playbook</el-radio>
              </el-radio-group>
            </el-form-item>     
          </el-form>
        </el-col>
        <el-col :span="20" style="padding-left: 10px">
          <Editor 
            v-bind:code.sync="form.code"
            v-bind:lang='form.typ'
            @getCode="getCode"
            ></Editor>
        </el-col>
      </el-row>
      

      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
  import Editor from '../../components/Editor.vue'
  export default {
    name: 'jobAddDialog',
    props: ['visible'],

    data() {
      return {
        form: {
          content: '',
          name: '', 
          typ: 'shell',
        },
        rules: {}
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
      }
    },
    methods: {
      getCode(code){
        this.form.content = code
      },

    },
    components: {
      Editor
    },
  }
</script>

<style>

</style>