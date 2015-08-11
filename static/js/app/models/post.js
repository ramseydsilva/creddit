define([
    "backbone",
    "../views/post"
], function (Backbone, PostView) {
    "use strict";

    return Backbone.Model.extend({
        
        initialize: function(options) {
            this.view = new PostView({
                el: options.el,
                model: this
            });            
            this.on("change:html", this.view.reRender, this.view);
        }
        
    });

});