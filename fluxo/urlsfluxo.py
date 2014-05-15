from django.conf.urls import patterns, include, url
urlpatterns = patterns('fluxo.views',
	url(r'^$', 'fluxoListar'),
	url(r'^pesquisar/$', 'fluxoPesquisar'),
	)