---
date: 2025-11-16
draft: false
title: Můj vlastní multi-vyhledávač
---
Dlouhou dobu jsem používal vyhledávač DuckDuckGo. Jedním z důvodů bylo, že obsahoval funkci **bangs**, což je velmi praktické pro efektivní vyhledávání. Umožňuje z jednoho vyhledávače přepínat na spoustu jiných. Například když hledám slovo `apple` a chci najít obrázky na Google, stačí napsat do DuckDuckGo `apple !gi` a okamžitě mě přesměruje na Google Images. Tato funkce byla velice návyková, ale občas nefungovala přesně podle očekávání. Navíc se mi nelíbilo, že DuckDuckGo má teoreticky přístup k dotazu, který nakonec směřuje úplně jinam, a tak jsem se rozhodl vytvořit vlastní alternativu.

Zvažoval jsem, kde projekt hostovat, a nakonec jsem zvolil **Cloudflare Workers** – primárně kvůli rychlosti a také proto, že je zdarma. Z pohledu bezpečnosti to není ideální, protože hosting není plně pod mojí kontrolou, ale Cloudflare v tomto ohledu důvěřuji.

Celý kód najdete na mém GitHubu [zde](https://github.com/adam4056/Search_router/tree/main). Na závěr musím říct, že projekt funguje výborně a mohu jej jen doporučit.