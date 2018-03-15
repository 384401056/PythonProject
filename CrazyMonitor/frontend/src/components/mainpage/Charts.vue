<template>
  <div id="Charts">
    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/mainPage' }">监控中心</el-breadcrumb-item>
      <el-breadcrumb-item :to="{name: 'hostinfopage', params: {group_id:group_id,group_name:group_name}}">{{ group_name
        }}
      </el-breadcrumb-item>
      <el-breadcrumb-item>{{ host_name }}</el-breadcrumb-item>
    </el-breadcrumb>

    <!--提示信息-->
    <el-card class="box-card" v-show="flag">
      <div slot="header" class="clearfix">
        <span>没有主机信息</span>
      </div>
    </el-card>

    <el-card class="box-card" v-show="!flag">
      <div slot="header" class="clearfix">
        <span style="color:#FFA340;">CPU 监控信息</span>
      </div>
      <div class="text item">
        <ve-line :data="cpu_chartData" :settings="cpu_chartSettings"></ve-line>
      </div>
    </el-card>

    <el-card class="box-card" v-show="!flag">
      <div slot="header" class="clearfix">
        <span style="color:#FFA340;">内存 监控信息</span>
      </div>
      <div class="text item">
        <ve-line :data="mem_chartData" :settings="mem_chartSettings"></ve-line>
      </div>
    </el-card>

  </div>
</template>


<script type="text/ecmascript-6">
  import { Loading } from 'element-ui';

  export default{
    name: 'Charts',
    data(){
      return {
        flag:false, //隐藏提示信息.
        loadingInstance:'', //loading组件实例.
        interval:'',
        group_id: '',
        host_id: '',
        host_name: '',
        host_services: [],
        group_name: '',
        serverData: {},
        requestList: [],
        cpu_chartData: {
          columns: [],
          rows: []
        },
        cpu_chartSettings: {
          metrics: [],
          dimension: ['日期']
        },

        mem_chartData: {
          columns: [],
          rows: []
        },
        mem_chartSettings: {
          metrics: [],
          dimension: ['日期']
        },

        nic_chartData: {
          columns: [],
          rows: []
        },
        nic_chartSettings: {
          metrics: [],
          dimension: ['日期']
        },
      }
    },
    methods: {
      /**
       * 每隔15秒获取一次新数据。
       */
      flushData(host_id, host_services){
        this.interval = setInterval(() => {
          this.getChartData(host_id, host_services);
        }, 15000)
      },

      /**
       * 获取图表数据
       * @param host_id: 主机id
       * @param host_services:主机监控服务列表。
       */
      getChartData(host_id, host_services){
        this.requestList = [];
        for (var index in host_services) {
          var serviceName = host_services[index].name;
          var url = this.$serverip + '/frontend/getRealLastestDataByHostId/' + host_id + '/' + serviceName + '/latest';
          this.requestList.push(this.$http.get(url));
        }

        //跟据host_services中的服务数据，来发送多个请求。
        this.$http.all(this.requestList)
          .then(response => {

            //将返回的数据组装进this.serverData
            for (var i in response) {
              var count = 0;
              var key = Object.keys(response[i].data.data)[0]; //取到服务名
              this.serverData[key] = response[i].data.data[key];
              //如果没有获取到数据
              if (this.serverData[key].length == 0) {
                continue;
              } else {
                count += 1;
              }

              this.serverData[key].shift();
              if (key === 'LinuxMemory') {
                var retData = this.AssemblyMemoryData(key, this.serverData[key]);
                this.mem_chartData = retData['chartData'];
                this.mem_chartSettings = retData['chartSettings'];
              }
              if (key === 'LinuxCPU') {
                var retData = this.AssemblyCPUData(key, this.serverData[key]);
                this.cpu_chartData = retData['chartData'];
                this.cpu_chartSettings = retData['chartSettings'];
              }
              if (key === 'LinuxNIC') {
//                var retData = this.AssemblyNICData(key,this.serverData[key]);
//                this.nic_chartData = retData['chartData'];
//                this.nic_chartSettings = retData['chartSettings'];
              }

              //如果count为0,说明确实没有数据。
              if (count == 0) {
                this.flag = true;
              }
            }
            this.loadingInstance.close(); //销毁loading实例。
          }).then(err => {
            console.log(err);
            this.loadingInstance.close(); //销毁loading实例。
        })
      },

      /**
       * 组装Memory监控信息。并返回chartData
       * @param servicekey
       * @param serverData
       * @constructor
       */
      AssemblyMemoryData(servicekey, serverData){
        var ret = {
          chartData: {
            columns: [],
            rows: []
          },
          chartSettings: {
            metrics: [],
            dimension: ['日期']
          }
        };

        var cols = ['日期'];
        var metrics = [];
        var rows = [];


        for (var key in serverData[0][0]) {
          switch(key){
            case 'kbmemfree':
              cols.push(key+'-空闲内存(MB)');
              metrics.push(key+'-空闲内存(MB)');
              break;
            case 'kbmemused':
              cols.push(key+'-已使用内存(MB)');
              metrics.push(key+'-已使用内存(MB)');
              break;
            case 'memused':
              cols.push(key+'-已使用百分比');
              metrics.push(key+'-已使用百分比');
              break;
            case 'kbbuffers':
              cols.push(key+'-缓冲区使用量(MB)');
              metrics.push(key+'-缓冲区使用量(MB)');
              break;
            case 'kbcached':
              cols.push(key+'-缓存数据使用量(MB)');
              metrics.push(key+'-缓存数据使用量(MB)');
              break;
            case 'kbcommit':
              cols.push(key+'-保障内存(MB)');
              metrics.push(key+'-保障内存(MB)');
              break;
            case 'commit':
              cols.push(key+'-保障内存百分比');
              metrics.push(key+'-保障内存百分比');
              break;
            case 'status':
              break;
            default:
              cols.push(key);
              metrics.push(key);
              break;
          }
        }

        for (var index in serverData) {
          var row = {};
          for (var key in serverData[index][0]) {
            switch(key){
              case 'kbmemfree':
                row[key+'-空闲内存(MB)'] = Math.round(serverData[index][0][key]/1024);
                break;
              case 'kbmemused':
                row[key+'-已使用内存(MB)'] = Math.round(serverData[index][0][key]/1024);
                break;
              case 'memused':
                row[key+'-已使用百分比'] = serverData[index][0][key];
                break;
              case 'kbbuffers':
                row[key+'-缓冲区使用量(MB)'] = Math.round(serverData[index][0][key]/1024);
                break;
              case 'kbcached':
                row[key+'-缓存数据使用量(MB)'] = Math.round(serverData[index][0][key]/1024);
                break;
              case 'kbcommit':
                row[key+'-保障内存(MB)'] = Math.round(serverData[index][0][key]/1024);
                break;
              case 'commit':
                row[key+'-保障内存百分比'] = serverData[index][0][key];
                break;
              case 'status':
                break;
              default:
                row[key] = serverData[index][0][key];
                break;
            }
          }
          var datetime = serverData[index][1];
          row['日期'] = datetime;
          rows.push(row);
        }



//        for (var key in serverData[0][0]) {
//          if (key != 'status') {
//            cols.push(key);
//            metrics.push(key);
//          }
//        }
//
//        for (var index in serverData) {
//          var row = {};
//          for (var key in serverData[index][0]) {
//            if (key != 'status') {
//              row[key] = serverData[index][0][key]
//            }
//          }
//          var datetime = serverData[index][1];
//          row['日期'] = datetime;
//          rows.push(row);
//        }

        ret['chartData']['columns'] = cols;
        ret['chartData']['rows'] = rows;
        ret['chartSettings']['metrics'] = metrics;

        return ret;
      },

      /**
       * 组装CPU监控数据,并返回chartData
       * @param servicekey
       * @param serverData
       * @constructor
       */
      AssemblyCPUData(servicekey, serverData){
        var ret = {
          chartData: {
            columns: [],
            rows: []
          },
          chartSettings: {
            metrics: [],
            dimension: ['日期']
          }
        };

        var cols = ['日期'];
        var metrics = [];
        var rows = [];

        for (var key in serverData[0][0]) {
          switch(key){
            case 'user':
              cols.push(key+'-用户使用百分比');
              metrics.push(key+'-用户使用百分比');
              break;
            case 'nice':
              cols.push(key+'-nice使用百分比');
              metrics.push(key+'-nice使用百分比');
              break;
            case 'system':
              cols.push(key+'-核心使用百分比');
              metrics.push(key+'-核心使用百分比');
              break;
            case 'iowait':
              cols.push(key+'-IO等待百分比');
              metrics.push(key+'-IO等待百分比');
              break;
            case 'steal':
              cols.push(key+'-虚拟进程百分比');
              metrics.push(key+'虚拟进程百分比');
              break;
            case 'idle':
              cols.push(key+'-空闲时间百分比');
              metrics.push(key+'-空闲时间百分比');
              break;
            default:
              break;
          }
        }

        for (var index in serverData) {
          var row = {};
          for (var key in serverData[index][0]) {
            switch(key){
              case 'user':
                row[key+-'用户使用百分比'] = serverData[index][0][key];
                break;
              case 'nice':
                row[key+'-nice使用百分比'] = serverData[index][0][key];
                break;
              case 'system':
                row[key+'-核心使用百分比'] = serverData[index][0][key];
                break;
              case 'iowait':
                row[key+'-IO等待百分比'] = serverData[index][0][key];
                break;
              case 'steal':
                row[key+'-虚拟进程百分比'] = serverData[index][0][key];
                break;
              case 'idle':
                row[key+'-空闲时间百分比'] = serverData[index][0][key];
                break;
              default:
                break;
            }
          }
          var datetime = serverData[index][1];
          row['日期'] = datetime;
          rows.push(row);
        }

//        for (var key in serverData[0][0]) {
//          if (key != 'status') {
//            cols.push(key);
//            metrics.push(key);
//          }
//        };
//
//        for (var index in serverData) {
//          var row = {};
//          for (var key in serverData[index][0]) {
//            if (key != 'status') {
//              row[key] = serverData[index][0][key];
//            }
//          }
//          var datetime = serverData[index][1];
//          row['日期'] = datetime;
//          rows.push(row);
//        };

        ret['chartData']['columns'] = cols;
        ret['chartData']['rows'] = rows;
        ret['chartSettings']['metrics'] = metrics;

        return ret;
      },

      AssemblyNICData(servicekey, serverData){
      },
    },
    mounted(){

      this.host_id = this.$route.params.host_id;
      this.host_name = this.$route.params.host_name;
      this.host_services = this.$route.params.host_services;
      this.group_id = this.$route.params.group_id;
      this.group_name = this.$route.params.group_name;

      this.loadingInstance = Loading.service({
        lock: true,
        text: 'Loading',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)'
      });

      this.getChartData(this.host_id, this.host_services);
      this.flushData(this.host_id, this.host_services);
    },

    //关闭定时任务
    beforeDestroy () {
      clearInterval(this.interval);
    },
  }


</script>

<style scoped>
  .box-card {
    margin-top: 30px;
    height: auto;
    width: auto;
  }
</style>
