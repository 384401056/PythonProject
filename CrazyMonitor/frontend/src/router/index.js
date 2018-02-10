import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import MainPage from '@/components/MainPage'

Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'HelloWorld',
    //   component: HelloWorld
    // }
    {
    	path:'/',
    	name:'login',
    	component: Login,
    },
    {
        path:'/mainPage',
        name:'mainPage',
        component: MainPage
    }
  ]
})
