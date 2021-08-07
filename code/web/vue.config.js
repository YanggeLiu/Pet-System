module.exports = {
    transpileDependencies: [
        'vuetify'
    ],
    pwa: {
        name: 'Cat_sys',
        themeColor: '#424242',
        msTileColor: '#424242',
        iconPaths: {
            favicon16: 'img/icons/logo-128x128.png',
            favicon32: 'img/icons/logo-128x128.png',
            favicon128: 'img/icons/logo-128x128.png',
            favicon144: 'img/icons/logo-144x144.png',
            favicon192: 'img/icons/logo-192x192.png',
            favicon256: 'img/icons/logo-256x256.png',
            favicon512: 'img/icons/logo-512x512.png',
            appleTouchIcon: 'img/icons/logo-144x144.png'
        },
        appleMobileWebAppCapable: 'yes',
        appleMobileWebStatusBarStyle: 'black',
        workboxPluginMode: 'InjectManifest',
        workboxOptions: {
            swSrc: 'dev/service-worker.js',
        }
    }
}
