# $Revision: 1.1 $
Summary:	Smart decoder for uuencode, xxencode, Base64 and BinHex
Summary(pl):	Uniwersalny dekoder uuencode, xxencode, Base64 i BinHex
Name:		uudeview
Version:	0.5.13
Release:	1
License:	GPL
Group:		Utilities/File
Group(pl):	Narz�dzia/Pliki
Source:		http://www.informatik.uni-frankfurt.de/~fp/uudeview/Apps/frank/%{_name}-%{_version}.tar.gz
URL:		http://www.uni-frankfurt.de/~fp/uudeview/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
UUDeview is a smart decoder for several surfaces which are common
in email and Usenet. It can decode uuencode, xxencode, Base64 and
BinHex. It can handle multiple files and multiple parts, even 
in random order. Also an encoder is attached, UUEnview.

%description -l pl
UUDeview jest przydatnym narz�dziem do dekodowania popularnych
format�w, takich jak uuencode, xxencode, Base64 i BinHex. Potrafi
poradzi� sobie z wieloma plikami w wielu cz�ciach, nawet wymieszanych.
W pakiecie znajduje si� tak�e program do kodowania plik�w na wy�ej
wymienione formaty (opr�cz BinHex).

%prep
%setup -q
%{_configure} --without-x

%build
make

%install
rm -rf $RPM_BUILD_ROOT

make install \
    bindir=$RPM_BUILD_ROOT%{_bindir} \
    infodir=$RPM_BUILD_ROOT%{_infodir} \
    mandir=$RPM_BUILD_ROOT%{_mandir}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	COPYING HISTORY HOWTO IAFA-PACKAGE 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
