<html>
<head>
  <title>역사OX퀴즈</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
  <meta name="author" content="채희동">
  <meta charset="utf-8">
</head>
<body>
<img src="초시계.gif">
기기창은 근대식 무기를 제조했다.<br>
<form method="post" action="메인.php">
  <input type="hidden" value="<?php echo$_POST['점수']+1;?>" name="점수">
  <input type="image" src="O.png" width="50%" align="left">
</form>
<form method="post" action="게임오버.php">
  <input type="hidden" value="<?php echo$_POST['점수'];?>" name="점수">
  <input type="image" src="X.png" width="50%" align="right" onclick="window.alert('기기창은 근대식 무기를 제조했다.')">
</form>
</form>
</body>
</html>
