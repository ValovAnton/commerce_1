### This is my realisation of CS50 harvard commerce project.

My name is *Valov Anton*. 

**this is project specification**
*Design an eBay-like e-commerce auction site that will allow users to post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist.”

*Trying to make mermaid schema
```mermaid
graph LR;
	active listings -- "login" --> Login;
	Login --"add to watchlist" --> watchlist page;
	active-listings -- "click to title" --> page with one listing;
	page with one listing -- "Buy now" --> Listing not active;
	active-listings -- "click to buylist" --> page with by list;
	Listing not active --> page with by list;
```
