Title: Project: Distributed Social Networking
date: 2024-09-01
tags: project, grading
authors: Hazel Victoria Campbell
status: published
summary: Distributed Social Networking (SocialDistribution)

---

<style>
    html body main {
        background-image: url("/theme/draft.png");
        background-repeat: repeat;
        background-size: 100%;
    }
</style>

[TOC]

# Description

The web is fundamentally interconnected and peer to peer. There's
no really great reason why we should all use facebook.com or
google+ or MySpace or something like that. If these social networks
came up with an API you could probably link between them and use
the social network you wanted. Furthermore, you might gain some
autonomy.

Thus, in the spirit of diaspora https://diasporafoundation.org/ 
(Diaspora was the predecessor to Mastodon)
we want to build something like diaspora but far, far simpler.

This blogging/social network platform will allow the importing of
other sources of information (GitHub) as well allow the
distribution and sharing of posts and content.

An author sitting on one node can aggregate
the posts of authors they follow on other nodes.   

We are going to go with an inbox model where you share posts to
your followers by sending them your posts. This is similar to
activity pub: https://www.w3.org/TR/activitypub/ ActivityPub
is the protocol that powers most distributed social media such
as Mastodon.
Activity Pub is great, but too complex for a class project.

We also won't be adding much in the way of encryption or security
to this platform. We're keeping it simple and restful.

Choose at least 3 other groups to work with!

## Scenario 

I log into SocialDistribution. I see my stream which is filled with
posts that have arrived in my inbox combined with public posts that my node knows about.
I browse them and I click like on anything by my friend Steph who is on another node.

When I click like, my node sends a like object to Steph's inbox
that references her post.

I then comment on Steph's post. This sends a comment object to
Steph's inbox that references her post.

Steph's node will process events at her inbox and record the
comments and likes appropriately.

Then I write a public post, a public service announcement (PSA)
about how public service announcements are pretentious preformative
social media, and you shouldn't make them. The irony is lost on me.
I make an unlisted image post that contains an image for the PSA
and reference it from my PSA post. Nonetheless, my node records my
post and makes a URL for both posts and then proceeds to send my
public posts to the inboxes of everyone who follows me. My node
knows who follows me and thus can just send the public post to each
of those inboxes. Perhaps there will be a scaling problem in the
future.

Later I write a friends-only post about how much I hate the movie The Room (2003).
Tommy Wiseau can't see it because I'm not friends with Tommy Wiseau, but this post is sent to Steph's inbox, and she can see it because she's my friend.

When Steph logs into her node she'll see her stream and my public
post and my friends-only post will be on her stream.
She should also see that I've liked and commented her post.

## Scenario Summary

All actions from authors are routed through the inbox of the receiving authors by the node itself.

Nodes will store copies of posts because they receive them in the inbox.

Likes and comments on posts are all sent to the inbox of the author.

Public posts are sent to the inboxes of all followers of the author.

Friends-only posts are sent to the inboxes of all friends of the author.

Posts, likes, comments, posts, are all sent to the inboxes of the authors that should be able to see them.

## Project Parts 

* Part 0 - sign up a repo
* Part 1 - 1/2 way implementation
* Part 2 - Lonely implementation
* Part 3 - Connected implementation
* Part 4 - Connect with Groups
* Part 5 - Finish it off!

# Collaboration
   
* You may consult with other teams. The submission must be your own team's source code.
* You may work with 5 other students (groups of 6)
* Work will be submitted together
* Collaboration must be documented in the README.md file
* Any external source code must be referenced and documented in the README.md file.
* You make collaborate/consult with other groups in order to get your web services to integrate with each other

# User Stories

* Identity
    * As an author, I want a consistent identity per node, so that URLs to me/my posts are predictable and don't stop working.
        * Note: This includes API links and web frontend links.
        * Note: This doesn't include authors/posts that are deleted.
    * As a node admin, I want to host multiple authors on my node, so I can have a friendly online community.
    * As an author, I want a public page with my profile information, so that I can link people to it.
    * As an author, I want to my (new, public) GitHub activity to be automatically turned into public posts, so everyone can see my GitHub activity too.
    * As an author, I want my profile page to show my public posts (most recent first), so they can decide if they want to follow me.
    * As an author, I want to be able to use my web-browser to manage my profile, so I don't have to use a clunky API.
* Posting
    * As an author, I want to make posts, so I can share my thoughts and pictures with other local authors.
    * As an author, I want my node to send my posts to my remote followers and friends, so that remote authors following me can see them. *Part 3-5 only*
    * As an author, I want to edit my posts locally, so that I'm not stuck with a typo on a popular post.
    * As an author, I want my node to re-send posts I've edited to everywhere they were already sent, so that people don't keep seeing the old version. *Part 3-5 only*
    * As an author, posts I make can be in CommonMark, so I can give my posts some basic formatting.
    * As an author, posts I make can be in simple plain text, because I don't always want all the formatting features of CommonMark.
    * As an author, posts I create can be images, so that I can share pictures and drawings.
    * As an author, posts I create that are in CommonMark can link to images, so that I can illustrate my posts.
    * As an author, I want to delete my own posts locally, so I can remove posts that are out of date or made by mistake.
    * As an author, I want my node to re-send posts I've deleted to everyone they were already sent, so I know remote users don't keep seeing my deleted posts forever. *Part 3-5 only*
    * As an author, I want to be able to use my web-browser to manage/author my posts, so I don't have to use a clunky API.
    * As an author, other authors cannot modify my posts, so that I don't get impersonated.
* Reading
    * As an author, I want a "stream" which shows all the posts I should know about, so I don't have to switch between different pages.
        * As an author, I want my stream page to show me all the public posts my node knows about, so I can find new people to follow.
        * As an author, I want my stream page to show me all the unlisted and friends-only posts of all the authors I follow.
        * As an author, I want my stream page to show me the most recent version of a post if it has been edited.
        * As an author, I want my stream page to **not** show me posts that have been deleted.
    * As an author, I want my "stream" page to be sorted with the most recent posts first. 
* Visibility
    * As an author, I want to be able to make my posts "public", so that everyone can see them.
    * As an author, I want to be able to make my posts "unlisted," so that my followers see them, and anyone with the link can also see them.
    * As an author, I want to be able to make my posts "friends-only," so that I don't have to worry about people I don't know seeing them.
    * As an author, I want my friends to see my friends-only, unlisted, and public posts in their stream.
    * As an author, I want anyone following me to see my unlisted and public posts in their stream.
    * As an author, I want everyone to see my public posts in their stream.
    * As an author, I want everyone to be able to see my public and unlisted posts, if they have a link to it.
    * As an author, I don't anyone who isn't a friend to be able to see my friends-only posts and images, so I can feel safe about posting.
    * As an author, I don't want anyone except the node admin to see my deleted posts.
    * As an author, posts I create should always be visible to me until they are deleted, so I can find them to edit them or review them or get the link or whatever I want to do with them.
* Sharing
    * As an author, I can share other author's public posts, so I can make things go viral! (repost, boost, retweet, etc)
    * As an author, posts that I share will show up on the timeline of anyone who is following me. 
    * As a node admin, I want to share public images with users on other nodes, so that they are visible by users of other nodes. *Part 3-5 only.*
    * As an author, I want my friends-only/unlisted images and posts to *not* be shareable, so I know that if someone wants to share it they'll at least have to take a screenshot.
        * Note: public posts (and image posts) are re-shareable.
    * As an author, I should be able to browse the public posts of everyone, so that I can see what's going on beyond authors I follow.
        * Note: this should include all local public posts and all public posts received in any inbox.
* Following/Friends
    * As an author, I want to follow local authors, so that I can see their public posts.
    * As an author, I want to follow remote authors, so that I can see their public posts. *Part 3-5 only.*
    * As an author, I want to be able to approve or deny other authors following me, so that I don't get followed by people I don't like.
    * As an author, I want to know if I have "follow requests," so I can approve them.
    * As an author, I want to unfollow authors I am following, so that I don't have to see their posts anymore.
    * As an author, if I am following another author, and they are following me, I want us to be considered friends, so that they can see my friends-only posts.
    * As an author, I want to unfriend other authors by unfollowing them, so that they can no longer see my friends-only posts.
    * As an author, my node will know about my followers, who I am following, and my friends, so that I don't have to keep track of it myself.
* Comments/Likes
    * As an author, I want to comment on posts that I can access, so I can make a witty reply.
    * As an author, I want to like posts that I can access, so I can show my appreciation.
    * As an author, when someone sends me a public post I want to see the likes, so I can tell if it's good or not.
    * As an author, comments on my friends-only posts are visible only to my friends and the comment's author.
* node Management
    * As a node admin, images can be hosted on my node, so that my users can use them in their CommonMark posts.
    * As a node admin, I want to be able to add, modify, and delete authors, to fix problems or remove unwanted users.
    * As a node admin, I want to OPTIONALLY be able to allow users to sign up but require my OK to finally be on my node, so that I can prevent unwanted users spambots.
    * As a node admin, I want to be able to connect to remote nodes by entering only the URL of the remote node, a username, and a password, so that I don't have to edit code.
    * As a node admin, I want a RESTful interface for most operations, so that I can connect to other nodes and allow my users to use alternate clients other than the web frontend.
    * As a node admin, I want to be able to add nodes to share with.
    * As a node admin, I want to be able to remove nodes and stop sharing with them.
    * As a node admin, I can prevent nodes from connecting to my node if they don't have a valid username and password.
    * As a node admin, node to node connections can be authenticated with HTTP Basic Auth, so that I don't have to deal with tokens.
    * As a node admin, I can disable the node to node interfaces for connections that I no longer want, in case another node goes bad.
    * As a node admin, I want everything to be stored in a well-indexed relational database, so that my website is snappy, and I can write SQL to fix things if I need to, make backups, etc...
        * Use Postgres on Heroku and SQLite for testing on your local machine.
        * Other DBaaS (e.g. Firebase) is forbidden.
    * As a node admin, I don't want arrays to be stored in database fields, so that my node won't get slower over time.
    * As a node admin, I don't want to have seperate frontend and backend web servers, so I don't have to manage two web servers/services.
    * As a node admin, I want deleted posts stay in the database and only be removed from the UI and API, so I can see what was deleted.
    * As a node admin, I want my node's UI to only communicate with my nodes web server, so I can prevent XSS.

# Main Concepts

* Node
    * A single webserver plus a single database
    * Serves and stores everything needed for the entire app
    * Doesn't rely on additional web servers
    * Can connect to other nodes to exchange posts, likes, comments, follow requests...
    * Keeps track of the identities, posts, likes, comments, etc. of its authors
* Author
    * Makes posts
    * Following other authors
    * Can have followers
    * Makes friends
    * Likes posts
    * Comments on posts
    * A generally nice person
    * Can register with the admins approval
    * Can find other authors by using the public timeline
* Local Node
    * The node that an author is signed up for and uses to manage their posts, likes, comments, and profile.
* Remote Node
    * Any node that isn't the author's local node.
* Local Author
    * Another author on the same node as an author.
* Remote Author
    * Another author on a different node as an author.
* Node Admin
    * Manages a node
    * Allows people to sign up
    * Responsible for private data
    * Keeps deleted data forever
* Follower
    * An author
    * Someone who follows you (you are an author)
    * Your node will send posts to the follower's inbox
* Following
    * An author
    * Someone you are following
    * Their node will send posts to your inbox
* Friend
    * You follow them, and they follow you
* Restful service
    * The model of the service and its API
* Server
    * A single Django or flask web server
    * running on a single computer
    * Has its own unique database
* UI
    * The HTML/CSS/JS coated version user interface 
    * Runs in the browser
    * Served from the web server of the node
    * Must only communicate with the node it was served from
* Post
    * It has a unique URL
    * The URL stays the same
    * The node keeps track of what inboxes have been notified
    * It can be edited
    * It can be deleted
    * It can be:
        * A picture
        * or A plain text
        * or A Markdown text
    * It can be:
        * public
        * or friends-only
        * or unlisted
        * or deleted
    * It can be liked
    * It can be commented on
    * Likes and comments are sent back to the author's inbox.
* Public Post
    * This is a post that will be sent to all of my follower's inboxes, to make sure their nodes know about it.
    * This is a post that will show up in all the streams of all the authors on all the nodes where I have at least one follower.
    * This is a post that will show up on my public profile page.
    * Anyone can see it.
    * Anyone can access it by URL.
    * Public posts can be liked by anyone.
    * Public posts can have comments from anyone.
* Unlisted Post
    * This post will **not** show up in the "stream" of authors that don't follow me.
    * This is a post that will be sent to all my follower's inboxes.
    * Anyone can access it by URL.
    * Anyone can see the unlisted post, if they already know about it.
    * Unlisted posts can be liked by anyone.
    * Unlisted posts can have comments from anyone.
* Friends-Only Post
    * This is a post that will be sent to all my friend's inboxes.
    * This is a post that will show up in all my friend's streams.
    * This post won't show up in anyone's stream unless they're my friend.
    * The URL can only be used by the author of the post and admins.
    * Friends-Only posts can be liked by the author's friends.
    * Friends-Only posts can have comments from the author's friends.
    * This post can be deleted.
* Deleted Post
    * When Public/Unlisted/Friends-Only post is deleted by the author, the node converts it to a Deleted Post.
    * This is a post that will be sent to all inboxes it was previously sent to.
    * This post will not show up in anyone's stream.
    * This post will not show up on any profile page.
    * This post cannot be accessed at all except by the local node administrator.
    * This post cannot be liked.
    * This post cannot be commented on.
* Inbox
    * **An inbox is not something the user ever actually sees. It is an API endpoint *only*.**
    * This is what a READER or USER of the social network has. They follow authors, and the authors they follow send objects to their inbox.
    * This is something that only exists in the API. There is no special inbox in the User Interface, posts sent to a user's inbox are integrated into a their stream.
    * This forms the backbone of the timeline of the social media user.
    * This receives likes and comments.
* Stream
    * The user interface showing date-sorted (most recent first) local, public posts combined with posts from everyone that user follows.
* Remote
    * A node to node connection. Requests from another node. HTTP Basic Auth authenticated.
* Local
    * A local user accessing the REST API. Likely will use their cookie-auth, basic auth, or token auth. Local usually implies you check whether or not the user should have access. For node local API access to the inbox should be limited to only that authenticated authors---don't snoop!
* Profile Page
    * A page that shows information about me as well as my public posts.
* Push
    * When the node that has the information sends it other relevant nodes, without being requested.
* Pull
    * When the node that needs the information requests from the node that has it.


Frontend/API Visibility | Admin             | Friend        | Follower       | Everyone
------------------------|-------------------|---------------|----------------|----------------
Public                  | control panel     | link + stream |  link + stream |  link + stream
Unlisted                | control panel     | link + stream |  link + stream |  link
Friends Only            | control panel     |               |                |
Deleted                 | control panel     |               |                |

Database/Node2Node     | Type | Author         | Friend                  | Follower                   | Anyone
-----------------------|------|----------------|-------------------------|----------------------------|--------
New Public             | push | from           | to `inbox`              | to `inbox`                 |
New Unlisted           | push |                | to `inbox`              | to `inbox`                 |
New Friends Only       | push |                | to `inbox`              |                            |
Deleted Public         | push |                | to `inbox`              | to `inbox`                 | to inboxes post was sent to before
Deleted Unlisted       | push |                | to `inbox`              | to `inbox`                 | to inboxes post was sent to before
Deleted Friends Only   | push |                | to `inbox`              |                            | to inboxes post was sent to before
Edited Public          | push |                | to `inbox`              | to `inbox`                 | to inboxes post was sent to before
Edited Unlisted        | push | from           | to `inbox`              | to `inbox`                 | to inboxes post was sent to before
Edited Friends Only    | push | from           | to `inbox`              |                            | to inboxes post was sent to before
Commented Public       | push | to `inbox`     | from                    | from                       | from
Commented Unlisted     | push | to `inbox`     | from                    | from                       | from
Commented Friends Only | push | to `inbox`     | from                    |                            |
Liked Public           | push | to `inbox`     | from                    | from                       | from
Liked Unlisted         | push | to `inbox`     | from                    | from                       | from
Liked Friends Only     | push | to `inbox`     | from                    |                            |
Follow                 | push | to `inbox`     |                         |                            | from
Follow-back (friend)   | push | from           |                         | to `inbox`                 |
Unfollow               | push |                | *not yet implemented*   | *not yet implemented*      |
View Public            | pull | to `post`      | optional from           | optional from              | optional from
View Unlisted          | pull | to `post`      | optional from           | optional from              | optional from
View Friends-Only      | pull |                | *not yet implemented*   |                            |
View Deleted           | pull |                |                         |                            |
View Following         | pull | to `followers` | optional from           | optional from              |

Notes on the above tables:
    * This can work entirely on push from the author's server to another author's inbox.
    * Yes, this means that only the local node (node where the post came from) will have a complete list of comments/likes. Mastodon/Diaspora also have this problem.
    * "Unfollow" the API is missing this functionality.
    * Yes, a node may have an out of date list of followers if a remote follower unfollows.
    * "View Friends-Only" the API is missing this functionality. 

## Authentication

* Remote node authentication is global between nodes. It requires an admin to allow node to node access.
* Remote node authentication is done solely with HTTP basic auth
* Local auth uses your local auth mechanisms (cookies, tokens, basic auth).
* Local auth is between an author's UI and an author's node server.
    * It could be the web UI you make
    * It could also be another custom UI (like an android app)
* Local refers the RESTful API for authors on that node.
    * This is useful for frameworks like react, vue, or angular to get access to data, and enable a more client heavy UI.
    * Even if your frontend does not use them, endpoints marked [local] should be usable by a future Android/iOS client to achieve the same functionality as frontend.

## Pagination

If something is paginated it has query options:

* page - how many pages of objects have been delivered
* size - how big is a page
* Page 4 of objects http://service/author/{author_id}/posts/{post_id}/comments?page=4
* Page 4 of objects but 40 per page http://service/author/{author_id}/posts/{post_id}/comments?page=4&size=40
* 1 based indexing. First page is 1.

# Communication

* HTTP Methods (PUT POST GET DELETE) not explicitly listed are not allowed methods
     * Most HTTP methods are local API only, and provided for local node use.
     * Local node use means for use by the frontend to communicate with the backend it came from.
* You are free to add your own endpoints for local node use, but you must document and test them.

## Who talks to Who

* Required: The backends talk to each other, mostly trough POST requests to the `inbox` URLs for remote authors.
* Optional: The frontend talks to the backend for the same node.
* Forbidden: The frontend talks to a backend of another node. 
 
## Overview

Almost all node-to-node communication proceeds by the node where something (post/like/comment/follow request) was created POSTing that thing that was created to the relevant authors inbox on a remote node.

node-to-node (marked as "[remote]") request other than "POST to inbox" are rarely needed, but you should support them in case the remote node needs to check something.

## Example (node-to-node API View)

The Frontend-to-Backend (also known as [local]) communication for this scenario is up to your team, this only describes the Backend-to-Backend communication between two different nodes.

1. I sign up for SocialDistribution on http://node1
2. node1 administrator approves my account.
3. Now an author object exists that represents me at http://node1/api/authors/555555555
4. I use the interface to make a follow request to Steph, who is node2/api/authors/777777777
5. My node POSTs the follow request to Steph's inbox at http://node2/api/authors/777777777/inbox
6. When Steph logs in, she sees my follow request and approves it.
7. Now Steph's node (node2) knows that I am following her.
8. Steph makes a public post.
9. Steph's node (node2) sends Steph's new post to my inbox with POST http://node1/api/authors/555555555/inbox.
10. I eventually see Steph's new post, and click like on it.
11. My node sends the like to Steph's inbox with POST http://node2/api/authors/777777777/inbox

# API Endpoints

## Authors

* URL: ://service/authors/
    * GET [local, remote]: retrieve all profiles on the node (paginated)
        * page: how many pages
        * size: how big is a page
* Example query: GET ://service/authors?page=10&size=5 
    * Gets the 5 authors, authors 45 to 49.
* Example: GET ://service/authors/

```.js
{
    "type": "authors",      
    "authors":[
        {
            "type":"author",
            "id":"http://127.0.0.1:5454/authors/1d698d25ff008f7538453c120f581471",
            "url":"http://127.0.0.1:5454/authors/1d698d25ff008f7538453c120f581471",
            "host":"http://127.0.0.1:5454/",
            "displayName":"Greg Johnson",
            "github": "http://github.com/gjohnson",
            "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
        },
        {
            "type":"author",
            "id":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
            "host":"http://127.0.0.1:5454/",
            "displayName":"Lara Croft",
            "url":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
            "github": "http://github.com/laracroft",
            "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
        }
    ]
}
```

## Single Author

* URL: ://service/authors/{AUTHOR_ID}/
    * GET [local, remote]: retrieve AUTHOR_ID's profile
    * PUT [local]: update AUTHOR_ID's profile
* Example Format:

```.js
{
    "type":"author",
    // ID of the Author
    "id":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
    // the home host of the author
    "host":"http://127.0.0.1:5454/",
    // the display name of the author
    "displayName":"Lara Croft",
    // url to the authors profile
    "url":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
    // HATEOS url for Github API
    "github": "http://github.com/laracroft",
    // Image from a public domain
    "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
}
```
## Followers

* URL: ://service/authors/{AUTHOR_ID}/followers
    * GET [local, remote]: get a list of authors who are AUTHOR_ID's followers
* URL: ://service/authors/{AUTHOR_ID}/followers/{FOREIGN_AUTHOR_ID}
    * Note: foreign author ID should be a percent encoded URL of the foreign author. An example URL would be:
        * `http://example-node-1/authors/178aba49-ca39-4741-b227-f40d072b1222/followers/http%3A%2F%2Fexample-node-2%2Fauthors%2F5f57808f-0bc9-4b3d-bdd1-bb07c976d12d`
    * DELETE [local]: remove FOREIGN_AUTHOR_ID as a follower of AUTHOR_ID
    * PUT [local]: Add FOREIGN_AUTHOR_ID as a follower of AUTHOR_ID (must be authenticated)
    * GET [local, remote] check if FOREIGN_AUTHOR_ID is a follower of AUTHOR_ID
        * Should return 404 if they're not
        * Should return similar format to Follow Request below if they are.
* Example: GET ://service/authors/{AUTHOR_ID}/followers

```.js
{
    "type": "followers",      
    "followers":[
        {
            "type":"author",
            "id":"http://127.0.0.1:5454/authors/1d698d25ff008f7538453c120f581471",
            "url":"http://127.0.0.1:5454/authors/1d698d25ff008f7538453c120f581471",
            "host":"http://127.0.0.1:5454/",
            "displayName":"Greg Johnson",
            "github": "http://github.com/gjohnson",
            "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
        },
        {
            "type":"author",
            "id":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
            "host":"http://127.0.0.1:5454/",
            "displayName":"Lara Croft",
            "url":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
            "github": "http://github.com/laracroft",
            "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
        }
    ]
}
```
   
## Follow Request

* When author 1 tries to follow author 2, author 1's node send the follow request to author 2's node.
* If the author 2 accepts the Follow Request then author 1 is following author 2.
    * If author 2 is also already following author 1, then they are now friends.
* Sent to inbox of "object" 
* Example format:

```.js
{
    "type": "Follow",      
    "summary":"Greg wants to follow Lara",
    "actor":{
        "type":"author",
        "id":"http://127.0.0.1:5454/authors/1d698d25ff008f7538453c120f581471",
        "url":"http://127.0.0.1:5454/authors/1d698d25ff008f7538453c120f581471",
        "host":"http://127.0.0.1:5454/",
        "displayName":"Greg Johnson",
        "github": "http://github.com/gjohnson",
        "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
    },
    "object":{
        "type":"author",
        // ID of the Author
        "id":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
        // the home host of the author
        "host":"http://127.0.0.1:5454/",
        // the display name of the author
        "displayName":"Lara Croft",
        // url to the authors profile
        "url":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
        // HATEOS url for Github API
        "github": "http://github.com/laracroft",
        // Image from a public domain
        "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
    }
}
```

## Post

* URL: ://service/authors/{AUTHOR_ID}/posts/{POST_ID}
    * GET [local, remote] get the public post whose id is POST_ID
        * friends-only posts: must be authenticated
    * DELETE [local] remove the post whose id is POST_ID
        * local posts: must be authenticated locally as the author
    * PUT [local] update a post where its id is POST_ID
        * local posts: must be authenticated locally as the author
* Creation URL ://service/authors/{AUTHOR_ID}/posts/
    * GET [local, remote] get the recent posts from author AUTHOR_ID (paginated)
        * Not authenticated: only public posts.
        * Authenticated locally as author: all posts.
        * Authenticated locally as friend of author: public + friends-only posts.
        * Authenticated as remote node: This probably should not happen. Remember, the way remote node becomes aware of local posts is by local node pushing those posts to inbox, not by remote node pulling.
    * POST [local] create a new post but generate a new id
        * Authenticated locally as author
* Be aware that Posts can be images that need base64 decoding.
    * posts can also hyperlink to images that are public
* Example Format:

```.js
{
    "type":"post",
    // title of a post
    "title":"A post title about a post about web dev",
    // id of the post
    "id":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e/posts/764efa883dda1e11db47671c4a3bbd9e"
    // where did you get this post from?
    "source":"http://lastplaceigotthisfrom.com/authors/xxxxxx/posts/yyyyyy",
    // where is it actually from
    "origin":"http://whereitcamefrom.com/authors/wwwwww/posts/zzzzzz",
    // a brief description of the post
    "description":"This post discusses stuff -- brief",
    // The content type of the post
    // assume either
    // text/markdown -- common mark
    // text/plain -- UTF-8
    // application/base64 # this an image that is neither a jpeg or png
    // image/png;base64 # this is an embedded png -- images are POSTS. So you might have a user make 2 posts if a post includes an image!
    // image/jpeg;base64 # this is an embedded jpeg
    // for HTML you will want to strip tags before displaying
    "contentType":"text/plain",
    "content":"Þā wæs on burgum Bēowulf Scyldinga, lēof lēod-cyning, longe þrāge folcum gefrǣge (fæder ellor hwearf, aldor of earde), oð þæt him eft onwōc hēah Healfdene; hēold þenden lifde, gamol and gūð-rēow, glæde Scyldingas. Þǣm fēower bearn forð-gerīmed in worold wōcun, weoroda rǣswan, Heorogār and Hrōðgār and Hālga til; hȳrde ic, þat Elan cwēn Ongenþēowes wæs Heaðoscilfinges heals-gebedde. Þā wæs Hrōðgāre here-spēd gyfen, wīges weorð-mynd, þæt him his wine-māgas georne hȳrdon, oð þæt sēo geogoð gewēox, mago-driht micel. Him on mōd bearn, þæt heal-reced hātan wolde, medo-ærn micel men gewyrcean, þone yldo bearn ǣfre gefrūnon, and þǣr on innan eall gedǣlan geongum and ealdum, swylc him god sealde, būton folc-scare and feorum gumena. Þā ic wīde gefrægn weorc gebannan manigre mǣgðe geond þisne middan-geard, folc-stede frætwan. Him on fyrste gelomp ǣdre mid yldum, þæt hit wearð eal gearo, heal-ærna mǣst; scōp him Heort naman, sē þe his wordes geweald wīde hæfde. Hē bēot ne ālēh, bēagas dǣlde, sinc æt symle. Sele hlīfade hēah and horn-gēap: heaðo-wylma bād, lāðan līges; ne wæs hit lenge þā gēn þæt se ecg-hete āðum-swerian 85 æfter wæl-nīðe wæcnan scolde. Þā se ellen-gǣst earfoðlīce þrāge geþolode, sē þe in þȳstrum bād, þæt hē dōgora gehwām drēam gehȳrde hlūdne in healle; þǣr wæs hearpan swēg, swutol sang scopes. Sægde sē þe cūðe frum-sceaft fīra feorran reccan",
    // the author has an ID where by authors can be disambiguated
    "author":{
        "type":"author",
        // ID of the Author
        "id":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
        // the home host of the author
        "host":"http://127.0.0.1:5454/",
        // the display name of the author
        "displayName":"Lara Croft",
        // url to the authors profile
        "url":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
        // HATEOS url for Github API
        "github": "http://github.com/laracroft",
        // Image from a public domain (optional, can be missing)
        "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
    },
    // comments about the post
    // return a maximum number of comments
    // total number of comments for this post
    "count": 1023,
    // the first page of comments
    "comments":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e/posts/de305d54-75b4-431b-adb2-eb6b9e546013/comments"
    // commentsSrc is OPTIONAL and can be missing
    // You should return ~ 5 comments per post.
    // should be sorted newest(first) to oldest(last)
    // this is to reduce API call counts
    "commentsSrc":{
        "type":"comments",
        "page":1,
        "size":5,
        "post":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e/posts/de305d54-75b4-431b-adb2-eb6b9e546013"
        "id":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e/posts/de305d54-75b4-431b-adb2-eb6b9e546013/comments"
        "comments":[
            {
                "type":"comment",
                "author":{
                    "type":"author",
                    // ID of the Author (UUID)
                    "id":"http://127.0.0.1:5454/authors/1d698d25ff008f7538453c120f581471",
                    // url to the authors information
                    "url":"http://127.0.0.1:5454/authors/1d698d25ff008f7538453c120f581471",
                    "host":"http://127.0.0.1:5454/",
                    "displayName":"Greg Johnson",
                    // HATEOS url for Github API
                    "github": "http://github.com/gjohnson",
                    // Image from a public domain
                    "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
                },
                "comment":"Sick Olde English",
                "contentType":"text/markdown",
                // ISO 8601 TIMESTAMP
                "published":"2015-03-09T13:07:04+00:00",
                // ID of the Comment (UUID)
                "id":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e/posts/de305d54-75b4-431b-adb2-eb6b9e546013/comments/f6255bb01c648fe967714d52a89e8e9c",
            }
        ]
    }
    // ISO 8601 TIMESTAMP
    "published":"2015-03-09T13:07:04+00:00",
    // visibility ["PUBLIC","FRIENDS","UNLISTED","DELETED"]
    "visibility":"PUBLIC"
    // for visibility PUBLIC means it is open to the wild web
    // FRIENDS means if we're friends I can see the post
    // FRIENDS should've already been sent the post so they don't need thi
    // "DELETED" should never show up in the restful API or frontend, but will need to be marked in the database
}
```

## Image Posts

Image Posts are just posts that are images. But they are encoded as base64 data.
You can inline an image post using a data URL, or you can use this 
shortcut to get the image if authenticated to see it.

* URL: ://service/authors/{AUTHOR_ID}/posts/{POST_ID}/image
    * GET [local, remote] get the public post converted to binary as an image
      * return 404 if not an image
* This end point decodes image posts as images. This allows the use of image tags in Markdown.
* You can use this to proxy or cache images.

## Comments

* URL: ://service/authors/{AUTHOR_ID}/posts/{POST_ID}/comments
    * GET [local, remote] get the list of comments of the post whose id is POST_ID (paginated)
    * POST [local] if you post an object of "type":"comment", it will add your comment to the post whose id is POST_ID
* example comment from ://service/authors/{AUTHOR_ID}/posts/{POST_ID}/comments

```.js
{
    "type":"comment",
    "author":{
        "type":"author",
        // ID of the Author (UUID)
        "id":"http://127.0.0.1:5454/authors/1d698d25ff008f7538453c120f581471",
        // url to the authors information
        "url":"http://127.0.0.1:5454/authors/1d698d25ff008f7538453c120f581471",
        "host":"http://127.0.0.1:5454/",
        "displayName":"Greg Johnson",
        // HATEOS url for Github API
        "github": "http://github.com/gjohnson",
        // Image from a public domain
        "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
    }
    "comment":"Sick Olde English",
    "contentType":"text/markdown",
    // ISO 8601 TIMESTAMP
    "published":"2015-03-09T13:07:04+00:00",
    // ID of the Comment (UUID)
    "id":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e/posts/de305d54-75b4-431b-adb2-eb6b9e546013/comments/f6255bb01c648fe967714d52a89e8e9c",
}
```
* example comments from a post:

```.js
{
    "type":"comments",
    "page":1,
    "size":5,
    "post":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e/posts/de305d54-75b4-431b-adb2-eb6b9e546013"
    "id":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e/posts/de305d54-75b4-431b-adb2-eb6b9e546013/comments"
    "comments":[
        {
            "type":"comment",
            "author":{
                "type":"author",
                // ID of the Author (UUID)
                "id":"http://127.0.0.1:5454/authors/1d698d25ff008f7538453c120f581471",
                // url to the authors information
                "url":"http://127.0.0.1:5454/authors/1d698d25ff008f7538453c120f581471",
                "host":"http://127.0.0.1:5454/",
                "displayName":"Greg Johnson",
                // HATEOS url for Github API
                "github": "http://github.com/gjohnson",
                // Image from a public domain
                "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
            },
            "comment":"Sick Olde English",
            "contentType":"text/markdown",
            // ISO 8601 TIMESTAMP
            "published":"2015-03-09T13:07:04+00:00",
            // ID of the Comment (UUID)
            "id":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e/posts/de305d54-75b4-431b-adb2-eb6b9e546013/comments/f6255bb01c648fe967714d52a89e8e9c",
        }
    ]
}
```

## Likes

* You can like posts and comments
* Send them to the inbox of the author of the post or comment
* URL: ://service/authors/{AUTHOR_ID}/inbox
    * POST [local, remote]: send a like object to AUTHOR_ID
* URL: ://service/authors/{AUTHOR_ID}/posts/{POST_ID}/likes
    * GET [local, remote] a list of likes from other authors on AUTHOR_ID's post POST_ID
* URL: ://service/authors/{AUTHOR_ID}/posts/{POST_ID}/comments/{COMMENT_ID}/likes
    * GET [local, remote] a list of likes from other authors on AUTHOR_ID's post POST_ID comment COMMENT_ID
* Example like object:

```.js
{
    "summary": "Lara Croft Likes your post",         
    "type": "Like",
    "author":{
        "type":"author",
        "id":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
        "host":"http://127.0.0.1:5454/",
        "displayName":"Lara Croft",
        "url":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
        "github":"http://github.com/laracroft",
        "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
    },
    "object":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e/posts/764efa883dda1e11db47671c4a3bbd9e"
}
```

## Liked

* URL: ://service/authors/{AUTHOR_ID}/liked
    * GET [local, remote] list what public things AUTHOR_ID liked.
      * It's a list of of likes originating from this author
      * Note: be careful here private information could be disclosed.
* Example Format:

```.js
{
    "type":"liked",
    "likes":[
        {
            "summary": "Lara Croft Likes your post",         
            "type": "Like",
            "author":{
                "type":"author",
                "id":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
                "host":"http://127.0.0.1:5454/",
                "displayName":"Lara Croft",
                "url":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
                "github":"http://github.com/laracroft",
                "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
            },
            "object":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e/posts/764efa883dda1e11db47671c4a3bbd9e"
        }
    ]
}
```

## Inbox

* The inbox is all the new posts from who you follow, as well as follow requests, likes, and comments you should be aware of
* The inbox is the API equivalent of the stream in the UI
* URL: ://service/authors/{AUTHOR_ID}/inbox
    * GET [local]: if authenticated get a list of posts sent to AUTHOR_ID (paginated)
        * Should be sorted most recent first
    * POST [local, remote]: send a post to the author
      * if the type is "post" then add that post to AUTHOR_ID's inbox
      * if the type is "follow" then add that follow is added to AUTHOR_ID's inbox to approve later
      * if the type is "Like" then add that like to AUTHOR_ID's inbox
      * if the type is "comment" then add that comment to AUTHOR_ID's inbox
    * DELETE [local]: clear the inbox
* Example, retrieving an inbox:

```.js
{
    "type":"inbox",
    "author":"http://127.0.0.1:5454/authors/c1e3db8ccea4541a0f3d7e5c75feb3fb",
    "items":[
        {
            "type":"post",
            "title":"A Friendly post title about a post about web dev",
            "id":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e/posts/764efa883dda1e11db47671c4a3bbd9e"
            "source":"http://lastplaceigotthisfrom.com/authors/xxxxxx/posts/yyyyyy",
            "origin":"http://whereitcamefrom.com/authors/wwwwww/posts/zzzzzz",
            "description":"This post discusses stuff -- brief",
            "contentType":"text/plain",
            "content":"Þā wæs on burgum Bēowulf Scyldinga, lēof lēod-cyning, longe þrāge folcum gefrǣge (fæder ellor hwearf, aldor of earde), oð þæt him eft onwōc hēah Healfdene; hēold þenden lifde, gamol and gūð-rēow, glæde Scyldingas. Þǣm fēower bearn forð-gerīmed in worold wōcun, weoroda rǣswan, Heorogār and Hrōðgār and Hālga til; hȳrde ic, þat Elan cwēn Ongenþēowes wæs Heaðoscilfinges heals-gebedde. Þā wæs Hrōðgāre here-spēd gyfen, wīges weorð-mynd, þæt him his wine-māgas georne hȳrdon, oð þæt sēo geogoð gewēox, mago-driht micel. Him on mōd bearn, þæt heal-reced hātan wolde, medo-ærn micel men gewyrcean, þone yldo bearn ǣfre gefrūnon, and þǣr on innan eall gedǣlan geongum and ealdum, swylc him god sealde, būton folc-scare and feorum gumena. Þā ic wīde gefrægn weorc gebannan manigre mǣgðe geond þisne middan-geard, folc-stede frætwan. Him on fyrste gelomp ǣdre mid yldum, þæt hit wearð eal gearo, heal-ærna mǣst; scōp him Heort naman, sē þe his wordes geweald wīde hæfde. Hē bēot ne ālēh, bēagas dǣlde, sinc æt symle. Sele hlīfade hēah and horn-gēap: heaðo-wylma bād, lāðan līges; ne wæs hit lenge þā gēn þæt se ecg-hete āðum-swerian 85 æfter wæl-nīðe wæcnan scolde. Þā se ellen-gǣst earfoðlīce þrāge geþolode, sē þe in þȳstrum bād, þæt hē dōgora gehwām drēam gehȳrde hlūdne in healle; þǣr wæs hearpan swēg, swutol sang scopes. Sægde sē þe cūðe frum-sceaft fīra feorran reccan",
            "author":{
                "type":"author",
                "id":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
                "host":"http://127.0.0.1:5454/",
                "displayName":"Lara Croft",
                "url":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
                "github": "http://github.com/laracroft",
                "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
            },
            "comments":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e/posts/de305d54-75b4-431b-adb2-eb6b9e546013/comments"
            "published":"2015-03-09T13:07:04+00:00",
            "visibility":"FRIENDS"
        },
        {
            "type":"post",
            "title":"DID YOU READ MY POST YET?",
            "id":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e/posts/999999983dda1e11db47671c4a3bbd9e",
            "source":"http://lastplaceigotthisfrom.com/authors/xxxxxx/posts/yyyyyy",
            "origin":"http://whereitcamefrom.com/authors/wwwwww/posts/zzzzzz",
            "description":"Whatever",
            "contentType":"text/plain",
            "content":"Are you even reading my posts Arjun?",
            "author":{
                "type":"author",
                "id":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
                "host":"http://127.0.0.1:5454/",
                "displayName":"Lara Croft",
                "url":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e",
                "github": "http://github.com/laracroft",
                "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
            },
            "comments":"http://127.0.0.1:5454/authors/9de17f29c12e8f97bcbbd34cc908f1baba40658e/posts/de305d54-75b4-431b-adb2-eb6b9e546013/comments"
            "published":"2015-03-09T13:07:04+00:00",
            "visibility":"FRIENDS"
        }
    ]
}
```

# Requirements

* Implement the webservice as described in the user stories
* Provide a webservice interface that is restful
* Provide a web UI interface that is usable
* Prove your project by connecting with at least 1 clone of your project. (Parts 3-5)
* Prove your project by connecting with at least 2 other groups. (Parts 4-5)
* Show that you are making a serious effort to connect with at least 4 other groups. (Parts 4-5)
* Prove your project by connecting with at least 3 other groups. (Part 5)
* Make a video demo of your blog (desktop-recorder is ok) 
    * Your video may **not** be a part of your presentation.
* Make a presentation about your blog 
* Follow the guidelines in the [project spec]({filename}/general/project.md) for URLs and services
* Allow users to accept or reject follow requests
* Images get the same protection that posts get as they are POSTS
* Follow the [API requirements](#api-requirements) in the following section
* Follow the [Infrastructure and Software Requirements](#infrastructure-and-software-requirements) in the following section

## API Requirements
   
When building your API, try to adhere to these rules for easy compatibility with other groups:
   
* REST API calls may be prefixed. ie. `http://service_address/api/authors/{AUTHOR_ID}/posts/`
* Document your service address, port, hostname, prefix(if used), and the username/password for HTTP Basic Auth in your README so that HTTP clients can connect to your API.
* You **must** be compatible with the API specification and examples listed above in this document. 
    * You **may** need to add some additional things for compatibility with other groups due to varying interpretations.
    * You **may** add additional endpoints and JSON keys as long as you provide the ones listed above.
    * If you follow something close to, but not compatible with the API specification in this document, then you will get something close to, but not exactly, a good grade.

## Test Requirements

The REST API must be fully tested.
    * Every API endpoint must be tested.
    * Every API functionality must be tested.
    * Every API method must be tested.
    * Every user story must be tested at the API level.
    * If a user story does not have an API, it must be tested by calling the Django code directly.
    * Tests that don't actually test what they say they're testing do not count.

These would be system/acceptance tests if the project didn't have a frontend.

Testing the user stories at the API level should give you the tests you need for every API endpoint, every API functionality, and every API method.
**Pretend you are writing tests to make sure a future Android client will work with your API.**

Not every user story has an API to test. For example, adding/removing nodes to connect with usually does not have an API. For these functions, please test them in whatever way is most convenient for your project, and then verify them using the API. You could write a test that adds a node to connect with by calling Python code or modifying the database directly, then use the API to check that the new node connection is working.

Frontend (Selenium, etc.) tests are not required. Code coverage (line coverage, statement coverage, branch coverage, MC/DC, etc.) is not required. Unit testing is not required.

## Documentation Requirements

* Every API endpoint is documented.
* Every API endpoint has multiple examples.
* Every JSON field in both request and response
    * Has a type 
    * Has an example value
    * Has an explanation of its purpose (when to use it)
    * For the request
    * For the response
* Explanation of anything interesting about each endpoint
    * Whether it is paginated, ...
        * How to use the pagination, ...

## Code Requirements

* Code is well organized and has good style
    * Readable
    * No smells such as "god files/classes/functions"
    * Each folder/file/class/function only does one thing
    * Comments add to the code
    * All names are meaningful
    * Meets style guide for relevant language
        * Python: PEP8
        * JS: https://github.com/rwaldron/idiomatic.js/ or https://github.com/standard/standard
        * HTML/CSS: https://google.github.io/styleguide/htmlcssguide.html
        * Browser/interpreter/transpiler/bundler should not have any warnings or errors
        * Passes W3 Validation
            * HTML: https://validator.w3.org/
            * CSS: https://jigsaw.w3.org/css-validator/
        * You may use the latest HTML/CSS/JS features if supported by Firefox. Check <https://caniuse.com/> or MDN
        * Not using any obsolete or deprecated HTML/CSS/JS
            * Check MDN, they have a little red trash icon
    * Good indentation
    * Well organized
    * It should be very easy for a TA or instructor to find the all the code responsible for a user story

## Tool Use Requirements

* All teammates are using Git and GitHub
    * Evidence of teammates using Git and GitHub to work together should be obvious
    * Working on code at the same time
    * Commit messages are helpful information for teammates and TA
    * Using Git and GitHub to communicate with each other
    * The repository (including branches and tags) is well-organized.
    * Commits/merges/PRs are small and there are a lot of them.
        * Small = less than 2 hours of code
        * PRs are not required

## Infrastructure and Software Requirements

<aside class="longWarning">
<p><strong>Failure to meet these requirements will result in a score of zero for project parts.</strong></p>
<p>We strongly recommend that you make your frontend using HTML, CSS, JS. You can use Jinja templates (it comes with Django) or <a href="https://developer.mozilla.org/en-US/docs/Web/API/Web_components">WebComponents</a>.</p>
<ul>
    <li>We will not be covering frontend frameworks such as React, Angular, Vue, Solid, Svelte... (there are dozens of these) in lecture or in lab, for a number of reasons:
        <ul>
            <li>We don't have time to cover this during the semester. It would require a second semester to cover these.<ul>
                <li>You will have to learn how to work with these frameworks yourself.</li>
            </ul></li>
            <li>React is losing popularity.<ul>
                <li>In ten years, knowing React will not be valuable anymore, because everyone will redo their websites in something else. This already happened with jQuery. 10 years ago all the 404 students wanted to learn jQuery, and now people barely use it.</li>
            </ul></li>
            <li>There is no standard frontend framework other than plain HTML/CSS/JS.</li>
            <li>The fact that large businesses like Facebook, Google, and Walmart use them does not mean they are good for a small semester project with a small team.</li>
            <li>All of the React-style (reactive paradigm) frameworks have major flaws that cannot be fixed, because the paradigm itself is flawed.</li>
            <li>All of the React-style (reactive paradigm) frameworks and most of the other frameworks are much more difficult to debug than plain JS or JS with a few libraries. This is because they make it difficult or impossible to determine why a component is being rerendered. They make it difficult or impossible to trace the code backwards from an error to the source of the problem.</li>
            <li>All of the component-based frameworks produce really bad HTML for the browser that is also difficult to debug or understand how it was produced.</li>
            <li>All frameworks using a shadow DOM are difficult to debug because the DOM updates are applied all at once, instead of step-by-step.</li>
            <li>All of the important contributions of React (components, shadow DOM, scoped CSS) have already been added to native HTML/CSS/JS, removing the need for React.<ul>
                <li>Once again, this already happened with jQuery. All the good parts of jQuery got added to native JS, and now people barely use it.</li>
            </ul></li>
            <li>A strong knowledge of HTML/CSS/JS allows you to quickly learn any framework, while knowing one framework does not teach you much about HTML/CSS/JS.</li>
            <li>It's very easy to make your own React-style frontend framework. There is nothing special about React. React's popularity comes from the fact that Facebook made it. Angular is popular because Google made it.</li>
            <li>Any particular frontend framework may not be able to meet the project requirements.</li>
        </ul></li>
    <li>TAs will not help you with frontend frameworks.</li>
    <li>Every semester there are at least a few students who choose to use a frontend framework and then, as a result:<ul>
        <li>End up having to redo large amounts of work when the framework turns out to not meet the requirements of the project</li> 
        <li>End up not being able to get parts of their application working due to the complexity and difficulty of debugging the framework code</li>
        <li>End up with a web app that is incredibly slow</li>
        <li>End up needing custom API endpoints which aren't specified above, so they have to do extra work</li>
        <li>End up fighting among themselves because only one teammember can understand the framework</li>
    </ul></li>
</ul>
<p>If you want to use React or a similar frontend framework such as Angular, Vue, Solid, Svelte... (there are dozens of these), despite these warnings, then all team members must fill out the frontend framework form. We offer this option only becuase some students want the experience for their resumé. However, it involves extra work. If <strong style="color: darkred;">all team members</strong> do not fill out the frontend framework form agreeing to use a front end framework despite the extra work required and the above warnings then you are not allowed to use a frontend frameworks, and using them will result in a mark of zero.</p>
<ul>
    <li>Backend frameworks are limited to Django and Flask only. We suggest Django. Flask requires extra work.</li>
    <li>Server-side rendering is limited to Jinja templates (provided by Django), or another templating engine that can run in Django/Flask.</li>
    <li>Combined frontend-backend frameworks, and server-side component rendering is not allowed unless you can get it working in Django on Heroku.<ul>
        <li>Server side rendering requiring a node server is not allowed.</li>
        <li>Anything requiring a node server is not allowed.</li>
        <li>Next.js, ... and similar frameworks are not allowed.</li>
    </ul></li>
</ul>
</aside>

* <input type="checkbox"> You must use a single git repository on GitHub Classroom that contains everything.
    * <input type="checkbox"> Must have a `development` branch.
    * <input type="checkbox"> Must have a `production` branch.
    * Must **not** contain built (compiled, transpiled, bundled) or downloaded artifacts, including but not limited to:
        * <input type="checkbox"> No downloaded Python packages, `virtualenv` `venv` etc.
        * <input type="checkbox"> No built Python artifacts: `.pyc` files, `__pycache__` directories, etc.
        * <input type="checkbox"> No downloaded JS packages: `node_modules` etc.
        * <input type="checkbox"> No HTML/CSS/JS output produced by compiler/transpiler/bundler
        * <input type="checkbox"> No esbuild, vite, rollup, webpack, etc. output.
        * Failure to meet the above restrictions may result in a mark of zero.
    * Note: If you want to keep a copy at the end of the semester, do not use GitHub fork: clone it to your computer, and push it to a new GitHub repository (manual fork).
    * Force-push, rebase, and other git operations that remove history from GitHub are strictly forbidden, and you may receive a zero for project parts or be removed from your team.
- <input type="checkbox"> Your project must be compatible with Firefox browser.
    * Firefox will be used as the standard for marking. We will not check your code in multiple browsers to try to get it working.
- <input type="checkbox"> Your project must be hosted on an approved hosting solution.
    * Heroku
        * An entire node of your project must only require: 
            * <input type="checkbox"> A single web "dyno"
            * <input type="checkbox"> with a single PostgreSQL add-on
        * <input type="checkbox"> Every teammate must be able to deploy their own project node to their own Heroku.
    * Individual hosting on approval: you must get approval in advance from the instructor. 
        * You are responsible for any problems that come up as a result.
        * You are responsible for any surprise fees that come up as a result.
        * Often when people use some other hosting service that isn't Heroku they get shut off, blocked by firewalls, and/or hit with surprise fees.
        * This only applies on an individual basis: teammates must still use Heroku.
            * Project code must still be deployable by teammates to Heroku.
        * Database provider must be the same provider as your website hosting.
- <input type="checkbox"> Every teammate must be able to deploy their own node using the same code.
    * This means 6 nodes using the same project code but running as different (Heroku) servers.
- <input type="checkbox"> Use a single Django or Flask server per node.
    * A single Django or Flask server must serve *everything*:
        * Frontend (for browser) dynamic 
        * Frontend (for browser) static content
            * <input type="checkbox"> Use [whitenoise](https://whitenoise.readthedocs.io/en/latest/) for static content.
        * Backend API
            * Use routes to distinguish.
        * Use Python 3.11+
    * Splitting frontend/backend hosting is strictly not allowed. Splitting static/dynamic is strictly not allowed.
        * They must be a part of the same Heroku + (Django or Flask) server.
        * Violation of this restriction will result in a mark of zero.
- <input type="checkbox"> Deployed nodes (Heroku): Must use a PostgreSQL database for all content storage.
- <input type="checkbox"> Local development nodes (your laptop): PostgreSQL or SQLite for all content storage.
    * SQLite is recommended.
- <input type="checkbox"> Everything that's not in a database files must be code managed by GitHub.
    * Code checked into git must be clean. 
    * Cloud (e.g. Firebase), NoSQL, key-value, and file system storage are strictly forbidden.
* License your code properly (use an OSI approved license)
    * Put your name (or some representation of you like GeneralHuxFan768) on it!

# Take-aways

* 1 Working Website
* 1 GitHub git repo
* 1 Presentation
    * May not include the video
* 1 OpenAPI ('Swagger') specification for your API 
* 1 Video

## Things that are allowed

* You may use React if you choose, but generally this is more difficult and takes more work so it is not recommended.
    * Django templates or lighter-weight frameworks like Vue are generally easier and take less work.
    * If you use React, you must still serve everything (including React js and html) through the same Django/Flask server that is serving the API backend.

# Groupwork Tips

* These optional. They are just advice. They usually lead to less conflict and a better end result.

The most successful teams:

* Do not use pull requests.
    * Pull requests are great in general, but they tend to cause problems because the project is very small and groups are also small.
* Use very very few branches (e.g. production and staging).
    * Do not use author branches (or branches where a single author is the only one touching them).
* Commit, pull, push the code they're working on, to the same branch that everyone else is working on, at least once an hour.
    * Commit code that doesn't break the overall project.
    * Avoid your version being broken for more than an hour.
    * Do not stay up all night, change everything, and push a hundred changes all over the code base as one giant pull request.
* Divide teamwork by user story, instead of frontend vs backend.

# Submission Instructions

* Submission will be by GitHub Classroom. Please follow the link on eClass.

# Warning!!!!
   
   This spec is subject to change!

# Marking

* Usually all teammates will share the same mark.
* An individual student's marks will be reduced if the instructor (or a TA in consultation with the instructor) finds that:
    * The student is not contributing or contributing significantly less than their teammates.
    * The individual student is significantly preventing their teammates from participating or contributing.
    * The individual student's is significantly misusing git/GitHub/Heroku/other software tools.
    * The indivudual student is engaging in significant "intellectual violence."
        * Intellectual violence is when one teammate uses their skill, knowledge, or experience, to intimidate or control the other teammate(s) rather than sharing and helping them learn.
    * The individual student is not communicating or only communicating very rarely with their team.
    * The individual student does not complete the peer feedback form (-1 mark for each part 1-4).
* Any concerns about teamwork must be brought to the instructor's (not the TA) attention *by email* well before the last lab.
    * It takes time to investigate these things. 

## Overall Marking

* Excellent 8 (A+): Clean code. Meets the requirements and ads extra polish. Everything is tested properly. Passes all tests. The API is documented in detail. The API is implemented as specified, and adds extra for compatibility. The UI meets all requirements, and has extra polish.
* Good 7 (B+): Code is mostly clean but has some rough spots. At most a couple of minor bugs. Almost all the requirements are met. Everything is tested. Passes almost all tests. Almost everything is documented. Almost all the API is implemented according to spec.
* Satisfactory 6 (C+): Code is low quality but working. Some bugs. Inconsistency. ¾ of the requirements are met. Almost everything is tested. Passes most tests. Most things are documented. API is implemented but doesn't meet spec.
* Unsatisfactory 4-5 (D-D+): There are significant bugs and issues. ½ of the requirements are met. ½ the tests exist and pass. At least ½ of the documentation is present. At least ½ of the API exists and works. At least ½ of the UI exists and works. At least ½ of the API exists and works.
* Partial Attempt 1-4 (F): Poor quality. Large pieces of code missing, some pieces exist. Some requirements are met. Some of the UI exists. Some of the API exists.
* Failure 0 (F): Missing. Not attempted. Not complete enough to make an evaluation. Violated a restriction. 

UI amount complete is marked by your TA testing user stories manually.

# Project Parts

## <a id="part0" href="#part0">Project Part 0</a>: Group Formation

You must form a group with only students from your same lab section. You can have different lecture sections, but your lab section must be the same. Furthermore, everyone must attend their registered lab section.

* There can be maximum 6 students per team.
* All team members must be registered for and attending the same lab section.
* Your team name must be from the list of [CSS colour names](https://developer.mozilla.org/en-US/docs/Web/CSS/named-color).
* Use the [GitHub Classroom Link on eClass](https://eclass.srv.ualberta.ca/course/view.php?update=8120398)
    * EVERY teammate should submit a link to your teams GitHub repo on eClass.
* Add a license and a README. The README should contain the names of the teammates.
* Use the format https://github.com/uofa-cmput404/f24-project-team-name

Do not submit a clone link or a link to a branch or file.

* 1 mark
* Submitted on eClass by all members
* 1 Github repo with a README and LICENSE
* Team name is a CSS color name

## <a id="part1" href="#part1">Project Part 1</a>: Halfway Prototype

### Requirements

For this part you need:
* ½ of the user stories except those marked for later parts, like "*Part 3-5 only*"
    * They work in the UI.
    * They work in the local API (imagine you are building an API for a future Android client)
    * It's obvious how to perform the user stories in the UI.
    * They are tested. See the [test requirements](#test-requirements).
    * You can walk the TA through how do the user stories in the UI, in the API, and walk the TA through the relevant code, tests, and documentation.
* Everything implemented is also documented. See the [documentation requirements](#documentation-requirements).
    * There are examples in the API documentation for the ½ of the user stories chosen above.
* Code follows the [code requirements](#code-requirements).
* The UI is good-looking, easy to read, easy to navigate.
* Teammates are using Git and GitHub according to the [tool use requirements](#tool-use-requirements)

### Submission

Due 4PM on Monday.

Create a git tag "part1" in your production branch before 4PM and submit only the link to your tag.

* A tag is just a name for a commit, so do not create the tag until you have your final commit for part 1!

Don't forget to push the tag to GitHub.

Submit only the link to the tag in the following format:

https://github.com/uofa-cmput404/f24-project-example-team/tree/part1

* Every team member must submit the link to eclass.

### Marking

* User Stories: UI
    * Excellent 8 (A): At least ½ of the user stories are usable using the UI.
    * Good 7 (B): Almost ½ of the user stories are usable using the UI.
    * Satisfactory 6 (C): At least 3/8ths of the user stories are usable using the UI.
    * Unsatisfactory 4-5 (D): At least ¼ of the user stories are usable using the UI.
* User Stories: API
    * Excellent 8 (A): At least ½ of the user stories with a relevant API are usable using the API. Adheres to the specification.
    * Good 7 (B): Almost ½ of the user stories with a relevant API are usable using the API. Adheres to the specification
    * Satisfactory 6 (C): At least 3/8ths of the user with a relevant API stories are usable using the API. Very close to adhering to the specification
    * Unsatisfactory 4-5 (D): At least ¼ of the user with a relevant API stories are usable using the API. Some parts deviate from the specification.
    * Attempt 0-3 (F): Missing API or major deviations from the specification.
* Test Cases
    * *User stories that have an API must be tested through the API. Other user stories can be tested by directly calling Django code.*
    * *Tests do not count unless they are accurately testing the functionality.*
    * Excellent 8 (A): At least ½ of the user stories have tests written and pass those tests. 
    * Good 7 (B): At least ½ of the user have tests written, most pass tests.
    * Satisfactory 6 (C): At least 3/8ths of the user have tests written, most pass tests.
    * Unsatisfactory 4-5 (D): At least ¼ of the user have tests written, most pass tests.
* UI Design (HTML & CSS)
    * Excellent 8 (A): Looks impressive! It's obvious how to do any of the ½ of the user stories.
    * Good 7 (B): Looks good. It's not obvious how you would use the UI to do some of ½ of the user stories.
    * Satisfactory 6 (C): HTML & CSS exists, it does not look good. Mostly easy to understand. It has issues. There is some way to do ½ of the user stories, even if it's not obvious.
    * Unsatisfactory 4-5 (D): HTML & CSS exists. Major UI issues. Hard to navigate. Hard to understand. There is some way to do almost all the ½ of the user stories.
    * Attempt 1-3 (F): Some pieces of the HTML & CSS exist, but some pieces of the HTML & CSS are missing that would be needed to do ½ of the user stories.
    * No attempt 0 (F): Very little HTML & CSS.
* Tool Use
    * *PRs are not required.*
    * Excellent 8 (A): Use of Git, GitHub issues, etc. is Evidence and Obvious. Commits/merges/PRs are small and frequent. Commit messages are helpful information for teammates. All the teammates are working at the same time, and using GitHub **and git** to help communicate and improve teamwork. You laugh in the face of merge conflicts! Well organized repository and branches.
    * Good 7 (B): Frequent but inconsistent use of Git, etc. Commits/merges/PRs are medium and with inconsistent frequency. All the teammates are working at the same time. Using GitHub to help communicate. Well organized repository and branches.
    * Satisfactory 6 (C): Uses Git, etc. Has some oversized merges. Commits/merges/PRs are large and far apart. All the teammates are working at the same time. Well organized repository and branches.
    * Unsatisfactory 4-5 (D): Limited of tool use. Only one teammate seems to be working at a time. Git exists but it has built artifacts in it. Git is disorganized.
    * Failure: Used file sharing, email attachments, sending files/code through discord, chat, messengers, or similar tools to work together. Git exists but it not being used, or it is being misused.
    * *Failure to commit and tag on time, failure to submit a link to the tag, etc. will result in an overall mark of zero for this project part: not just a zero for Tool Use.*
    * *Force push, rebase, or other operations that destroy git history, along with forging git history, authorship, messages, dates, etc. will also result in an overall mark of zero for this project part, and you will be reported to the Faculty under the Student Academic Integrity Policy.*
* TA Walkthrough
    * Excellent 8 (A): Able to walk through ½ user stories with UI and API. No snags, bugs, last second workarounds, or missing pieces. Code is easily located. Documentation is easily located.
    * Good 7 (B): A couple of snags, bugs, last second workarounds.
    * Satisfactory 6 (C): Some snags bugs, last second workarounds, or tiny missing pieces.
    * Unsatisfactory 4-5 (D): Many snags, bugs, last second workarounds, small missing pieces.
    * Attempt 0-3 (F): No walkthrough. Unable to demo. Showstopper bugs. Major missing pieces.
* Web Service API Documentation
    * Excellent 8 (A): Well documented. Highly detailed. Clear descriptions, has useful example requests and responses from your API for every use of the API and ½ of user stories. 
    * Good 7 (B): Well documented, medium detail. A few things are unclear. Has example requests and responses from your API for every use of the API and ½ of user stories. 
    * Satisfactory 6 (C): Well documented, but missing details. Every endpoint is documented.  Some things are unclear. Example requests and responses have a few issues. Slightly less than ½ of user stories have examples.
    * Unsatisfactory 4-5 (D): Low on details. Many things are unclear. Every endpoint is documented. Missing some example requests and responses.
    * Attempt 0-3 (F): Major pieces of documentation are missing. 
* Standards & Code Style
    * Excellent 8 (A): Adheres to standards, code is well organized and clean. Code is easy to read. Comments add to code readablility when necessary. Code meets Python, JS, HTML and CS style guides. Excellent indentation, naming. Code units only do one thing. It's easy to find the code responsible for handling any of the ½ user stories.
    * Good 7 (B): Adheres to standards, code is well organized and clean. Missing comments. Some minor issues with code style. Code units only do one thing. It takes a little digging sometimes to find the code responsible for a user story.
    * Satisfactory 6 (C): Adheres to standards, there is an attempt at organization. Commented out code, unreachable code, or code with no clear purpose. Code units only do one thing. Occasional spots of poor style. It's not clear where the code for a user story will be.
    * Unsatisfactory: 4-5 (D): Browser, Python, transpiler, bundler, etc. warnings. Code is poorly organized God files/classes/functions. Have to search or grep code to find the code responsible for something.
    * Attempt 0-3 (F): HTML errors, browser errors, CSS errors, JS errors, Python errors. Code is disorganized. Code is hard to find. Code is missing.

## Project Part 2: Centralized Prototype

### Submission

Due 4PM on Monday.

Create a git tag "part2" in your production branch before 4PM and submit only the link to your tag.

* A tag is just a name for a commit, so do not create the tag until you have your final commit for part 1!

Don't forget to push the tag to GitHub.

Submit only the link to the tag in the following format:

https://github.com/uofa-cmput404/f24-project-example-team/tree/part1

* Every team member must submit the link to eclass.

### Marking

* 7 Marks
* Total Project
    * Excellent 7: Excellent effort. Relatively consistent. All the 6: Good quality. Some inconsistency. 90% of
    the project implemented
    * Satisfactory 5: Codebase in places. Passes some tests. Some parts run
    * Unsatisfactory 3: Effort exists, it's missing lots of components but something is there.
    * Failure 0: Missing. No attempted. Not complete enough to evaluate.
* Code Base 
    * Excellent : Excellent effort. Relatively consistent. At least ½
    of the project implemented. Clean code
    * Good : Good quality. Some inconsistency. About ½ of
    the project implemented
    * Satisfactory : Codebase in places. Passes some tests. Some
    parts run
    * Unsatisfactory : Does not meet Satisfactory level
* Test Cases 
    * Excellent: System is well tested
    * Good: System has some blind spots for testing
    * Satisfactory: Effort was placed on testing but it is inconsistent.
    * Unsatisfactory: test cases are inappropriate but exist.
    * Failure: Missing test cases
* UI 2
    * Excellent: UI Exists and is coherent. Shows evidence of
    planning.
    * Good: UI Exists. Some issues
    * Satisfactory: UI Exists, it's not good. It has issues.
    * Unsatisfactory: A UI was attempted, a UI exists.
    * Failure: No UI, or what was attempted is not substantial.
* Tool Use
    * Excellent: Use of at least Git is Evidence and Obvious
    * Good: Frequent but inconsistent use of Git, etc.
    * Satisfactory: Uses Git, etc.
    * Unsatisfactory: Limited of tool use
    * Failure: Used filesharing and email attachments instead of git
* TA Walkthrough
    * Excellent: Coherent demo, shows off features. Limited snags.
    * Good: Coherent demo, shows off features. Some snags.
    * Satisfactory: Lots of snags. Can demo it.
    * Unsatisfactory: Unfinished, hard to demo.
    * Failure: no demo or unable to demo.
* Web Service API & Documentation
    * Excellent: Documented, adheres to the specification & examples listed above where it exists. Open API specification exists, has clear descriptions,
    and has example requests and responses from your API. 
    * Good: Documented, exists, tries to adhere to requirements. Open API specification exists,
    and has some descriptions and a few example requests and responses.
    * Satisfactory: Some of the webservice exists. Open API specification exists, but no descriptions
    or example requests and responses.
    * Unsatisfactory: Well you tried right? Open API specification does not exist.
    * Failure: Ok you didn't try. 
* Design
    * Excellent: Adheres to standards, well-designed
    * Good: Adheres to standards somewhat, some awkward parts
    * Satisfactory: Some good parts, some nasty parts
    * Unsatisfactory: Little effort went into documenting and
    designing the project
    * Failure: failure to learn from the class and apply concepts even remedially.

## Project Part 3: Distribution

### Requirements

* Everyone on the team must be able to deploy their own *node* (using the same project code) to their own Heroku app with their own Heroku Postgres database.
    * 1 codebase, 1 repo deployed to 6 nodes each on 6 different Heroku servers using 6 different databases, 6 different web servers, at 6 different addresses for 6 different team members.
* All nodes must be able coordinating. All user stories involving multiple authors must work in both situations:
    * All authors on the same node
    * Authors on different nodes
* For example if the user story is "As an author, I want to be able to approve or deny other authors following me, so that I don't get followed by people I don't like."
    * This needs to work when the author following is on a different node from the author they are following.
    * It also needs to work if they're on the same node.

### Submission

Due 4PM Monday.

eClass has a limitation where it only shows the due date for the last lab section of the week, but for Monday labs it is due Monday. For Wednesday labs it is due Wednesday.

Create a git tag "part2" before 4PM and submit only the link to your tag.

Don't forget to push the tag to GitHub.

Submit only the link to the tag in the following format:

https://github.com/uofa-cmput404/w24-project-example-team/tree/part2

### Marking

* 7 Marks
* Total Project
    * Excellent 7: Excellent effort. Relatively consistent. All of the project implemented. Clean code. Nodes coordinates and connect fine. API follows spec & examples listed in this document.
    * Good 6: Good quality. Some inconsistency. All of the project implemented except several user stories. Node-to-node connection is fixable and functional.
    * Satisfactory 5: Codebase in places. Passes some tests. Most parts run. Some things coordinate and connect between nodes.
    * Unsatisfactory 3: Effort exists, it's missing lots of components but at least ½ is there.
    * Failure 0: Missing. No attempted. Not complete enough to evaluate.
* Web Service Coordination
    * Excellent: Web service coordinates with another node successfully. Most interoperation requirements met.
    * Good: Web service coordinates with another node successfully. Most interoperation requirements met. Some snags.
    * Satisfactory: The basics of coordination with another node are covered. Probably many snags.
    * Unsatisfactory 0: Coordination with another node barely works.
    * Failure: Failure to coordinate and connect with another node.
* Code Base 
    * Excellent : Excellent effort. Relatively consistent. All of the project implemented. Clean code.
    * Good : Good quality. Some inconsistency. All of the project implemented except several user stories.
    * Satisfactory : At least half of codebase in place. Passes some tests. Some parts run.
    * Unsatisfactory : Does not meet Satisfactory level.
* Test Cases 
    * Excellent: System is well tested.
    * Good: System has some blind spots for testing.
    * Satisfactory: Effort was placed on testing but it is inconsistent.
    * Unsatisfactory: test cases are inappropriate but exist.
    * Failure: Missing test cases.
* UI
    * Excellent: UI Exists and is coherent. Shows evidence of planning.
    * Good: UI Exists. Some issues.
    * Satisfactory: UI Exists, it's not good. It has issues.
    * Unsatisfactory: A UI was attempted, a UI exists.
    * Failure: No UI, or what was attempted is not substantial.
* Tool Use
    * Excellent: Use of at least Git is Evidence and Obvious
    * Good: Frequent but inconsistent use of Git, etc.
    * Satisfactory: Uses Git, etc.
    * Unsatisfactory: Limited of tool use
    * Failure: Used filesharing and email attachments instead of git
* TA Walkthrough
    * Excellent: Coherent demo, shows off features. Limited snags.
    * Good: Coherent demo, shows off features. Some snags.
    * Satisfactory: Lots of snags. Can demo it.
    * Unsatifactory: Unfinished, hard to demo.
    * Failure: no demo or unable to demo.
* Web Service API & Documentation
    * Excellent: Documented, adheres to the specification & examples listed above.  Open API specification exists, has clear descriptions, and has example requests and responses from your API. 
    * Good: Documented, exists, tries to adhere to requirements. Open API specification exists, and has some descriptions and a few example requests and responses.
    * Satisfactory: Some of the webservice exists. Open API specification exists, but no descriptions or example requests and responses.
    * Unsatisfactory: Well you tried right? Open API specification does not exist.
    * Failure: Ok you didn't try. 
* Design
    * Excellent: Adheres to standards, well designed.
    * Good: Adheres to standards somewhat, some awkward parts.
    * Satisfactory: Some good parts, some nasty parts.
    * Unsatisfactory: Little effort went into documenting and designing the project.
    * Failure: Failure to learn from the class and apply concepts even remedially.

## Project Part 3: Federation

### Submission

Due 4PM Monday.

eClass has a limitation where it only shows the due date for the last lab section of the week, but for Monday labs it is due Monday. For Wednesday labs it is due Wednesday.

Create a git tag "part3" before 4PM and submit only the link to your tag.

Don't forget to push the tag to GitHub.

Submit only the link to the tag in the following format:

https://github.com/uofa-cmput404/w24-project-example-team/tree/part3

### Marking

* 5 Marks
* Total Project
    * Excellent 5: Excellent effort. Team is working with 4 other teams to coordinate and connect. Coordinates and connects fine with 2 or more teams and another node from a team member. API follows spec & examples listed in this document.
    * Good 4: Some issues, not quite excellent but definitely fixable and functional with 1 or more teams and another node from a team member. API follows spec & examples listed in this document.
    * Satisfactory 3: There are issues, it does run, it does coordinate with 1 or more teams.
    * Unsatisfactory 2: Not connected to other groups, still connects to another node of a team member.
    * Failure 0: Missing. No attempted. Not complete enough to evaluate.
* Web Service API & Documentation
    * Excellent: Documented, adheres to requirements to augments them with compatibility. Open API specification exists, has clear descriptions, and has example requests and responses from your API.
    * Good: Documented, exists, tries to adhere to requirements. Open API specification exists, and has some descriptions and a few example requests and responses.
    * Satisfactory: Some of the webservice exists. Open API specification exists, but no descriptions or example requests and responses.
    * Unsatisfactory: Webservice exists, barely. Open API specification does not exist.
    * Failure: it is not usable.
* Web Service Coordination
    * Excellent: Web service coordinates with 2+ other group projects and itself successfully. Most interoperation requirements met.
    * Good: Web service coordinates with 1+ other group projects and itself successfully. Most interoperation requirements met. Some snags.
    * Satisfactory: The basics of coordination are covered. Probably many snags.
    * Unsatisfactory 0: Coordination barely works.
    * Failure: failure to coordinate
* Design
    * Excellent: Adheres to standards, well designed.
    * Good: Adheres to standards somewhat, some awkward parts.
    * Satisfactory: Some good parts, some nasty parts.
    * Unsatisfactory: Little effort went into documenting and designing the project.
    * Failure: failure to apply what was learned in class.

## Project Part 4: Polish

### Submission

Due 4PM Monday.

eClass has a limitation where it only shows the due date for the last lab section of the week, but for Monday labs it is due Monday. For Wednesday labs it is due Wednesday.

Create a git tag "part4" before 4PM and submit only the link to your tag.

Don't forget to push the tag to GitHub.

Submit only the link to the tag in the following format:

https://github.com/uofa-cmput404/w24-project-example-team/tree/part4

### Presentation

Your presentation will be 5 minutes max. Then you will have a minute or two for questions.

Your presentation should focus on:

* Important functions
    * You won't have time for every function in 5 minutes, so make sure to cover the most important functions.
* Your UI
    * This is what makes your project different from the other teams, so be sure to show it off!
    * We don't really need to see the Django admin panel.
* Federation
    * Walkthroughnstrate your working connection with other team(s).

Guide for a good presentation:

* Ideally, everyone in your team should take turns speaking.
    * However, I do understand that some people have public speaking anxiety, so you won't be penalized if someone doesn't speak.
* Ideally, your presentation will use your live web app.
    * The most successful teams in the past use note cards.
    * Prepare backup slides in case something goes wrong that prevents you from doing a live demo.
* The best presentations tell a story, walking through a typical user scenario.
    * An example of such a scenario is the one in the "Scenario" section above. But don't use that one, come up with your own that shows
    off your app.
* Rehearse your presentation in person as a team to make sure it is close to 5 minutes.
* Make sure your team has a laptop that works with the projector *before* the presentation day.

During the other team's presentations:

* Rudeness to the other teams will not be tolerated.
* Your team must arrive on time. Late teams will not be allowed to present.
* You and your team must stay for all presentations and show respect, support, and appreciation for the other teams hard work.
* You may ask thoughtful questions after each presentation.
* Wait until after questions to applaud. Otherwise, everyone ends up awkwardly applauding each team twice.

### Marking

* 10 Marks
* Total Project
    * Excellent 10: Excellent effort. Coordinates and connects fine. Good demo. Clear application of what was learned in class. 3 or more groups connected. Posts with embedded images are visible. Image posts are visible. API follows spec & examples listed in this document.
    * Good 8: Some issues, not quite excellent but definitely operational and functional. 2 or more groups connected. Posts with embedded images are visible. Image posts are visible. API follows spec & examples listed in this document.
    * Satisfactory 6: There are issues, it does run, it does coordinate. Meets satisfactory aspects of rubric. 2 or more group connected. Image posts are visible. API follows spec & examples listed in this document.
    * Unsatisfactory 4: Well you tried, but it's hardly working. Meets unsatisfactory aspects of rubric. 1 or more group connected.
    * Failure 0: Missing. No attempted. Not complete enough to evaluate. Often hits failure aspects of rubric.
* Note: these are ordered by importance, but you need to meet all these parts and we care about the final quality.
* Code Base
    * Excellent: Excellent effort. Relatively consistent. At least 90% of requirements implemented. Clean code
    * Good: Good quality. Some inconsistency. About 90% of requirements implemented.
    * Satisfactory: Codebase in places. Passes some tests. Some parts run.
    * Unsatisfactory: Does not meet Satisfactory level
* UI 3
    * Excellent: UI Exists and works well. Shows evidence of planning. Looks great.
    * Good: UI Exists.  Looks good
    * Satisfactory: UI exists. Looks poor.
    * Unsatisfactory: UI exists. Doesn't work well. Worse than poor.
    * Failure: Missing or unusable.
* Web Service Coordination
    * Excellent: Web service coordinates with 2+ other group projects successfully. Most interoperation requirements met.
    * Good: Web service coordinates with 2+ other group projects successfully. Most interoperation requirements met. Some snags.
    * Satisfactory: The basics of coordination are covered. Probably many snags.
    * Unsatisfactory: Coordination doesn't work or barely works.
* Web Service API & Documentation
    * Excellent: Documented, adheres to requirements to augments them with compatibility.  Open API specification exists, has clear descriptions, and has example requests and responses from your API. 
    * Good: Documented, exists, tries to adhere to requirements.  Open API specification exists, and has some descriptions and a few example requests and responses.
    * Satisfactory: Some of the webservice exists. Open API specification exists, and has a few example requests and responses.
    * Unsatisfactory: Effort taken but incomplete. Open API specification exists, but no descriptions or example requests and responses.
    * Failure: API or Documentation Missing. Open API specification does not exist.
* Test Cases
    * Excellent: System is well tested
    * Good: System has some tests
    * Unsatisfactory: test cases are inappropriate
    * Failure: Missing test cases
* Tool Use
    * Excellent: Use of at least Git is Evidence and Obvious
    * Good: Frequent but inconsistent use of Git, etc.
    * Satisfactory: Infrequent use of Git, etc.
    * Unsatisfactory: Limited tool use
    * Failure: lack of tool use
* Design
    * Excellent: Adheres to standards, well designed
    * Good: Adheres to standards somewhat, some awkward parts
    * Satisfactory: Some good parts, some nasty parts
    * Unsatisfactory: Little effort went into documenting and designing the project
    * Failure: clear lack of design
* Adhering to Standards
    * Excellent: Excellent attempt at making a standards compliant website. Most things are compliant.
    * Good: An attempt at making a standards compliant website. Some not compliant.
    * Satisfactory: Inconsistent.
    * Unsatisfactory: poor attempt to meet standards.
    * Failure: failed to apply what was learned in class
* Addressing Feedback:
    * Excellent: TAs suggestions were implemented, TA approves of implementation set.
    * Good: The good TA suggestions were implemented ;)
    * Satisfactory: Feedback ignored mostly, but some followed.
    * Unsatisfactory: Majority of Feedback ignored.
    * Failure: Feedback ignored.
* Presentation:
    * Excellent: Presentation within time, shows teamwork, promotes the application, uses the live application to show functionality.
    * Good: Presentation nearly within time, some team works, reasonable presentation.
    * Satisfactory: Presentation exists but has problems.
    * Unsatisfactory: Missing or terrible presentation (lack of practice, lack of preparation, irrelevant) OR presentation includes the video demo.
    * Failure: no presentation
* Video Walkthrough:
    * Excellent: Video is well presented and not boring, less than 2 minutes. Posted to the discussion forum thread to share it with everyone in the class.
    * Good: Video presents the functionality and is less than 2 minutes.
    * Satisfactory: Video is longer than 2 minutes, or doesn't accurately present the project.
    * Unsatisfactory: A video exists and it is a demo.
    * Failure: lack of video, failure to make a video.
* AJAX
    * Excellent: Uses AJAX appropriately and well (documented)
    * Good: Uses some AJAX (documented)
    * Satisfactory: AJAX not really used
    * Unsatisfactory: An attempt was made.
    * Failure: No AJAX

# License

     * Parts of this document are derived from the W3C Documentation for Activity Pub
     * Copyright © 2018 W3C® (MIT, ERCIM, Keio, Beihang). W3C liability, trademark and permissive document license rules apply. 
     * https://www.w3.org/Consortium/Legal/2015/copyright-software-and-document
```.plain
     License
     
     By obtaining and/or copying this work, you (the licensee) agree that you have read, understood, and will comply with the following terms and conditions.
     
     Permission to copy, modify, and distribute this work, with or without modification, for any purpose and without fee or royalty is hereby granted, provided that you include the following on ALL copies of the work or portions thereof, including modifications:
     
         The full text of this NOTICE in a location viewable to users of the redistributed or derivative work.
         Any pre-existing intellectual property disclaimers, notices, or terms and conditions. If none exist, the W3C Software and Document Short Notice should be included.
         Notice of any changes or modifications, through a copyright statement on the new code or document such as "This software or document includes material copied from or derived from [title and URI of the W3C document]. Copyright © [YEAR] W3C® (MIT, ERCIM, Keio, Beihang)." 
     
     Disclaimers
     
     THIS WORK IS PROVIDED "AS IS," AND COPYRIGHT HOLDERS MAKE NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF THE SOFTWARE OR DOCUMENT WILL NOT INFRINGE ANY THIRD PARTY PATENTS, COPYRIGHTS, TRADEMARKS OR OTHER RIGHTS.
     
     COPYRIGHT HOLDERS WILL NOT BE LIABLE FOR ANY DIRECT, INDIRECT, SPECIAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF ANY USE OF THE SOFTWARE OR DOCUMENT.
     
     The name and trademarks of copyright holders may NOT be used in advertising or publicity pertaining to the work without specific, written prior permission. Title to copyright in this work will at all times remain with copyright holders.
```
