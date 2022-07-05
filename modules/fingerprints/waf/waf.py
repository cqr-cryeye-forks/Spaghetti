from modules.fingerprints.waf import airlock, anquanboa, aws, baidu, barracuda, bigip, binarysec, blockdos, chinacache, \
    ciscoacexml, cloudflare, cloudfront, dotdefender, edgecast, fortiweb, hyperguard, incapsula, isaserver, modsecurity, \
    netcontinuum, paloalto, profense, radware, requestvalidationmode, safedog, secureiis, sengnix, sitelock, sonicwall, \
    sucuri, trafficshield, urlscan, varnish, wallarm, webknight


def test_waf(headers, content):
    return (
        airlock.Airlock().run(headers),
        anquanboa.Anquanbao().run(headers),
        aws.Aws().run(headers),
        baidu.Baidu().run(headers),
        barracuda.Barracuda().run(headers),
        bigip.BigIP().run(headers),
        binarysec.BinarySEC().run(headers),
        blockdos.BlockDoS().run(headers),
        chinacache.ChinaCache().run(headers),
        ciscoacexml.CiscoAceXML().run(headers),
        cloudflare.Cloudflare().run(headers),
        cloudfront.Cloudfront().run(headers),
        dotdefender.DotDefender().run(headers),
        edgecast.Edgecast().run(headers),
        fortiweb.FortiWeb().run(headers),
        hyperguard.Hyperguard().run(headers),
        incapsula.Incapsula().run(headers),
        isaserver.Isaserver().run(content),
        modsecurity.Modsecurity().run(headers),
        netcontinuum.NetContinuum().run(headers),
        paloalto.PaloAlto().run(headers),
        profense.Profense().run(headers),
        radware.Radware().run(headers),
        requestvalidationmode.RequestValidationMode().run(content),
        safedog.Safedog().run(headers),
        secureiis.SecureIIS().run(content),
        sengnix.Senginx().run(content),
        sitelock.SiteLock().run(content),
        sonicwall.SonicWall().run(content),
        sucuri.Sucuri().run(headers),
        trafficshield.TrafficShield().run(headers),
        urlscan.Urlscan().run(headers),
        varnish.Varnish().run(headers),
        wallarm.Wallarm().run(headers),
        webknight.WebKnight().run(headers)
    )
