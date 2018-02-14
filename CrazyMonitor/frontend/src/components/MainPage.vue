<template>
	<div id="mainPage">
		<el-container>
		  <el-header height="80px" style="margin:0px">
      </el-header>
      <el-container>

        <el-aside width="200px">
          <el-menu :default-active="activeIndex" class="el-menu-demo" mode="vertical" @select="handleSelect">
            <el-menu-item index="1">监控中心</el-menu-item>
            <el-menu-item index="2">订单管理</el-menu-item>
          </el-menu>
        </el-aside>

		    <el-main>
           <router-view/>
        </el-main>

		  </el-container>
		</el-container>
	</div>
</template>

<script type="text/ecmascript-6">

  export default{
    name:'mainPage',
    data(){
      return {
        activeIndex: '1',
        activeIndex2: '1'
      }
    },
//    mounted(){
//      this.$router.push('/mainPage/monitorcenter');
//    },
    methods: {
      handleSelect(key, keyPath) {
        switch(key[0])
          {
          case "1":
            this.$router.push('/mainPage');
            break;
          case "2":
            break;
          default:
            break;
          }
      },
      getRquest(){
        this.$http.get('http://127.0.0.1:8000/frontend/getAllHostGroup')
          .then(res=>{
            console.log(res.data)
          }).then(err=>{
          console.log(err)
        })
      }
    }
  }

</script>


<style scoped>


  .el-menu {
    border: solid 0px #FFFFFF;
  }

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
