<template>
  <div>
    <Panel>
      <div slot="title">{{$t('m.Problems_List')}}</div>
      <Table v-if="contestRuleType == 'ACM' || OIContestRealTimePermission"
             :columns="ACMTableColumns"
             :data="problems"
             :no-data-text="$t('m.No_Problems')"></Table>
      <Table v-else
             :data="problems"
             :columns="OITableColumns"
             no-data-text="$t('m.No_Problems')"></Table>
    </Panel>
  </div>
</template>

<script>
  import {mapState, mapGetters} from 'vuex'
  import {ProblemMixin} from '@oj/components/mixins'
  import utils from '../../../../../utils/utils';

  export default {
    name: 'ContestProblemList',
    mixins: [ProblemMixin],
    data () {
      return {
        ACMTableColumns: [
          {
            title: '#',
            sortType: 'ASC',
            width: 150,
            render: (h, params) => this.renderCellByKey(h, params, '_id')
          },
          {
            title: this.$i18n.t('m.Title'),
            render: (h, params) => this.renderCellByKey(h, params, 'title')
          },
          {
            title: this.$i18n.t('m.Total'),
            render: (h, params) => this.renderCellByKey(h, params, 'submission_number')
          },
          {
            title: this.$i18n.t('m.AC_Rate'),
            render: (h, params) => this.renderCellByValue(h, params, this.getACRate(params.row.accepted_number, params.row.submission_number))
          }
        ],
        OITableColumns: [
          {
            title: '#',
            key: '_id',
            width: 150
          },
          {
            title: this.$i18n.t('m.Title'),
            key: 'title'
          }
        ]
      }
    },
    mounted () {
      this.getContestProblems()
    },
    methods: {
      getContestProblems () {
        this.$store.dispatch('getContestProblems').then(res => {
          if (this.isAuthenticated) {
            if (this.contestRuleType === 'ACM') {
              this.addStatusColumn(this.ACMTableColumns, res.data.data)
            } else if (this.OIContestRealTimePermission) {
              this.addStatusColumn(this.ACMTableColumns, res.data.data)
            }
          }
        })
      },
      renderCell (h, params, keyVaule=null, type='key') {
        if (type !== 'key' && type !== 'value') {
          console.error('type must be key or value')
          return
        }
        const value = type === 'key' ? params.row[keyVaule] : keyVaule
        return h('div', {
          on: {
            click: (event) => {
              utils.handleClick.call(this, event, {
                name: 'contest-problem-details',
                params: {
                  contestID: this.$route.params.contestID,
                  problemID: params.row._id
                }
              })
            }
          }
        }, value)
      },
      renderCellByKey(h, params, key) {
        return this.renderCell(h, params, key, 'key')
      },
      renderCellByValue(h, params, value) {
        return this.renderCell(h, params, value, 'value')
      }
    },
    computed: {
      ...mapState({
        problems: state => state.contest.contestProblems
      }),
      ...mapGetters(['isAuthenticated', 'contestRuleType', 'OIContestRealTimePermission'])
    }
  }
</script>

<style scoped lang="less">
</style>
