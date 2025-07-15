pkgname=gdl-helper
pkgver=1.1
pkgrel=1
pkgdesc="Project GDL Helper"
arch=('any')
url="https://github.com/GMDProjectL/gdl-helper"
license=('GPL')
depends=('python-requests' 'python-systemd' 'pyside6' 'grub' 'kwrite')
makedepends=()
checkdepends=()
optdepends=()
backup=()
options=()
install=
source=(${pkgname}::"git+file://${PWD}")

package() {
    cd "$srcdir"
    export UPDATER_DIST="${pkgdir}/opt/gdl-helper"

    mkdir -p "${UPDATER_DIST}"
    mkdir -p "${UPDATER_DIST}/window"
    mkdir -p "${UPDATER_DIST}/ui_generated"
    mkdir -p "${UPDATER_DIST}/ui"
    mkdir -p "${UPDATER_DIST}/locales"

    install -Dm0644 $srcdir/${pkgname}/main.py -t ${UPDATER_DIST}
    install -Dm0644 $srcdir/${pkgname}/bootloader_update_thread.py -t ${UPDATER_DIST}
    install -Dm0644 $srcdir/${pkgname}/ui/mainwindow.ui -t ${UPDATER_DIST}/ui
    install -Dm0644 $srcdir/${pkgname}/ui_generated/ui_mainwindow.py -t ${UPDATER_DIST}/ui_generated
    install -Dm0644 $srcdir/${pkgname}/locales/__init__.py -t ${UPDATER_DIST}/locales
    install -Dm0644 $srcdir/${pkgname}/locales/en.json -t ${UPDATER_DIST}/locales
    install -Dm0644 $srcdir/${pkgname}/locales/ru.json -t ${UPDATER_DIST}/locales
    install -Dm0644 $srcdir/${pkgname}/window/mainwindow.py -t ${UPDATER_DIST}/window
    install -Dm0644 $srcdir/${pkgname}/window/bootloaderupdatewindow.py -t ${UPDATER_DIST}/window
    
    install -Dm0644 $srcdir/${pkgname}/assets/gdl-helper.desktop -t "${pkgdir}/usr/share/applications"
}