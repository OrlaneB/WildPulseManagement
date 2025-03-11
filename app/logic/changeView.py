
def changeView(stackedWidget,toView):
    if toView == "main" :
        stackedWidget.setCurrentIndex(0)
    else:
        stackedWidget.setCurrentWidget(toView)