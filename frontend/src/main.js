import Vue from 'vue'
import App from './App.vue'
import router from './router' 
import VueAxios from 'vue-axios'
import ElementUI from 'element-ui';
import RestApi from './utils/request'
import VueCodemirror from 'vue-codemirror'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faTasks, faList } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import 'codemirror/lib/codemirror.css'
import 'element-ui/lib/theme-chalk/index.css';


library.add(faTasks)
library.add(faList)


Vue.use(ElementUI);
Vue.use(VueCodemirror)
Vue.use(VueAxios, RestApi)
Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false



new Vue({
    router,
    render: h => h(App),
}).$mount('#app')
