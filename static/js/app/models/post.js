define([
    "backbone",
    "../views/post"
], function (Backbone, PostView) {
    "use strict";

    return Backbone.Model.extend({
        
        initialize: function() {
            if (this.attributes.id) {
                this.renderView();
            } else {
                this.once("change:id", this.renderView, this);
            }
        },

        renderView: function() {
            this.view = new PostView({
                el: this.attributes.el || "<li>"+this.attributes.html+"</li>",
                model: this
            });
        }
        
    });

});