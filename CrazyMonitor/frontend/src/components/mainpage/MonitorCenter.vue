<template>
  <div id="MonitorCenter">
    <el-breadcrumb separator="/">
      <el-breadcrumb-item>监控中心</el-breadcrumb-item>
    </el-breadcrumb>
    <div  v-for="item in hg_data.data">
      <el-card class="box-card">
        <div slot="header" class="clearfix" @click="toHostList(item.id,item.name)">
          主机组:
            <span style="margin-left: 10px;color:#FFA340;" v-text="item.name"></span>
        </div>

        <div class="text item">
          <el-row>
            <el-col :span="4" ><div class="grid-content bg-purple">主机数量：</div></el-col>
            <el-col :span="4">
              <el-button class="text-button" style="color:#2852ae;" v-text="item.hosts.length" ></el-button>
            </el-col>
          </el-row>
        </div>
        <div class="text item">
          <el-row>
            <el-col :span="4" ><div class="grid-content bg-purple">监控服务：</div></el-col>
            <el-col :span="4" v-for="service,key in item.services" :key="key">
              <el-tooltip :content="service.memo" placement="bottom" effect="light">
                <el-button style="color:#00c065;" v-text="service.name" class="text-button"></el-button>
              </el-tooltip>
            </el-col>
          </el-row>
        </div>
        <div class="text item">
          <el-row>
            <el-col :span="4" ><div class="grid-content bg-purple">触发器：</div></el-col>
            <el-col :span="4" v-for="t,key in item.triggers" :key="key">
                <el-tooltip :content="t.memo" placement="bottom" effect="light">
                  <el-button style="color:#2852ae;" class="text-button" v-text="t.name"></el-button>
                </el-tooltip>
            </el-col>
          </el-row>
        </div>
      </el-card>
    </div>

  </div>
</template>


<script type="text/ecmascript-6">
  export default{
    name: 'MonitorCenter',
    data(){
      return {
        hg_data:{},
      }
    },
    mounted(){
      this.$http.get(this.$serverip+'/frontend/getAllHostGroup')
        .then(res=>{
          this.hg_data = res.data
      }).then(err=>{
          console.log(err)
      })
    },
    methods:{
      toHostList(group_id, group_name){
        this.$router.push({
          name: 'hostinfopage',
          params: {
            group_id: group_id,
            group_name:group_name,
          }
        });
      }
    }
  }


</script>

<style scoped>

  .clearfix {
    cursor: pointer;
  }


  .text-button {
    cursor: Default;
    border: none;
    padding: 5px 5px;
    background-color: #fff;
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
