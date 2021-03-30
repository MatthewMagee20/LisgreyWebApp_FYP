const filesToCache = [
    '/',
    '/offline',
    '/404',
    'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css',
    'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js',
    '/static/css/stylesheet.css',
]

const staticCacheName = 'pages-cache-v1';

self.addEventListener('install', event => {
    console.log('Attempting to install service worker and cache static assets');
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    );
});

self.addEventListener('fetch', event => {

    // if statements are for url's that will not be cached
    console.log('Fetch event for ', event.request.url);
    if ( event.request.url.indexOf( '/takeaway/basket/' ) !== -1 ) {
        return false;
    }
    if ( event.request.url.indexOf( '/takeaway/contact_information/' ) !== -1 ) {
        return false;
    }
    if ( event.request.url.indexOf( '/contact/' ) !== -1 ) {
        return false;
    }
    if ( event.request.url.indexOf( '/reservation/' ) !== -1 ) {
        return false;
    }
    if ( event.request.url.indexOf( '/admin/' ) !== -1 ) {
        return false;
    }
    if ( event.request.url.indexOf( '/map' ) !== -1 ) {
        return false;
    }

    event.respondWith(
        caches.match(event.request)
            .then(response => {
                if (response) {
                    console.log('Found ', event.request.url, ' in cache');
                    return response;
                }
                console.log('Network request for ', event.request.url);
                return fetch(event.request)
                    .then(response => {
                        if (response.status === 404) {
                            return caches.match('404.html'); // if 404, show custom 404 template
                        }
                        return caches.open(staticCacheName)
                            .then(cache => {
                                cache.put(event.request.url, response.clone());
                                return response;
                            });
                    });
            }).catch(error => {
            console.log('Error, ', error);
            return caches.match('/offline'); // if resource not in cache, show offline page
        })
    );
});
