from django import template

register = template.Library()

@register.filter
def hashtag_link(article):
    # #안녕 을 입력하고 스페이스로 띄어쓰기를 해주기 때문에 ' '(공백)을 표시해줘야함
    content = article.content + ' ' 
    hashtags = article.hashtags.all()

    for hashtag in hashtags:
        # replace(바꿀거, 넣어줄거)
        # 마지막에 공백 안넣어주면 hashtag로 인식을 못함
        content = content.replace(
            hashtag.content+' ',
            f'<a href="/articles/{hashtag.pk}/hashtag/">{hashtag.content}</a> '
        )
    return content