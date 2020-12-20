<?php
if($_COOKIE['account']){
	header('location:https://yourip.com');
}
else{
	header('location:https://yourip.com/login.html');
}
?>
