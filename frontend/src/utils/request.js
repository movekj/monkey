import axios from 'axios'
import ElementUI from 'element-ui';

const restApi = axios.create({
    baseURL: process.env.VUE_APP_BASE_API, 
    timeout: 10000
  })

restApi.interceptors.response.use(function (response) {
    return response;
}, function (error) {
    if (401 === error.response.status){
        ElementUI.Message({
            type: 'error',
            message: 'Unauthorized: ' + error.response.data.msg
        })
    }
    else  if (403 === error.response.status){
        ElementUI.Message({
            type: 'error',
            message: 'Forbidden: ' +  error.response.data.msg
        })
    }
    else  if (404 === error.response.status){
        ElementUI.Message({
            type: 'error',
            message: 'NotFound: ' +  error.response.data.msg
        })
    } else if (400 === error.response.status) {
        let errors = ''
        for (let key in error.response.data.errors){
            errors = errors + '{' + 'key: ' + key + ', ' + 'msg: ' + error.response.data.errors[key] + '}'
        }
        errors = 'BadRequest: ' + errors
        console.log(error.response.data.errors)
        ElementUI.Message({
            type: 'error',
            message: errors
        })
    } else if (String(error.response.status).startsWith('50')){
        ElementUI.Message({
            type: 'error',
            message: 'ServerError: ' + 'status_code: ' + error.response.status
        })
    } else {
        ElementUI.Message({
            type: 'error',
            message: 'UnknownError: 请联系系统管理员'
        })  
    }

    return Promise.reject(error);
});

export default restApi