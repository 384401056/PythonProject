import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import MainPage from '@/components/MainPage'
import MonitorCenter from '@/components/mainpage/MonitorCenter'
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
        //name:'mainPage', //由于此路由设置了默认路由，所以不能再设置name属性，否则会有告警。
        component: MainPage,
        children:[
            {
                name:'monitorcenter',
                path: '', //此外设置为空，就是上层路由的默认路由。
                component: MonitorCenter
            },
            {
              name:'hostinfopage',
              path: 'hostinfopage/:group_id',
              component: HostInfoPage
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
