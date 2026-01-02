---
date: 2025-11-16
draft: false
title: My own multi-search engine
---
For a long time, I used the DuckDuckGo search engine. One of the reasons was that it included the **bangs** feature, which is very practical for efficient searching. It allows you to switch from one search engine to many others. For example, when I search for the word `apple` and want to find images on Google, I just type `apple !gi` into DuckDuckGo, and it immediately redirects me to Google Images. This feature was very addictive, but sometimes it didn't work exactly as expected. Furthermore, I didn't like that DuckDuckGo theoretically has access to a query that ultimately ends up somewhere else entirely, so I decided to create my own alternative.

I considered where to host the project and eventually chose **Cloudflare Workers** – primarily for its speed and also because it is free. From a security perspective, it's not ideal because the hosting is not fully under my control, but I trust Cloudflare in this regard.

You can find the full code on my GitHub [here](https://github.com/adam4056/Search_router/tree/main). In conclusion, I must say that the project works excellently, and I can highly recommend it.