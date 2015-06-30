define([
    "backbone",
    "../models/post"
], function (Backbone, PostModel) {
    "use strict";
    
    return Backbone.Collection.extend({
        
        model: PostModel,
        
        url: function() {
            return "/api/post/";
        },
        
        initialize: function() {
            var self = this;
            if (fp) {
                this.timer = setInterval(function() {
                    self.fetch({
                        url: self.url() + "?i=1&fp=" + fp,
                        remove: false
                    });
               }, 5000);
            }
        }
    });

});