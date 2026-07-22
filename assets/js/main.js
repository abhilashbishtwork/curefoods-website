(function(){
  "use strict";

  // Mobile menu
  var toggle = document.querySelector(".nav-toggle");
  var menu = document.querySelector(".mobile-menu");
  var close = document.querySelector(".mobile-close");
  if(toggle && menu){
    toggle.addEventListener("click", function(){ menu.classList.add("open"); document.body.style.overflow="hidden"; });
  }
  if(close && menu){
    close.addEventListener("click", function(){ menu.classList.remove("open"); document.body.style.overflow=""; });
  }
  menu && menu.querySelectorAll("a").forEach(function(a){
    a.addEventListener("click", function(){ menu.classList.remove("open"); document.body.style.overflow=""; });
  });

  // Theme toggle (persists preference; defaults to system)
  var themeBtn = document.querySelector("[data-theme-toggle]");
  var root = document.documentElement;
  function applyTheme(t){
    if(t){ root.setAttribute("data-theme", t); } else { root.removeAttribute("data-theme"); }
  }
  try{
    var saved = localStorage.getItem("cf-theme");
    if(saved) applyTheme(saved);
  }catch(e){}
  if(themeBtn){
    themeBtn.addEventListener("click", function(){
      var current = root.getAttribute("data-theme");
      var next = current === "dark" ? "light" : "dark";
      applyTheme(next);
      try{ localStorage.setItem("cf-theme", next); }catch(e){}
    });
  }

  // FAQ: only one open at a time within a group (progressive enhancement, optional)
  document.querySelectorAll(".faq-list").forEach(function(list){
    list.addEventListener("toggle", function(e){
      if(e.target.tagName === "DETAILS" && e.target.open){
        list.querySelectorAll("details[open]").forEach(function(d){
          if(d !== e.target) d.removeAttribute("open");
        });
      }
    }, true);
  });

  // Service worker registration for installable PWA
  if("serviceWorker" in navigator){
    window.addEventListener("load", function(){
      navigator.serviceWorker.register("/sw.js").catch(function(){});
    });
  }

  // Active nav link highlight
  var path = location.pathname.replace(/index\.html$/, "");
  document.querySelectorAll(".nav-desktop a, .mobile-menu a").forEach(function(a){
    var href = a.getAttribute("href");
    if(!href) return;
    if(href === path || (href !== "/" && path.indexOf(href.replace(/index\.html$/, "")) === 0 && href !== "/")){
      a.setAttribute("aria-current", "page");
    }
  });
})();
