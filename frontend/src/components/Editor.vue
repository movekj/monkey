<template>
  <codemirror
    ref="cmEditor"
    :value="value"
    :options="cmOptions"
    @input="onCmCodeChange"
    @ready="onCmReady"
    style="height: 100%"
  />
</template>

<script>
import 'codemirror/lib/codemirror.js'
import 'codemirror/theme/idea.css'
import 'codemirror/mode/shell/shell.js'
import 'codemirror/mode/python/python.js'
import 'codemirror/mode/yaml/yaml.js'
import 'codemirror/addon/comment/comment.js'
import 'codemirror/addon/hint/show-hint.css'
import 'codemirror/addon/hint/show-hint.js'
import 'codemirror/addon/hint/anyword-hint.js'
import 'codemirror/addon/edit/closebrackets.js'
import 'codemirror/addon/edit/matchbrackets.js'
import 'codemirror/addon/comment/comment.js'
import 'codemirror/addon/fold/foldgutter.css'
import 'codemirror/addon/fold/foldcode.js'
import 'codemirror/addon/fold/foldgutter.js'
import 'codemirror/addon/fold/brace-fold.js'
import 'codemirror/addon/fold/indent-fold.js'
import 'codemirror/addon/fold/comment-fold.js'
import 'codemirror/addon/display/placeholder'
import 'codemirror/addon/selection/active-line.js'


export default {
  props: ['lang', 'readOnly', 'code'],
  name: 'Editor',
  data () {
    return {
      value: '',
      cmOptions: {
        tabSize: 4,
        mode: this.editorMode,
        theme: 'idea',
        smartIndent: true,
        lineNumbers: true,
        styleActiveLine: true,
        indentUnit: 4,
        indentWithSpaces: true,
        lineWrapping: true, 
        readOnly: this.readOnly,
        line: true,
        gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter", "CodeMirror-lint-markers"], 
        foldGutter: true,
        autofocus: true,
        matchBrackets: true, 
        autoCloseBrackets: true,
        extraKeys: { Tab(cm) {
          if (cm.somethingSelected()) {
            cm.indentSelection("add");
            } else {
              cm.replaceSelection(cm.getOption("indentWithTabs")? "\t":
                Array(cm.getOption("indentUnit") + 1).join(" "), "end", "+input");
            }
          } 
        }
      },
      langMp: {
        mode: {
          'playbook': 'text/x-yaml',
          'python': 'text/x-cython',
          'shell': 'text/x-sh'
        }, 
        placeholder: {
          'playbook': '# ansible playbook\n',
          'python': '#!/usr/bin/python\n',
          'shell': '#!/bin/sh\n'
        }

      }, 

    }
  },
  watch: {
    lang(newVal) {
      this.setOption('mode', this.langMp.mode[newVal])
      this.value = this.langMp.placeholder[newVal]
    },
    code(newVal){
      this.value = newVal
    }
  },
  mounted(){
  
    if (this.lang.length > 0){
      this.setOption('mode', this.langMp.mode[this.lang])
      if (this.code.length == 0){
        this.value = this.langMp.placeholder[this.lang]
      }

    } else {
      this.setOption('mode', this.langMp.mode.shell)
      if (this.code.length == 0){
        this.value = this.langMp.placeholder[this.langMp.mode.shell]
      }

    }

  },
  methods: {
    onCmCodeChange(newCode) {
      this.$emit('getCode', this.value)
      this.value = newCode
    },
    onCmReady(cm) {
      cm.on('keypress', () => {
        cm.showHint({completeSingle:false})
      })
    },
    setOption(key, value) {
      this.$refs.cmEditor.codemirror.setOption(key, value)
    }

  },
}
</script>