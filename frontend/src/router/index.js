import Vue from 'vue'
import Router from 'vue-router'
import layout from '../layout'

Vue.use(Router)
export default new Router({
    mode: 'history', 
    routes: [
        {
            path: '/',
            component: layout
        }
    ]
})