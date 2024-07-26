<html>
<head>
  <title>역사OX퀴즈</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
  <meta name="author" content="채희동">
  <meta charset="utf-8">
</head>
<body>
<img src="초시계.gif">
임오군란 이후 조선은 조일상민수륙무역장정을 체결해 일본 상인의 내지무역을 허용했다.<br>
<form method="post" action="게임오버.php">
  <input type="hidden" value="<?php echo$_POST['점수'];?>" name="점수">
  <input type="image" src="O.png" width="50%" align="left" onclick="window.alert('임오군란 이후 조선은 조청상민수륙무역장정을 체결해 청나라 상인의 내지무역을 허용했다.')">
</form>
<form method="post" action="메인.php">
  <input type="hidden" value="<?php echo$_POST['점수']+1;?>" name="점수">
  <input type="image" src="X.png" width="50%" align="right">
</form>
</form>
</body>
</html>
