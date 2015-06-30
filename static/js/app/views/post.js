define([
    "backbone",
    "handlebars"
    
], function(Backbone, HandleBars, template) {
    'use strict';
    
    return Backbone.View.extend({

        events: {
            'submit form': 'addReply'
        },

        getParent: function() {
            return this.model.collection.findWhere({id: this.model.attributes.parent });
        },

        initialize: function() {

            if (!$.contains(document, this.el)) {
                this.$el.hide();
                var parent = this.getParent();
                parent.view.$(">.children").prepend(this.el);
                this.$el.fadeIn();
            }
            
            this.$(".post").each(function(i, e) {
                app.posts.add({
                    id: parseInt(e.id),
                    el: e
                })
            });
        },

        addReply: function(e) {
            e.preventDefault();
            var form = $(e.target);
            this.model.collection.create({
                text: form.find("textarea").val(),
                parent: this.model.id
            }, {
                wait: true,
                success: function() {
                    form.find("textarea").val("");
                    if (!form.hasClass("always_show")) {
                        form.hide();
                    }
                }
            });

            return false;
        }
    });

});