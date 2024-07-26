<html>
<head>
  <title>역사OX퀴즈</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
  <meta name="author" content="채희동">
  <meta charset="utf-8">
</head>
<body>
<img src="초시계.gif">
병인박해로 인해서 프랑스가 강화도를 침범해 병인양요가 일어났다.<br>
<form method="post" action="메인.php">
  <input type="hidden" value="<?php echo$_POST['점수']+1;?>" name="점수">
  <input type="image" src="O.png" width="50%" align="left">
</form>
<form method="post" action="게임오버.php">
  <input type="hidden" value="<?php echo$_POST['점수'];?>" name="점수">
  <input type="image" src="X.png" width="50%" align="right" onclick="window.alert('병인박해로 인해서 프랑스가 강화도를 침범해 병인양요가 일어났다')">
</form>
</form>
</body>
</html>
