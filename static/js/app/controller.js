require([
    'backbone_tastypie',
    './collections/post'
],
function(Tastypie, PostCollection) {
    "use strict";
    
    app.posts = new PostCollection();
    
    var first_post = $(".post")[0];
    if (first_post) {
        app.posts.add({
            id: parseInt(first_post.getElementsByTagName("article")[0].id),
            el: first_post
        });
    }
    
});