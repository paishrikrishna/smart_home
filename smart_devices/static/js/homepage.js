
// varialble declaration

var d = document.getElementsByClassName("main");

//function declaration

__init__(d);
ongoing_task();


// function definition

function __init__(d){
  // made divs clickable
  console.log("r");
  for(let i = 0 ;i < d.length ; i++){
    d[i].onclick = function(){
      console.log(d[i].id);
    };
  }
}

function ongoing_task(){
  let xhr = new XMLHttpRequest();
  xhr.open('get', 'http://127.0.0.1:8000/ongoing_task');
  xhr.send();

  xhr.onload = function() {
      //console.log(JSON.parse(xhr.response)['pump_status']);
      //onsole.log(JSON.parse(xhr.response)['foo'])
      var tasks = JSON.parse(xhr.response)['task'];
      var status = JSON.parse(xhr.response)['status'];
      console.log(tasks);
      console.log(status);

      for(var i=0; i<tasks.length;i++){
        add_task(tasks[i],status[i]);
      }
  };
}

function add_task(tasks,status){
  var parent = document.getElementById("ongoing_task_add");
  var div = document.createElement("div");
    if(status=="P"){
      div.style = "border-color:black;background-color:red;color:white;margin-top:2px;padding:1px;width:98%;border-style:solid;border-width:2px;font-size:30px;";
    }
    else{
      div.style = "border-color:black;background-color:orange;color:white;margin-top:2px;padding:1px;width:98%;border-style:solid;border-width:2px;font-size:30px;";
    }
  var textnode = document.createTextNode(tasks);
  div.id="task_name";
  div.onclick = function(){
    //alert(this.innerText);
    location.href="http://127.0.0.1:8000/task_page";
  };
  div.append(textnode);
  parent.append(div);
}
