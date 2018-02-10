<template>
	<div id="mainPage">
		<el-container>
		  <el-header height="80px">
      </el-header>
      <el-container>
        <el-aside width="200px">
          <NavManu></NavManu>
        </el-aside>
		    <el-main>
           <router-view/>
        </el-main>
		  </el-container>
		</el-container>
	</div>
</template>

<script>
  import NavManu from '../components/mainpage/NavMenu'
  import Content from '../components/mainpage/Content'

  export default{

    name:'mainPahe',
    data(){
      return {

      }
    },

    components:{
        'NavManu':NavManu,
        'Content':Content
    },


  }  

</script>


<style scoped>
  .el-header, .el-footer {
    background-color: #FFA340;
    color: #333;
    text-align: center;
  }
  
  .el-aside {
    background-color: transparent;
    color: #333;
    text-align: center;
  }
  
  .el-main {
    background-color: transparent;
    color: #333;
    text-align: center;
  }
  
  body > .el-container {
    margin-bottom: 40px;
  }
  
  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }
  
  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
</style>