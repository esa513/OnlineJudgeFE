<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
  export default {
    name: 'app',
    components: {}
  }
</script>

<style lang="less">
  body {
    margin: 0;
    padding: 0;
    font-family: "Microsoft YaHei", Arial, sans-serif; /* 中文字体 */
    font-family: "Times New Roman", "Helvetica Neue", "Helvetica", "PingFang SC", "Hiragino Sans GB"; /* 英文字体 */
    font-size: 14px;
    -webkit-font-smoothing: antialiased;
    background-color: #324157;
  }

  #app {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 100%;
  }
</style>
