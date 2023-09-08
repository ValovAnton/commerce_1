from django.urls import path

from . import views

urlpatterns = [
    path("create_listing", views.create_listing, name="create_listing"),
    path("listing_category", views.listing_category, name="listing_category"),
    path("<int:auction_id>", views.auction_id, name="auction_id"),
    path("add_comment/<int:auct_id>", views.add_comment, name="add_comment"),
    path("add_to_watchlist/<int:auct_id>", views.add_to_watchlist, name="add_to_watchlist"),
    path("remove_from_watchlist/<int:auct_id>", views.remove_from_watchlist, name="remove_from_watchlist"),
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("buy_now/<int:auct_id>", views.buy_now, name="buy_now"),
    #path("buylist", views.buylist, name="buylist"),
    path("makebid/<int:auct_id>", views.makebid, name="makebid"),
    path("close_auction/<int:auct_id>", views.close_auction, name="close_auction"),
    path("winlist", views.winlist, name="winlist"),

]
