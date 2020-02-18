# Redditor Recommendations

Most social media sites recommend users that a given person may want to friend or follow. For examples, on Facebook, Instagram, Twitter, and LinkedIn, the following are typically displayed somewhere on the frontpage:

![friend-recommendations](images/friend-recommendations.png)

On Reddit, however, one finds only recommendations for specific subreddits (i.e. communities organized by topic discussion) rather than for individual users, such as the following:

![subreddit-recommendations](images/subreddit-recommendations.png)

Reddit has two features that allows users to more easily find posts by specific users. The first is the "friend" feature, which allows users to have posts by all of those they have marked as friends collected in a single subreddit, r/friends. The second is the "follow" feature, which publishes posts by people that the user follows directly to the front page. Both features are sparingly used. The follow button is currently located on the profile pages of users, as in the following:


![redditor-profile](images/redditor-profile.png)


There is an argument to be made that keeping the focus of Reddit on discussions, rather than individual posters, is what would be best for keeping the original spirit of the website. However, given that shifting the focus to individuals would attract celebrities, influencers, and advertisers, it is understable that Reddit would face strong financial pressure to promote its "follow" feature. Indeed, Reddit announced in the summer of 2019 that it will soon enact greater transparency protocols (in particular, allowing redditors to view who follows them), signaling a possible new direction for the site.

In addition to bolstering transparency and privacy, implementing a system for recommendation specific redditors will likely also be eventually be part of Reddit's plan for growing its follow feature. The app in this Github repo, Redditor Recommendations (RR), demonstrates one way that this can be done for the 10% of the site's 300 million users who comment and post, who may be the most likely to adopt and promote new features like the follow button. RR does this by combing through years of comment history to determine the top subreddits of each user (as ranked by the cumulative score, or karma, gained by the user on those subs), and then recommends the top contributors to those subs. For example, in the following image

![graph](images/graph.png)

the two subreddits from which the user has reaped the most karma are the Batman and Patriots themed subeddits. The redditors in the second column of the image are those with the highest scores on those two subreddits, and are thus the redditors that RR recommends to the original user as accounts to follow. In addition to the redditor recommendation, RR also provides the top subreddits that those redditors receive karma from. Listing these subreddits is done primarily to provide a better picture of who the new person is that the user may start following, but it is also beneficial to have this list serve as subreddit recommendation system in tself. 

The app, when turned on by the creator, is located at swiftaugur.club, and currently looks as follows:



