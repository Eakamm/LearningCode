<template>
    <div id="style"  @click="jump('dd')">
      <el-row :style="isColor">
        <el-col :span="14" :offset="5">
          <tab-bar-button v-slot:img>
            <i :class="iconName" style="font-size:40px"></i>
          </tab-bar-button>
        </el-col>

        <el-col :span="16" :offset="4">
          <tab-bar-button v-slot:text>
            <span style="font-size:22px">
              {{title}}
            </span>

          </tab-bar-button>
        </el-col>
      </el-row>
    </div>
</template>

<script>

import TabBarButton from "./TabBarButton"
export default {
    props: {
      title:{
         type: String,
         default: ""
      },
      iconName:{
        type: String,
        default: "el-icon-s-grid"
      },
      path:{
        type:String,
        default: "/"
      }
    },
    data() {
        return {
          color: "#409EFF"
        };
    },
    computed: {
      isActivity(){
        // console.log(this.$route.path)

        return this.$route.path == this.path
      },
      isColor(){
        return this.isActivity? {color: this.color} : {}
      }
    },
    created() {

    },
    mounted() {

    },
    watch: {

    },
    methods: {
       jump(d){
        console.log(d)
        this.$router.push(this.path)
      }
    },
    components: {
      TabBarButton
    },
}
</script>

<style >

</style>
