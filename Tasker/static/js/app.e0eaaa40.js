(function(e){function t(t){for(var r,u,c=t[0],i=t[1],l=t[2],p=0,d=[];p<c.length;p++)u=c[p],Object.prototype.hasOwnProperty.call(a,u)&&a[u]&&d.push(a[u][0]),a[u]=0;for(r in i)Object.prototype.hasOwnProperty.call(i,r)&&(e[r]=i[r]);s&&s(t);while(d.length)d.shift()();return o.push.apply(o,l||[]),n()}function n(){for(var e,t=0;t<o.length;t++){for(var n=o[t],r=!0,c=1;c<n.length;c++){var i=n[c];0!==a[i]&&(r=!1)}r&&(o.splice(t--,1),e=u(u.s=n[0]))}return e}var r={},a={app:0},o=[];function u(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,u),n.l=!0,n.exports}u.m=e,u.c=r,u.d=function(e,t,n){u.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},u.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},u.t=function(e,t){if(1&t&&(e=u(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(u.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)u.d(n,r,function(t){return e[t]}.bind(null,r));return n},u.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return u.d(t,"a",t),t},u.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},u.p="/";var c=window["webpackJsonp"]=window["webpackJsonp"]||[],i=c.push.bind(c);c.push=t,c=c.slice();for(var l=0;l<c.length;l++)t(c[l]);var s=i;o.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},"56d7":function(e,t,n){"use strict";n.r(t);n("e260"),n("e6cf"),n("cca6"),n("a79d");var r=n("2b0e"),a=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"app"}},[n("vc-calendar",{attrs:{"is-expanded":"",attributes:e.computedTasks}})],1)},o=[],u=(n("99af"),n("b0c0"),n("a4d3"),n("e01a"),n("a78e")),c=n.n(u),i=n("bc3a"),l=n.n(i),s={name:"App",data:function(){return{currentDate:new Date,tasks:[]}},computed:{computedTasks:function(){var e=[],t=["gray","red","orange","yellow","green","teal","blue","indigo","purple","pink"];for(var n in console.log(this.tasks),this.tasks){var r=this.tasks[n];e.push({key:r.pk,dot:t[t.length*Math.random()|0],dates:{start:new Date(r.fields.created_on),end:new Date(r.fields.due_on)},popover:{label:"".concat(r.fields.name,": ").concat(r.fields.description)}})}return e}},methods:{getData:function(){var e=this,t=c.a.get("department_id");l.a.get(`${window.location.protocol}://${window.location.hostname}/api/get-tasks/`.concat(t,"/")).then((function(t){var n=t.data;e.tasks=n})).catch((function(e){return console.log(e)}))}},mounted:function(){this.getData(),window.webpackHotUpdate&&(console.log("In Dev Mode."),c.a.set("department_id",1,{expires:1,path:""}))}},p=s,d=n("2877"),f=Object(d["a"])(p,a,o,!1,null,null,null),h=f.exports,v=n("c894"),b=n("5887"),g=n.n(b),m=n("86e3"),y=n.n(m),w=n("404b"),k=n.n(w);r["default"].config.productionTip=!1,r["default"].use(v["a"]),r["default"].use(g.a,{componentPrefix:"vc"}),r["default"].component("calendar",y.a),r["default"].component("date-picker",k.a),r["default"].customElement("vue-widget",h)}});
//# sourceMappingURL=app.e0eaaa40.js.map
