// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Router from './router'
import axios from 'axios'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import VChart from 'v-charts'

Vue.use(ElementUI);
Vue.use(VChart);
Vue.productionTip = false;
//直接在Vue的属性中加入axios,然后就可以全局使用Vue.$http来调用。$http的名字是自定义的。
Vue.prototype.$http = axios;
// Vue.prototype.$serverip = 'http://10.88.20.110:8000';
Vue.prototype.$serverip = 'http://localhost:8000';

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router:Router,
  components: { App },
  template: '<App/>'
});


