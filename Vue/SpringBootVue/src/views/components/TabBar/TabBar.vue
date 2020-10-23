<template>
    <div id="tabBar">
      <el-container>
        <!-- 头部导航 -->
        <el-header>
          XXXXXXXXXXXX
        </el-header>
        <!-- 主体 -->
        <el-main>
          <router-view></router-view>
        </el-main>

        <!-- 底部选择栏 -->
        <el-footer height = "80px">
          <el-row type="flex" class="tab-bar">
            <el-col>
              <tab-bar-style title="首页" iconName="el-icon-user-solid" path="/home"/>
            </el-col>
            <el-col>
              <tab-bar-style title="首页" iconName="el-icon-user-solid" path="/ca"/>
            </el-col>
            <el-col >
               <tab-bar-style title="首页" iconName="el-icon-user-solid" path="/cart"/>
            </el-col>
            <el-col>
               <tab-bar-style title="首页" iconName="el-icon-user-solid" path="/profile"/>
            </el-col>
          </el-row>
        </el-footer>
      </el-container>
    </div>
</template>

<script>
import TabBarStyle from './TabBarStyle';

export default {
    props: {

    },
    data() {
        return {

        };
    },
    computed: {

    },
    created() {

    },
    mounted() {

    },
    watch: {

    },
    methods: {

    },
    components: {
      TabBarStyle
    },
}
</script>

<style>

  .el-container{
    position:absolute;
    top:0;
    right:0;
    bottom:0;
    left:0;
  }
</style>
