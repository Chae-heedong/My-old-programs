<html>
<head>
  <title>역사OX퀴즈</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
  <meta name="author" content="채희동">
  <meta charset="utf-8">
</head>
<body>
<img src="초시계.gif">
흥선대원군은 1866년 프랑스 선교사와 천주교 신자를 죽이는 병인박해를 저질렀다.<br>
<form method="post" action="메인.php">
  <input type="hidden" value="<?php echo$_POST['점수']+1;?>" name="점수">
  <input type="image" src="O.png" width="50%" align="left">
</form>
<form method="post" action="게임오버.php">
  <input type="hidden" value="<?php echo$_POST['점수'];?>" name="점수">
  <input type="image" src="X.png" width="50%" align="right" onclick="window.alert('흥선대원군은 1866년 프랑스 선교사와 천주교 신자를 죽이는 병인박해를 저질렀다.')">
</form>
</form>
</body>
</html>
