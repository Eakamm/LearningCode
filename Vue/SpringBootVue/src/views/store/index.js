import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state:{
    num: 1,
    profiles:[
      {
          name: "zhangsan",
          age: 12
      },
      {
          name: "lisi",
          age: 22
      },
      {
          name: "wangwu",
          age: 8
      }
    ]
  },
  getters:{
    filterProfile: state => {
      return state.profiles.filter(profile => profile.age >= 10)
    },
    // 传入参数
    filterProfileWithAge: state => age => {
      return state.profiles.filter(profile => profile.age >= age)
    }
  },
  mutations:{
    increment(state){
      state.num++
    },
    // 提交一个对象，payload(载荷)
    reduce(state, payload){
      state.num -= payload.num
    }
  }
})

export default store
