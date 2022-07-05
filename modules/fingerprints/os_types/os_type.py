from modules.fingerprints.os_types import bsd, windows, linux, solaris, unix, mac


def detect_os(headers):
    return (
        bsd.Bsd().run(headers),
        windows.Windows().run(headers),
        linux.Linux().run(headers),
        solaris.Solaris().run(headers),
        unix.Unix().run(headers),
        mac.Mac().run(headers)
    )
