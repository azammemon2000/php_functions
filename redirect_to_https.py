<?php
// Will redirect to same page on https instead of http

  if($_SERVER["HTTPS"] != "on")
  {
      header("Location: https://" . $_SERVER["HTTP_HOST"] . $_SERVER["REQUEST_URI"]);
      exit();
  }
?>
