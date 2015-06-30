define([
    "./config"
], function(config) {

    var isProd = require.toUrl('.').indexOf('build') > 0;
    if (isProd) {
        var extraConfig = {
            bundles: {
                creddit: ['./controller']
            }
        };
        require.config(extraConfig);
    }
    
    window.app = {
        rootUrl: "/"
    }
    
    require(['creddit']);
    
});
