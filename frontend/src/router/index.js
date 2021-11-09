import Vue from 'vue'
import Router from 'vue-router'
import layout from '../layout'
import Job from '../views/Job'
import Task from '../views/Task'
import TaskTemplate from '../views/TaskTemplate'

Vue.use(Router)

export default new Router({
    mode: 'history', 
    routes: [
        {
            path: '/',
            component: layout,
            children: [
                {
                    path: 'job',
                    component: Job
                },
                {
                    path: 'task',
                    component: Task
                },
                {
                    path: 'task/template',
                    component: TaskTemplate
                },
            ]           
        }
    ]
})