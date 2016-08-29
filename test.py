import TwitterWebsiteSearch
import lxml
import lxml.html as lh


def test1():
    with open('samplehtml/769043391917199360.html', 'r') as file:
        tweethtml = file.read()
        res = TwitterWebsiteSearch.parse_tweets(tweethtml)

        print(res)


def test1_1():
    res = TwitterWebsiteSearch.search('10 peach emoji colored hair looks to inspire you from:ELLEmagazine')
    print(res)

def test2():
    s = ''' 
    <div class="js-tweet-text-container">
  <p class="TweetTextSize TweetTextSize--26px js-tweet-text tweet-text" lang="en" data-aria-label-part="0">10 peach emoji colored hair looks to inspire you <img class="Emoji Emoji--forText" src="https://abs.twimg.com/emoji/v2/72x72/1f351.png" draggable="false" alt="🍑" title="Peach" aria-label="Emoji: Peach"><img class="Emoji Emoji--forText" src="https://abs.twimg.com/emoji/v2/72x72/1f351.png" draggable="false" alt="🍑" title="Peach" aria-label="Emoji: Peach"><img class="Emoji Emoji--forText" src="https://abs.twimg.com/emoji/v2/72x72/1f351.png" draggable="false" alt="🍑" title="Peach" aria-label="Emoji: Peach">
  <a href="https://t.co/6DGIXFbFm2" rel="nofollow" dir="ltr" data-expanded-url="http://ellemag.co/wdgeKDr" class="twitter-timeline-link u-hidden" target="_blank" title="http://ellemag.co/wdgeKDr">
  <span class="tco-ellipsis"></span>
  <span class="invisible">http://</span>
  <span class="js-display-url">ellemag.co/wdgeKDr</span>
  <span class="invisible"></span>
  <span class="tco-ellipsis"><span class="invisible">&nbsp;</span></span>
  </a>
  </p>
</div>
    '''
    html =lh.fromstring(s)

    text_p = html.cssselect('p.tweet-text')
    
    res = ''

    for item in text_p[0].cssselect('img.Emoji'):
        item.tail = item.get('alt') + item.tail if item.tail else item.get('alt')
    
    for item in text_p[0].cssselect('span.invisible'):
        item.getparent().remove(item)

    print(text_p[0].text_content())
    print(text_p[0].text_content())

if __name__ == '__main__':
    test1()