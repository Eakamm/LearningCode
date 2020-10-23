import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)


const constantRoutes = [
  {
    path:"/login",
    name:"登录",
    meta:{
      title: "登录"
    },
    component: (resolve) => require(['@/views/Login'], resolve)
  },
  {
    path:"/register",
    name:"注册",
    meta:{
      title: "注册"
    },
    component: (resolve) => require(['@/views/register/register'], resolve)
  },
  {
    path:"/register2",
    name:"注册2",
    meta:{
      title: "注册2"
    },
    component: (resolve) => require(['@/views/register/register2'], resolve)
  },
  {
    path:"/home",
    meta:{
      title: "首页"
    },
    component: (resolve) => require(['@/views/Home/Home'], resolve)
  },
  {
    path:"/ca",
    meta:{
      title: "分类"
    },
    component: (resolve) => require(['@/views/Home/Home'], resolve)
  },
  {
    path:"/cart",
    meta:{
      title: "购物车"
    },
    component: (resolve) => require(['@/views/Home/Home'], resolve)
  },
  {
    path:"/profile",
    meta:{
      title: "我的"
    },
    component: (resolve) => require(['@/views/Home/Home'], resolve)
  }

]

const router = new VueRouter({
  mode: 'history', // 去掉url中的#
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

router.beforeEach((to,from,next) => {
  document.title = to.meta.title
  console.log(to)
  next()
})

export default router
