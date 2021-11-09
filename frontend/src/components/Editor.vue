<template>
  <codemirror
    ref="cmEditor"
    :value="code"
    :options="cmOptions"
    @input="onCmCodeChange"
    style="height: 100%"
  />
</template>

<script>
import 'codemirror/mode/javascript/javascript.js'
import 'codemirror/mode/shell/shell.js'
import 'codemirror/mode/python/python.js'
import 'codemirror/mode/yaml/yaml.js'
import 'codemirror/theme/base16-dark.css'


export default {
  props: ['lang'],
  name: 'Editor',
  data () {
    return {
      code: 'const a = 10',
      cmOptions: {
        tabSize: 4,
        mode: this.editorMode,
        theme: 'base16-dark',
        lineNumbers: true,
        line: true,
      },
      langModeMp: {
        'ansible-playbook': 'text/x-yaml',
        'python': 'text/x-cython',
        'shell': 'text/x-sh'
      }
    }
  },
  watch: {
    lang(newVal) {
      this.setLangMode(this.langModeMp[newVal])
      console.log(newVal)
    },
  },
  mounted(){
    if (this.lang){
      this.setLangMode(this.langModeMp[this.lang])

    } else {
      this.setLangMode(this.langModeMp.shell)
    }
  },
  methods: {
    onCmCodeChange(newCode) {
      this.$emit('getCode', this.code)
      this.code = newCode
    },

    setLangMode(mode) {
      console.log('before mode', this.$refs.cmEditor.codemirror, mode)
      this.$refs.cmEditor.codemirror.setOption('mode', mode)
      console.log('after mode', this.$refs.cmEditor.codemirror, mode)
    }

  },
}
</script>