import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import MainPage from '@/components/MainPage'
import MonitorCenter from '@/components/mainpage/MonitorCenter'
import Content2 from '@/components/mainpage/Content2'
import HostInfoPage from '@/components/mainpage/HostInfoPage'

Vue.use(Router)

export default new Router({
  routes: [
    {
    	path:'/',
    	name:'login',
    	component: Login,
    },
    {
        path:'/mainPage',
        name:'mainPage',
        component: MainPage,
        children:[
            {
                name:'monitorcenter',
                path: 'monitorcenter',
                component: MonitorCenter
            },
            {
              name:'hostinfopage',
              path: 'hostinfopage',
              component: HostInfoPage
            },
            {
                name:'content2',
                path: 'content2',
                component: Content2
            },

          ]
    },
    {
        //其它路由，重定向
        path: '*',
        redirect: '/'
    }
  ]
})
