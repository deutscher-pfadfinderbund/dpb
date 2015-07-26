<?php
$error = false;
$data['snippetsList'] = '';
$data['totalSnippets'] = '';
$data['returnMsg'] = '';
$data['returnDangerMsg'] = '';
if (file_exists('../langs/' . $_GET['language'] . '.php')) {
    $lang = $_GET['language'];
} else { // default
    $lang = 'en_EN';
}
require_once '../langs/' . $lang . '.php';
if (!isset($_GET['index']) || !is_numeric($_GET['index']) || !isset($_GET['title']) || !isset($_GET['code']) || !preg_match('`[a-zA-Z0-9_ -]{1,150}`', $_GET['title'])) {
    $error = true;
    if (!preg_match('`[a-zA-Z0-9_ -]{1,150}`', $_GET['title'])) {
        $return_msg = '<div class="alert alert-danger alert-dismissable"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>' . TITLE_MUST_MATCH . '</div>';
    } else {
        $return_msg = '<div class="alert alert-danger alert-dismissable"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>' . WRONG_DATA . '</div>';
    }
} else {
    require_once 'Snippets.php';
    $snippets = new Snippets('snippets.xml', true);
    $snippets->getSnippets();
    $out = $snippets->editSnippet($_GET['index'], utf8_decode(urldecode($_GET['title'])), utf8_decode(urldecode($_GET['code'])));
    $return_msg = '<div class="alert alert-success alert-dismissable"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>' . SNIPPET_UPDATED . '</div>';
    $return_danger_msg = '';
    if ($out === 'script_forbidden') {
        $return_danger_msg = '<div class="alert alert-danger alert-dismissable"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>' . SCRIPT_FORBIDDEN . '</div>';
    } elseif ($out === 'php_forbidden') {
        $return_danger_msg = '<div class="alert alert-danger alert-dismissable"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>' . PHP_FORBIDDEN . '</div>';
    }
}
if ($error == false) {
    $data['snippetsList']  = $snippets->render();
    $data['totalSnippets'] = $snippets->total_snippets;
}
$data['returnMsg'] = $return_msg;
$data['returnDangerMsg'] = $return_danger_msg;
echo json_encode($data);
