import Vue from 'vue'
import App from './App.vue'
import VueCodemirror from 'vue-codemirror'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faTasks, faList} from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import 'codemirror/lib/codemirror.css'

library.add(faTasks)
library.add(faList)


Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.use(VueCodemirror, /* {
    options: { theme: 'base16-dark', ... },
    events: ['scroll', ...]
  } */)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
