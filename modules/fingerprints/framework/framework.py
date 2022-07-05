from modules.fingerprints.framework import cakephp, cherrypy, django, flask, fuelphp, grails, laravel, mvc, nette, \
    phalcon, symfony, zend, yii, rails


def test_frameworks(headers, content):
    return (
        cakephp.Cakephp().run(headers),
        cherrypy.Cherrypy().run(headers),
        django.Django().run(headers),
        flask.Flask().run(headers),
        fuelphp.Fuelphp().run(headers, content),
        grails.Grails().run(headers),
        laravel.Laravel().run(headers),
        mvc.Mvc().run(headers),
        nette.Nette().run(headers),
        phalcon.Phalcon().run(headers),
        rails.Rails().run(headers),
        symfony.Symfony().run(headers),
        yii.Yii().run(headers, content),
        zend.Zend().run(headers)
    )
