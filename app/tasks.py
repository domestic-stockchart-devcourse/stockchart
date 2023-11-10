from background_task import background


@background(schedule=60*10)
def crawl_news():
    pass


@background(schedule=60*10)
def crawl_chart():
    pass
