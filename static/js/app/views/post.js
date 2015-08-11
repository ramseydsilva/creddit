define([
    "backbone",
    "handlebars"
    
], function(Backbone, HandleBars, template) {
    'use strict';
    
    return Backbone.View.extend({

        tagName: 'li',
        
        events: {},

        registerEvents: function() {
            this.events = {};
            this.events['submit #'+this.model.id+' form'] = 'submitReply';
            this.events['click #'+this.model.id+' a'] = 'handleClick';
        },

        insertToDom: function() {
            if (!this.parent) {
                this.parent = $("#"+this.model.attributes.parent);
            }
            if (!$.contains(document, this.el)) {
                if (this.parent) {
                    this.parent.next().prepend(this.$el);
                }
            }
        },
        
        addChildrenViews: function() {
            this.$("> .post > .children > li").each(function(i, e) {
                var id = parseInt(e.getElementsByTagName("article")[0].id);
                if (!app.posts.find(id)) {
                    app.posts.add({
                        id: id,
                        el: e
                    });
                }
            });            
        },

        initialize: function(options) {
            if (this.model.attributes.id) {
                this.registerEvents();
            }
            this.insertToDom();
            if (options.el) {
                this.addChildrenViews();
            } else {
                this.render();
            }
            this.cacheDomItems();
        },

        submitReply: function(e) {
            var self = this;
            e.preventDefault();
            this.model.collection.create({
                text: this.reply_textarea.val(),
                parent: this.model.id
            }, {
                wait: true,
                success: function() {
                    self.reply_textarea.val("");
                    if (!self.form.hasClass("always_show")) {
                        self.form.hide();
                    }
                }
            });

            return false;
        },

        handleClick: function(e) {
            var a = $(e.target);
            var href = a.attr("href");
            
            if (a.hasClass("reply")) {
                e.preventDefault();
                this.form.toggle();
            } else if (href.indexOf("subscribe") + href.indexOf("vote") > -2) {
                var self = this;
                e.preventDefault();
                $.ajax({
                    url: href,
                    method: "GET",
                    data: {
                        ajax: true
                    },
                    success: function() {
                        self.model.fetch();
                    }
                })
                return false;
            } else {
                return true;
            }
        },

        reRender: function() {
            this.insertToDom();
            this.render();
            this.cacheDomItems();
            this.registerEvents();
            this.undelegateEvents();
            this.delegateEvents();
        },

        render: function() {
            if (this.$(">.post article").length) {
                this.$(">.post article").replaceWith(this.model.attributes.html);
            } else if(this.model.attributes.html) {
                this.$el.html("<div class='post'>"+this.model.attributes.html + "<ul class='children'></ul></div>");
            } else {
                this.$el.html("<div class='post'><article></article><ul class='children'></ul></div>");
            }
        },

        cacheDomItems: function() {
            this.form = this.$("#"+this.model.id+" form");
            this.reply_textarea = this.form.find("textarea");
        }

    });

});