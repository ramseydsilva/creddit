require([
    'backbone_tastypie',
    './collections/post'
],
function(Tastypie, PostCollection) {
    "use strict";
    
    app.posts = new PostCollection();
    $(".post").each(function(i, e) {
        app.posts.add({
            id: parseInt(e.id),
            el: e
        })
    });
    
});