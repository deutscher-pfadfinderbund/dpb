/*jshint globalstrict: true, unused:false*/
/*global $, jQuery, window, prettyPrint, parent*/
'use strict';
function makeResponsive()
{
    if ($('body').width() < 768) {
        $('.container').addClass('container-xs');
    }
}

/* get custom Bootstrap styles */

function getBootstrapStyles()
{
    var bodyBackground;
    var previewBackground;
    var choiceTitleBorderTop;
    var choiceTitleBorderTopAfter;

    bodyBackground = previewBackground = $('body').css('background-color');
    if(bodyBackground.match(/rgb(255, 255, 255)/)) {
        $('body').css('background-color', '#fafafa');
    } else {
        bodyBackground = shadeRGBColor(bodyBackground, 0.07);
        choiceTitleBorderTop = shadeRGBColor(bodyBackground, -0.2);
        choiceTitleBorderTopAfter = shadeRGBColor(bodyBackground, 0.3);
        $('body').css('background-color', bodyBackground);
        $('.choice-title, #preview-title, #code-title').css('border-top-color', choiceTitleBorderTop);
        $('<style>.choice-title:after, #preview-title:after, #code-title:after{border-top-color: '+choiceTitleBorderTopAfter+'}</style>').appendTo('head');
        $('#preview').css('background-color', previewBackground);
    }
}

function shadeRGBColor(color, percent) {
    var f=color.split(','),t=percent<0?0:255,p=percent<0?percent*-1:percent,R=parseInt(f[0].slice(4)),G=parseInt(f[1]),B=parseInt(f[2]);
    return 'rgb('+(Math.round((t-R)*p)+R)+','+(Math.round((t-G)*p)+G)+','+(Math.round((t-B)*p)+B)+')';
}

/* btn-toggle */

function toggleBtn(toggleGroup) {
    $(toggleGroup).find('.btn').toggleClass('active');
    $(toggleGroup).find('.btn').toggleClass('btn-success');
    $(toggleGroup).find('.btn').toggleClass('btn-default');
    if($(toggleGroup).find('.active').attr('data-attr') == 'true') {
        return true;
    } else {
        return false;
    }
}

function toggleAllBtns(toggleGroup, trueFalse) {
    $(toggleGroup).each(function() {
        if(!trueFalse) { // set all buttons to true
            $(this).find('button[data-attr="true"]').addClass('active').removeClass('btn-default').addClass('btn-success');
            $(this).find('button[data-attr="false"]').removeClass('active').removeClass('btn-success').addClass('btn-default');
        } else { // set all buttons to false
            $(this).find('button[data-attr="false"]').addClass('active').removeClass('btn-default').addClass('btn-success');
            $(this).find('button[data-attr="true"]').removeClass('active').removeClass('btn-success').addClass('btn-default');
        }
    });
    $(toggleGroup).find('.btn').toggleClass('active');
    $(toggleGroup).find('.btn').toggleClass('btn-success');
    $(toggleGroup).find('.btn').toggleClass('btn-default');
    if($(toggleGroup).find('.active').attr('data-attr') == 'true') {
        return true;
    } else {
        return false;
    }
}

/* get current edit element code */

function getCode(selector)
{
    var elementCode;
    if($(window.parent.document.body).find('.mce-tinymce-inline')[0]) {
        elementCode = $(window.parent.document.body).find('.mce-edit-focus').find(selector).clone().wrap('<div>').parent().html();
    } else {
        elementCode = $(window.parent.document.body).find('iframe').contents().find(selector).clone().wrap('<div>').parent().html();
    }
    return elementCode;
}

/* code update */

function updateCode()
{
    var code = $('#test-wrapper').html(); // get preview content

    /* remove table content only for new tables (with false-text content) */

    if($('<div>').html(code).find('table.table').length > 0) {
        if($('<div>').html(code).find('table.table').attr('data-attr') == 'new-table') {
            code = $('<div>').html(code).find('th, td').text('').closest('div').html();
        }
    }

    var find = new Array(/\s?data-mce-[a-z]+="[^"]+"/g);
    var replace = new Array('', '', '', '', '');

    for (var i = find.length - 1; i >= 0; i--) {
        code = code.replace(find[i], replace[i]);
    }

    /* render code */

    /* remove unwanted classes, attrs, ... */

    var allowedAttrs = new Array(['class']);
    var allowedEmpty   = new Array(['span']);

    if($('#test-wrapper').hasClass('test-icon-wrapper')) {

    /* keep styles for icons and add beginning space
    (otherwise tinymce will not allow empty tag and will remove your icon) */

        allowedAttrs.push(['style']);
        code = '&nbsp;' + $.trim(escapeHtml($.htmlClean(code, {format:true, allowedAttributes: allowedAttrs, allowEmpty: allowedEmpty})));
    } else if($('#test-wrapper').hasClass('test-snippet-wrapper')) { // keep all original code for snippets
        code = $.trim(escapeHtml(code));
    } else {
        code = $.trim(escapeHtml($.htmlClean(code, {format:true, allowedAttributes: allowedAttrs, allowEmpty: allowedEmpty})));
    }
    $('#code-wrapper').fadeOut(200, function() {
        $(this).html('<pre class="prettyprint">' + code + '</pre>');
        // PR.prettyPrint();
        prettyPrint();
        $(this).fadeIn(200);
    });
    parent.document.getElementById('bs-code').value = code;
}

/* code escape html */

function escapeHtml(text)
{
  var map = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    '\'': '&#039;'
  };

  return text.replace(/[&<>"']/g, function (m) { return map[m]; });
}

/* code toggle */

$('#code-slide-link').on('click', function () {
    $('#code-wrapper').slideToggle(400, function () {
        if ($('#code-wrapper').css('display') == 'block') {
            $('#code-slide-link i').removeClass('glyphicon-arrow-down').addClass('glyphicon-arrow-up');
        } else {
            $('#code-slide-link i').removeClass('glyphicon-arrow-up').addClass('glyphicon-arrow-down');
        }
    });
});

/*
 * HTML5 Sortable jQuery Plugin
 * http://farhadi.ir/projects/html5sortable
 *
 * Copyright 2012, Ali Farhadi
 * Released under the MIT license.
 */
(function($) {
var dragging, placeholders = $();
$.fn.sortable = function(options) {
    var method = String(options),
        items;
    options = $.extend({
        connectWith: false,
        calllback: function () {}
    }, options);
    return this.each(function() {
        if (/^enable|disable|destroy$/.test(method)) {
            items = $(this).children($(this).data('items')).attr('draggable', method == 'enable');
            if (method == 'destroy') {
                items.add(this).removeData('connectWith items')
                    .off('dragstart.h5s dragend.h5s selectstart.h5s dragover.h5s dragenter.h5s drop.h5s');
            }
            return;
        }
        var isHandle, index;
        items = $(this).children(options.items);
        var placeholder = $('<' + (/^ul|ol$/i.test(this.tagName) ? 'li' : 'div') + ' class="sortable-placeholder">');
        items.find(options.handle).mousedown(function() {
            isHandle = true;
        }).mouseup(function() {
            isHandle = false;
        });
        $(this).data('items', options.items);
        placeholders = placeholders.add(placeholder);
        if (options.connectWith) {
            $(options.connectWith).add(this).data('connectWith', options.connectWith);
        }
        items.attr('draggable', 'true').on('dragstart.h5s', function(e) {
            if (options.handle && !isHandle) {
                return false;
            }
            isHandle = false;
            var dt = e.originalEvent.dataTransfer;
            dt.effectAllowed = 'move';
            dt.setData('Text', 'dummy');
            index = (dragging = $(this)).addClass('sortable-dragging').index();
        }).on('dragend.h5s', function() {
            if($(this).hasClass('sortable-dragging')) {
                dragging.removeClass('sortable-dragging').show();
                placeholders.detach();
                // if (index != dragging.index()) {
                //     items.parent().trigger('sortupdate', {item: dragging});
                // }
                options.callback.call(this);
            }
            dragging = null;
        }).not('a[href], img').on('selectstart.h5s', function() {
            this.dragDrop && this.dragDrop();
            return false;
        }).end().add([this, placeholder]).on('dragover.h5s dragenter.h5s drop.h5s', function(e) {
            if (!items.is(dragging) && options.connectWith !== $(dragging).parent().data('connectWith')) {
                return true;
            }
            if (e.type == 'drop') {
                e.stopPropagation();
                placeholders.filter(':visible').after(dragging);
                return false;
            }
            e.preventDefault();
            e.originalEvent.dataTransfer.dropEffect = 'move';
            if (items.is(this)) {
                if (options.forcePlaceholderSize) {
                    placeholder.height(dragging.outerHeight());
                }
                dragging.hide();
                $(this)[placeholder.index() < $(this).index() ? 'after' : 'before'](placeholder);
                placeholders.not(placeholder).detach();
            } else if (!placeholders.is(this) && !$(this).children(options.items).length) {
                placeholders.detach();
                $(this).append(placeholder);
            }
            return false;
        });
    });
};
})(jQuery);

$.fn.scrollToTop = function(){ if (this.length > 0) $('body, html').animate({scrollTop: $(this).offset().top}, 500); };