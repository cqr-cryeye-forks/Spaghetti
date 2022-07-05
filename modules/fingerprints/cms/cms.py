from modules.fingerprints.cms import drupal, joomla, wordpress, magento


def check_cms(content):
    return (
        drupal.Drupal().run(content),
        joomla.Joomla().run(content),
        wordpress.Wordpress().run(content),
        magento.Magento().run(content)
    )
