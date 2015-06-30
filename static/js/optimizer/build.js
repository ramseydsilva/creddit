{
    appDir: '../app',
    baseUrl: "../app",
    dir: '../build-2be438a',

    skipDirOptimize: false,
    skipModuleInsertion: false,
    mainConfigFile: "../app/config.js",
    optimize: "uglify2",
    
    bundles: {
        'superadmin': ['./controller']
    },
    
    modules: [
        {
            name: "./controller"
        }
    ]
    
}
