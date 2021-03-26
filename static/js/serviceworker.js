const filesToCache = [
    '/',

];

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
    console.log('Fetch event for ', event.request.url);
    if ( event.request.url.indexOf( '/takeaway/basket/' ) !== -1 ) { // ignore the caching of basket session variable
        return false;
    }
    if ( event.request.url.indexOf( '/takeaway/contact_information/' ) !== -1 ) { // ignore the caching of basket session variable
        return false;
    }
    if ( event.request.url.indexOf( '/contact/' ) !== -1 ) { // ignore the caching of basket session variable
        return false;
    }
    if ( event.request.url.indexOf( '/reservation/' ) !== -1 ) { // ignore the caching of basket session variable
        return false;
    }
    if ( event.request.url.indexOf( '/accounts/login/' ) !== -1 ) { // ignore the caching of basket session variable
        return false;
    }
    if ( event.request.url.indexOf( '/accounts/logout/' ) !== -1 ) { // ignore the caching of basket session variable
        return false;
    }
    // if ( event.request.url.indexOf( '/home' ) !== -1 ) { // ignore the caching of basket session variable
    //     return false;
    // }
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
                            return caches.match('pages/404.html');
                        }
                        return caches.open(staticCacheName)
                            .then(cache => {
                                cache.put(event.request.url, response.clone());
                                return response;
                            });
                    });
            }).catch(error => {
            console.log('Error, ', error);
            return caches.match('pages/offline.html');
        })
    );
});



