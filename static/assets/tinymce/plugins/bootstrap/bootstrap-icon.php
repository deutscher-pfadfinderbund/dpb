<?php
$bootstrap_css_path = addslashes($_GET['bootstrap_css_path']);

/* language */

if (file_exists('langs/' . $_GET['language'] . '.php')) {
    require_once 'langs/' . $_GET['language'] . '.php';
} else { // default
    require_once 'langs/en_EN.php';
}
if (isset($_GET['glyphicon'])) {
    $glyphicon = urldecode($_GET['glyphicon']);
    $iconSize  = urldecode($_GET['iconSize']);
    $iconColor = urldecode($_GET['iconColor']);
    $iconCode  = '<span class="glyphicon ' . $glyphicon . '" id="icon-test" style="font-size:' . $iconSize . ';color:' . $iconColor . '"></span>';
} else {
    $glyphicon = 'glyphicon-home';
    $iconSize  = false;
    $iconColor = false;
    $iconCode  = '<span class="glyphicon glyphicon-home" id="icon-test"></span>';
}
?>
<!DOCTYPE html>
<html lang="fr">
<head>
    <link rel="stylesheet" href="<?php echo $bootstrap_css_path; ?>">
    <link rel="stylesheet" href="css/plugin.min.css">
    <link rel="stylesheet" href="css/bootstrap-iconpicker.min.css">
    <link rel="stylesheet" media="screen" type="text/css" href="css/colorpicker.min.css" />
    <link href="google-code-prettify/prettify.css" type="text/css" rel="stylesheet" />
    <link href='http://fonts.googleapis.com/css?family=Source+Code+Pro' rel='stylesheet' type='text/css'>
</head>
<body>
    <div class="container">
        <div class="row margin-bottom-md ">
            <div class="choice-title">
                <span><?php echo ICON; ?></span>
            </div>
            <div class="text-center">
                <button class="btn btn-default" id="iconpicker"></button>
            </div>
        </div>
        <div class="row margin-bottom-md">
            <div class="choice-title">
                <span><?php echo ICON_SIZE; ?></span>
            </div>
            <div class="text-center">
                <div class="choice selector select-size margin-bottom-md">
                    <p><i class="glyphicon <?php echo $glyphicon; ?>"></i> extra-small</p>
                </div>
                <div class="choice selector select-size margin-bottom-md">
                    <h4><i class="glyphicon <?php echo $glyphicon; ?>"></i> small</h4>
                </div>
                <div class="choice selector select-size margin-bottom-md">
                    <h3><i class="glyphicon <?php echo $glyphicon; ?>"></i> medium</h3>
                </div>
                <div class="choice selector select-size margin-bottom-md">
                    <h2><i class="glyphicon <?php echo $glyphicon; ?>"></i> large</h2>
                </div>
                <strong><?php echo CUSTOM; ?></strong> : <input name="size-input" size="10" value=""> <strong>px</strong>
            </div>
        </div>
        <div class="row margin-bottom-md ">
            <div class="choice-title">
                <span><?php echo COLOR; ?></span>
            </div>
            <div class="text-center">
                <div class="choice selector select-color">
                    <span class="color btn-default"></span>
                </div>
                <div class="choice selector select-color">
                    <span class="color btn-primary"></span>
                </div>
                <div class="choice selector select-color">
                    <span class="color btn-success"></span>
                </div>
                <div class="choice selector select-color">
                    <span class="color btn-info"></span>
                </div>
                <div class="choice selector select-color">
                    <span class="color btn-warning"></span>
                </div>
                <div class="choice selector select-color">
                    <span class="color btn-danger"></span>
                </div>
                <div id="colorselector">
                    <label><?php echo CUSTOM; ?> : </label><div style="background-color: rgb(239, 239, 239);"></div>
                </div>
            </div>
        </div>
        <div class="row" id="preview">
            <div id="preview-title">
                <span class="btn-primary"><?php echo PREVIEW; ?></span>
            </div>
            <!-- don't remove beginning space,
            otherwise tinymce will not allow empty tag and will remove your icon -->
            <div class="col-sm-12 margin-bottom-md text-center test-icon-wrapper" id="test-wrapper">
                &nbsp;<?php echo $iconCode; ?>
            </div>
        </div>
        <div class="row">
            <div id="code-title">
                <a href="#" id="code-slide-link">code <i class="glyphicon glyphicon-arrow-up"></i></a>
            </div>
            <div class="col-sm-12 text-center" id="code-wrapper">
                <pre><?php
                    echo htmlspecialchars($iconCode);
                    ?></pre>
            </div>
        </div>
    </div>
<script type="text/javascript" src="js/jquery-2.1.1.min.js"></script>
<script type="text/javascript" src="js/bootstrap.min.js"></script>
<script type="text/javascript" src="js/colorpicker.min.js"></script>
<script type="text/javascript" src="js/utils.min.js"></script>
<script type="text/javascript" src="js/jquery.htmlClean.min.js"></script>
<script type="text/javascript" src="js/iconset/iconset-glyphicon.min.js"></script>
<script type="text/javascript" src="js/bootstrap-iconpicker.min.js"></script>
<script type="text/javascript" src="google-code-prettify/prettify.js"></script>
<script type="text/javascript">
    var glyphicon = '<?php echo $glyphicon; ?>'; //console.log(glyphicon);
    var iconSize  = '<?php echo $iconSize; ?>'; // console.log(iconSize);
    var iconColor = '<?php echo $iconColor; ?>'; //console.log(iconColor);
    var iconCode  = '<?php echo $iconCode; ?>'; //console.log(iconCode);

    $(document).ready(function () {

        makeResponsive();
        getBootstrapStyles();

        /* icon size */

        if (!iconSize) { // default size
            iconSize = $('.selector.select-size h3').css('font-size');
        }

        if (!iconColor) {
            iconColor = $('.selector.select-color .btn-primary').attr('data-color');
        }

        $('.selector.select-size').each(function (event, element) {

            /* select the good one on load ; */

            if ($(element).find('i').css('font-size') == iconSize) {
                $(element).addClass('active');
            }

            /* set color on load */

            $('.selector.select-size i').css('color', iconColor);

            $(element).on('click', function (event) {
                $('.selector.select-size').removeClass('active');
                $(this).addClass('active');
                iconSize = $(this).find('i').parent().css('font-size');
                $('#icon-test').css('font-size', iconSize);
                iconCode = $('#test-wrapper').html();
                updateCode();
            });
        });

        /* if none selected, add custom size into input on load */

        if (!$('.selector.select-size').hasClass('active')) {
            $('input[name="size-input"]').val(<?php echo str_replace('px', '', $iconSize); ?>);
        }

        $('input[name="size-input"]').on('keyup', function () {
            var value = $(this).prop('value');
            if (value > 0) {
                iconSize = $(this).prop('value') + 'px';
                $('#icon-test').css('font-size', iconSize);
                $('.selector.select-size').removeClass('active');
                iconCode = $('#test-wrapper').html();
                updateCode();
            } else {
                iconSize = $('.selector.select-size.active').find('i').parent().css('font-size');
                $('#icon-test').css('font-size', iconSize);
                updateCode();
            }
        });

        /* color selectors */

        $('.selector.select-color').each(function (event, element) {

            /* select the good one on load ; */

            $(element).find('span.color').attr('data-color', $(element).find('span.color').css('background-color')); // we catch background because it changes on hover
            if ($(element).find('span.color').attr('data-color') == iconColor) {
                $(element).addClass('active');
            }
            $(element).on('click', function (event) {
                $('.selector.select-color').removeClass('active');
                $(this).addClass('active');
                iconColor = $(this).find('span').attr('data-color');
                $('.selector .glyphicon').css('color', iconColor);
                $('#icon-test').css('color', iconColor);
                $('#iconpicker i.glyphicon').css('color', iconColor);
                iconCode = $('#test-wrapper').html();
                updateCode();
            });
        });

        /* color picker */

        /* select the good one on load */

        $('#colorselector div').css('background-color', iconColor);

        /* instanciate colorpicker */

        $('#colorselector').ColorPicker({
            color: iconColor,
            onShow: function (colpkr) {
                $(colpkr).fadeIn(500);

                return false;
            },
            onHide: function (colpkr) {
                $(colpkr).fadeOut(500);

                return false;
            },
            onChange: function (hsb, hex, rgb) {
                iconColor = '#' + hex;
                $('.selector .glyphicon').css('color', iconColor);
                $('#colorselector div').css('background-color', iconColor);
                $('#icon-test').css('color', iconColor);
                $('#iconpicker i.glyphicon').css('color', iconColor);
                $('.selector.select-color').removeClass('active');
                iconCode = $('#test-wrapper').html();
                updateCode();
            }
        });

        /* icon picker */

        $('#iconpicker').iconpicker({
            arrowClass: 'btn-success',
            arrowPrevIconClass: 'glyphicon glyphicon-chevron-left',
            arrowNextIconClass: 'glyphicon glyphicon-chevron-right',
            cols: 5,
            icon: glyphicon,
            iconset: 'glyphicon',
            labelHeader: '{0} of {1} pages',
            labelFooter: '{0} - {1} of {2} icons',
            placement: 'bottom',
            rows: 10,
            cols: 20,
            search: false,
            selectedClass: 'btn-success',
            unselectedClass: ''
        }).on('change', function (e) {
            changeIcon();
        });

        $('#iconpicker i.glyphicon').css('color', iconColor);

        /* icon */

        function changeIcon()
        {
            var newGlyphicon = $('#iconpicker').find('input[type="hidden"]').prop('value');
            iconCode = iconCode.replace(glyphicon, newGlyphicon);
            $('.selector.select-size i').removeClass(glyphicon).addClass(newGlyphicon);
            $('#test-wrapper').html(iconCode);
            glyphicon = newGlyphicon;
            updateCode();
        }

        /* update code on load */

        if ($('.selector.select-size').hasClass('active')) {
            $('.selector.select-size.active').trigger('click');
        } else { // if custom size
            $('input[name="size-input"]').trigger('keyup');
        }
    });
</script>
</body>
</html>
