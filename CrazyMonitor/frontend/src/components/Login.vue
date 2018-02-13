<template>
  <div id="loginForm">
      <el-container>
        <el-header height="80px">
        </el-header>

        <el-main>
          <el-card class="box-card">
           <el-form ref="loginform" :model="loginform" status-icon label-width="100px" class="el-form" label-position="right">
              <el-form-item label="用户名：" prop="name"
                :rules="[
                      { required: true, message: '请输入用户名', trigger: 'blur' },
                    ]"
              >
                <el-input v-model="loginform.name" @keyup.enter.native="submitForm('loginform')"></el-input>
              </el-form-item>
              <el-form-item label="密码：" prop="pwd"
                :rules="[
                      { required: true, message: '请输入密码', trigger: 'blur' },
                    ]"
              >
                <el-input type="password" v-model="loginform.pwd" auto-complete="off" @keyup.enter.native="submitForm('loginform')"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="submitForm('loginform')">登录</el-button>
                <el-button type="default" @click="reset('loginform')">重置</el-button>
              </el-form-item>
            </el-form>
          </el-card>
        </el-main>

      </el-container>
  </div>
</template>

<script type="text/ecmascript-6">
  export default{
    name:'loginForm',
    data(){
      return{
          loginform:{
            name:'',
            pwd:'',
          },
      }
    },
    methods:{
      submitForm(formName){
        this.$refs[formName].validate((valid) => {
          if (valid) {
            //如果有值就跳转
            this.$router.push('/mainPage')
          } else {
            // console.log('error submit!!');
            return false;
          }
        });
      },
      reset(formName){
        this.$refs[formName].resetFields();
      }
    }
  }

</script>



<style scoped>
  .el-header, .el-footer {
    background-color: #FFA340;
    color: #333;
    text-align: center;
    line-height: 60px;
  }

  .el-main {
    background-color: #FFFFFF;
    color: #333;
    text-align: center;
    line-height: 100%;
    display: table-cell;
    vertical-align: middle;
    margin-top: 100px;
  }

  body > .el-container {
    margin-bottom: 10px;
  }

  .el-form{
      margin-top: 40px;
  }

  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 100%;
  }

  .el-container:nth-child(7) .el-aside {
    line-height: 100%;
  }

  .box-card {
    width: 480px;
    margin: auto;
  }

</style>
