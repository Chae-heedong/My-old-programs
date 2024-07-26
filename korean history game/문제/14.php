<html>
<head>
  <title>역사OX퀴즈</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
  <meta name="author" content="채희동">
  <meta charset="utf-8">
</head>
<body>
<img src="초시계.gif">
1868년 조선이 미국과의 통상을 거부하자 미국인 오페르트가 남연군(흥선대원군의 아버지)의 묘지를 도굴하려 했다. <br>
<form method="post" action="게임오버.php">
  <input type="hidden" value="<?php echo$_POST['점수'];?>" name="점수">
  <input type="image" src="O.png" width="50%" align="left" onclick="window.alert('1868년 조선이 독일과의 통상을 거부하자 독일인 오페르트가 남연군(흥선대원군의 아버지)의 묘지를 도굴하려 했다. 이를 오페르트 도굴 사건이라고 부른다.')">
</form>
<form method="post" action="메인.php">
  <input type="hidden" value="<?php echo$_POST['점수']+1;?>" name="점수">
  <input type="image" src="X.png" width="50%" align="right">
</form>
</form>
</body>
</html>
