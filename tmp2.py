from TwitterWebsiteSearch import TwitterClient
from TwitterWebsiteSearch import SearchQuery

TwitterClient.FIDDLER_DEBUG = True
tc = TwitterClient()
sq = SearchQuery('a', max_position='TWEET-794346675695403010-797411613296889856-BD1UO2FFu9QAAAAAAAAETAAAAAcAAAASAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

# res = tc.search_query(sq)
# res2 = tc.search_query(res['next_query'])
# print(res)

x = '''
      <li class="js-stream-item stream-item stream-item
" data-item-id="794346664383381504" id="stream-item-tweet-794346664383381504" data-item-type="tweet">
    


  

  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable
       original-tweet js-original-tweet
      
       has-cards  has-content
"
      
data-tweet-id="794346664383381504"
data-item-id="794346664383381504"
data-permalink-path="/Vahllen/status/794346664383381504"








  data-screen-name="Vahllen" data-name="\/ahllen" data-user-id="1116328064"
  data-you-follow="false"
  data-follows-you="false"
  data-you-block="false"









data-disclosure-type=""




 data-has-cards="true"







 data-component-context="tweet"


    >


    <div class="context">
      
      
    </div>

    <div class="content">
      

      
      <div class="stream-item-header">
          <a  class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/Vahllen" data-user-id="1116328064">
    <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/794863830438473730/BW0iPhEK_bigger.jpg" alt="">
    <strong class="fullname js-action-profile-name show-popup-with-id" data-aria-label-part>\/ahllen</strong>
    <span>&rlm;</span><span class="username js-action-profile-name" data-aria-label-part><s>@</s><b>Vahllen</b></span>
    
  </a>

        <small class="time">
  <a href="/Vahllen/status/794346664383381504" class="tweet-timestamp js-permalink js-nav js-tooltip" title="6:12 pm - 3 Nov 2016" ><span class="_timestamp js-short-timestamp " data-aria-label-part="last" data-time="1478221977" data-time-ms="1478221977000" data-long-form="true">Nov 3</span></a>
</small>

          
          
      </div>


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0">eureka seven&#39;s the best mecha because one episode there&#39;s <strong>a</strong> fight in <strong>a</strong> denny’s parking lot but they couldn’t call it <strong>a</strong> denny’s so it&#39;s named <a href="https://t.co/rr1Bt1Sj26" class="twitter-timeline-link u-hidden" data-pre-embedded="true" dir="ltr" >pic.twitter.com/rr1Bt1Sj26</a></p>
</div>




      
            <div class="AdaptiveMedia
      
      
      is-square
      
      
      "
    >
    <div class="AdaptiveMedia-container
        js-adaptive-media-container
        "
      >
        <div class="AdaptiveMedia-singlePhoto">
    <div class="AdaptiveMedia-photoContainer js-adaptive-photo "
  data-image-url="https://pbs.twimg.com/media/CwYVNBzWQAAgEce.jpg"
  
  
  data-element-context="platform_photo_card">
  <img data-aria-label-part src="https://pbs.twimg.com/media/CwYVNBzWQAAgEce.jpg" alt=""
      style="width: 100%; top: -0px;"
>
</div>


</div>


    </div>
  </div>



      
      

      
      <div class="stream-item-footer">
  
        <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="30">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>30 replies .</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="2652">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>2,652 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="3816">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>3,816 likes</span>
      </span>
    </span>
  </div>

    <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
      <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionReply"
    data-modal="ProfileTweet-reply"
    type="button">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount ">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">30</span>
        </span>
      </div>
  </button>
</div>
      <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet"
    
    data-modal="ProfileTweet-retweet"
    type="button">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">2.7K</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">2.7K</span>
        </span>
      </div>
  </button>
</div>

      <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">3.8K</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">3.8K</span>
        </span>
      </div>
  </button>
</div>

      


        <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--dots"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
  </ul>
</div>

</div>

  </div>

    </div>

</div>
  



      
      

    </div>
  </div>


</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="794346658314076160" id="stream-item-tweet-794346658314076160" data-item-type="tweet">
    


  

  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable
       original-tweet js-original-tweet
      
       
"
      
data-tweet-id="794346658314076160"
data-item-id="794346658314076160"
data-permalink-path="/LordofWentworth/status/794346658314076160"








  data-screen-name="LordofWentworth" data-name="Lᴏʀᴅ Wᴇɴᴛᴡᴏʀᴛʜ" data-user-id="712213221445410816"
  data-you-follow="false"
  data-follows-you="false"
  data-you-block="false"









data-disclosure-type=""












 data-component-context="tweet"


    >


    <div class="context">
      
      
    </div>

    <div class="content">
      

      
      <div class="stream-item-header">
          <a  class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/LordofWentworth" data-user-id="712213221445410816">
    <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/712213811873378304/E_u51Oxv_bigger.jpg" alt="">
    <strong class="fullname js-action-profile-name show-popup-with-id" data-aria-label-part>Lᴏʀᴅ Wᴇɴᴛᴡᴏʀᴛʜ</strong>
    <span>&rlm;</span><span class="username js-action-profile-name" data-aria-label-part><s>@</s><b>LordofWentworth</b></span>
    
  </a>

        <small class="time">
  <a href="/LordofWentworth/status/794346658314076160" class="tweet-timestamp js-permalink js-nav js-tooltip" title="6:12 pm - 3 Nov 2016" ><span class="_timestamp js-short-timestamp " data-aria-label-part="last" data-time="1478221976" data-time-ms="1478221976000" data-long-form="true">Nov 3</span></a>
</small>

          
          
      </div>


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0">So the govt &#39;broke&#39; <strong>a</strong> $100k <strong>a</strong> year lease (at our cost) to allow Day to lease his own building, because it was &#39;Conservative HQ&#39; in Adelaide</p>
</div>




      
        

      
      

      
      <div class="stream-item-footer">
  
        <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="2">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>2 replies .</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="81">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>81 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="42">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>42 likes</span>
      </span>
    </span>
  </div>

    <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
      <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionReply"
    data-modal="ProfileTweet-reply"
    type="button">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount ">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">2</span>
        </span>
      </div>
  </button>
</div>
      <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet"
    
    data-modal="ProfileTweet-retweet"
    type="button">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">81</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">81</span>
        </span>
      </div>
  </button>
</div>

      <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">42</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">42</span>
        </span>
      </div>
  </button>
</div>

      


        <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--dots"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
  </ul>
</div>

</div>

  </div>

    </div>

</div>
  



      
      

    </div>
  </div>


</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="794346645597069312" id="stream-item-tweet-794346645597069312" data-item-type="tweet">
    


  

  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable
       original-tweet js-original-tweet
      
       
"
      
data-tweet-id="794346645597069312"
data-item-id="794346645597069312"
data-permalink-path="/benjaminbruce/status/794346645597069312"








  data-screen-name="benjaminbruce" data-name="Ben Bruce" data-user-id="172592669"
  data-you-follow="false"
  data-follows-you="false"
  data-you-block="false"









data-disclosure-type=""












 data-component-context="tweet"


    >


    <div class="context">
      
      
    </div>

    <div class="content">
      

      
      <div class="stream-item-header">
          <a  class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/benjaminbruce" data-user-id="172592669">
    <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/786311470409670656/1Pd_qace_bigger.jpg" alt="">
    <strong class="fullname js-action-profile-name show-popup-with-id" data-aria-label-part>Ben Bruce<span class="Icon Icon--verified Icon--small">
  <span class="u-hiddenVisually">Verified account</span>
</span></strong>
    <span>&rlm;</span><span class="username js-action-profile-name" data-aria-label-part><s>@</s><b>benjaminbruce</b></span>
    
  </a>

        <small class="time">
  <a href="/benjaminbruce/status/794346645597069312" class="tweet-timestamp js-permalink js-nav js-tooltip" title="6:12 pm - 3 Nov 2016" ><span class="_timestamp js-short-timestamp " data-aria-label-part="last" data-time="1478221973" data-time-ms="1478221973000" data-long-form="true">Nov 3</span></a>
</small>

          
          
      </div>


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0">It&#39;s <strong>a</strong> Finding Dory sort of evening <img class="Emoji Emoji--forText" src="https://abs.twimg.com/emoji/v2/72x72/1f420.png" draggable="false" alt="��" title="Tropical fish" aria-label="Emoji: Tropical fish"></p>
</div>




      
        

      
      

      
      <div class="stream-item-footer">
  
        <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="18">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>18 replies .</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="143">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>143 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="1140">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>1,140 likes</span>
      </span>
    </span>
  </div>

    <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
      <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionReply"
    data-modal="ProfileTweet-reply"
    type="button">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount ">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">18</span>
        </span>
      </div>
  </button>
</div>
      <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet"
    
    data-modal="ProfileTweet-retweet"
    type="button">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">143</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">143</span>
        </span>
      </div>
  </button>
</div>

      <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">1.1K</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">1.1K</span>
        </span>
      </div>
  </button>
</div>

      


        <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--dots"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
  </ul>
</div>

</div>

  </div>

    </div>

</div>
  



      
      

    </div>
  </div>


</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="794346644028461056" id="stream-item-tweet-794346644028461056" data-item-type="tweet">
    


  

  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable
       original-tweet js-original-tweet
      
       has-cards  has-content
"
      
data-tweet-id="794346644028461056"
data-item-id="794346644028461056"
data-permalink-path="/yagurlbubblez87/status/794346644028461056"








  data-screen-name="yagurlbubblez87" data-name="Bubbz��" data-user-id="250353399"
  data-you-follow="false"
  data-follows-you="false"
  data-you-block="false"





 data-possibly-sensitive="true"



data-disclosure-type=""




 data-has-cards="true"







 data-component-context="tweet"


    >


    <div class="context">
      
      
    </div>

    <div class="content">
      

      
      <div class="stream-item-header">
          <a  class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/yagurlbubblez87" data-user-id="250353399">
    <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/796021921037058055/LQ94wspd_bigger.jpg" alt="">
    <strong class="fullname js-action-profile-name show-popup-with-id" data-aria-label-part>Bubbz<span class="Emoji Emoji--forLinks" style="background-image:url('https://abs.twimg.com/emoji/v2/72x72/1f49e.png')" title="Revolving hearts" aria-label="Emoji: Revolving hearts">&nbsp;</span><span class="visuallyhidden" aria-hidden="true">��</span></strong>
    <span>&rlm;</span><span class="username js-action-profile-name" data-aria-label-part><s>@</s><b>yagurlbubblez87</b></span>
    
  </a>

        <small class="time">
  <a href="/yagurlbubblez87/status/794346644028461056" class="tweet-timestamp js-permalink js-nav js-tooltip" title="6:12 pm - 3 Nov 2016" ><span class="_timestamp js-short-timestamp " data-aria-label-part="last" data-time="1478221972" data-time-ms="1478221972000" data-long-form="true">Nov 3</span></a>
</small>

          
          
      </div>


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0">I want <strong>a</strong> bear this size for christmas. Imma add it to my wishlist now <a href="https://t.co/5FeS9ixBqL" class="twitter-timeline-link u-hidden" data-pre-embedded="true" dir="ltr" >pic.twitter.com/5FeS9ixBqL</a></p>
</div>




      
            <div class="AdaptiveMedia
      
      AdaptiveMedia--hiddenWhenNotExpanded
      is-square
      
      
      "
    >
      <div class="media-not-displayed">
  <h2>The following media may contain sensitive material.</h2>


    <p>If you'd prefer not to see these warnings, log in to change your <a href="/settings/account" target="_blank">Tweet media settings.</a>
      Don't have an account? <a href="/signup" target="_blank">Sign up!</a></p>

  <button type="button" class="btn display-this-media">
    View content
  </button>


    <a class="media-learn-more" href="https://support.twitter.com/articles/20169200-media-settings-and-best-practices" target="_blank">Learn more</a>
</div>

    <div class="AdaptiveMedia-container
        js-adaptive-media-container
        hidden"
      >
        <div class="AdaptiveMedia-singlePhoto">
    <div class="AdaptiveMedia-photoContainer js-adaptive-photo "
  data-image-url="https://pbs.twimg.com/media/CwYWDnIW8AEy_uh.jpg"
  
  
  data-element-context="platform_photo_card">
  <img data-aria-label-part src="https://pbs.twimg.com/media/CwYWDnIW8AEy_uh.jpg" alt=""
      style="width: 100%; top: -62px;"
>
</div>


</div>


    </div>
  </div>



      
      

      
      <div class="stream-item-footer">
  
        <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="2">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>2 replies .</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="64">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>64 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="102">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>102 likes</span>
      </span>
    </span>
  </div>

    <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
      <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionReply"
    data-modal="ProfileTweet-reply"
    type="button">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount ">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">2</span>
        </span>
      </div>
  </button>
</div>
      <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet"
    
    data-modal="ProfileTweet-retweet"
    type="button">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">64</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">64</span>
        </span>
      </div>
  </button>
</div>

      <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">102</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">102</span>
        </span>
      </div>
  </button>
</div>

      


        <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--dots"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
  </ul>
</div>

</div>

  </div>

    </div>

</div>
  



      
      

    </div>
  </div>


</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="794346642573029376" id="stream-item-tweet-794346642573029376" data-item-type="tweet">
    


  

  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable
       original-tweet js-original-tweet
      
       
"
      
data-tweet-id="794346642573029376"
data-item-id="794346642573029376"
data-permalink-path="/emmajthomsonn/status/794346642573029376"








  data-screen-name="emmajthomsonn" data-name="Emma Thomson" data-user-id="3373989791"
  data-you-follow="false"
  data-follows-you="false"
  data-you-block="false"









data-disclosure-type=""












 data-component-context="tweet"


    >


    <div class="context">
      
      
    </div>

    <div class="content">
      

      
      <div class="stream-item-header">
          <a  class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/emmajthomsonn" data-user-id="3373989791">
    <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/795398828610453504/ZDqkiN5l_bigger.jpg" alt="">
    <strong class="fullname js-action-profile-name show-popup-with-id" data-aria-label-part>Emma Thomson</strong>
    <span>&rlm;</span><span class="username js-action-profile-name" data-aria-label-part><s>@</s><b>emmajthomsonn</b></span>
    
  </a>

        <small class="time">
  <a href="/emmajthomsonn/status/794346642573029376" class="tweet-timestamp js-permalink js-nav js-tooltip" title="6:12 pm - 3 Nov 2016" ><span class="_timestamp js-short-timestamp " data-aria-label-part="last" data-time="1478221972" data-time-ms="1478221972000" data-long-form="true">Nov 3</span></a>
</small>

          
          
      </div>


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0">If anyone wants to take me on <strong>a</strong> date to the fair now is the time to speak up!</p>
</div>




      
        

      
      

      
      <div class="stream-item-footer">
  
        <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" aria-hidden="true" data-tweet-stat-count="0">
        <span class="ProfileTweet-actionCountForAria" >0 replies .</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="17">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>17 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="21">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>21 likes</span>
      </span>
    </span>
  </div>

    <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
      <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionReply"
    data-modal="ProfileTweet-reply"
    type="button">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount ProfileTweet-actionCount--isZero ">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true"></span>
        </span>
      </div>
  </button>
</div>
      <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet"
    
    data-modal="ProfileTweet-retweet"
    type="button">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">17</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">17</span>
        </span>
      </div>
  </button>
</div>

      <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">21</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">21</span>
        </span>
      </div>
  </button>
</div>

      


        <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--dots"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
  </ul>
</div>

</div>

  </div>

    </div>

</div>
  



      
      

    </div>
  </div>


</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="794346627251191808" id="stream-item-tweet-794346627251191808" data-item-type="tweet">
    


  

  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable
       original-tweet js-original-tweet
      
       
"
      
data-tweet-id="794346627251191808"
data-item-id="794346627251191808"
data-permalink-path="/TallahForTrump/status/794346627251191808"








  data-screen-name="TallahForTrump" data-name="Black Women 4 Trump" data-user-id="771529979846766592"
  data-you-follow="false"
  data-follows-you="false"
  data-you-block="false"









data-disclosure-type=""












 data-component-context="tweet"


    >


    <div class="context">
      
      
    </div>

    <div class="content">
      

      
      <div class="stream-item-header">
          <a  class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/TallahForTrump" data-user-id="771529979846766592">
    <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/772831237320810496/C9iD4iDd_bigger.jpg" alt="">
    <strong class="fullname js-action-profile-name show-popup-with-id" data-aria-label-part>Black Women 4 Trump</strong>
    <span>&rlm;</span><span class="username js-action-profile-name" data-aria-label-part><s>@</s><b>TallahForTrump</b></span>
    
  </a>

        <small class="time">
  <a href="/TallahForTrump/status/794346627251191808" class="tweet-timestamp js-permalink js-nav js-tooltip" title="6:12 pm - 3 Nov 2016" ><span class="_timestamp js-short-timestamp " data-aria-label-part="last" data-time="1478221968" data-time-ms="1478221968000" data-long-form="true">Nov 3</span></a>
</small>

          
          
      </div>


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0">You&#39;ve seen the emails, now let this resonate: Haiti is <strong>a</strong> source, transit, &amp; destination country for child sex trafficking. <a href="/hashtag/PodestaEmails28?src=hash" data-query-source="hashtag_click" class="twitter-hashtag pretty-link js-nav" dir="ltr" ><s>#</s><b>PodestaEmails28</b></a></p>
</div>




      
        

      
      

      
      <div class="stream-item-footer">
  
        <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="60">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>60 replies .</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="768">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>768 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="712">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>712 likes</span>
      </span>
    </span>
  </div>

    <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
      <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionReply"
    data-modal="ProfileTweet-reply"
    type="button">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount ">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">60</span>
        </span>
      </div>
  </button>
</div>
      <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet"
    
    data-modal="ProfileTweet-retweet"
    type="button">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">768</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">768</span>
        </span>
      </div>
  </button>
</div>

      <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">712</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">712</span>
        </span>
      </div>
  </button>
</div>

      


        <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--dots"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
  </ul>
</div>

</div>

  </div>

    </div>

</div>
  



      
      

    </div>
  </div>


</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="794346624285863936" id="stream-item-tweet-794346624285863936" data-item-type="tweet">
    


  

  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable
       original-tweet js-original-tweet
      
       
"
      
data-tweet-id="794346624285863936"
data-item-id="794346624285863936"
data-permalink-path="/DeanteVH/status/794346624285863936"








  data-screen-name="DeanteVH" data-name="DEANTE&#39; HITCHCOCK" data-user-id="4270307660"
  data-you-follow="false"
  data-follows-you="false"
  data-you-block="false"









data-disclosure-type=""












 data-component-context="tweet"


    >


    <div class="context">
      
      
    </div>

    <div class="content">
      

      
      <div class="stream-item-header">
          <a  class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/DeanteVH" data-user-id="4270307660">
    <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/795047009967341568/xLXJs9T9_bigger.jpg" alt="">
    <strong class="fullname js-action-profile-name show-popup-with-id" data-aria-label-part>DEANTE&#39; HITCHCOCK</strong>
    <span>&rlm;</span><span class="username js-action-profile-name" data-aria-label-part><s>@</s><b>DeanteVH</b></span>
    
  </a>

        <small class="time">
  <a href="/DeanteVH/status/794346624285863936" class="tweet-timestamp js-permalink js-nav js-tooltip" title="6:12 pm - 3 Nov 2016" ><span class="_timestamp js-short-timestamp " data-aria-label-part="last" data-time="1478221968" data-time-ms="1478221968000" data-long-form="true">Nov 3</span></a>
</small>

          
          
      </div>


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0">I did <strong>a</strong> song with Jermaine Dupri and Da Brat. That&#39;s bucket list worthy. 9 year old me going brazy right now</p>
</div>




      
        

      
      

      
      <div class="stream-item-footer">
  
        <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="5">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>5 replies .</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="18">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>18 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="65">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>65 likes</span>
      </span>
    </span>
  </div>

    <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
      <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionReply"
    data-modal="ProfileTweet-reply"
    type="button">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount ">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">5</span>
        </span>
      </div>
  </button>
</div>
      <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet"
    
    data-modal="ProfileTweet-retweet"
    type="button">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">18</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">18</span>
        </span>
      </div>
  </button>
</div>

      <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">65</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">65</span>
        </span>
      </div>
  </button>
</div>

      


        <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--dots"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
  </ul>
</div>

</div>

  </div>

    </div>

</div>
  



      
      

    </div>
  </div>


</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="794346608884387840" id="stream-item-tweet-794346608884387840" data-item-type="tweet">
    


  

  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable
       original-tweet js-original-tweet
      
       
"
      
data-tweet-id="794346608884387840"
data-item-id="794346608884387840"
data-permalink-path="/kamij0sh/status/794346608884387840"








  data-screen-name="kamij0sh" data-name="KAMI神" data-user-id="2716256146"
  data-you-follow="false"
  data-follows-you="false"
  data-you-block="false"









data-disclosure-type=""












 data-component-context="tweet"


    >


    <div class="context">
      
      
    </div>

    <div class="content">
      

      
      <div class="stream-item-header">
          <a  class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/kamij0sh" data-user-id="2716256146">
    <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/792227681496621056/taUkWA3b_bigger.jpg" alt="">
    <strong class="fullname js-action-profile-name show-popup-with-id" data-aria-label-part>KAMI神</strong>
    <span>&rlm;</span><span class="username js-action-profile-name" data-aria-label-part><s>@</s><b>kamij0sh</b></span>
    
  </a>

        <small class="time">
  <a href="/kamij0sh/status/794346608884387840" class="tweet-timestamp js-permalink js-nav js-tooltip" title="6:12 pm - 3 Nov 2016" ><span class="_timestamp js-short-timestamp " data-aria-label-part="last" data-time="1478221964" data-time-ms="1478221964000" data-long-form="true">Nov 3</span></a>
</small>

          
          
      </div>


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0">WHY IS THERE ONLY <strong>A</strong> SUCH THING AS <strong>A</strong> BAD STUDENT BUT NEVER <strong>A</strong> BAD TEACHER? Bad grades are always the fault of the student. That&#39;s not right!</p>
</div>




      
        

      
      

      
      <div class="stream-item-footer">
  
        <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" aria-hidden="true" data-tweet-stat-count="0">
        <span class="ProfileTweet-actionCountForAria" >0 replies .</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="24">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>24 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="31">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>31 likes</span>
      </span>
    </span>
  </div>

    <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
      <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionReply"
    data-modal="ProfileTweet-reply"
    type="button">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount ProfileTweet-actionCount--isZero ">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true"></span>
        </span>
      </div>
  </button>
</div>
      <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet"
    
    data-modal="ProfileTweet-retweet"
    type="button">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">24</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">24</span>
        </span>
      </div>
  </button>
</div>

      <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">31</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">31</span>
        </span>
      </div>
  </button>
</div>

      


        <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--dots"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
  </ul>
</div>

</div>

  </div>

    </div>

</div>
  



      
      

    </div>
  </div>


</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="794346598721552387" id="stream-item-tweet-794346598721552387" data-item-type="tweet">
    


  

  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable
       original-tweet js-original-tweet
      
       
"
      
data-tweet-id="794346598721552387"
data-item-id="794346598721552387"
data-permalink-path="/ESPNStatsInfo/status/794346598721552387"








  data-screen-name="ESPNStatsInfo" data-name="ESPN Stats &amp; Info" data-user-id="53120768"
  data-you-follow="false"
  data-follows-you="false"
  data-you-block="false"
 data-mentions="OU_Football"








data-disclosure-type=""












 data-component-context="tweet"


    >


    <div class="context">
      
      
    </div>

    <div class="content">
      

      
      <div class="stream-item-header">
          <a  class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/ESPNStatsInfo" data-user-id="53120768">
    <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/747495844157472769/Np_LXZ_x_bigger.jpg" alt="">
    <strong class="fullname js-action-profile-name show-popup-with-id" data-aria-label-part>ESPN Stats &amp; Info<span class="Icon Icon--verified Icon--small">
  <span class="u-hiddenVisually">Verified account</span>
</span></strong>
    <span>&rlm;</span><span class="username js-action-profile-name" data-aria-label-part><s>@</s><b>ESPNStatsInfo</b></span>
    
  </a>

        <small class="time">
  <a href="/ESPNStatsInfo/status/794346598721552387" class="tweet-timestamp js-permalink js-nav js-tooltip" title="6:12 pm - 3 Nov 2016" ><span class="_timestamp js-short-timestamp " data-aria-label-part="last" data-time="1478221962" data-time-ms="1478221962000" data-long-form="true">Nov 3</span></a>
</small>

          
          
      </div>


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0">Baker Mayfield (<a href="/OU_Football" class="twitter-atreply pretty-link js-nav" dir="ltr" data-mentioned-user-id="407208905" ><s>@</s><b>OU_Football</b></a>): 3rd time he&#39;s thrown 4 TD passes in <strong>a</strong> half in his career.</p>
</div>




      
        

      
      

      
      <div class="stream-item-footer">
  
        <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="3">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>3 replies .</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="63">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>63 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="150">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>150 likes</span>
      </span>
    </span>
  </div>

    <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
      <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionReply"
    data-modal="ProfileTweet-reply"
    type="button">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount ">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">3</span>
        </span>
      </div>
  </button>
</div>
      <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet"
    
    data-modal="ProfileTweet-retweet"
    type="button">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">63</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">63</span>
        </span>
      </div>
  </button>
</div>

      <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">150</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">150</span>
        </span>
      </div>
  </button>
</div>

      


        <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--dots"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
  </ul>
</div>

</div>

  </div>

    </div>

</div>
  



      
      

    </div>
  </div>


</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="794346587950415872" id="stream-item-tweet-794346587950415872" data-item-type="tweet">
    


  

  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable
       original-tweet js-original-tweet
      
       
"
      
data-tweet-id="794346587950415872"
data-item-id="794346587950415872"
data-permalink-path="/Jbeq760/status/794346587950415872"








  data-screen-name="Jbeq760" data-name="Jbeq♛" data-user-id="2268041100"
  data-you-follow="false"
  data-follows-you="false"
  data-you-block="false"









data-disclosure-type=""












 data-component-context="tweet"


    >


    <div class="context">
      
      
    </div>

    <div class="content">
      

      
      <div class="stream-item-header">
          <a  class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/Jbeq760" data-user-id="2268041100">
    <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/797325296558952449/wtsJBNp__bigger.jpg" alt="">
    <strong class="fullname js-action-profile-name show-popup-with-id" data-aria-label-part>Jbeq♛</strong>
    <span>&rlm;</span><span class="username js-action-profile-name" data-aria-label-part><s>@</s><b>Jbeq760</b></span>
    
  </a>

        <small class="time">
  <a href="/Jbeq760/status/794346587950415872" class="tweet-timestamp js-permalink js-nav js-tooltip" title="6:12 pm - 3 Nov 2016" ><span class="_timestamp js-short-timestamp " data-aria-label-part="last" data-time="1478221959" data-time-ms="1478221959000" data-long-form="true">Nov 3</span></a>
</small>

            <span class="Tweet-geo u-floatRight js-tooltip" title="La Verne, CA">
      <a class="ProfileTweet-actionButton u-linkClean js-nav js-geo-pivot-link" href="/search?q=place%3A7183cae332544afd" role="button" data-place-id="7183cae332544afd">
        <span class="Icon Icon--geo"></span>
          <span class="u-hiddenVisually">La Verne, CA</span>
      </a>
  </span>

          
      </div>


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0">Class of 2017 y&#39;all better enjoy tf out of homecoming tomorrow! There&#39;s honestly nothing like being <strong>a</strong> senior at pv on that day</p>
</div>




      
        

      
      

      
      <div class="stream-item-footer">
  
        <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" aria-hidden="true" data-tweet-stat-count="0">
        <span class="ProfileTweet-actionCountForAria" >0 replies .</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="24">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>24 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="68">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>68 likes</span>
      </span>
    </span>
  </div>

    <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
      <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionReply"
    data-modal="ProfileTweet-reply"
    type="button">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount ProfileTweet-actionCount--isZero ">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true"></span>
        </span>
      </div>
  </button>
</div>
      <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet"
    
    data-modal="ProfileTweet-retweet"
    type="button">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">24</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">24</span>
        </span>
      </div>
  </button>
</div>

      <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">68</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">68</span>
        </span>
      </div>
  </button>
</div>

      


        <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--dots"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
  </ul>
</div>

</div>

  </div>

    </div>

</div>
  



      
      

    </div>
  </div>


</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="794346579230498816" id="stream-item-tweet-794346579230498816" data-item-type="tweet">
    


  

  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable
       original-tweet js-original-tweet
      
       
"
      
data-tweet-id="794346579230498816"
data-item-id="794346579230498816"
data-permalink-path="/JJ_Avrams/status/794346579230498816"








  data-screen-name="JJ_Avrams" data-name="Avram" data-user-id="1697961506"
  data-you-follow="false"
  data-follows-you="false"
  data-you-block="false"









data-disclosure-type=""












 data-component-context="tweet"


    >


    <div class="context">
      
      
    </div>

    <div class="content">
      

      
      <div class="stream-item-header">
          <a  class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/JJ_Avrams" data-user-id="1697961506">
    <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/796557838067740672/8el58xdk_bigger.jpg" alt="">
    <strong class="fullname js-action-profile-name show-popup-with-id" data-aria-label-part>Avram</strong>
    <span>&rlm;</span><span class="username js-action-profile-name" data-aria-label-part><s>@</s><b>JJ_Avrams</b></span>
    
  </a>

        <small class="time">
  <a href="/JJ_Avrams/status/794346579230498816" class="tweet-timestamp js-permalink js-nav js-tooltip" title="6:12 pm - 3 Nov 2016" ><span class="_timestamp js-short-timestamp " data-aria-label-part="last" data-time="1478221957" data-time-ms="1478221957000" data-long-form="true">Nov 3</span></a>
</small>

          
          
      </div>


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0">You&#39;re uneducated if you think Tarantino fits with <strong>a</strong> Deadpool movie just because he&#39;s &quot;that crazy director&quot;</p>
</div>




      
        

      
      

      
      <div class="stream-item-footer">
  
        <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="1">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>1 reply .</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="15">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>15 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="41">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>41 likes</span>
      </span>
    </span>
  </div>

    <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
      <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionReply"
    data-modal="ProfileTweet-reply"
    type="button">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount ">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">1</span>
        </span>
      </div>
  </button>
</div>
      <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet"
    
    data-modal="ProfileTweet-retweet"
    type="button">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">15</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">15</span>
        </span>
      </div>
  </button>
</div>

      <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">41</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">41</span>
        </span>
      </div>
  </button>
</div>

      


        <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--dots"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
  </ul>
</div>

</div>

  </div>

    </div>

</div>
  



      
      

    </div>
  </div>


</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="794346554710573056" id="stream-item-tweet-794346554710573056" data-item-type="tweet">
    


  

  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable
       original-tweet js-original-tweet
      
       has-cards  has-content
"
      
data-tweet-id="794346554710573056"
data-item-id="794346554710573056"
data-permalink-path="/bfraser747/status/794346554710573056"








  data-screen-name="bfraser747" data-name="Brian Fraser" data-user-id="274891222"
  data-you-follow="false"
  data-follows-you="false"
  data-you-block="false"









data-disclosure-type=""




 data-has-cards="true"







 data-component-context="tweet"


    >


    <div class="context">
      
      
    </div>

    <div class="content">
      

      
      <div class="stream-item-header">
          <a  class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/bfraser747" data-user-id="274891222">
    <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/791021821193654272/GuWsuGci_bigger.jpg" alt="">
    <strong class="fullname js-action-profile-name show-popup-with-id" data-aria-label-part>Brian Fraser</strong>
    <span>&rlm;</span><span class="username js-action-profile-name" data-aria-label-part><s>@</s><b>bfraser747</b></span>
    
  </a>

        <small class="time">
  <a href="/bfraser747/status/794346554710573056" class="tweet-timestamp js-permalink js-nav js-tooltip" title="6:12 pm - 3 Nov 2016" ><span class="_timestamp js-short-timestamp " data-aria-label-part="last" data-time="1478221951" data-time-ms="1478221951000" data-long-form="true">Nov 3</span></a>
</small>

          
          
      </div>


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0"><img class="Emoji Emoji--forText" src="https://abs.twimg.com/emoji/v2/72x72/1f4a5.png" draggable="false" alt="��" title="Collision symbol" aria-label="Emoji: Collision symbol"><img class="Emoji Emoji--forText" src="https://abs.twimg.com/emoji/v2/72x72/1f4a5.png" draggable="false" alt="��" title="Collision symbol" aria-label="Emoji: Collision symbol"> <a href="/hashtag/VoteTrump?src=hash" data-query-source="hashtag_click" class="twitter-hashtag pretty-link js-nav" dir="ltr" ><s>#</s><b>VoteTrump</b></a>

<a href="/hashtag/Trump?src=hash" data-query-source="hashtag_click" class="twitter-hashtag pretty-link js-nav" dir="ltr" ><s>#</s><b>Trump</b></a> is doing this to give back 2 America &amp; <a href="/hashtag/MAGA?src=hash" data-query-source="hashtag_click" class="twitter-hashtag pretty-link js-nav" dir="ltr" ><s>#</s><b>MAGA</b></a>

He&#39;s <strong>a</strong> 70 yr old Billionaire &amp; doesn&#39;t have do this

<a href="/hashtag/HillaryIndictment?src=hash" data-query-source="hashtag_click" class="twitter-hashtag pretty-link js-nav" dir="ltr" ><s>#</s><b>HillaryIndictment</b></a><a href="https://t.co/g9vbKKtciv" class="twitter-timeline-link u-hidden" data-pre-embedded="true" dir="ltr" >pic.twitter.com/g9vbKKtciv</a></p>
</div>




      
            <div class="AdaptiveMedia
      
      
      is-square
      
      
      "
    >
    <div class="AdaptiveMedia-container
        js-adaptive-media-container
        "
      >
        <div class="AdaptiveMedia-singlePhoto">
    <div class="AdaptiveMedia-photoContainer js-adaptive-photo "
  data-image-url="https://pbs.twimg.com/media/CwYV-tjUkAAMjIH.jpg"
  
  
  data-element-context="platform_photo_card">
  <img data-aria-label-part src="https://pbs.twimg.com/media/CwYV-tjUkAAMjIH.jpg" alt=""
>
</div>


</div>


    </div>
  </div>



      
      

      
      <div class="stream-item-footer">
  
        <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="40">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>40 replies .</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="1143">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>1,143 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="1241">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>1,241 likes</span>
      </span>
    </span>
  </div>

    <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
      <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionReply"
    data-modal="ProfileTweet-reply"
    type="button">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount ">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">40</span>
        </span>
      </div>
  </button>
</div>
      <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet"
    
    data-modal="ProfileTweet-retweet"
    type="button">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">1.1K</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">1.1K</span>
        </span>
      </div>
  </button>
</div>

      <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">1.2K</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">1.2K</span>
        </span>
      </div>
  </button>
</div>

      


        <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--dots"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
  </ul>
</div>

</div>

  </div>

    </div>

</div>
  



      
      

    </div>
  </div>


</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="794346494887346190" id="stream-item-tweet-794346494887346190" data-item-type="tweet">
    


  

  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable
       original-tweet js-original-tweet
      
       
"
      
data-tweet-id="794346494887346190"
data-item-id="794346494887346190"
data-permalink-path="/Vulnerable/status/794346494887346190"








  data-screen-name="Vulnerable" data-name="anxiety" data-user-id="2920084603"
  data-you-follow="false"
  data-follows-you="false"
  data-you-block="false"









data-disclosure-type=""












 data-component-context="tweet"


    >


    <div class="context">
      
      
    </div>

    <div class="content">
      

      
      <div class="stream-item-header">
          <a  class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/Vulnerable" data-user-id="2920084603">
    <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/709849901849579520/WedEaryX_bigger.jpg" alt="">
    <strong class="fullname js-action-profile-name show-popup-with-id" data-aria-label-part>anxiety</strong>
    <span>&rlm;</span><span class="username js-action-profile-name" data-aria-label-part><s>@</s><b>Vulnerable</b></span>
    
  </a>

        <small class="time">
  <a href="/Vulnerable/status/794346494887346190" class="tweet-timestamp js-permalink js-nav js-tooltip" title="6:12 pm - 3 Nov 2016" ><span class="_timestamp js-short-timestamp " data-aria-label-part="last" data-time="1478221937" data-time-ms="1478221937000" data-long-form="true">Nov 3</span></a>
</small>

          
          
      </div>


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0">i keep shit to myself for <strong>a</strong> reason</p>
</div>




      
        

      
      

      
      <div class="stream-item-footer">
  
        <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" aria-hidden="true" data-tweet-stat-count="0">
        <span class="ProfileTweet-actionCountForAria" >0 replies .</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="582">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>582 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="749">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>749 likes</span>
      </span>
    </span>
  </div>

    <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
      <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionReply"
    data-modal="ProfileTweet-reply"
    type="button">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount ProfileTweet-actionCount--isZero ">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true"></span>
        </span>
      </div>
  </button>
</div>
      <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet"
    
    data-modal="ProfileTweet-retweet"
    type="button">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">582</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">582</span>
        </span>
      </div>
  </button>
</div>

      <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">749</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">749</span>
        </span>
      </div>
  </button>
</div>

      


        <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--dots"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
  </ul>
</div>

</div>

  </div>

    </div>

</div>
  



      
      

    </div>
  </div>


</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="794346466181521412" id="stream-item-tweet-794346466181521412" data-item-type="tweet">
    


  

  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable
       original-tweet js-original-tweet
      
       has-cards  has-content
"
      
data-tweet-id="794346466181521412"
data-item-id="794346466181521412"
data-permalink-path="/hellspawnmotel/status/794346466181521412"








  data-screen-name="hellspawnmotel" data-name="LEO" data-user-id="4657375403"
  data-you-follow="false"
  data-follows-you="false"
  data-you-block="false"









data-disclosure-type=""




 data-has-cards="true"







 data-component-context="tweet"


    >


    <div class="context">
      
      
    </div>

    <div class="content">
      

      
      <div class="stream-item-header">
          <a  class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/hellspawnmotel" data-user-id="4657375403">
    <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/793323052591218688/0E8yqL-t_bigger.jpg" alt="">
    <strong class="fullname js-action-profile-name show-popup-with-id" data-aria-label-part>LEO</strong>
    <span>&rlm;</span><span class="username js-action-profile-name" data-aria-label-part><s>@</s><b>hellspawnmotel</b></span>
    
  </a>

        <small class="time">
  <a href="/hellspawnmotel/status/794346466181521412" class="tweet-timestamp js-permalink js-nav js-tooltip" title="6:12 pm - 3 Nov 2016" ><span class="_timestamp js-short-timestamp " data-aria-label-part="last" data-time="1478221930" data-time-ms="1478221930000" data-long-form="true">Nov 3</span></a>
</small>

          
          
      </div>


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0"><strong>a</strong> burger boy for <a href="/hashtag/huevember?src=hash" data-query-source="hashtag_click" class="twitter-hashtag pretty-link js-nav" dir="ltr" ><s>#</s><b>huevember</b></a> day 3<a href="https://t.co/858uPBcfEQ" class="twitter-timeline-link u-hidden" data-pre-embedded="true" dir="ltr" >pic.twitter.com/858uPBcfEQ</a></p>
</div>




      
            <div class="AdaptiveMedia
      
      
      is-square
      
      
      "
    >
    <div class="AdaptiveMedia-container
        js-adaptive-media-container
        "
      >
        <div class="AdaptiveMedia-singlePhoto">
    <div class="AdaptiveMedia-photoContainer js-adaptive-photo "
  data-image-url="https://pbs.twimg.com/media/CwYV4YSWIAA7rV1.jpg"
  
  
  data-element-context="platform_photo_card">
  <img data-aria-label-part src="https://pbs.twimg.com/media/CwYV4YSWIAA7rV1.jpg" alt=""
      style="width: 100%; top: -27px;"
>
</div>


</div>


    </div>
  </div>



      
      

      
      <div class="stream-item-footer">
  
        <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" aria-hidden="true" data-tweet-stat-count="0">
        <span class="ProfileTweet-actionCountForAria" >0 replies .</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="39">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>39 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="109">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>109 likes</span>
      </span>
    </span>
  </div>

    <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
      <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionReply"
    data-modal="ProfileTweet-reply"
    type="button">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount ProfileTweet-actionCount--isZero ">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true"></span>
        </span>
      </div>
  </button>
</div>
      <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet"
    
    data-modal="ProfileTweet-retweet"
    type="button">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">39</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">39</span>
        </span>
      </div>
  </button>
</div>

      <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">109</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">109</span>
        </span>
      </div>
  </button>
</div>

      


        <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--dots"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
  </ul>
</div>

</div>

  </div>

    </div>

</div>
  



      
      

    </div>
  </div>


</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="794346465191546880" id="stream-item-tweet-794346465191546880" data-item-type="tweet">
    


  

  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable
       original-tweet js-original-tweet
      
       has-cards  has-content
"
      
data-tweet-id="794346465191546880"
data-item-id="794346465191546880"
data-permalink-path="/pocha_393/status/794346465191546880"








  data-screen-name="pocha_393" data-name="��️OCHA" data-user-id="1251365671"
  data-you-follow="false"
  data-follows-you="false"
  data-you-block="false"









data-disclosure-type=""




 data-has-cards="true"







 data-component-context="tweet"


    >


    <div class="context">
      
      
    </div>

    <div class="content">
      

      
      <div class="stream-item-header">
          <a  class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/pocha_393" data-user-id="1251365671">
    <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/795594428781973504/TIeX4XeF_bigger.jpg" alt="">
    <strong class="fullname js-action-profile-name show-popup-with-id" data-aria-label-part><span class="Emoji Emoji--forLinks" style="background-image:url('https://abs.twimg.com/emoji/v2/72x72/1f17f.png')" title="Negative squared Latin capital letter p" aria-label="Emoji: Negative squared Latin capital letter p">&nbsp;</span><span class="visuallyhidden" aria-hidden="true">��️</span>OCHA</strong>
    <span>&rlm;</span><span class="username js-action-profile-name" data-aria-label-part><s>@</s><b>pocha_393</b></span>
    
  </a>

        <small class="time">
  <a href="/pocha_393/status/794346465191546880" class="tweet-timestamp js-permalink js-nav js-tooltip" title="6:12 pm - 3 Nov 2016" ><span class="_timestamp js-short-timestamp " data-aria-label-part="last" data-time="1478221930" data-time-ms="1478221930000" data-long-form="true">Nov 3</span></a>
</small>

          
          
      </div>


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0">P  P  <strong>A</strong>  P <a href="https://t.co/McjP4Mzo4L" class="twitter-timeline-link u-hidden" data-pre-embedded="true" dir="ltr" >pic.twitter.com/McjP4Mzo4L</a></p>
</div>




      
            <div class="AdaptiveMedia
      
      
      is-square
      
      
      "
    >
    <div class="AdaptiveMedia-container
        js-adaptive-media-container
        "
      >
        <div class="AdaptiveMedia-singlePhoto">
    <div class="AdaptiveMedia-photoContainer js-adaptive-photo "
  data-image-url="https://pbs.twimg.com/media/CwYV42IUUAAp9y1.jpg"
  
  
  data-element-context="platform_photo_card">
  <img data-aria-label-part src="https://pbs.twimg.com/media/CwYV42IUUAAp9y1.jpg" alt=""
      style="width: 100%; top: -0px;"
>
</div>


</div>


    </div>
  </div>



      
      

      
      <div class="stream-item-footer">
  
        <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="25">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>25 replies .</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="22067">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>22,067 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="32768">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>32,768 likes</span>
      </span>
    </span>
  </div>

    <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
      <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionReply"
    data-modal="ProfileTweet-reply"
    type="button">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount ">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">25</span>
        </span>
      </div>
  </button>
</div>
      <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet"
    
    data-modal="ProfileTweet-retweet"
    type="button">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">22K</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">22K</span>
        </span>
      </div>
  </button>
</div>

      <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">33K</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">33K</span>
        </span>
      </div>
  </button>
</div>

      


        <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--dots"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
  </ul>
</div>

</div>

  </div>

    </div>

</div>
  



      
      

    </div>
  </div>


</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="794346464529022976" id="stream-item-tweet-794346464529022976" data-item-type="tweet">
    


  

  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable
       original-tweet js-original-tweet
      
       has-cards  has-content
"
      
data-tweet-id="794346464529022976"
data-item-id="794346464529022976"
data-permalink-path="/historyinmoment/status/794346464529022976"








  data-screen-name="historyinmoment" data-name="History in Moments" data-user-id="2780215928"
  data-you-follow="false"
  data-follows-you="false"
  data-you-block="false"









data-disclosure-type=""




 data-has-cards="true"







 data-component-context="tweet"


    >


    <div class="context">
      
      
    </div>

    <div class="content">
      

      
      <div class="stream-item-header">
          <a  class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/historyinmoment" data-user-id="2780215928">
    <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/505634039173087232/qiu4I73i_bigger.jpeg" alt="">
    <strong class="fullname js-action-profile-name show-popup-with-id" data-aria-label-part>History in Moments</strong>
    <span>&rlm;</span><span class="username js-action-profile-name" data-aria-label-part><s>@</s><b>historyinmoment</b></span>
    
  </a>

        <small class="time">
  <a href="/historyinmoment/status/794346464529022976" class="tweet-timestamp js-permalink js-nav js-tooltip" title="6:12 pm - 3 Nov 2016" ><span class="_timestamp js-short-timestamp " data-aria-label-part="last" data-time="1478221930" data-time-ms="1478221930000" data-long-form="true">Nov 3</span></a>
</small>

          
          
      </div>


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0"><strong>A</strong> pile of American bison skulls waiting to be ground for fertilizer c. 1870 <a href="https://t.co/WsjAQyl0gy" class="twitter-timeline-link u-hidden" data-pre-embedded="true" dir="ltr" >pic.twitter.com/WsjAQyl0gy</a></p>
</div>




      
            <div class="AdaptiveMedia
      
      
      is-square
      
      
      "
    >
    <div class="AdaptiveMedia-container
        js-adaptive-media-container
        "
      >
        <div class="AdaptiveMedia-singlePhoto">
    <div class="AdaptiveMedia-photoContainer js-adaptive-photo "
  data-image-url="https://pbs.twimg.com/media/CwYV5ewWgAA96Yo.jpg"
  
  
  data-element-context="platform_photo_card">
  <img data-aria-label-part src="https://pbs.twimg.com/media/CwYV5ewWgAA96Yo.jpg" alt=""
>
</div>


</div>


    </div>
  </div>



      
      

      
      <div class="stream-item-footer">
  
        <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="2">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>2 replies .</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="44">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>44 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="61">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>61 likes</span>
      </span>
    </span>
  </div>

    <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
      <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionReply"
    data-modal="ProfileTweet-reply"
    type="button">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount ">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">2</span>
        </span>
      </div>
  </button>
</div>
      <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet"
    
    data-modal="ProfileTweet-retweet"
    type="button">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">44</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">44</span>
        </span>
      </div>
  </button>
</div>

      <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">61</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">61</span>
        </span>
      </div>
  </button>
</div>

      


        <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--dots"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
  </ul>
</div>

</div>

  </div>

    </div>

</div>
  



      
      

    </div>
  </div>


</li>

      <li class="js-stream-item stream-item stream-item withheld-item
" data-item-id="794346452478808064" id="stream-item-tweet-794346452478808064" data-item-type="tweet">
    


  <div class="tweet original-tweet withheld-tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable js-original-tweet   has-cards  has-content
" 
data-tweet-id="794346452478808064"
data-item-id="794346452478808064"
data-permalink-path="/EdwardsDaley/status/794346452478808064"








  data-screen-name="EdwardsDaley" data-name="Amy Leigh��GloryDays" data-user-id="305193950"
  data-you-follow="false"
  data-follows-you="false"
  data-you-block="false"
 data-mentions="LittleMix"








data-disclosure-type=""




 data-has-cards="true"







 data-component-context="tweet"

>
  <div class="StreamItemContent--withheld">
    <div class="stream-item-header">
      
      
      <a class="account-group">
        <strong class="fullname">Tweet withheld</strong>
      </a>
      <small class="time">
  <a href="/EdwardsDaley/status/794346452478808064" class="tweet-timestamp js-permalink js-nav js-tooltip" title="6:12 pm - 3 Nov 2016" ><span class="_timestamp js-short-timestamp " data-aria-label-part="last" data-time="1478221927" data-time-ms="1478221927000" data-long-form="true">Nov 3</span></a>
</small>

    </div>
    <p class="js-tweet-text">
      
      This Tweet from <span class="u-dir" dir="ltr">@EdwardsDaley</span> has been withheld in response to a report from the copyright holder.
 <a href="https://support.twitter.com/articles/15795" target="_blank">Learn more</a>
</p>
    <div class="stream-item-footer">
    </div>
    
  </div>
</div>


</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="794346451727974400" id="stream-item-tweet-794346451727974400" data-item-type="tweet">
    


  

  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable
       original-tweet js-original-tweet
      
       
"
      
data-tweet-id="794346451727974400"
data-item-id="794346451727974400"
data-permalink-path="/LifeLimits/status/794346451727974400"








  data-screen-name="LifeLimits" data-name="Think Different" data-user-id="1343486720"
  data-you-follow="false"
  data-follows-you="false"
  data-you-block="false"









data-disclosure-type=""












 data-component-context="tweet"


    >


    <div class="context">
      
      
    </div>

    <div class="content">
      

      
      <div class="stream-item-header">
          <a  class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/LifeLimits" data-user-id="1343486720">
    <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/3660782814/07c999843011b10a4ae21dcd7ccb95e2_bigger.png" alt="">
    <strong class="fullname js-action-profile-name show-popup-with-id" data-aria-label-part>Think Different</strong>
    <span>&rlm;</span><span class="username js-action-profile-name" data-aria-label-part><s>@</s><b>LifeLimits</b></span>
    
  </a>

        <small class="time">
  <a href="/LifeLimits/status/794346451727974400" class="tweet-timestamp js-permalink js-nav js-tooltip" title="6:12 pm - 3 Nov 2016" ><span class="_timestamp js-short-timestamp " data-aria-label-part="last" data-time="1478221926" data-time-ms="1478221926000" data-long-form="true">Nov 3</span></a>
</small>

          
          
      </div>


      
        <div class="js-tweet-text-container">
  <p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0">Every day is <strong>a</strong> NEW beginning, take <strong>a</strong> deep breath and START AGAIN.</p>
</div>




      
        

      
      

      
      <div class="stream-item-footer">
  
        <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" aria-hidden="true" data-tweet-stat-count="0">
        <span class="ProfileTweet-actionCountForAria" >0 replies .</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="161">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>161 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="180">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>180 likes</span>
      </span>
    </span>
  </div>

    <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
      <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionReply"
    data-modal="ProfileTweet-reply"
    type="button">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount ProfileTweet-actionCount--isZero ">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true"></span>
        </span>
      </div>
  </button>
</div>
      <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet"
    
    data-modal="ProfileTweet-retweet"
    type="button">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">161</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">161</span>
        </span>
      </div>
  </button>
</div>

      <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">180</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">180</span>
        </span>
      </div>
  </button>
</div>

      


        <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--dots"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
  </ul>
</div>

</div>

  </div>

    </div>

</div>
  



      
      

    </div>
  </div>


</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="794346430106173441" id="stream-item-tweet-794346430106173441" data-item-type="tweet">
    


  

  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable
       original-tweet js-original-tweet
      
       
"
      
data-tweet-id="794346430106173441"
data-item-id="794346430106173441"
data-permalink-path="/Maichardology/status/794346430106173441"








  data-screen-name="Maichardology" data-name="Justine ��" data-user-id="705037871233667074"
  data-you-follow="false"
  data-follows-you="false"
  data-you-block="false"









data-disclosure-type=""












 data-component-context="tweet"


    >


    <div class="context">
      
      
    </div>

    <div class="content">
      

      
      <div class="stream-item-header">
          <a  class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/Maichardology" data-user-id="705037871233667074">
    <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/795222497763299328/Shv0NOdn_bigger.jpg" alt="">
    <strong class="fullname js-action-profile-name show-popup-with-id" >Justine <span class="Emoji Emoji--forLinks" style="background-image:url('https://abs.twimg.com/emoji/v2/72x72/1f47d.png')" title="Extraterrestrial alien" aria-label="Emoji: Extraterrestrial alien">&nbsp;</span><span class="visuallyhidden" aria-hidden="true">��</span></strong>
    <span>&rlm;</span><span class="username js-action-profile-name" ><s>@</s><b>Maichardology</b></span>
    
  </a>

        <small class="time">
  <a href="/Maichardology/status/794346430106173441" class="tweet-timestamp js-permalink js-nav js-tooltip" title="6:12 pm - 3 Nov 2016" ><span class="_timestamp js-short-timestamp " data-aria-label-part="last" data-time="1478221921" data-time-ms="1478221921000" data-long-form="true">Nov 3</span></a>
</small>

          
          
      </div>


      
          <p class="u-hiddenVisually" aria-hidden="true" data-aria-label-part="1">Justine <span class="Emoji Emoji--forLinks" style="background-image:url('https://abs.twimg.com/emoji/v2/72x72/1f47d.png')" title="Extraterrestrial alien" aria-label="Emoji: Extraterrestrial alien">&nbsp;</span><span class="visuallyhidden" aria-hidden="true">��</span> Retweeted abi</p>


<div class="js-tweet-text-container">
  <p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="4">of course, they just can&#39;t accept the fact that they&#39;re having <strong>a</strong> grand time together. Pati smile ginagawan ng issue. Gahd i heyt drugs <a href="https://t.co/CQVrMFm0xD" rel="nofollow" dir="ltr" data-expanded-url="https://twitter.com/maichrdx/status/794342905632522240" class="twitter-timeline-link u-hidden" target="_blank" title="https://twitter.com/maichrdx/status/794342905632522240" ><span class="tco-ellipsis"></span><span class="invisible">https://</span><span class="js-display-url">twitter.com/maichrdx/statu</span><span class="invisible">s/794342905632522240</span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span>…</span></a></p>
</div>


<p class="u-hiddenVisually" aria-hidden="true" data-aria-label-part="3">Justine <span class="Emoji Emoji--forLinks" style="background-image:url('https://abs.twimg.com/emoji/v2/72x72/1f47d.png')" title="Extraterrestrial alien" aria-label="Emoji: Extraterrestrial alien">&nbsp;</span><span class="visuallyhidden" aria-hidden="true">��</span> added,</p>
  
      <div class="QuoteTweet
    
    u-block js-tweet-details-fixer">
  <div class="QuoteTweet-container">
    <a class="QuoteTweet-link js-nav" href="/maichrdx/status/794342905632522240" aria-hidden="true"
       >
    </a>
    <div class="QuoteTweet-innerContainer u-cf js-permalink js-media-container"
      data-item-id="794342905632522240"
      data-item-type="tweet"
      data-screen-name="maichrdx"
      data-user-id="704262767268605952"
      href="/maichrdx/status/794342905632522240"
      tabindex="0">
      <div class="tweet-content">
            <div class="QuoteMedia">
      <div class="QuoteMedia-container js-quote-media-container">
          <div class="QuoteMedia-triplePhoto">
    <div class="QuoteMedia-halfPhoto">
      <div class="QuoteMedia-photoContainer js-quote-photo"
  data-image-url="https://pbs.twimg.com/media/CwYSpd7UoAEaM9R.jpg"
  
  data-element-context="platform_photo_card">
  <img data-aria-label-part src="https://pbs.twimg.com/media/CwYSpd7UoAEaM9R.jpg" alt=""
      style="height: 100%; left: -49px;"
>
</div>

    </div>
  <div class="QuoteMedia-quarterPhotoContainer">
      <div class="QuoteMedia-quarterPhoto">
        <div class="QuoteMedia-photoContainer js-quote-photo"
  data-image-url="https://pbs.twimg.com/media/CwYSpeEVIAAp7kl.jpg"
  
  data-element-context="platform_photo_card">
  <img data-aria-label-part src="https://pbs.twimg.com/media/CwYSpeEVIAAp7kl.jpg" alt=""
      style="width: 100%; top: -0px;"
>
</div>

      </div>
      <div class="QuoteMedia-quarterPhoto">
        <div class="QuoteMedia-photoContainer js-quote-photo"
  data-image-url="https://pbs.twimg.com/media/CwYSpd-UcAAO-hv.jpg"
  
  data-element-context="platform_photo_card">
  <img data-aria-label-part src="https://pbs.twimg.com/media/CwYSpd-UcAAO-hv.jpg" alt=""
      style="width: 100%; top: -0px;"
>
</div>

      </div>
  </div>
</div>

      </div>
  </div>

        <div class="QuoteTweet-authorAndText u-alignTop">
            
  <div class="QuoteTweet-originalAuthor u-cf u-textTruncate stream-item-header js-user-profile-link">
    <b class="QuoteTweet-fullname u-linkComplex-target">abi</b>
    <span class="QuoteTweet-screenname u-dir" dir="ltr">
      <span class="at">@</span>maichrdx
    </span>
  </div>

          
          <div class="QuoteTweet-text tweet-text u-dir js-ellipsis"
            lang="en"
            data-aria-label-part="2"
            
            dir="ltr">Ang saya nila oh <img class="Emoji Emoji--forText" src="https://abs.twimg.com/emoji/v2/72x72/1f62d.png" draggable="false" alt="��" title="Loudly crying face" aria-label="Emoji: Loudly crying face"><img class="Emoji Emoji--forText" src="https://abs.twimg.com/emoji/v2/72x72/1f495.png" draggable="false" alt="��" title="Two hearts" aria-label="Emoji: Two hearts"> <span class="twitter-atreply pretty-link js-nav" dir="ltr" data-mentioned-user-id="98310564" ><s>@</s><b>aldenrichards02</b></span> <span class="twitter-atreply pretty-link js-nav" dir="ltr" data-mentioned-user-id="63701775" ><s>@</s><b>mainedcm</b></span> 

© ALDUB Scoopers
<span data-query-source="hashtag_click" class="twitter-hashtag pretty-link js-nav" dir="ltr" ><s>#</s><b>ALDUBLOSTinLOVE</b></span> <span class="twitter-timeline-link u-hidden" data-pre-embedded="true" dir="ltr" >pic.twitter.com/Og7KOLZgMU</span></div>
        </div>
      </div>
    </div>
  </div>
</div>





      
        

      
      

      
      <div class="stream-item-footer">
  
        <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount" aria-hidden="true" data-tweet-stat-count="0">
        <span class="ProfileTweet-actionCountForAria" >0 replies .</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="97">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>97 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="51">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>51 likes</span>
      </span>
    </span>
  </div>

    <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
      <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionReply"
    data-modal="ProfileTweet-reply"
    type="button">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount ProfileTweet-actionCount--isZero ">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true"></span>
        </span>
      </div>
  </button>
</div>
      <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet"
    
    data-modal="ProfileTweet-retweet"
    type="button">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">97</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">97</span>
        </span>
      </div>
  </button>
</div>

      <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">51</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">51</span>
        </span>
      </div>
  </button>
</div>

      


        <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--dots"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
  </ul>
</div>

</div>

  </div>

    </div>

</div>
  



      
      

    </div>
  </div>


</li>

      <li class="js-stream-item stream-item stream-item
" data-item-id="794346425857478657" id="stream-item-tweet-794346425857478657" data-item-type="tweet">
    


  

  <div class="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable
       original-tweet js-original-tweet
      
       
"
      
data-tweet-id="794346425857478657"
data-item-id="794346425857478657"
data-permalink-path="/musicfacts_LM/status/794346425857478657"








  data-screen-name="musicfacts_LM" data-name="LM Music Facts" data-user-id="3193848216"
  data-you-follow="false"
  data-follows-you="false"
  data-you-block="false"









data-disclosure-type=""












 data-component-context="tweet"


    >


    <div class="context">
      
      
    </div>

    <div class="content">
      

      
      <div class="stream-item-header">
          <a  class="account-group js-account-group js-action-profile js-user-profile-link js-nav" href="/musicfacts_LM" data-user-id="3193848216">
    <img class="avatar js-action-profile-avatar" src="https://pbs.twimg.com/profile_images/796072828013596673/jgwfcWxl_bigger.jpg" alt="">
    <strong class="fullname js-action-profile-name show-popup-with-id" >LM Music Facts</strong>
    <span>&rlm;</span><span class="username js-action-profile-name" ><s>@</s><b>musicfacts_LM</b></span>
    
  </a>

        <small class="time">
  <a href="/musicfacts_LM/status/794346425857478657" class="tweet-timestamp js-permalink js-nav js-tooltip" title="6:12 pm - 3 Nov 2016" ><span class="_timestamp js-short-timestamp " data-aria-label-part="last" data-time="1478221920" data-time-ms="1478221920000" data-long-form="true">Nov 3</span></a>
</small>

          
          
      </div>


      
          <p class="u-hiddenVisually" aria-hidden="true" data-aria-label-part="1">LM Music Facts Retweeted Little Mix Voting</p>


<div class="js-tweet-text-container">
  <p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="4">We are almost losing our lead. Keep voting for Little Mix to reach <strong>a</strong> bigger gap <a href="https://t.co/ExQ75KSzzO" rel="nofollow" dir="ltr" data-expanded-url="https://twitter.com/lmvotingnow/status/794323254576082944" class="twitter-timeline-link u-hidden" target="_blank" title="https://twitter.com/lmvotingnow/status/794323254576082944" ><span class="tco-ellipsis"></span><span class="invisible">https://</span><span class="js-display-url">twitter.com/lmvotingnow/st</span><span class="invisible">atus/794323254576082944</span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span>…</span></a></p>
</div>


<p class="u-hiddenVisually" aria-hidden="true" data-aria-label-part="3">LM Music Facts added,</p>
  
      <div class="QuoteTweet
    
    u-block js-tweet-details-fixer">
  <div class="QuoteTweet-container">
    <a class="QuoteTweet-link js-nav" href="/LMVotingNow/status/794323254576082944" aria-hidden="true"
       >
    </a>
    <div class="QuoteTweet-innerContainer u-cf js-permalink js-media-container"
      data-item-id="794323254576082944"
      data-item-type="tweet"
      data-screen-name="LMVotingNow"
      data-user-id="740580175692234752"
      href="/LMVotingNow/status/794323254576082944"
      tabindex="0">
      <div class="tweet-content">
        <div class="QuoteTweet-authorAndText u-alignTop">
            
  <div class="QuoteTweet-originalAuthor u-cf u-textTruncate stream-item-header js-user-profile-link">
    <b class="QuoteTweet-fullname u-linkComplex-target">Little Mix Voting</b>
    <span class="QuoteTweet-screenname u-dir" dir="ltr">
      <span class="at">@</span>LMVotingNow
    </span>
  </div>

          
          <div class="QuoteTweet-text tweet-text u-dir js-ellipsis"
            lang="en"
            data-aria-label-part="2"
            
            dir="ltr">Yay! We took the lead! Keep voting Mixers - <span rel="nofollow" dir="ltr" data-expanded-url="http://987ampradio.cbslocal.com/2016/11/03/tweet-or-delete-little-mix-shout-out-to-my-ex-vs-tritonal-ft-adam-lambert-broken/" class="twitter-timeline-link" target="_blank" title="http://987ampradio.cbslocal.com/2016/11/03/tweet-or-delete-little-mix-shout-out-to-my-ex-vs-tritonal-ft-adam-lambert-broken/" ><span class="tco-ellipsis"></span><span class="invisible">http://</span><span class="js-display-url">987ampradio.cbslocal.com/2016/11/03/twe</span><span class="invisible">et-or-delete-little-mix-shout-out-to-my-ex-vs-tritonal-ft-adam-lambert-broken/</span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span>…</span></span></div>
        </div>
      </div>
    </div>
  </div>
</div>





      
        

      
      

      
      <div class="stream-item-footer">
  
        <div class="ProfileTweet-actionCountList u-hiddenVisually">
    
    
    <span class="ProfileTweet-action--reply u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="2">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>2 replies .</span>
      </span>
    </span>
    <span class="ProfileTweet-action--retweet u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="72">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>72 retweets</span>
      </span>
    </span>
    <span class="ProfileTweet-action--favorite u-hiddenVisually">
      <span class="ProfileTweet-actionCount"  data-tweet-stat-count="59">
        <span class="ProfileTweet-actionCountForAria" data-aria-label-part>59 likes</span>
      </span>
    </span>
  </div>

    <div class="ProfileTweet-actionList js-actions" role="group" aria-label="Tweet actions">
      <div class="ProfileTweet-action ProfileTweet-action--reply">
  <button class="ProfileTweet-actionButton u-textUserColorHover js-actionButton js-actionReply"
    data-modal="ProfileTweet-reply"
    type="button">
    <div class="IconContainer js-tooltip" title="Reply">
      <span class="Icon Icon--reply"></span>
      <span class="u-hiddenVisually">Reply</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount ">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">2</span>
        </span>
      </div>
  </button>
</div>
      <div class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt">
  <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet"
    
    data-modal="ProfileTweet-retweet"
    type="button">
    <div class="IconContainer js-tooltip" title="Retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweet</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">72</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button">
    <div class="IconContainer js-tooltip" title="Undo retweet">
      <span class="Icon Icon--retweet"></span>
      <span class="u-hiddenVisually">Retweeted</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">72</span>
        </span>
      </div>
  </button>
</div>

      <div class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState">
  <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Like</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">59</span>
        </span>
      </div>
  </button><button class="ProfileTweet-actionButtonUndo u-linkClean js-actionButton js-actionFavorite" type="button">
    <div class="IconContainer js-tooltip" title="Undo like">
      <div class="HeartAnimationContainer">
        <div class="HeartAnimation"></div>
      </div>
      <span class="u-hiddenVisually">Liked</span>
    </div>
      <div class="IconTextContainer">
        <span class="ProfileTweet-actionCount">
          <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">59</span>
        </span>
      </div>
  </button>
</div>

      


        <div class="ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions">
    <div class="dropdown">
  <button class="ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle" type="button">
      <div class="IconContainer js-tooltip" title="More">
        <span class="Icon Icon--dots"></span>
        <span class="u-hiddenVisually">More</span>
      </div>
  </button>
  <div class="dropdown-menu">
  <div class="dropdown-caret">
    <div class="caret-outer"></div>
    <div class="caret-inner"></div>
  </div>
  <ul>
    
      <li class="copy-link-to-tweet js-actionCopyLinkToTweet">
        <button type="button" class="dropdown-link">Copy link to Tweet</button>
      </li>
      <li class="embed-link js-actionEmbedTweet" data-nav="embed_tweet">
        <button type="button" class="dropdown-link">Embed Tweet</button>
      </li>
  </ul>
</div>

</div>

  </div>

    </div>

</div>
  



      
      

    </div>
  </div>


</li>








 


'''

res3 = tc.parse_tweets(x)

