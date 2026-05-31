var CACHE_NAME = 'django-pwa-cache-v1';
var urlsToCache = [
    '/',
    '/static/css/base.css',
    '/static/images/icon-160x160.png'
];

// Instalar el Service Worker y almacenar en caché los recursos estáticos
self.addEventListener('install', function(event) {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(function(cache) {
                return cache.addAll(urlsToCache);
            })
    );
});

// Responder con recursos en caché si no hay conexión a internet
self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request)
            .then(function(response) {
                if (response) {
                    return response;
                }
                return fetch(event.request);
            })
    );
});
