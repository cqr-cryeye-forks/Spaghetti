from modules.fingerprints.lang import asp, java, php, perl, python, ruby


def detect_langs(content, headers):
    return (
        asp.Asp().run(content, headers),
        java.Java().run(content, headers),
        php.Php().run(content, headers),
        perl.Perl().run(content, headers),
        python.Python().run(content, headers),
        ruby.Ruby().run(content, headers)
    )
