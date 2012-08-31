from django.shortcuts import render_to_response
from django.template.context import RequestContext


def home(request):
    return render_to_response('core/home.html', context_instance=RequestContext(request))


def about(request):
    return render_to_response('core/about.html', context_instance=RequestContext(request))


def privacy(request):
    return render_to_response('core/privacy.html', context_instance=RequestContext(request))


def terms(request):
    return render_to_response('core/terms.html', context_instance=RequestContext(request))


def contact(request):
    return render_to_response('core/contact.html', context_instance=RequestContext(request))