<template>
  <div id="HostInfoPage">
    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/mainPage' }">监控中心</el-breadcrumb-item>
      <el-breadcrumb-item>主机信息</el-breadcrumb-item>
    </el-breadcrumb>

    <!--提示信息-->
    <el-card class="box-card" v-show="flag">
      <div slot="header" class="clearfix">
        <span>没有主机信息</span>
      </div>
    </el-card>

    <!--主机卡片-->
    <div v-for="item in host_list">
      <el-card class="box-card" v-show="!flag">
        <div slot="header" class="clearfix" @click="toHostDetail(item.id)">
          <el-row>
            <el-col :span="12">
              <div class="grid-content bg-purple">
                主机名称：
                <span style="margin-left: 10px;color:#FFA340;" v-text="item.name"></span>
              </div>
            </el-col>
            <el-col :span="12">
              <div class="grid-content bg-purple-light">
                主机编号：
                <span style="margin-left: 10px;color:#FFA340;" v-text="item.id"></span>
              </div>
            </el-col>
          </el-row>
        </div>
        <div class="text item" style="font-size: 16px">
          <div class="text item">
            <el-row>
                <el-col :span="4"><div class="grid-content bg-purple-light">主机状态:</div></el-col>
                <el-col :span="4">
                  <div class="grid-content bg-purple">
                    <i class="el-icon-success" style="color: #00c065;font-size: 20px" v-show="item.status"></i>
                    <i class="el-icon-warning" style="color: #dd6161" v-show="!item.status"></i>
                  </div>
                </el-col>
              <el-col :span="4">
                <div class="grid-content bg-purple">主机IP地址:</div>
              </el-col>
              <el-col :span="4">
                <div class="grid-content bg-purple" v-text="item.ip_addr">主机IP地址:</div>
              </el-col>
            </el-row>
          </div>

          <div class="text item">
            <el-row>
              <el-col :span="4" ><div class="grid-content bg-purple">监控服务:</div></el-col>
              <el-col :span="4" v-for="service,key in item.services" :key="key">
                <el-tooltip :content="service.memo" placement="bottom" effect="light">
                  <el-button v-text="service.name" class="text-button">
                  </el-button></el-tooltip>
              </el-col>
            </el-row>
          </div>
        </div>
      </el-card>
    </div>

    <div id="pagination">
      <el-pagination
        background
        layout="prev, pager, next"
        :total="1">
      </el-pagination>
    </div>

  </div>
</template>


<script type="text/ecmascript-6">
  export default{
    name: 'HostInfoPage',
    data(){
      return {
        group_id:'',
        host_list:[],
        flag:true,
        text_update:'更新数据',
      }
    },
    beforeMount(){

    },
    mounted(){
      this.group_id = this.$route.params.group_id;
      this.$http.get('http://127.0.0.1:8000/frontend/getHostsByGroupId/'+this.group_id)
        .then(res=>{
          if (res.data.status == 1){
            this.host_list = res.data;
            if (res.data.data.length == 0){ //如果此主机组下没有主机，则flag=false。
              this.flag=true; //显示提示信息。
            }else{
              this.flag=false; //隐藏提示信息。
              this.host_list = res.data.data;
            }
          }
        }).then(err=>{
        console.log(err);
      });
    },
    methods:{
      update_host_data(host_id){
        console.log(host_id)
        this.$http.get('http://127.0.0.1:8000/frontend/getRealLastestDataByHostId/'+host_id)
          .then(res=>{
            if (res.data.status == 1){
              this.host_data = res.data.data;
              console.log(this.host_data)
            }
          }).then(err=>{
          console.log(err);
        })
      },
    }
  }


</script>

<style scoped>

  #pagination{
    margin-top: 30px;
  }


  .update_btn{
    cursor: pointer;
    padding: 5px 5px;
  }

  .text-button {
    /*cursor: Default;*/
    /*border: none;*/
    padding: 5px 5px;
    /*background-color: #fff;*/
  }

  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    margin-top: 30px;
    height: auto;
    width: auto;
  }
</style>
