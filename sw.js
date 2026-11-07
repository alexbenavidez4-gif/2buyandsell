/* 2BuyAndSell service worker: opens fast, shows a friendly page when offline.
   Only touches this site's own files. Logins and data (Supabase) always go straight to the network. */
const V = "2bas-v1";
const PRECACHE = ["/offline.html", "/site.css", "/app.js", "/img/app-192.png", "/img/logo-icon-128.png"];
self.addEventListener("install", e => { e.waitUntil(caches.open(V).then(c => c.addAll(PRECACHE)).then(() => self.skipWaiting())); });
self.addEventListener("activate", e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== V).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener("fetch", e => {
  const req = e.request, url = new URL(req.url);
  if (req.method !== "GET" || url.origin !== location.origin) return;           // leave Supabase, fonts, CDNs alone
  if (req.mode === "navigate") {                                                 // pages: always try the network first
    e.respondWith(fetch(req).then(res => { const copy = res.clone(); caches.open(V).then(c => c.put(req, copy)); return res; })
      .catch(() => caches.match(req).then(r => r || caches.match("/offline.html"))));
    return;
  }
  if (/\.(css|js|png|jpg|jpeg|webp|svg|webmanifest)$/.test(url.pathname)) {      // files: use the saved copy, refresh it quietly
    e.respondWith(caches.match(req).then(hit => {
      const net = fetch(req).then(res => { if (res.ok) { const copy = res.clone(); caches.open(V).then(c => c.put(req, copy)); } return res; }).catch(() => hit);
      return hit || net;
    }));
  }
});
