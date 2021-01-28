const ListItem = Vue.component('list-item', {
  template: `
  <li style="list-style-position: inside">
    <input @input="$emit('update:item', $event.target.value)" :readonly="!editable" :style="!editable ? 'outline: none;border: none;' : ''"  style="padding: 2px;margin: 2px;border: 1px solid #999;" type="text" :value="item">    
    <span v-show="editable" @click="$emit('remove')" style="font-size: 12px;color: #f54;cursor: pointer">삭제</span>
  </li>`,
  props: ['item', 'editable']
})

const List = Vue.component('list', {
  template: `
  <div>
    <div style="display: flex;align-items: center;"> 
      <div style="margin: 12px 0;">{{title}} </div>
      <span style="margin-left: 8px;font-size: 12px;font-weight: normal;marign-left: 4px;color: #4a5ea3;cursor: pointer" @click="() => { editable = !editable }">
        {{ editable ? '완료' : '편집' }}
      </span>    
    </div>
    <div>     
      <ul>
        <list-item :editable.sync="editable" v-for="(item, idx) in dataList" :key="idx" :item.sync="dataList[idx]" @remove="removeItem(idx)"></list-item>      
        <li style="list-style-position: inside" v-show="editable">
          <input @keyup.enter="addItem" v-model="addData" :readonly="!editable" style="padding: 2px;margin: 2px;border: 1px solid #4a5ea3;" type="text">    
          <span @click="addItem" v-show="editable" style="font-size: 12px;color: #4a5ea3;cursor: pointer">추가</span>
        </li>
      </ul>
    </div>
  </div>
  `,
  components: {
    'list-item': ListItem
  },
  props: {
    title: {
      default: ""
    },
    dataList: {
      required: true,
      default: []
    }
  },
  data() {
    return {
      editable: false,
      addData: "",
    }
  },
  methods: {
    removeItem(idx) {
      this.dataList.splice(idx, 1)
    },
    addItem() {
      this.dataList.push(this.addData);
      this.addData = "";
    }
  }
})

const app = new Vue({
  el: '#app',
  components: {
    'list': List,
  },
  data() {
    return {
      policyData: null
    }
  },
  mounted() {
    this.getPolicyData();
  },
  computed: {
    getPolicyDataJson() {
      return this.syntaxHighlight(JSON.stringify(this.policyData, null, 2));
    }
  },
  methods: {
    getPolicyData() {
      axios.get('/getPolicyFile')
        .then(res => {
          console.log(res.data);
          this.policyData = res.data;
        });
    },
    writeConfig() {
      axios.post('/writePolicyFile', this.policyData)
        .then(res => {
          alert("정책이 저장되었습니다.");
        })
        .catch(err => {
          alert("오류가 발생했습니다.");
        })
    },
    syntaxHighlight(json) {
      json = json.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
      return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function (match) {
        var cls = 'number';
        if (/^"/.test(match)) {
          if (/:$/.test(match)) {
            cls = 'key';
          } else {
            cls = 'string';
          }
        } else if (/true|false/.test(match)) {
          cls = 'boolean';
        } else if (/null/.test(match)) {
          cls = 'null';
        }
        return '<span class="' + cls + '">' + match + '</span>';
      });
    }
  }
})