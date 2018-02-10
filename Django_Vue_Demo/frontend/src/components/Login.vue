<template>
  <div id="border">
    <el-container>
      <el-container>
        <el-header>
          
        </el-header>
        <el-main>

        </el-main>

        <el-footer>

        </el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<script>
  
  export default{
    name:'login',
    data(){
      return{

      }
    },
  }

</script>



<style>
  .el-header, .el-footer {
    background-color: #FF8C00;
    color: #333;
    text-align: center;
    line-height: 60px;
  }
  
  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 100%;
  }
  
  body > .el-container {
    margin-bottom: 10px;
  }
  
  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 100%;
  }
  
  .el-container:nth-child(7) .el-aside {
    line-height: 100%;
  }
</style>