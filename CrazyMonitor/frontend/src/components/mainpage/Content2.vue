<template>
	<div id="contentTable">
		<el-breadcrumb separator="/">
          <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
          <el-breadcrumb-item>活动管理</el-breadcrumb-item>
          <el-breadcrumb-item>活动列表</el-breadcrumb-item>
          <el-breadcrumb-item>活动详情</el-breadcrumb-item>
        </el-breadcrumb>
		<el-table :data="tableData" border style="width: 100%">
		    <el-table-column
		      prop="date"
		      label="日期"
		      width="180">
		    </el-table-column>
		    <el-table-column
		      prop="name"
		      label="姓名"
		      width="180">
		    </el-table-column>
		    <el-table-column
		      prop="address"
		      label="地址">
		    </el-table-column>
  		</el-table>
	</div>
</template>


<script>
export default{
	name:'contentTable',
    data(){
      return{
          tableData: [{
		      date: '2016-05-02',
		      name: '李小龙',
		      address: '上海市普陀区金沙江路 1518 弄'
		    }, {
		      date: '2016-05-04',
		      name: '李小龙',
		      address: '上海市普陀区金沙江路 1517 弄'
		    }, {
		      date: '2016-05-01',
		      name: '王小虎',
		      address: '上海市普陀区金沙江路 1519 弄'
		    }, {
		      date: '2016-05-03',
		      name: '王小虎',
		      address: '上海市普陀区金沙江路 1516 弄'
		    }]
      }
    },
}


</script>

<style scoped>
	
  .el-breadcrumb {
     height:40px;
     margin-left: 10px;
  }
</style>