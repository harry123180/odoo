odoo.define('estate.clicker_systray_item', function (require) {
    'use strict';

    const SystrayMenu = require('web.SystrayMenu');
    const Widget = require('web.Widget');

    const ClickerSystrayItem = Widget.extend({
        template: 'ClickerSystrayItemTemplate', // 确保与您的XML模板名称相匹配
        events: {
            'click .js_clicker_increment': '_onClickIncrement', // 点击事件处理器
        },
        init: function () {
            this._super.apply(this, arguments);
            this.clickCount = 0;
        },
        _onClickIncrement: function () {
            this.clickCount++;
            this.$('.js_clicker_count').text(this.clickCount); // 更新计数器显示
        },
    });

    SystrayMenu.Items.push(ClickerSystrayItem);

    return ClickerSystrayItem;
});
