//function start_qrqc(){
//	var python = require("python-shell")
//	var path = require("path")
//	
//	var options ={
//		scriptPath : path.join(__dirname,'/../engine/')
//	}
//
//	var qrqc = new python('board.py', options);
//	qrqc.on('message', function(message){
//		swal(message);
//
//	})
//}
//function startTest(){
//	var python = require("python-shell")
//	var path = require("path")
//
//	var test = document.getElementById('test').value
//	document.getElementById('test').value="";
//	var options ={
//		scriptPath : path.join(__dirname,'/../engine/')
//		pythonPath :'C:/Users/FK300833/PycharmProjects/QRQC/venv/Scripts'
//		args:[test]
//	}
//
//	var qrqc = new python('it_qrqc_safety.py', options);
//	qrqc.on('message', function(message){
//		swal(message);
//
//	})
//}
let {PythonShell} = require('python-shell')
function startTest(){
	
	 
	PythonShell.run('it_qrqc_safety.py', null, function (err) {
	  if (err) throw err;
	  console.log('finished');
	});
}
