from django.conf.urls import patterns, include, url
urlpatterns = patterns('fluxoCaixa.views',
	url(r'^$', 'fluxoListar'),
	url(r'^pesquisar/$', 'fluxoPesquisar'),
	)