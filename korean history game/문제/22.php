<html>
<head>
  <title>역사OX퀴즈</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
  <meta name="author" content="채희동">
  <meta charset="utf-8">
</head>
<body>
<img src="초시계.gif">
1876년 체결된 강화도 조약은 평등한 조약이다.<br>
<form method="post" action="게임오버.php">
  <input type="hidden" value="<?php echo$_POST['점수'];?>" name="점수">
  <input type="image" src="O.png" width="50%" align="left" onclick="window.alert('강화도 조약은 일본에게 치외 법권과 해양 측량권을 허용한 불평등 조약이었다.')">
</form>
<form method="post" action="메인.php">
  <input type="hidden" value="<?php echo$_POST['점수']+1;?>" name="점수">
  <input type="image" src="X.png" width="50%" align="right">
</form>
</form>
</body>
</html>
