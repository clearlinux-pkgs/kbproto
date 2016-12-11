#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kbproto
Version  : 1.0.7
Release  : 9
URL      : http://xorg.freedesktop.org/releases/individual/proto/kbproto-1.0.7.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/proto/kbproto-1.0.7.tar.bz2
Summary  : KB extension headers
Group    : Development/Tools
License  : HPND
Requires: kbproto-doc
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : xmlto

%description
X Keyboard Extension
This extension defines a protcol to provide a number of new capabilities
and controls for text keyboards.

%package dev
Summary: dev components for the kbproto package.
Group: Development
Provides: kbproto-devel

%description dev
dev components for the kbproto package.


%package dev32
Summary: dev32 components for the kbproto package.
Group: Default

%description dev32
dev32 components for the kbproto package.


%package doc
Summary: doc components for the kbproto package.
Group: Documentation

%description doc
doc components for the kbproto package.


%prep
%setup -q -n kbproto-1.0.7
pushd ..
cp -a kbproto-1.0.7 build32
popd

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
%configure --disable-static  --libdir=/usr/lib32
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
pushd ../build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do mv $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/XKB.h
/usr/include/X11/extensions/XKBgeom.h
/usr/include/X11/extensions/XKBproto.h
/usr/include/X11/extensions/XKBsrv.h
/usr/include/X11/extensions/XKBstr.h
/usr/lib64/pkgconfig/kbproto.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/pkgconfig/32kbproto.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/kbproto/*
