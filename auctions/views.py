from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Auction, Category, Comment, Bid



def index(request):
    auct = Auction.objects.filter(active=True).order_by('-date_end')
    category = Category.objects.all()
    return render(request, "auctions/index.html", {
        "auctions": auct,
        "category": category,
        "filtered": "All"
    })

def listing_category(request):
    if request.method == "POST":
        digit_category = int(request.POST["category_select"])
        if digit_category == 0:
            auct = Auction.objects.filter(active=True)
            category = 'All'
        else:
            category = Category.objects.get(pk=digit_category)
            auct = Auction.objects.filter(category=category, active=True)
        all_category = Category.objects.all()
        return render(request, "auctions/index.html", {
            "auctions": auct,
            "category": all_category,
            "filtered": category
        })


def auction_id(request, auction_id):
    if request.method == "GET":
        auct = Auction.objects.get(pk=auction_id)
        isListingWatchlist = request.user in auct.watchlist.all()
        return render(request, "auctions/auction.html", {
            "auct": auct,
            "comments": auct.comments.all(),
            "iswatching":isListingWatchlist
        })


def add_comment(request, auct_id):

    new_comment = request.POST.get("new_comment")
    if new_comment:

        auction = Auction.objects.get(pk=auct_id)
        com_obj = Comment(
            text= new_comment,
            user = request.user,
            auction = auction
        )
        com_obj.save()
    return HttpResponseRedirect(reverse("auction_id", args=(auct_id,)))


def add_to_watchlist(request, auct_id):
    auction = Auction.objects.get(pk=int(auct_id))
    user = request.user
    auction.watchlist.add(user)
    return HttpResponseRedirect(reverse("auction_id", args=(auct_id,)))

def remove_from_watchlist(request, auct_id):
    auction = Auction.objects.get(pk=int(auct_id))
    user = request.user
    auction.watchlist.remove(user)
    auction.save()
    return HttpResponseRedirect(reverse("auction_id", args=(auct_id,)))

def watchlist(request):
    if request.method == "GET":
        if request.user:
            user = request.user
            auctions = Auction.objects.filter(watchlist=user, active=True)
            return render(request, "auctions/watchlist.html", {
                "auctions": auctions,
            })
        else:
            return HttpResponseRedirect(reverse('index'))

def winlist(request):
    user = request.user
    auctions = Auction.objects.filter(winner=user, active=False)
    return render(request, "auctions/winlist.html", {
        "auctions": auctions,
    })



def close_auction(request, auct_id):
    auction = Auction.objects.get(pk=int(auct_id))

    auction.active = False
    high_bid_user = auction.high_bid.user
    auction.winner.add(high_bid_user)
    auction.save()
    return HttpResponseRedirect(reverse('index'))



def makebid(request, auct_id):
    auction = Auction.objects.get(pk=int(auct_id))
    user = request.user
    bid = float(request.POST['bid'])

    new_bid = Bid(bid=bid, user=user)
    if not auction.high_bid:
        auction.high_bid = new_bid
        new_bid.save()
        auction.save()
    else:
        if auction.high_bid.bid < bid:
            auction.high_bid = new_bid
            new_bid.save()
            auction.save()


    return HttpResponseRedirect(reverse('index'))




def buylist(request):
    if request.method == "GET":
        if request.user:
            user = request.user
            auctions = Auction.objects.filter(bought_by=user)
            return render(request, "auctions/buylist.html", {
                "auctions": auctions,
            })
        else:
            return HttpResponseRedirect(reverse('index'))

def buy_now(request, auct_id):

    auction = Auction.objects.get(pk=int(auct_id))
    user = request.user
    auction.active = False
    auction.winner.add(user)

    auction.watchlist.remove(user)

    auction.save()
    return HttpResponseRedirect(reverse('winlist'))


def create_listing(request):
    if request.method == "GET":
        category = Category.objects.all()
        return render(request, "auctions/create.html", {
            "category": category
        })
    else:
        title = request.POST["title"]
        description = request.POST["description"]
        wanted = float(request.POST["wanted"])
        category = Category.objects.get(pk = int(request.POST["category"]))
        image_url= request.POST["image_url"]
        owner = request.user
        newListing = Auction(
            title = title,
            description=description,
            wanted= wanted,
            category=category,
            owner=owner,
            image_url=image_url,
            )
        newListing.save()
        bid = Bid()
        return HttpResponseRedirect(reverse('index'))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
