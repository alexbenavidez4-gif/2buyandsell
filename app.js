/* 2BuyAndSell app helpers: registers the app, adds the tab bar on agent pages, and the Install button. */
(function(){
  "use strict";
  if ("serviceWorker" in navigator) { window.addEventListener("load", function(){ navigator.serviceWorker.register("/sw.js").catch(function(){}); }); }

  var path = location.pathname.replace(/\.html$/, "").replace(/\/+$/, "") || "/";
  var TABS = [
    ["/dashboard", "Home",   '<path d="M3 11.5 12 4l9 7.5"/><path d="M5 10v10h14V10"/>'],
    ["/people",    "People", '<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9" r="2.5"/><path d="M15.5 14.2c3 .2 5.5 2.6 5.5 5.8"/>'],
    ["/hounds",    "Hounds", '<circle cx="7" cy="9" r="2"/><circle cx="12" cy="6.5" r="2"/><circle cx="17" cy="9" r="2"/><path d="M8.5 17c0-2.2 1.6-4.5 3.5-4.5s3.5 2.3 3.5 4.5c0 1.6-1.6 2.5-3.5 2.5S8.5 18.6 8.5 17z"/>'],
    ["/social",    "Social", '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>']
  ];
  var onAgentPage = TABS.some(function(t){ return t[0] === path; });
  var standalone = window.matchMedia("(display-mode: standalone)").matches || window.navigator.standalone === true;

  function css(t){ var s=document.createElement("style"); s.textContent=t; document.head.appendChild(s); }

  /* ---- bottom tab bar (phones, and always inside the installed app) ---- */
  if (onAgentPage) {
    css(".tabbar{position:fixed;left:0;right:0;bottom:0;z-index:40;display:none;background:#fff;border-top:1px solid #e7e1d6;padding:6px 6px calc(6px + env(safe-area-inset-bottom));box-shadow:0 -4px 18px rgba(22,32,42,.06)}"+
        ".tabbar a{flex:1;display:flex;flex-direction:column;align-items:center;gap:2px;padding:4px 0;color:#6b7580;text-decoration:none;font:700 12px/1.1 'Source Sans 3',system-ui,sans-serif;border-radius:12px}"+
        ".tabbar a svg{width:24px;height:24px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}"+
        ".tabbar a[aria-current=page]{color:#1a467c;background:#eef3f9}"+
        "@media (max-width:760px){.tabbar{display:flex}body{padding-bottom:calc(74px + env(safe-area-inset-bottom))}}"+
        (standalone ? ".tabbar{display:flex}body{padding-bottom:calc(74px + env(safe-area-inset-bottom))}" : ""));
    var nav = document.createElement("nav"); nav.className = "tabbar"; nav.setAttribute("aria-label", "App sections");
    nav.innerHTML = TABS.map(function(t){
      return '<a href="'+t[0]+'"'+(t[0]===path?' aria-current="page"':'')+'><svg viewBox="0 0 24 24" aria-hidden="true">'+t[2]+'</svg>'+t[1]+'</a>';
    }).join("");
    if (document.body) document.body.appendChild(nav); else document.addEventListener("DOMContentLoaded", function(){ document.body.appendChild(nav); });
  }

  /* ---- Install the app ---- */
  var deferred = null;
  window.addEventListener("beforeinstallprompt", function(e){ e.preventDefault(); deferred = e; });
  window.addEventListener("appinstalled", function(){ var c=document.getElementById("installCard"); if(c) c.remove(); });
  var ua = navigator.userAgent, isIOS = /iPhone|iPad|iPod/.test(ua) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);
  var isAndroid = /Android/.test(ua);

  function howTo(){
    var box = document.createElement("div");
    box.setAttribute("role","dialog"); box.setAttribute("aria-label","Install the app");
    box.style.cssText = "position:fixed;inset:0;z-index:60;background:rgba(16,24,32,.55);display:flex;align-items:flex-end;justify-content:center;padding:12px";
    var steps = isIOS
      ? "<li>Open <b>2buyandsell.com</b> in <b>Safari</b> (not Chrome).</li><li>Tap the <b>Share</b> button <span style='font-size:18px'>⎙</span> at the bottom.</li><li>Scroll down and tap <b>Add to Home Screen</b>, then <b>Add</b>.</li>"
      : isAndroid
      ? "<li>Open <b>2buyandsell.com</b> in <b>Chrome</b>.</li><li>Tap the <b>⋮</b> menu at the top right.</li><li>Tap <b>Install app</b> (or <b>Add to Home screen</b>).</li>"
      : "<li>Open <b>2buyandsell.com</b> in <b>Chrome</b> or <b>Edge</b>.</li><li>Click the <b>install icon</b> at the right end of the address bar.</li><li>On your phone, open the site and use <b>Add to Home Screen</b>.</li>";
    box.innerHTML = "<div style='background:#fff;border-radius:20px;max-width:440px;width:100%;padding:20px 20px 16px;font:17px/1.45 \"Source Sans 3\",system-ui,sans-serif;color:#16202a'>"+
      "<div style='display:flex;gap:12px;align-items:center;margin-bottom:8px'><img src='/img/app-192.png' width='52' height='52' alt='' style='border-radius:12px;border:1px solid #e7e1d6'><b style='font-size:20px'>Get the 2BuyAndSell app</b></div>"+
      "<ol style='padding-left:22px;margin:8px 0 14px'>"+steps+"</ol>"+
      "<p style='color:#56616d;font-size:15px;margin:0 0 14px'>The app icon lands on your home screen and opens straight to your dashboard. It's free and updates itself.</p>"+
      "<button type='button' style='width:100%;min-height:48px;border:0;border-radius:999px;background:#1a467c;color:#fff;font:700 17px system-ui,sans-serif;cursor:pointer'>Got it</button></div>";
    box.addEventListener("click", function(e){ if (e.target === box || e.target.tagName === "BUTTON") box.remove(); });
    document.body.appendChild(box);
  }
  window.install2bas = function(){
    if (deferred) { deferred.prompt(); deferred.userChoice.then(function(){ deferred = null; }); return; }
    howTo();
  };

  /* Install card on the dashboard (hidden once they're using the app) */
  if (path === "/dashboard" && !standalone) {
    var tries = 0;
    (function addCard(){
      var quick = document.querySelector(".quick");
      if (!quick) { if (tries++ < 40) setTimeout(addCard, 250); return; }
      if (document.getElementById("installCard")) return;
      var a = document.createElement("a"); a.href = "#install"; a.id = "installCard";
      a.innerHTML = "<b>📲 Install the app</b><span>Put 2BuyAndSell on your phone</span>";
      a.style.background = "#ec8a34"; a.style.color = "#1a1006";
      a.addEventListener("click", function(e){ e.preventDefault(); window.install2bas(); });
      quick.appendChild(a);
    })();
  }
})();
