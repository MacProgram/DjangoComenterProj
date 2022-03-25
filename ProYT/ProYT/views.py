from django.http import HttpResponse
from django.template import Template, Context


def Principal(request):
    DoxOut = open(
        r"D:/Users/lukym/Desktop/Projects/Dproject/static/index.html")
    plt = Template(DoxOut.read())
    DoxOut.close()

    pris = open(
        r"D:/Users/lukym/Desktop/Projects/Dproject/static/styler.css")
    ctx = Context(pris.read())
    Doc = plt.render(ctx)

    return HttpResponse(Doc)
