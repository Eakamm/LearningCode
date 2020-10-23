<template>
    <div>
      <el-divider>state</el-divider>
      {{this.$store.state.num}}

      <el-divider>Mutation</el-divider>
      <el-button @click="increment">+</el-button>
      <el-button @click="reduce">-2</el-button>

      <el-divider>Getters无参</el-divider>
      <li v-for="value in profiles" :key="value.name">
        {{value.name}}
      </li>

      <el-divider>Getters有参</el-divider>
      <el-input v-model="age" placeholder="请输入年龄"></el-input>
      <li v-for="(item, index) in profiles">
        {{item.name}}
      </li>

    </div>
</template>

<script>
export default {
    props: {

    },
    data() {
      return {
        age: 0
      };
    },
    computed: {
      profiles(){
        // 无参
        // return this.$store.getters.filterProfile
        // 有参
        return this.$store.getters.filterProfileWithAge(this.age)
      }
    },
    created() {

    },
    mounted() {

    },
    watch: {

    },
    methods: {
      increment(){
        this.$store.commit('increment')
      },
      reduce(){
        //无参
        // this.$store.commit('reduce')
        // 传入单个参数
        // this.$store.commit('reduce', 2)
        // 传入对象
        // this.$store.commit('reduce', {
        //   num: 2
        // })
        // 对象风格提交
        this.$store.commit({
          type:"reduce",
          num: 2
        })
      }
    },
    components: {

    },
}
</script>

<style>

</style>
