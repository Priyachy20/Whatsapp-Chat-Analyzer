(this["webpackJsonpstreamlit-browser"]=this["webpackJsonpstreamlit-browser"]||[]).push([[44],{1837:function(e,t,o){"use strict";o.r(t),o.d(t,"default",(function(){return c}));var n=o(2),r=o(4),a=o(6),i=o(7),u=o(0),l=o.n(u),s=o(211),p=o(166),m=o(1),c=function(e){Object(a.a)(o,e);var t=Object(i.a)(o);function o(){var e;Object(n.a)(this,o);for(var r=arguments.length,a=new Array(r),i=0;i<r;i++)a[i]=arguments[i];return(e=t.call.apply(t,[this].concat(a))).formClearHelper=new s.b,e.state={value:e.initialValue},e.commitWidgetValue=function(t){e.props.widgetMgr.setIntValue(e.props.element,e.state.value,t)},e.onFormCleared=function(){e.setState({value:e.props.element.default},(function(){return e.commitWidgetValue({fromUi:!0})}))},e.onChange=function(t){e.setState({value:t},(function(){return e.commitWidgetValue({fromUi:!0})}))},e}return Object(r.a)(o,[{key:"initialValue",get:function(){var e=this.props.widgetMgr.getIntValue(this.props.element);return void 0!==e?e:this.props.element.default}},{key:"componentDidMount",value:function(){this.props.element.setValue?this.updateFromProtobuf():this.commitWidgetValue({fromUi:!1})}},{key:"componentDidUpdate",value:function(){this.maybeUpdateFromProtobuf()}},{key:"componentWillUnmount",value:function(){this.formClearHelper.disconnect()}},{key:"maybeUpdateFromProtobuf",value:function(){this.props.element.setValue&&this.updateFromProtobuf()}},{key:"updateFromProtobuf",value:function(){var e=this,t=this.props.element.value;this.props.element.setValue=!1,this.setState({value:t},(function(){e.commitWidgetValue({fromUi:!1})}))}},{key:"render",value:function(){var e=this.props.element,t=e.options,o=e.help,n=e.label,r=e.formId,a=this.props,i=a.disabled,u=a.widgetMgr;return this.formClearHelper.manageFormClearListener(u,r,this.onFormCleared),Object(m.jsx)(p.b,{label:n,options:t,disabled:i,width:this.props.width,onChange:this.onChange,value:this.state.value,help:o})}}]),o}(l.a.PureComponent)}}]);