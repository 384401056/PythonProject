/**
 * Created by Administrator on 2017/8/9.
 */

new Vue({
    el: '#app',
    data: {
        content: [],
        pm: {}
    },
    mounted:function(){
        this.$http.get('http://127.0.0.1:8000/' ).then(function(response){
                this.content = response.data.dataList
                console.log(response)
        }, function(response){
                console.log(response.err)
        });
    },
    methods: {
        onClick: function () {
            this.$http.post('http://127.0.0.1:8000/post', this.pm).then(function(response){
                console.log(response)
                //this.$set('params', {})
            },function(response){
                console.log(response.err)
            })
        }
    }


    //mounted: function() {
    //    this.$http.get('http://127.0.0.1:8000/')
    //        .then((response) => {
    //            this.content = response.data.dataList
    //            console.log(response)
    //        })
    //        .catch(function(response) {
    //            console.log(response)
    //        })
    //}



    //mounted: function() {
    //    this.$nextTick(function () {
    //        this.$http.get('http://127.0.0.1:8000/').then(function(res) {
    //            this.content = res.data.dataList
    //        },function(){
    //            console.log('失败!')
    //        })
    //    })
    //}
})


