import Vue from 'vue'
import Router from 'vue-router'
import Callback from '../components/Callback'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/callback',
      name: 'callback',
      component: Callback
    }
  ]
})
