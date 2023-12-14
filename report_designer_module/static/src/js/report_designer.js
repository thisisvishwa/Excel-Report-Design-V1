odoo.define('report_designer_module.report_designer', function (require) {
    "use strict";

    var core = require('web.core');
    var Widget = require('web.Widget');
    var rpc = require('web.rpc');
    var QWeb = core.qweb;

    var ReportDesigner = Widget.extend({
        template: 'report_designer_module.report_designer_template',
        events: {
            'click .generate-report': '_onGenerateReport',
            'change .model-selection': '_onModelChange',
            'change .field-selection': '_onFieldChange',
        },

        init: function (parent, options) {
            this._super(parent, options);
            this.models = [];
            this.fields = [];
            this.reportParameters = [];
        },

        start: function () {
            var self = this;
            return this._fetchModels().then(function () {
                self._renderModelSelection();
            });
        },

        _fetchModels: function () {
            var self = this;
            return rpc.query({
                model: 'ir.model',
                method: 'search_read',
                args: [[]],
            }).then(function (models) {
                self.models = models;
            });
        },

        _fetchFields: function (model) {
            var self = this;
            return rpc.query({
                model: 'ir.model.fields',
                method: 'search_read',
                args: [[['model', '=', model]]],
            }).then(function (fields) {
                self.fields = fields;
            });
        },

        _renderModelSelection: function () {
            this.$('.model-selection').html(QWeb.render('report_designer_module.model_selection', {models: this.models}));
        },

        _renderFieldSelection: function () {
            this.$('.field-selection').html(QWeb.render('report_designer_module.field_selection', {fields: this.fields}));
        },

        _onModelChange: function (event) {
            var self = this;
            var model = $(event.target).val();
            this._fetchFields(model).then(function () {
                self._renderFieldSelection();
            });
        },

        _onFieldChange: function (event) {
            var field = $(event.target).val();
            this.reportParameters.push(field);
        },

        _onGenerateReport: function () {
            rpc.query({
                model: 'report.designer',
                method: 'generate_report',
                args: [this.reportParameters],
            });
        },
    });

    core.action_registry.add('report_designer', ReportDesigner);

    return ReportDesigner;
});