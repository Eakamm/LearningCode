let vue = new Vue({
  el:"#app",
  data:{
    list:[
      {
        name: "《算法导论》",
        beginDate: "2006-9",
        price: 85.00,
        count: 1
      },
      {
        name: "《UNIX编程艺术》",
        beginDate: "2006-2",
        price: 59.00,
        count: 1
      },
      {
        name: "《编程大全》",
        beginDate: "2008-10",
        price: 39.00,
        count: 1
      },
      {
        name: "《代码大全》",
        beginDate: "2006-3",
        price: 128.00,
        count: 1
      }
    ],
    isZero: false
  },
  methods: {
    get() {
      
    },
    add(index){
      this.list[index].count++;
    },
    sub(index){
      if(this.list[index].count == 0){
        alert(商品数量必须大于0);
      }else{
        this.list[index].count--;
      }

    },
    remove(index){
      this.list.splice(index,1);
    }
  },
  computed: {
    totalPrice() {
      let total = 0;
      for (const iterator of this.list) {
        console.log(iterator)
        total+=iterator.price*iterator.count;
      }
      return total;
    }
  },
  filters:{
    showPrice(price){
      return '￥'+price.toFixed(2);
    }
  }
})