<?php
$username='data_account';
$password='database_pwd';

try{
	$conn = new PDO('mysql:host=localhost;dbname=Account',$username,$password);
}
catch(PDOException $e){
	echo $e->getMessage();
}

$result = $conn->query('select password from Account where account='.$_GET['account']);
$row=$result->fetch();

if($_GET['password']==$row['password']){
	setcookie('account',$_GET['account'],time()+60);
	header("location:https://yourip.xom/index.html");
}
else{
	header("location:https://yourip.com/Fail.html");
}
$conn=null;
?>
