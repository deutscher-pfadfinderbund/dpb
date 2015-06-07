/**
 * TinyMce Bootstrap plugin
 *
 * @version 1.1.0
 * @author Gilles Migliori - gilles.migliori@gmail.com
 *
 */

/*jshint globalstrict: true, unused:false*/
/*global $, jQuery, tinymce, window, document*/
'use strict';

tinymce.PluginManager.requireLangPack('bootstrap');
tinymce.PluginManager.add('bootstrap', function(editor, url) {

    var iFrameDefaultWidth = 885,
        bootstrapElements,
        bootstrapDefaultCssPath,
        bootstrapCssPath,
        DefaultImagesPath,
        imagesPath;

    /* Default Bootstrap Elements */

    if(typeof(editor.settings.bootstrapConfig.bootstrapElements) == 'undefined') {
        editor.settings.bootstrapConfig.bootstrapElements = {
            'btn': true,
            'icon': true,
            'image': true,
            'table': true,
            'template': true,
            'breadcrumb': true,
            'pagination': true,
            'pager': true,
            'label': true,
            'badge': true,
            'alert': true,
            'panel': true,
            'snippet': true
        };
    }

    bootstrapElements = editor.settings.bootstrapConfig.bootstrapElements;

    if(typeof(editor.settings.bootstrapConfig) == 'undefined') {
        editor.settings.bootstrapConfig = [
        ];
    }

    /* Set valid elements to prevent tinymce from removing glyphicon or other empty tags */

    if ((editor.settings.verify_html !== false || editor.settings.valid_elements !== '*[*]') && editor.settings.bootstrapConfig.overwriteValidElements !== false) {
        editor.settings.valid_elements = getValidElements();
    }

    /* Default Bootstrap css path */

    if(typeof(editor.settings.bootstrapConfig.bootstrapCssPath) == 'undefined') {
        bootstrapDefaultCssPath = url + '/css/bootstrap.min.css';
        editor.settings.bootstrapConfig.bootstrapCssPath = bootstrapDefaultCssPath;
    }
    bootstrapCssPath = editor.settings.bootstrapConfig.bootstrapCssPath;

    /* Default Images path */

    if(typeof(editor.settings.bootstrapConfig.imagesPath) == 'undefined') {
        DefaultImagesPath = url + '/';
        editor.settings.bootstrapConfig.imagesPath = {'imagesPath': DefaultImagesPath};
    }
    imagesPath = editor.settings.bootstrapConfig.imagesPath;

    /* Snippet Management (Allow / Disallow) */

    if(typeof(editor.settings.bootstrapConfig.bootstrapElements.snippet === true && editor.settings.bootstrapConfig.allowSnippetManagement) == 'undefined') {
        editor.settings.bootstrapConfig.allowSnippetManagement = true;
    }

    /* Add Bootstrap css to editor */

    var content_css = editor.settings.content_css;
    if(typeof(content_css) == 'undefined') {
        content_css = bootstrapCssPath + ',' + url + '/css/editor-content.min.css';
    } else {
        content_css = content_css + ',' + bootstrapCssPath + ',' + url + '/css/editor-content.min.css';
    }
    editor.settings.content_css = content_css;

    /**
     * Open iframe dialog,
     * Get and transmit selected element attributes to iframe
     * @param  string iframeUrl
     * @param  string iframeTitle
     * @param  string iframeHeight
     * @param  string type      the dialog to display
     * (bsBtn|bsIcon|bsImage|bsTable|bsTemplate|bsBreadcrumb|bsPagination|bsPager|bsLabel|bsBadge|bsAlert|bsPanel|bsSnippet)
     * @return void
     */
    function showDialog(iframeUrl, iframeTitle, iframeHeight, type)
    {

        /* get selected element values to transmit to iframe */

        var selectedNode = getSelectedNode();
        var nodeAttributes = '';
        if($(selectedNode).hasClass('active')) {
            if($(selectedNode).hasClass('btn')) {
                nodeAttributes = getNodeAttributes(selectedNode, 'bsBtn');
            } else if($(selectedNode).hasClass('glyphicon')) {
                nodeAttributes = getNodeAttributes(selectedNode, 'bsIcon');
            } else  if($(selectedNode).is('img')) {
                nodeAttributes = getNodeAttributes(selectedNode, 'bsImage');
            } else if($(selectedNode).hasClass('table')) {
                nodeAttributes = getNodeAttributes(selectedNode, 'bsTable');
            } else if($(selectedNode).hasClass('breadcrumb')) {
                nodeAttributes = getNodeAttributes(selectedNode, 'bsBreadcrumb');
            } else if($(selectedNode).hasClass('pagination')) {
                nodeAttributes = getNodeAttributes(selectedNode, 'bsPagination');
            } else if($(selectedNode).hasClass('pager')) {
                nodeAttributes = getNodeAttributes(selectedNode, 'bsPager');
            } else if($(selectedNode).hasClass('label')) {
                nodeAttributes = getNodeAttributes(selectedNode, 'bsLabel');
            } else if($(selectedNode).hasClass('badge')) {
                nodeAttributes = getNodeAttributes(selectedNode, 'bsBadge');
            } else if($(selectedNode).hasClass('alert')) {
                nodeAttributes = getNodeAttributes(selectedNode, 'bsAlert');
            } else if($(selectedNode).hasClass('panel')) {
                nodeAttributes = getNodeAttributes(selectedNode, 'bsPanel');
            }
        }
        var getTheHtml = function (){
            var html = '';
            var language = tinymce.activeEditor.getParam('language');
            if(!language) {
                language = 'en_EN';
            }
            html += '<input type="hidden" name="bs-code" id="bs-code" />';
            var qrySign = '?';
            if(iframeUrl.match(/\?/)) {
                qrySign = '&';
            }
            html += '<iframe src="'+ url + '/' + iframeUrl + qrySign + 'language=' + language + '&images_path=' + imagesPath + '&bootstrap_css_path=' + bootstrapCssPath + '&' + nodeAttributes + '&' + new Date().getTime() + '"></iframe>';

            return html;
        };

        var iFrameWidth = iFrameDefaultWidth;

        if($(window).width() < 885) {
            iFrameWidth = $(window).width()*0.9;
        }

        if($(window).height() > iframeHeight) {
            iframeHeight = ($(window).height()*0.9) - 90;
        }

        var win = editor.windowManager.open({
            title: iframeTitle,
            width : iFrameWidth,
            height : iframeHeight,
            html: getTheHtml(),
            buttons: [
                {
                    text: 'OK',
                    subtype: 'primary',
                    onclick: function(element) {
                        renderContent(element, type);
                        this.parent().parent().close();
                    }
                },
                {
                    text: 'Cancel',
                    onclick: function() {
                        this.parent().parent().close();
                    }
                }
            ]
        });

        /* OK / Cancel buttons position for responsive */

        $('.mce-floatpanel').find('.mce-widget.mce-abs-layout-item.mce-first').css({'left':'auto', 'right':'82px'});
        $('.mce-floatpanel').find('.mce-widget.mce-last.mce-abs-layout-item').css({'left':'auto', 'right':'10px'});

        $(window).on('resize', function() {
            resizeDialog();
        });
    }

    function resizeDialog()
    {
        var iFrameWidth = iFrameDefaultWidth;
        if($(window).width() > iFrameDefaultWidth) {
            iFrameWidth = iFrameDefaultWidth;
        } else {
            iFrameWidth = $(window).width()*0.9;
        }
        $('.mce-floatpanel').width(iFrameWidth).css('left', ($(window).width() - iFrameWidth) / 2);
        $('.mce-floatpanel').find('.mce-container-body, .mce-foot, .mce-abs-layout').width(iFrameWidth);
        if(iFrameWidth < 768) {
            $('iframe').contents().find('.container').addClass('container-xs');
        } else {
            $('iframe').contents().find('.container').removeClass('container-xs');
        }
    }

    /**
     * gets the selected node in editor, or the active parent matching a bootstrap element
     * @return matching bootstrap element
     */
    function getSelectedNode()
    {
        var selectedNode = editor.selection.getNode();
        if(!$(selectedNode).hasClass('active') || $(selectedNode).closest('ol.breadcrumb').length > 0 || $(selectedNode).closest('ul.pagination').length > 0 || $(selectedNode).closest('ul.pager').length > 0 || $(selectedNode).closest('div.alert').length > 0) { // li without link HAS class 'active' in bootstrap

            /* look for .table|.breadcrumb|.pagination|.pager|.alert|.panel in parents */

            var classes = ['.table', '.breadcrumb', '.pagination', '.pager', '.alert', '.panel'];
            var found = false;

            for (var i = 0; i < classes.length; i++) {
                if($(selectedNode).closest(classes[i]).length > 0 && found === false) {
                    selectedNode = $(selectedNode).closest(classes[i]);
                    found = true;
                }
            }
        }

        return selectedNode;
    }

    /**
     * insert|update editor content
     * @param  string element the 'ok' button of iframe
     * @param  string type    type of content to insert|update
     *                        (bsBtn|bsIcon|bsImage|bsTable|bsTemplate|bsBreadcrumb|bsPagination|bsPager|bsLabel|bsBadge|bsAlert|bsPanel)
     * @return void
     */
    function renderContent(element, type)
    {
        var markup = htmlDecode(document.getElementById('bs-code').value) + '<p></p>';
        var selectedNode = getSelectedNode();
        if($(selectedNode).hasClass('active')) {

            /* insert new content */

            $(selectedNode).after(markup);

            /* remove old content */

            var typesClasses = {
                'bsBtn': 'btn',
                'bsIcon': 'glyphicon',
                'bsImage': 'img',
                'bsTable': 'table',
                'bsBreadcrumb': 'breadcrumb',
                'bsPagination': 'pagination',
                'bsPager': 'pager',
                'bsLabel': 'label',
                'bsBadge': 'badge',
                'bsAlert': 'alert',
                'bsPanel': 'panel'
            };

            for(var key in typesClasses)
            {
              var value = typesClasses[key];
                if(type == key) {
                    if(type == 'bsImage' && $(selectedNode).is('img')) {
                        editor.dom.remove(selectedNode);
                    } else if($(selectedNode).hasClass(value)) { // remove old element
                        editor.dom.remove(selectedNode);
                    }
                }
            }
        } else {

            /* if none selected, insert new content */

            editor.insertContent(markup);
        }
        /* remove the '<br data-mce-bogus="1"> added by tinyMce in pagination with firefox */
        tinymce.activeEditor.dom.remove(tinymce.activeEditor.dom.select('br[data-mce-bogus="1"]'));
    }

    /**
     * get selected node attributes to transmit to iframe
     * @param  string selectedNode
     * @param  string type         type of the clicked btn
     *                             (bsBtn|bsIcon|bsImage|bsTable|bsTemplate|bsBreadcrumb|bsPagination|bsPager|bsLabel|bsBadge|bsAlert|bsPanel)
     * @return string              node attributes
     */
    function getNodeAttributes(selectedNode, type)
    {
        var urlString = '';
        if(type == 'bsBtn') {
            var i;
            var btnCode = $(selectedNode)[0].outerHTML.replace(' active', '');
            var btnIcon = '';
            if($(selectedNode).find('span')[0]) {
                btnIcon = $(selectedNode).find('span').attr('class').split(' ')[1];
            }
            var styles = new Array('default', 'btn-primary', 'btn-success', 'btn-info', 'btn-warning', 'btn-danger');
            var btnStyle = '';
            for (i = styles.length - 1; i >= 0; i--) {
                if($(selectedNode).hasClass(styles[i])) {
                    btnStyle = styles[i];
                }
            }
            var sizes = new Array('btn-xs', 'btn-sm', 'btn-lg');
            var btnSize = '';
            for (i = sizes.length - 1; i >= 0; i--) {
                if($(selectedNode).hasClass(sizes[i])) {
                    btnSize = sizes[i];
                }
            }
            var btnTag = $(selectedNode).prop('tagName').toLowerCase();
            var btnHref = '';
            if(btnTag == 'a') {
                btnHref = $(selectedNode).attr('href');
            }
            var btnType = '';
            if(btnTag == 'button' || btnTag == 'input') {
                btnType = $(selectedNode).attr('type');
            }
            var btnText;
            if(btnTag == 'button' || btnTag == 'a') {
                btnText = $(selectedNode).remove('i').text();
            } else {
                btnText = $(selectedNode).val();
            }
            var iconPos = 'prepend';
            if($(selectedNode).find('span')[0]) {
                var reg = new RegExp('/^' + btnText + '/');
                if(reg.test($(selectedNode).html()) === true) {
                    iconPos = 'append';
                }
            }
            btnCode   = encodeURIComponent(btnCode);
            btnIcon   = encodeURIComponent(btnIcon);
            btnStyle  = encodeURIComponent(btnStyle);
            btnSize   = encodeURIComponent(btnSize);
            btnTag    = encodeURIComponent(btnTag);
            btnHref   = encodeURIComponent(btnHref);
            btnType   = encodeURIComponent(btnType);
            btnText   = encodeURIComponent(btnText);
            iconPos   = encodeURIComponent(iconPos);
            urlString =  'btnCode=' + btnCode + '&btnIcon=' + btnIcon + '&btnStyle=' + btnStyle + '&btnSize=' + btnSize + '&btnTag=' + btnTag + '&btnHref=' + btnHref + '&btnType=' + btnType + '&btnText=' + btnText + '&iconPos=' + iconPos;
        }
        else if(type == 'bsImage') {
            var imgSrc       = $(selectedNode).attr('src');
            var imgAlt       = '';
            var imgWidth     = '';
            var imgHeight    = '';
            var imgStyle     = '';
            var imgResponsive = 'false';
            if($(selectedNode).hasClass('img-rounded')) {
                imgStyle = 'img-rounded';
            } else if($(selectedNode).hasClass('img-circle')) {
                imgStyle = 'img-circle';
            } else if($(selectedNode).hasClass('img-thumbnail')) {
                imgStyle = 'img-thumbnail';
            }
            if($(selectedNode).hasClass('img-responsive')) {
                imgResponsive = 'true';
            }
            if($(selectedNode).attr('alt')) {
                imgAlt       = $(selectedNode).attr('alt');
            }
            if($(selectedNode).attr('width')) {
                imgWidth       = $(selectedNode).attr('width');
            }
            if($(selectedNode).attr('height')) {
                imgHeight       = $(selectedNode).attr('height');
            }
            imgSrc    = encodeURIComponent(imgSrc);
            imgAlt    = encodeURIComponent(imgAlt);
            imgWidth  = encodeURIComponent(imgWidth);
            imgHeight = encodeURIComponent(imgHeight);
            imgStyle  = encodeURIComponent(imgStyle);
            urlString =  'imgSrc=' + imgSrc + '&imgAlt=' + imgAlt + '&imgWidth=' + imgWidth + '&imgHeight=' + imgHeight + '&imgStyle=' + imgStyle + '&imgResponsive=' + imgResponsive;
        } else if(type == 'bsIcon') {
            var glyphicon = $(selectedNode).attr('class').split(' ')[1];
            var iconSize  = $(selectedNode).css('font-size');
            var iconColor = $(selectedNode).css('color');
            glyphicon = encodeURIComponent(glyphicon);
            iconSize  = encodeURIComponent(iconSize);
            iconColor = encodeURIComponent(iconColor);
            urlString =  'glyphicon=' + glyphicon + '&iconSize=' + iconSize + '&iconColor=' + iconColor;
        }
        else if(type == 'bsTable') {
            selectedNode = $(selectedNode).closest('.table');
            var tableStriped    = 'false';
            var tableBordered   = 'false';
            var tableHover      = 'false';
            var tableCondensed  = 'false';
            var tableResponsive = 'false';
            if($(selectedNode).hasClass('table-striped')) {
                tableStriped = 'true';
            }
            if($(selectedNode).hasClass('table-bordered')) {
                tableBordered = 'true';
            }
            if($(selectedNode).hasClass('table-hover')) {
                tableHover = 'true';
            }
            if($(selectedNode).hasClass('table-condensed')) {
                tableCondensed = 'true';
            }
            if($(selectedNode).hasClass('table-responsive')) {
                tableResponsive = 'true';
            }
            urlString =  'tableStriped=' + tableStriped + '&tableBordered=' + tableBordered + '&tableHover=' + tableHover + '&tableCondensed=' + tableCondensed + '&tableResponsive=' + tableResponsive;
        }
        else if(type == 'bsBreadcrumb' || type == 'bsPagination' || type == 'bsPager' || type == 'bsLabel' || type == 'bsBadge' || type == 'bsAlert'| type == 'bsPanel') {
            urlString =  'edit=true';
        }

        return urlString;
    }

    function htmlDecode(input){
        var e = document.createElement('div');
        e.innerHTML = input;
        return e.childNodes.length === 0 ? '' : e.childNodes[0].nodeValue;
    }

    // Add custom css for toolbar icons

    editor.on('init', function()
    {
        var cssURL = url + '/css/editor.min.css';
        if(document.createStyleSheet){
            document.createStyleSheet(cssURL);
        } else {
            var cssLink = editor.dom.create('link', {
                        rel: 'stylesheet',
                        href: cssURL
                      });
            document.getElementsByTagName('head')[0].
                      appendChild(cssLink);
        }
        initCallbackEvents();
    });

    /* callback events to select bootstrap elements on click and allow updates */

    /**
     * initCallbackEvents
     * @return void
     */
    function initCallbackEvents()
    {
        tinymce.activeEditor.on('click keyup', function(e) {
            var elementSelector = '';
            var editorBtnName = '';
            if($(e.target).is('img')) { // image
                elementSelector = 'img';
                editorBtnName = 'insertImageBtn';
            } else if($(e.target).attr('class')) {
                if($(e.target).attr('class').match(/btn/)) {
                    elementSelector = '.btn';
                    editorBtnName = 'insertBtnBtn';
                } else if($(e.target).attr('class').match(/glyphicon/)) {
                    elementSelector = '.glyphicon';
                    editorBtnName = 'insertIconBtn';
                } else if($(e.target).attr('class').match(/label/)) {
                    elementSelector = '.label';
                    editorBtnName = 'insertLabelBtn';
                } else if($(e.target).attr('class').match(/badge/)) {
                    elementSelector = '.badge';
                    editorBtnName = 'insertBadgeBtn';
                } else if($(e.target).attr('class').match(/alert/)) {
                    elementSelector = '.alert';
                    editorBtnName = 'insertAlertBtn';
                }
            } else if($(e.target).closest('.table').attr('class')) { // table
                elementSelector = '.table';
                editorBtnName = 'insertTableBtn';
            } else if($(e.target).closest('.breadcrumb').attr('class')) { // breadcrumb
                elementSelector = '.breadcrumb';
                editorBtnName = 'insertBreadcrumbBtn';
            } else if($(e.target).closest('.pagination').attr('class')) { // pagination
                elementSelector = '.pagination';
                editorBtnName = 'insertPaginationBtn';
            } else if($(e.target).closest('.pager').attr('class')) { // pager
                elementSelector = '.pager';
                editorBtnName = 'insertPagerBtn';
            } else if($(e.target).closest('.alert').attr('class')) { // alert
                elementSelector = '.alert';
                editorBtnName = 'insertAlertBtn';
            } else if($(e.target).closest('.panel').attr('class')) { // panel
                elementSelector = '.panel';
                editorBtnName = 'insertPanelBtn';
            }

            /* deactivate all previous activated */

            deactivateAll();

            if(elementSelector === '') {
                return;
            }

            /* activate current */

            activate(e.target, elementSelector, editorBtnName);
        });
        deactivateAll(); // onLoad
    }

    function activate(element, elementSelector, editorBtnName)
    {
        if(elementSelector == '.glyphicon') {
            editor.selection.setCursorLocation(element);
        } else if(elementSelector == '.btn') {
            editor.selection.setCursorLocation(element, true);
        }
        if(elementSelector == '.table') {
            $(element).closest('.table').addClass('active');
            toggleEditorButton(editorBtnName, 'on');
        } else if(elementSelector == '.breadcrumb') {
            $(element).closest('.breadcrumb').addClass('active');
            toggleEditorButton(editorBtnName, 'on');
        } else if(elementSelector == '.pagination') {
            $(element).closest('.pagination').addClass('active');
            toggleEditorButton(editorBtnName, 'on');
        } else if(elementSelector == '.pager') {
            $(element).closest('.pager').addClass('active');
            toggleEditorButton(editorBtnName, 'on');
        } else if(elementSelector == '.alert') {
            $(element).closest('.alert').addClass('active');
            toggleEditorButton(editorBtnName, 'on');
        } else if(elementSelector == '.panel') {
            $(element).closest('.panel').addClass('active');
            toggleEditorButton(editorBtnName, 'on');
        } else {
            $(element).addClass('active');
            toggleEditorButton(editorBtnName, 'on');
        }
    }

    function deactivateAll()
    {
        var elements = new Array('.btn', '.glyphicon', 'img', '.table', '.breadcrumb', '.pagination', '.pager', '.label', '.badge', '.alert', '.panel');
        for (var i = 0; i < elements.length; i++) {
            $(editor.dom.select(elements[i])).removeClass('active');
        }
        toggleEditorButton('allBtns', 'off');
    }

    function toggleEditorButton(editorBtnName, onOff)
    {
        var editorBtns = editor.buttons.bootstrap.items;
        for (var i = editorBtns.length - 1; i >= 0; i--) {
            if(editorBtnName == 'allBtns' || editorBtns[i]._name == editorBtnName) {
                if(onOff == 'on') {
                    editorBtns[i].addClass('active');
                } else {
                    editorBtns[i].removeClass('active');
                }
            }
        }
    }

    var bsItems = [];

    // Create and render a buttongroup with buttons

    var bs3Btn = tinymce.ui.Factory.create({
        type: 'button',
        text: '',
        classes: 'widget btn bs-icon-btn',
        icon: 'bootstrap-icon',
        tooltip: 'Bootstrap Elements'
    });
    bsItems.push(bs3Btn);
    if(bootstrapElements.btn) {
        var insertBtn = tinymce.ui.Factory.create({
            type: 'button',
            classes: 'widget btn bs-icon-btn',
            // text: 'btn',
            icon: 'icon-btn',
            name: 'insertBtnBtn',
            tooltip: 'Insert/Edit Bootstrap Button',
            onclick: function() {
                showDialog('bootstrap-btn.php', 'Insert/Edit Bootstrap Button', 580, 'bsBtn');
            }
        });
        bsItems.push(insertBtn);
    }
    if(bootstrapElements.image) {
        var insertImage = tinymce.ui.Factory.create({
            type: 'button',
            classes: 'widget btn bs-icon-btn',
            icon: 'icon-image',
            name: 'insertImageBtn',
            tooltip: 'Insert/Edit Bootstrap Image',
            onclick: function() {
                showDialog('bootstrap-image.php', 'Insert/Edit Bootstrap Image', 580, 'bsImage');
            }
        });
        bsItems.push(insertImage);
    }
    if(bootstrapElements.icon) {
        var insertIcon = tinymce.ui.Factory.create({
            type: 'button',
            classes: 'widget btn bs-icon-btn',
            icon: 'icon-icon',
            name: 'insertIconBtn',
            tooltip: 'Insert/Edit Bootstrap Icon',
            onclick: function() {
                showDialog('bootstrap-icon.php', 'Insert/Edit Bootstrap Icon', 450, 'bsIcon');
            }
        });
        bsItems.push(insertIcon);
    }
    if(bootstrapElements.table) {
        var insertTable = tinymce.ui.Factory.create({
            type: 'button',
            classes: 'widget btn bs-icon-btn',
            icon: 'icon-table',
            name: 'insertTableBtn',
            tooltip: 'Insert/Edit Bootstrap Table',
            onclick: function() {
                showDialog('bootstrap-table.php', 'Insert/Edit Bootstrap Table', 620, 'bsTable');
            }
        });
        bsItems.push(insertTable);
    }
    if(bootstrapElements.template) {
        var insertTemplate = tinymce.ui.Factory.create({
            type: 'button',
            classes: 'widget btn bs-icon-btn',
            icon: 'icon-template',
            name: 'insertTemplateBtn',
            tooltip: 'Insert Bootstrap Template',
            onclick: function() {
                showDialog('bootstrap-template.php', 'Insert Bootstrap Template', 580, 'bsTemplate');
            }
        });
        bsItems.push(insertTemplate);
    }
    if(bootstrapElements.breadcrumb) {
        var insertBreadcrumb = tinymce.ui.Factory.create({
            type: 'button',
            classes: 'widget btn bs-icon-btn',
            icon: 'icon-breadcrumb',
            name: 'insertBreadcrumbBtn',
            tooltip: 'Insert/Edit Bootstrap Breadcrumb',
            onclick: function() {
                showDialog('bootstrap-breadcrumb.php', 'Insert/Edit Bootstrap Breadcrumb', 580, 'bsBreadcrumb');
            }
        });
        bsItems.push(insertBreadcrumb);
    }
    if(bootstrapElements.pagination) {
        var insertPagination = tinymce.ui.Factory.create({
            type: 'button',
            classes: 'widget btn bs-icon-btn',
            icon: 'icon-pagination',
            name: 'insertPaginationBtn',
            tooltip: 'Insert/Edit Bootstrap Pagination',
            onclick: function() {
                showDialog('bootstrap-pagination.php', 'Insert/Edit Bootstrap Pagination', 650, 'bsPagination');
            }
        });
        bsItems.push(insertPagination);
    }
    if(bootstrapElements.pager) {
        var insertPager = tinymce.ui.Factory.create({
            type: 'button',
            classes: 'widget btn bs-icon-btn',
            icon: 'icon-pager',
            name: 'insertPagerBtn',
            tooltip: 'Insert/Edit Bootstrap Pager',
            onclick: function() {
                showDialog('bootstrap-pager.php', 'Insert/Edit Bootstrap Pager', 450, 'bsPager');
            }
        });
        bsItems.push(insertPager);
    }
    if(bootstrapElements.label) {
        var insertLabel = tinymce.ui.Factory.create({
            type: 'button',
            classes: 'widget btn bs-icon-btn',
            icon: 'icon-label',
            name: 'insertLabelBtn',
            tooltip: 'Insert/Edit Bootstrap Label',
            onclick: function() {
                showDialog('bootstrap-label.php', 'Insert/Edit Bootstrap Label', 350, 'bsLabel');
            }
        });
        bsItems.push(insertLabel);
    }
    if(bootstrapElements.badge) {
        var insertBadge = tinymce.ui.Factory.create({
            type: 'button',
            classes: 'widget btn bs-icon-btn',
            icon: 'icon-badge',
            name: 'insertBadgeBtn',
            tooltip: 'Insert/Edit Bootstrap Badge',
            onclick: function() {
                showDialog('bootstrap-badge.php', 'Insert/Edit Bootstrap Badge', 350, 'bsBadge');
            }
        });
        bsItems.push(insertBadge);
    }
    if(bootstrapElements.alert) {
        var insertAlert = tinymce.ui.Factory.create({
            type: 'button',
            classes: 'widget btn bs-icon-btn',
            icon: 'icon-alert',
            name: 'insertAlertBtn',
            tooltip: 'Insert/Edit Bootstrap Alert',
            onclick: function() {
                showDialog('bootstrap-alert.php', 'Insert/Edit Bootstrap Alert', 580, 'bsAlert');
            }
        });
        bsItems.push(insertAlert);
    }
    if(bootstrapElements.panel) {
        var insertPanel = tinymce.ui.Factory.create({
            type: 'button',
            classes: 'widget btn bs-icon-btn',
            icon: 'icon-panel',
            name: 'insertPanelBtn',
            tooltip: 'Insert/Edit Bootstrap Panel',
            onclick: function() {
                showDialog('bootstrap-panel.php', 'Insert/Edit Bootstrap Panel', 650, 'bsPanel');
            }
        });
        bsItems.push(insertPanel);
    }
    if(bootstrapElements.snippet) {
        var insertSnippet = tinymce.ui.Factory.create({
            type: 'button',
            classes: 'widget btn bs-icon-btn',
            icon: 'icon-snippet',
            name: 'insertSnippetBtn',
            tooltip: 'Insert/Edit Snippet',
            onclick: function() {
                showDialog('bootstrap-snippet.php?allowEdit=' + editor.settings.bootstrapConfig.allowSnippetManagement, 'Insert Snippet', 650, 'bsSnippet');
            }
        });
        bsItems.push(insertSnippet);
    }
    editor.addButton('bootstrap', {
        type: 'buttongroup',
        classes: 'bs-btn',
        items: bsItems
    });

    /**
     * set tinymce valid_elements according to html5 shema
     * based on veprbl / html5_valid_elements.js
     * https://gist.github.com/veprbl/1136304
     * @return string
     */
    function getValidElements()
    {
        var valid_elements = '@[accesskey|draggable|style|class|hidden|tabindex|contenteditable|id|title|contextmenu|lang|dir<ltr?rtl|spellcheck|onabort|onerror|onmousewheel|onblur|onfocus|onpause|oncanplay|onformchange|onplay|oncanplaythrough|onforminput|onplaying|onchange|oninput|onprogress|onclick|oninvalid|onratechange|oncontextmenu|onkeydown|onreadystatechange|ondblclick|onkeypress|onscroll|ondrag|onkeyup|onseeked|ondragend|onload|onseeking|ondragenter|onloadeddata|onselect|ondragleave|onloadedmetadata|onshow|ondragover|onloadstart|onstalled|ondragstart|onmousedown|onsubmit|ondrop|onmousemove|onsuspend|ondurationmouseout|ontimeupdate|onemptied|onmouseover|onvolumechange|onended|onmouseup|onwaiting],a[target<_blank?_self?_top?_parent|ping|media|href|hreflang|type|rel<alternate?archives?author?bookmark?external?feed?first?help?index?last?license?next?nofollow?noreferrer?prev?search?sidebar?tag?up],abbr,address,area[alt|coords|shape|href|target<_blank?_self?_top?_parent|ping|media|hreflang|type|shape<circle?default?poly?rect|rel<alternate?archives?author?bookmark?external?feed?first?help?index?last?license?next?nofollow?noreferrer?prev?search?sidebar?tag?up],article,aside,audio[src|preload<none?metadata?auto|autoplay<autoplay|loop<loop|controls<controls|mediagroup],blockquote[cite],body,br,button[autofocus<autofocus|disabled<disabled|form|formaction|formenctype|formmethod<get?put?post?delete|formnovalidate?novalidate|formtarget<_blank?_self?_top?_parent|name|type<reset?submit?button|value],canvas[width,height],caption,cite,code,col[span],colgroup[span],command[type<command?checkbox?radio|label|icon|disabled<disabled|checked<checked|radiogroup|default<default],datalist[data],dd,del[cite|datetime],details[open<open],dfn,div,dl,dt,-em/i,embed[src|type|width|height],eventsource[src],fieldset[disabled<disabled|form|name],figcaption,figure,footer,form[accept-charset|action|enctype|method<get?post?put?delete|name|novalidate<novalidate|target<_blank?_self?_top?_parent],-h1,-h2,-h3,-h4,-h5,-h6,header,hgroup,hr,iframe[name|src|srcdoc|seamless<seamless|width|height|sandbox],img[alt=|src|ismap|usemap|width|height],input[accept|alt|autocomplete<on?off|autofocus<autofocus|checked<checked|disabled<disabled|form|formaction|formenctype|formmethod<get?put?post?delete|formnovalidate?novalidate|formtarget<_blank?_self?_top?_parent|height|list|max|maxlength|min|multiple<multiple|name|pattern|placeholder|readonly<readonly|required<required|size|src|step|type<hidden?text?search?tel?url?email?password?datetime?date?month?week?time?datetime-local?number?range?color?checkbox?radio?file?submit?image?reset?button?value|width],ins[cite|datetime],kbd,keygen[autofocus<autofocus|challenge|disabled<disabled|form|name],label[for|form],legend,li[value],mark,map[name],menu[type<context?toolbar?list|label],meter[value|min|low|high|max|optimum],nav,noscript,object[data|type|name|usemap|form|width|height],ol[reversed|start],optgroup[disabled<disabled|label],option[disabled<disabled|label|selected<selected|value],output[for|form|name],-p,param[name,value],-pre,progress[value,max],q[cite],ruby,rp,rt,samp,script[src|async<async|defer<defer|type|charset],section,select[autofocus<autofocus|disabled<disabled|form|multiple<multiple|name|size],small,source[src|type|media],span,-strong/b,-sub,summary,-sup,table,tbody,td[colspan|rowspan|headers],textarea[autofocus<autofocus|disabled<disabled|form|maxlength|name|placeholder|readonly<readonly|required<required|rows|cols|wrap<soft|hard],tfoot,th[colspan|rowspan|headers|scope],thead,time[datetime],tr,ul,var,video[preload<none?metadata?auto|src|crossorigin|poster|autoplay<autoplay|mediagroup|loop<loop|muted<muted|controls<controls|width|height],wbr';

        return valid_elements;
    }
});