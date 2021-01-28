const AbnormalDetectChart = Vue.component('abnormal-detect-chart', {
  extends: VueChartJs.Scatter,
  props: {
    chartData: {
      required: true
    }
  },
  watch: {
    chartData() {
      this.drawChartData();
    }
  },
  mounted() {
    this.drawChartData();
  },
  methods: {
    drawChartData() {
      const defeaultDataSet = {
        borderColor: '#efefef',
        borderWidth: 2,
        pointRadius: 9,
        pointHoverRadius: 8,
      }
      this.renderChart({
        datasets: [
          {
            ...defeaultDataSet,
            parsing: false,
            label: 'Leak',
            backgroundColor: "#80cbc5",
            data: this.chartData.leak
          },
          {
            ...defeaultDataSet,
            parsing: false,
            label: 'Leak Normal',
            backgroundColor: "#ffde4b",
            data: this.chartData.leakNormal
          },
          {
            ...defeaultDataSet,
            parsing: false,
            label: 'Normal',
            backgroundColor: "#cdc1bd",
            data: this.chartData.normal
          },
          {
            ...defeaultDataSet,
            parsing: false,
            label: 'Normal Leak',
            backgroundColor: "#ed5a5c",
            data: this.chartData.normalLeak
          },
        ]
      }, {
        tooltips: {
          custom: (tooltip) => {
            if (!tooltip) return;
            tooltip.displayColors = false;
          },
          callbacks: {
            title: (tooltipItem, data) => {
              console.log(tooltipItem[0].xLabel)
              return moment(tooltipItem[0].xLabel).format("LLLL");
            },
            label: (context) => {
              return context.yLabel;
            }
          }
        },
        legend: {
          position: 'top',
          labels: {
            fontColor: '#c3c3c3',
            padding: 15
          }
        },
        layout: {
          padding: {
            top: 20,
          }
        },
        scales: {
          xAxes: [{
            type: 'time',
            time: {
              displayFormats: {
                'day': 'YYYY MM DD',
              },
              unit: 'day',
            }
          }]
        },
        responsive: true,
        maintainAspectRatio: false
      });
    }
  }
});

const ActChart = Vue.component('act-chart', {
  extends: VueChartJs.Bar,
  props: {
    chartData: {
      required: true
    }
  },
  watch: {
    chartData() {
      this.drawChartData();
    }
  },
  mounted() {
    this.drawChartData();
  },
  methods: {
    argMax(array) {
      if (array.length <= 0) return false;
      return array.map((x, i) => [x, i]).reduce((r, a) => (a[0] > r[0] ? a : r))[1];
    },
    drawChartData() {
      const labels = Object.keys(this.chartData);
      const data = Object.values(this.chartData);

      const bgColors = labels.map(res => '#cdc1bd');
      bgColors[this.argMax(data) || 0] = '#ed5a5c';

      this.renderChart({
        labels,
        datasets: [
          {
            data,
            backgroundColor: bgColors
          }
        ]
      }, {
        legend: {
          display: false
        },
        responsive: true,
        maintainAspectRatio: false
      });
    }
  }
});

const dateActChart = Vue.component('date-act-chart', {
  extends: VueChartJs.Line,
  props: {
    chartData: {
      required: true
    }
  },
  watch: {
    chartData() {
      this.drawChartData();
    }
  },
  mounted() {
    this.drawChartData();
  },
  methods: {
    drawChartData() {
      const sampleData = [{
        x: 1607415006274,
        y: 1
      },
      {
        x: 1607501422936,
        y: 2
      },
      {
        x: 1607701422936,
        y: 2
      }];

      const bgColors = ["#b6777e", "#8d6782", "#80cbc5", "#ffde4b", "#ed5a5c",];
      const datasets = [];

      Object.keys(this.chartData).forEach((item, idx, arr) => {
        let key = arr[idx];
        datasets.push({
          label: key,
          backgroundColor: bgColors[idx],
          data: this.chartData[key]
        });
      });

      console.log(datasets)

      this.renderChart({
        backgroundColor: ["#fea", "208ecd", "#faa"],
        datasets: datasets
      }, {
        legend: {
          display: false
        },
        scales: {
          yAxes: [{
            stacked: true
          }],
          xAxes: [{
            type: 'time',
            time: {
              displayFormats: {
                'day': 'YYYY MM DD',
              },
            },
          }]
        },
        responsive: true,
        maintainAspectRatio: false
      });
    }
  }
});

const app = new Vue({
  el: '#app',
  component: {
    AbnormalDetectChart,
    ActChart,
    dateActChart
  },
  data() {
    return {
      currentUser: null,
      chartData: null
    }
  },
  computed: {
    getChartDataByUser() {
      return this.chartData.chartData[this.currentUser];
    }
  },
  created() {
    const locale = window.navigator.userLanguage || window.navigator.language;
    moment.locale(locale);
  },
  mounted() {
    axios.get('/getStatistics')
      .then(res => {
        this.chartData = res.data;
        this.currentUser = res.data.userList[0]
      });
  }
});